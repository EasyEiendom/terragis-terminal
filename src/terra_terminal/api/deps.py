from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Request

from terra_terminal.clients import NorgesBankClient, SSBClient
from terra_terminal.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with httpx.AsyncClient(timeout=settings.http_timeout_s) as client:
        app.state.http_client = client
        yield


def http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http_client


def ssb_client(request: Request) -> SSBClient:
    return SSBClient(client=http_client(request))


def norges_bank_client(request: Request) -> NorgesBankClient:
    return NorgesBankClient(client=http_client(request))
