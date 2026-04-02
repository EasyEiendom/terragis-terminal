"""Norges Bank open data — SDMX-JSON time series."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx

from terra_terminal.config import settings


@dataclass(frozen=True)
class Observation:
    period: str
    value: float | None


class NorgesBankClient:
    def __init__(
        self,
        base_url: str | None = None,
        timeout: float | None = None,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base = (base_url or settings.norges_bank_base_url).rstrip("/")
        self._timeout = timeout if timeout is not None else settings.http_timeout_s
        self._client = client

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is not None:
            return self._client
        return httpx.AsyncClient(timeout=self._timeout)

    async def fetch_series_raw(
        self,
        path: str,
        *,
        start_period: str | None = None,
        end_period: str | None = None,
    ) -> dict[str, Any]:
        """GET SDMX-JSON. `path` is e.g. `IR/B.KPRA..` (policy rate)."""
        url = f"{self._base}/{path.lstrip('/')}"
        params: dict[str, str] = {"format": "sdmx-json"}
        if start_period:
            params["startPeriod"] = start_period
        if end_period:
            params["endPeriod"] = end_period
        c = await self._get_client()
        r = await c.get(url, params=params)
        r.raise_for_status()
        return r.json()

    @staticmethod
    def parse_sdmx_observations(payload: dict[str, Any]) -> list[Observation]:
        """Flatten first dataset series into dated observations."""
        data = payload.get("data") or {}
        structure = data.get("structure") or {}
        dims = structure.get("dimensions") or {}
        obs_dims = dims.get("observation") or []
        if not obs_dims:
            return []
        time_values = obs_dims[0].get("values") or []

        datasets = data.get("dataSets") or []
        if not datasets:
            return []
        series = (datasets[0].get("series") or {})
        if not series:
            return []
        first_key = next(iter(series))
        observations = (series[first_key].get("observations") or {})

        out: list[Observation] = []
        for idx_str, cell in sorted(observations.items(), key=lambda x: int(x[0])):
            idx = int(idx_str)
            period = time_values[idx]["id"] if idx < len(time_values) else idx_str
            val: float | None
            if cell and cell[0] is not None and cell[0] != "":
                try:
                    val = float(cell[0])
                except (TypeError, ValueError):
                    val = None
            else:
                val = None
            out.append(Observation(period=period, value=val))
        return out

    async def policy_rate(
        self,
        *,
        start_period: str = "2020-01-01",
    ) -> list[Observation]:
        """Styringsrenten (daily series in API; values step on change days)."""
        raw = await self.fetch_series_raw("IR/B.KPRA..", start_period=start_period)
        return self.parse_sdmx_observations(raw)
