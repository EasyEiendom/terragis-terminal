"""SSB PxWeb API v0 client (json-stat2)."""

from __future__ import annotations

from typing import Any

import httpx

from terra_terminal.config import settings


class SSBClient:
    """Thin wrapper around SSB table POST endpoints."""

    def __init__(
        self,
        base_url: str | None = None,
        timeout: float | None = None,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base = (base_url or settings.ssb_base_url).rstrip("/")
        self._timeout = timeout if timeout is not None else settings.http_timeout_s
        self._client = client

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is not None:
            return self._client
        return httpx.AsyncClient(timeout=self._timeout)

    async def fetch_table_metadata(self, table_id: str, lang: str = "no") -> dict[str, Any]:
        """GET /{lang}/table/{id} — variable codes and allowed values (no data cells)."""
        url = f"{self._base}/{lang}/table/{table_id}"
        c = await self._get_client()
        r = await c.get(url)
        r.raise_for_status()
        return r.json()

    async def query_table(
        self,
        table_id: str,
        query: list[dict[str, Any]],
        *,
        lang: str = "no",
        response_format: str = "json-stat2",
    ) -> dict[str, Any]:
        """POST table slice; `query` uses SSB PxWeb selection objects."""
        url = f"{self._base}/{lang}/table/{table_id}"
        body = {"query": query, "response": {"format": response_format}}
        c = await self._get_client()
        r = await c.post(url, json=body)
        r.raise_for_status()
        return r.json()

    async def housing_price_index(
        self,
        *,
        region: str = "TOTAL",
        boligtype: str = "00",
        contents_code: str = "Boligindeks",
        last_n_quarters: int = 24,
        lang: str = "no",
    ) -> dict[str, Any]:
        """Table 07221 — used dwelling price index by region and dwelling type."""
        q: list[dict[str, Any]] = [
            {"code": "Region", "selection": {"filter": "item", "values": [region]}},
            {"code": "Boligtype", "selection": {"filter": "item", "values": [boligtype]}},
            {"code": "ContentsCode", "selection": {"filter": "item", "values": [contents_code]}},
            {"code": "Tid", "selection": {"filter": "top", "values": [str(last_n_quarters)]}},
        ]
        return await self.query_table("07221", q, lang=lang)
