# TerraGIS — Norwegian Real Estate Terminal

## Repository

- **GitHub:** [EasyEiendom/terragis-terminal](https://github.com/EasyEiendom/terragis-terminal)
- **MVP branch:** `initial-mvp` — use this branch for the first integration with Easy sandbox / data connections configured in GitHub.

## Product intent

Bloomberg-class **analytics** for Norwegian real estate: risk and portfolio intelligence, macro and housing series, spatial risk overlays — **not** a broker terminal and **not** personalized investment advice (Finanstilsynet / verdipapirhandelloven boundary). Compete on **risk analytics**; avoid replicating Eiendomsverdi’s AVM data moat for point estimates.

## Canonical specs (read before large changes)

- `compass_artifact_wf-7ce9f6b8-e2e0-45e5-9c01-48378bd7f359_text_markdown.md` — architecture blueprint (APIs, stack, Medallion, regulatory notes).
- `Literature MD/Norwegian Real Estate Risk & Analytics Platform — Institutional Blueprint.md` — institutional module design.

## Stack (target)

- **API:** FastAPI (Python), WebSockets later for streaming.
- **Risk:** Riskfolio-Lib + quarterly regional returns; PyPortfolioOpt / QuantLib as needed.
- **Data:** Medallion (Bronze / Silver / Gold) on Azure Norway East; PostGIS SRID **25833** (eastern Norway), **25832** for Bergen/Stavanger when needed.
- **Matrikkel / Grunnbok:** Maskinporten + formal Kartverket agreement — treat as **critical path**, not in public-ingest MVP.

## Free public ingest (no auth) — safe to implement first

- **SSB** `https://data.ssb.no/api/v0/` — e.g. table **07221** (house price index), **06035**, **185487**; POST `json-stat2`.
- **Norges Bank** `https://data.norges-bank.no/api/data/` — SDMX-JSON; policy rate `IR/B.KPRA..`.
- **NVE** — flood / varsom APIs and ArcGIS layers (spatial joins to matrikkel later).

## Hard constraints

- **Do not** scrape FINN.no; use SSB / Eiendom Norge aggregates or licensed data.
- **GDPR / utleveringsforskriften:** matrikkel and grunnbok data are sensitive; DPIA before production use of personal data.
- Attribute open data: **© Kartverket** where required; follow NLOD for SSB/NVE as applicable.

## Repo layout (this phase)

- `src/terra_terminal/` — Python package: HTTP clients, FastAPI app.
- `tests/` — pytest.

## Commands

```bash
pip install -e ".[dev]"
uvicorn terra_terminal.api.main:app --reload --host 127.0.0.1 --port 8000
pytest -q
```
