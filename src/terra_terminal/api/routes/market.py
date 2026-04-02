from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query

from terra_terminal.api import deps
from terra_terminal.clients import NorgesBankClient, SSBClient

router = APIRouter()


@router.get("/ssb/table/{table_id}/metadata")
async def ssb_table_metadata(
    table_id: str,
    ssb: Annotated[SSBClient, Depends(deps.ssb_client)],
    lang: str = Query(default="no", description="no | en"),
) -> dict[str, Any]:
    return await ssb.fetch_table_metadata(table_id, lang=lang)


@router.get("/ssb/housing-price-index")
async def ssb_housing_price_index(
    ssb: Annotated[SSBClient, Depends(deps.ssb_client)],
    region: str = Query(default="TOTAL", description="SSB region code, e.g. TOTAL, 001 (Oslo m/Bærum)"),
    boligtype: str = Query(default="00", description="00=all, 03=blokkleiligheter"),
    last_n_quarters: int = Query(default=24, ge=1, le=200),
    lang: str = Query(default="no"),
) -> dict[str, Any]:
    return await ssb.housing_price_index(
        region=region,
        boligtype=boligtype,
        last_n_quarters=last_n_quarters,
        lang=lang,
    )


@router.get("/norges-bank/policy-rate")
async def norges_bank_policy_rate(
    nb: Annotated[NorgesBankClient, Depends(deps.norges_bank_client)],
    start_period: str = Query(default="2020-01-01", description="SDMX startPeriod (date)"),
) -> list[dict[str, float | str | None]]:
    obs = await nb.policy_rate(start_period=start_period)
    return [{"period": o.period, "value": o.value} for o in obs]
