from fastapi import FastAPI

from terra_terminal import __version__
from terra_terminal.api.deps import lifespan
from terra_terminal.api.routes import market

app = FastAPI(
    title="TerraGIS Norwegian RE Terminal",
    version=__version__,
    description="Public market data: SSB housing statistics, Norges Bank rates.",
    lifespan=lifespan,
)
app.include_router(market.router, prefix="/market", tags=["market"])


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "terra-terminal"}
