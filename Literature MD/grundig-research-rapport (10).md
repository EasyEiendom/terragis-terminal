# Institusjonell eiendomsrisiko- og analyseplattform for Norge

## Executive summary

Norge har et av Europas mest datarike eiendomsmarkeder, men profesjonelle aktører (bank, pensjon, fondsforvaltere, eiendomsutviklere og tilsyn) arbeider fortsatt fragmentert: tinglysings-/grunnboksdata, matrikkel, plan- og temadata, transaksjoner, leiepriser/yield, kreditt- og ESG-data lever i separate systemer, med varierende tilgangskontroll og lisensregimer. Kartverket peker selv på at eiendomsdata inneholder personopplysninger og at tilgang styres av utleveringsforskriften, noe som gjør «enkel scraping» uaktuelt for et institusjonelt produkt. citeturn6search13turn6search26

Denne rapporten spesifiserer et “Bloomberg Terminal for eiendom” som er **eksplisitt norsk**: (1) en dataplattform som respekterer norsk rett (tinglysing, matrikkel, plan- og bygg, husleie, borettslag/eierseksjon, energimerking, eiendomsskatt, GDPR, AML, DORA), (2) et risikobibliotek som modellerer norske særtrekk som **borettslag/fellesgjeld**, **tvangssalg** og **olje-/regioneksponering**, og (3) dashboards som matcher arbeidsflyten til norske brukere (DNB/SpareBank 1-kreditt, KLP/Storebrand-portefølje, PE/fonds, listed property/utviklere, Finanstilsynet/Norges Bank/kommuner). Rapporten bygger på konkrete norske kilder og API-er: SSBs PxWebApi v2 (lansert høsten 2025, 7 500 tabeller, rate-limits) citeturn21search0turn21search8, Norges Banks åpne data-API (valuta og renter inkl. styringsrente/Nowa) citeturn23search0turn23search12, NVE kart-/GIS-tjenester (EUREF89/EPSG:25833 standard) citeturn23search20, samt Nasjonal arealplanbase (NAP) for regulerings-/kommuneplaner og høringer citeturn22search11turn22search23.

## Strategisk markedsforståelse

### Markedslandskap og brukerpersonas

Norsk eiendomsanalyse er i praksis et samspill mellom **offentlige registre** (Kartverket/SSB/NVE/kommuner), **kommersielle datavarehus** (Eiendomsverdi, Ambita m.fl.) og **transaksjons-/meglerøkosystemet** (FINN, DNB Næringsmegling, Malling/Newsec/CBRE osv.). Offentlig data finnes, men er ofte lisens- og tilgangsstyrt når personopplysninger inngår (grunnbok/matrikkel). citeturn6search13turn6search26

Nedenfor er 5 primære institusjonelle brukergrupper i Norge og hva en terminal må løse for dem.

| Brukertype (Norge) | Kritiske daglige oppgaver | Typiske nåverktøy | Norske pain points som plattform må løse |
|---|---|---|---|
| Bank/CRE-kreditt og porteføljerisiko (DNB, SpareBank 1, Nordea m.fl.) | Kredittbeslutning, belåningsgrad/LTV, kontantstrøm- og covenant‑overvåking, pante- og heftelsessjekk, tidlig-varsling (leietaker/utleier) | Excel/Power BI, interne kredittmotorer, grunnbokutskrifter via tredjepart (Ambita/Infoland), megler-/yieldrapporter | (1) Tidkrevende “collateral due diligence” på servitutter/heftelser; (2) uensartede leiekontraktdata; (3) svak kobling mellom eiendom → selskapsnettverk → betalings-/pantestatus; (4) begrenset “real‑time” risiko (tvangssalg/konkurs/utleggstrekk) |
| Pensjon/liv og institusjonelle eiendomsporteføljer (KLP, Storebrand m.fl.) | Asset allocation, porteføljeovervåking (risiko/avkastning), ESG/CSRD/taksonomi, klima‑ og overgangsrisiko, benchmarking mot indeks | Excel, porteføljesystemer, ESG‑verktøy, konsulentrapporter, benchmark‑indekser | (1) Krever sporbarhet til kilder (tilsyn/CSRD‑kontroll); (2) vanskelig å dokumentere EU‑taksonomi/energikrav på byggnivå; (3) geodata-klimarisiko må inn i investeringskomitéformat (heatmaps + forklarbarhet) |
| Fonds-/PE- og transaksjonsteam (norske og nordiske) | Screening av deal‑pipeline, comparables, DCF, sensitivitet (rente/valuta), scenariostresstest, markeds-/likviditetsanalyse | Excel/Argus‑lignende DCF, meglerdata, egne SQL/BI‑lag | (1) Mangler “single source of truth” for transaksjoner/yield/leie pr. mikrosegment; (2) må manuelt “normalisere” reguleringsstatus, byggkvalitet/TEK, energimerke og leietakerrisiko; (3) vanskelig å etterprøve data ved investor-DD |
| Store eiendomsbesittere/forvaltere og utviklere (OBOS Eiendom, børsnoterte, kommunale/Statsbygg‑lignende) | Leiekontraktstyring og reforhandling, capex/rehab, prosjektstyring, planstatus (kommune-/reguleringsplan), energitiltak | FDV/forvaltningssystemer, prosjektverktøy, kartportaler, manuell planinnsyn | (1) Plan-/reguleringsdata fragmentert; NAP løser mye, men må oversettes til “risiko/økonomi”; (2) TEK/energikrav og energimerking må kobles til CAPEX‑plan; (3) tenant churn/konkurs må inn som driftssignal |
| Regulatorer/tilsyn og offentlige analysebrukere (Finanstilsynet, Norges Bank, kommuner) | Systemrisiko (bolig/CRE), kreditt- og kapitalkravsforståelse, markedsovervåking (pris/volum), sårbarhetsanalyse klima/plan | Offentlige statistikker, rapporter/Excel, egne analysemodeller | (1) Behov for konsistente indikatorer og metadata; (2) sporbarhet og revisjonssti; (3) geografisk “drill‑down” uten å bryte personvern/tilgangsregler |

**Kjernekrav på tvers:** sporbarhet til lovlige datakilder, datakontrakter med lisens-/tilgangskontroll, geospatial “first-class” data (EUREF89/UTM), og risiko-/modellforklarbarhet.

### Segmentering og regionale dynamikker

**Bolig (boligmarkedet)** i Norge er sterkt datadrevet gjennom tinglyste transaksjoner og statistikk. SSBs eiendomsomsetningsstatistikk dekker tinglyst omsetning for alle typer fast eiendom og borettslagsboliger, fordelt på eiendomstype og omsetningstype. citeturn20search3  
**Boligmassen** (byggår, areal m.m.) ligger i stor grad på matrikkelgrunnlag; SSB beskriver selv at boligstatistikken bygger på opplysninger i matrikkelen og andre kilder. citeturn20search11turn20search15

**Næringseiendom (kontor, retail, hotell, “alternative”)** preges mer av private datasett (leie/yield/deals). Norske megler- og analyseselskaper publiserer løpende prime‑yields og markedsoppdateringer, f.eks. Newsec sin yield‑oversikt og DNB Næringsmegling sine sektorrapporter. citeturn4search4turn4search2

**Logistikk/industri** (inkl. “last mile”) krever mikrogeografi (tilgjengelighet, vei/knutepunkt) + klimarisiko (flom/skred) og energikapasitet. NVE peker på at deres WMS‑/karttjenester nå standardiseres på EUREF89/EPSG:25833, som forenkler integrasjon av farekart i samme koordinatsystem som norsk forvaltning. citeturn23search20

**Regionale drivere (typiske norske eksempler):**
Oslo/Akershus har høyest transaksjons- og likviditetsgrad og mest detaljert markedsovervåking (meglerhus, plan- og byutvikling). Stavanger/Rogaland har historisk tydeligere kobling til olje-/energisektor og sysselsettingssykler – dette bør modelleres som en særskilt makrofaktor (se risikomodulen). Bergen og Trondheim har egne universitets-/offentlig-sektor-drevne leiemarkeder og ulike tilbudsrestriksjoner via plan.

### Nøkkelaktører og verdikjeder

En terminal må forstå verdikjeden fra **tomt/plan → utvikling → salg/utleie → finansiering/risiko → drift/ESG**. I Norge er OBOS Eiendom et eksempel på en stor næringseiendomsaktør med portefølje på hundretusener av kvadratmeter og eiendommer i flere byer, mens DNB Næringsmegling er en sentral markedsaktør for næringseiendom og publiserer løpende markedsoppdateringer. citeturn7search3turn5search17

## Norsk dataøkosystem og plattformarkitektur

### Offentlige datakilder i Norge

Dette er kjernen i en institusjonell plattform: du må bygge på **autoritative registrer** og vite hvilke som er gratis, hvilke som krever avtale, og hvilke som er tilgangsstyrt.

#### Kartverket

Kartverket skiller mellom **matrikkel** (teknisk eiendomsregister: grenser, bygninger, adresser) og **grunnbok** (tinglyste rettigheter: eierskap, panteretter, servitutter). Eiendomsregisteret beskriver eksplisitt denne forskjellen. citeturn6search25turn6search1

Samtidig understreker Kartverket at eiendomsdata inneholder personopplysninger og at **utleveringsforskriften** bestemmer hvem som kan få tilgang til data i grunnbok og matrikkel. citeturn6search13turn6search26

**API-tilgang og kost:**
Kartverket beskriver et **tjeneste-API for grunnbok** som leverer informasjon i ulike formater (xml, pdf, tekst) og at det «ikke er øvre grense» for antall oppslag via tjenestene (forutsatt lovlig tilgang og avtale). citeturn10search21  
Kartverket/Geonorge har samtidig historikk på at enkelte matrikkel-uttrekk ble gratis tilgjengelig (f.eks. bygningspunkt/eiendomskart fra matrikkel), mens bekreftede grunnboksutskrifter og kopier fortsatt er betalt. citeturn6search17

**Geodata (kritisk for risiko):**
Kartverket tilbyr også åpne geodata/terrengdata via API og peker spesielt på at terrengdata kan brukes til flom- og rasanalyser. citeturn10search2  
For kyst/sea‑level finnes “Se havnivå” og et tilhørende API for vannstandsdata/tidevann. citeturn10search14turn10search29

#### SSB: Statistikkbanken (PxWebApi v2) og Klass

SSB lanserte **PxWebApi v2** høsten 2025, utviklet sammen med SCB, og oppgir at API-et gir tilgang til alle deres ~7 500 tabeller via GET og POST. citeturn21search0turn21search8  
SSB oppgir også konkrete API‑driftsrammer: **800 000 dataceller per uttrekk** og **30 spørringer per minutt** (per nå), og at API-ene er åpne og ikke krever registrering; data lisensieres under CC BY 4.0. citeturn21search2turn21search8

For en eiendomsplattform er følgende SSB-domener spesielt viktige:
SSBs **eiendomsomsetning** dekker tinglyst omsetning av alle typer fast eiendom og borettslagsboliger (omsetningsverdi, type, fritt salg m.m.). citeturn20search3  
SSBs **boligstatistikk** viser boligbestanden etter bygningstype, bruksareal, byggeår osv., og bygger på matrikkelgrunnlag. citeturn20search11turn20search15

Klass‑API (kodeverk/klassifikasjoner) er relevant for robuste dimensjoner (kommunenummer, næringskoder, regionnivåer osv.). SSB tilbyr en egen API-portal for Klassifikasjoner og kodelister (Klass). citeturn21search2turn21search6

#### Norges Bank: makro, renter, valuta, likviditet

Norges Bank har et **åpent data-API** som gir maskinell tilgang til utvalgt statistikk, implementert som REST-grensesnitt, med datasett for **valutakurser** og **renter** (styringsrente, Nowa og renter på norske statspapirer). citeturn23search0turn23search12  
Datatorget/Querybuilder bekrefter at tjenesten kan benyttes uten autentisering og viser oppdateringstider per datasett. citeturn23search7

For valutakurser presiserer Norges Bank at kursene publiseres daglig ca. kl. 16:00 CET og er midtkurser (indikative, ikke bindende). citeturn23search16  
Dette er direkte nyttig for valutaeksponering i real estate (NOK/EUR, NOK/USD) og for valutajusterte cashflow‑scenarier.

#### NIBOR / pengemarkedsreferanser

Nibor administreres av **Norske Finansielle Referanser AS (NoRe)**, et heleid datterselskap av Finans Norge; beregning/publisering utføres av Global Rate Set Systems (GRSS). citeturn23search9turn23search5  
For en institusjonell plattform bør NIBOR håndteres som en “benchmark time series” med governance‑metadata (metodikk, endringer, BMR‑krav). NoRe publiserer rammeverk og metodikkdokumenter for dette. citeturn23search19turn23search11

#### NVE: klima- og naturfare (flom, skred) + GIS-standardisering

NVE er kjerneleverandør av fysiske klimarisikodata (flomsoner, skredsoner, temakart). På GIS/standard-siden er det spesielt viktig at NVE oppgir at alle deres WMS/karttjenester er over på **EUREF89 (EPSG:25833)** som standard koordinatsystem. citeturn23search20  
Dette gjør “overlay” mot matrikkel/plan/eiendomsgeometri vesentlig enklere.

#### Energimerking og energidata: NVE + Enova

Plikt til energiattest og energivurdering av anlegg er regulert i **energimerkeforskriften** (forskrift 18.12.2009 nr. 1665). NVE peker på denne som hjemmel og at NVE fører tilsyn med etterlevelse. citeturn22search2turn22search14  
Lovdata-teksten for energimerkeforskriften sier at **Enova SF forvalter energimerkesystemet** innenfor forskriftens rammer. citeturn22search18  
Enovas energimerkeportal oppgir at du kan søke etter energiattester for boliger og bygninger i Norge (praktisk datainngang, men integrasjon må avklares juridisk/teknisk). citeturn22search22turn22search26

For mer generell energistatistikk (forbruk, tiltak, etc.) har Enova en dataportal for åpne data. citeturn2search3

#### Kommunale plan- og reguleringsdata: NAP, Geonorge og planstandarder

Kartverket beskriver **Nasjonal arealplanbase (NAP)** som et digitalt register med all arealplanlegging i Norge, basert på standarder for digital arealplanlegging og gjenbruk av planinformasjon. citeturn22search11turn22search23  
Kartverket påpeker også forventning om at planregister føres og oppdateres raskt (i samme kontekst nevnes “senest 8 dager etter vedtak”). citeturn22search11  
Geonorge “Plan” samler kommuneplaner og reguleringsplaner (inkl. planforslag) som nasjonale/regionale datasett. citeturn22search35

#### Meteorologisk institutt og Norsk klimaservicesenter

For historisk vær/klima og ekstremhendelser er MET Norges **Frost API** et robust utviklergrensesnitt for historiske observasjoner/klimadata. citeturn10search1turn10search5  
For fremtidige klimaframskrivninger og klimatilpasning er Norsk klimaservicesenter en sentral kilde (klimaframskrivninger og fylkesvise klimaprofiler publiseres bl.a. via Miljødirektoratet og klimaservicesenter). citeturn10search0turn10search19turn10search23

#### Radon og grunnforhold: NGU/DSA

DSA beskriver at NGU og DSA har utviklet et **nasjonalt radon-aktsomhetskart**, og at kartdata kan vises i WMS og lastes ned i ulike formater. citeturn10search7  
Dette kan være en “property hazard layer” i scorecard.

#### Brønnøysundregistrene: virksomhets-, insolvens- og heftelsesdata

Brønnøysundregistrene tilbyr åpne API-er for bl.a. Enhetsregisteret (OpenAPI‑dokumentasjon). citeturn21search32  
For risikomotorer er det spesielt relevant at BR tilbyr ITU/UTT (intet til utlegg / utleggstrekk) som API med Maskinporten-scope. citeturn20search6turn20search25  
BR har også statistikk fra Konkursregisteret (konkursbo og tvangsavviklingsbo) oppdatert løpende. citeturn20search5  
SSB publiserer samtidig konkursstatistikk (f.eks. kvartalsvis), som kan brukes til makro/region‑kredittsyklus. citeturn20search1

#### Domstoler: tvangssalg (foreclosure) som datainngang

Oslo tingrett publiserer nøkkeltall for **tvangssalg av bolig** (begjæringer, besluttede tvangssalg), som kan brukes som proxy for “foreclosure pressure” i markedet (og til PD/LGD‑kalibrering i kombinasjon med prisdata). citeturn20search8

#### Skatteetaten og kommunal eiendomsskatt

Eiendomsskatt er regulert i **eigedomsskattelova** og besluttes av kommunen. citeturn22search1turn22search5  
Skatteetaten beskriver at for kommuner som bruker Skatteetatens beregnede markedsverdi, hentes grunnlaget for eiendomsskatt fra skattemeldingen – relevant for modellering av skattekostnader og for å forklare avvik i kommunale takster. citeturn22search9

### Kommersielle/private datakilder

For å bli “institusjonell” må plattformen kombinere offentlige kilder med private datasett som dekker **pris/leie/yield i næring**, **transaksjonscomps**, **leietaker-/kontraktsdata**, og **ESG‑metadata**.

Kategorier og norske eksempler:

Transaksjoner og “market tape”:
Eiendomsverdi sier de samler, strukturerer og analyserer data om hele det norske eiendomsmarkedet (bolig/fritid/næring) og leverer et “sanntidsbilde” av prisene. citeturn6search16  
SSB dekker tinglyst omsetning bredt, men private aktører kan gi raskere/mer granular “feed” for visse segmenter og gjenbruke data i operasjonelle prosesser. citeturn20search3

Eiendomsdokumenter og integrasjon:
Ambita beskriver Eiendomsregisteret som tilgang til tinglyst informasjon fra grunnbok og teknisk info fra matrikkel, og at dette kan integreres via komponenter/REST/webservices i egne systemer. citeturn6search12turn6search5

Yield-/leie- og næringsmarkedsdata:
Newsec publiserer løpende prime‑yield oversikter. citeturn4search4  
DNB Næringsmegling publiserer sektoroppdateringer. citeturn5search17  
Malling & Co og Akershus Eiendom publiserer også markedsrapporter/nøkkeltall. citeturn4search0turn4search5  
CBRE publiserer markedsutsikter som kontekst for kapitalkostnad vs yield-spread (nyttig i stress). citeturn4search32

Proptech/forvaltning/FDV:
Visma Property Solutions posisjonerer seg som styrings- og beslutningsverktøy for aktører i næringseiendom. citeturn6search3turn6search28  
Placepoint posisjonerer seg som en plattform som samler data fra offentlige og private kilder til beslutningsgrunnlag. citeturn6search22

ESG-sertifiseringer:
I Norge er BREEAM‑NOR (Grønn Byggallianse) en sentral standard i nybygg/rehab for næring og ofte en del av investor- og leietakerkrav. citeturn3search3  
CSRD/taksonomi øker behovet for standardisert rapportering og kontroll (se regelverk). citeturn19search4turn19search16

### Data pipeline design og lagring i Norge

#### Datamodell: “Property graph + time series + geospatial”

En norsk “terminal” bør ikke starte med tabeller alene. Den bør starte med en **kanonisk objektmodell** som kan håndtere flere juridiske eiendomsformer og koblinger:

Kjerneobjekter:
Eiendomsenhet: gårds-/bruksnr (og festenr/sektion/anleggseiendom der relevant), samt borettslagsandel vs eierseksjon som ulike juridiske objekter  
Bygg og bruksenhet: bygnings‑ID, BRA, byggeår, energikategorier (TEK/rehab)  
Transaksjon: tinglyst overdragelse, kjøpesum, dato, type omsetning (fritt salg vs internt), megler, FINN‑annonsering (hvis lisensiert)  
Leiekontrakt: leietaker, areal, leie, indeksregulering, løpetid, opsjoner, garantier (bankgaranti/depositum)  
Finansiering/pant: pantedokumenter, prioritet, pantobligasjoner, fellesgjeld (borettslag), renter (NIBOR/fast/hedge)  
Planstatus: kommuneplan/reguleringsplan (NAP), hensynssoner, utnyttelsesgrad, byggeforbud, dispensasjoner  
Klima/geo: flom, skred, havnivå, radon, grunnforhold  
Selskap/person: juridiske eiere/utleiere/utviklere, konsernstruktur, konkurs/utleggstrekk (BR) citeturn21search32turn20search6turn20search5

Teknisk implikasjon: bruk **graph** for eierskapsnettverk og relasjoner, **time-series** for priser/renter/yields/ledighet, og **PostGIS** for alt romlig.

#### Koordinatsystem og geodata-standard

For norske karttjenester anbefales EUREF89 UTM‑soner, der EPSG:25833 er anbefalt for hele fastlands‑Norge og Svalbard, og EPSG:25832 anbefales for Sør‑Norge til og med Trøndelag. citeturn23search4  
NVE har standardisert sine WMS/karttjenester på EPSG:25833. citeturn23search20  
Dette bør bygges inn som “geospatial contract”: alle geometrier lagres i én standard SRID (typisk 25833), med kontrollert transformasjon der kilde SRID avviker. Kartverket beskriver også transformasjonsproblematikk og EUREF89‑relasjon til ITRF. citeturn23search2

#### Datainnhenting: batch + hendelser

Batch (daglig/ukentlig):
SSB PxWebApi v2 for pris-/volumtabeller, demografi, sysselsetting osv. (med rate limits og cell‑limits). citeturn21search8  
NAP/plan-data synkroniseringer  
Konkurs-/virksomhetsdata (BR)  
Klimafremskrivninger (Klimaservicesenter)

Strømming/hendelser (nær “real time”):
NIBOR/Nowa/policy rate (daglig) citeturn23search12turn23search9  
Valutakurser (daglig, ca 16:00 CET) citeturn23search16  
Kunngjøringer/utleggstrekk/endringslogger (der lovlig) via BR‑API for relevante brukergrupper citeturn20search6turn11search0  
Oppdateringer i grunnbok/matrikkel via avtalte kanaler (Kartverket/leverandører) citeturn10search21turn6search13

#### Norsk dataresidens og skyregioner

For institusjonelle kunder (bank/pensjon) må dataplattformen designes for **in‑country data residency** og robust tredjepartsstyring.

Azure:
Microsofts offentlige regionliste viser **Norway East** og **Norway West**, der Norway West er “restricted access” for spesifikke scenarier (typisk in‑country DR) og Norway East har availability zones. citeturn17view0turn15search8

Google Cloud:
Google har annonsert en kommende skyregion i Norge (Oslo), men Googles regionliste (oppdatert 27. mars 2026) viser ikke Norge som aktiv region ennå. citeturn13view0turn15search13  
Implikasjon: planlegg multi‑cloud/region‑fallback og vær eksplisitt i kontrakter om hvor data “at rest” og prosessering skjer.

AWS:
AWS sin offisielle regionliste viser Europa-regioner som Stockholm (eu-north-1) men ingen Norge-region. citeturn16view0  
AWS Local Zones‑listen per i dag inkluderer ikke Oslo (Nordics inkluderer bl.a. København/Helsinki). citeturn15search27

## Risikotaksonomi og analysemoduler

### Omfattende risikotaksonomi

Under er en praktisk risikoramme som kan implementeres som et **Risk Factor Library** + **Risk Engines** (beregning) + **Viz** (dashboard).

| Risikokategori | Norske nøkkelmål | Typiske data-inputs (Norge) | Modelltilnærming | Visualisering/UX-ide |
|---|---|---|---|---|
| Markedsrisiko | Prisindeks‑sjokk, cap rate‑skift, likviditet (omsetningshastighet) | SSB eiendomsomsetning og boligprisindekser citeturn20search3turn20search7 + megler/yieldrapporter citeturn4search4turn5search17 | Regime‑modeller (høy/lav likviditet), VaR/ES, scenario på yield‑spread vs rentekost | Heatmap pr. region/segment + “liquidity gauge” |
| Kredittrisiko (leietaker/utvikler) | PD/LGD, covenant‑brudd, rentebetjening | BR virksomhet/konkurs/ITU/UTT citeturn21search32turn20search5turn20search6 + kontraktsdata | Hazard‑modeller, rating‑mapping, nettverksrisiko (graph) | “Tenant watchlist” med hendelser og netting |
| Renterisiko | NIBOR/Nowa-sensitivitet, rentebinding, hedging-gap | Norges Bank renter (styringsrente/Nowa) citeturn23search12turn23search0 + NIBOR/NoRe citeturn23search9turn23search19 | DV01/convexity på CF, scenario (parallel shift/curve twist), basis‑risiko NIBOR vs Nowa | Interaktiv “rate ladder” + CF waterfall |
| Konsentrasjonsrisiko | Geografi, segment, leietaker, enkeltasset‑størrelse | Porteføljestruktur + plan/geo | Herfindahl, tail‑risk konsentrasjon, “single point of failure” | Treemap + kart med eksponering |
| Regulatorisk/politisk | Planendringer, TEK17, eiendomsskatt, husleie | NAP/plan-data citeturn22search11turn22search23, TEK17 citeturn18search0turn18search2, eigedomsskattelova citeturn22search1, husleieloven citeturn8search3 | “Policy event” stresstest, klassifisering av planrisiko | Planstatus‑kort m/ varsling |
| Fysisk klimarisiko | Flom, skred, havnivå, radon | NVE hazard layers (EPSG:25833) citeturn23search20, Kartverket Se havnivå API citeturn10search14turn10search29, DSA/NGU radon WMS citeturn10search7, MET/Frost citeturn10search1 | Score per hazard + forventet skadeandel (PML), “damage functions” + klimaframskrivningsscenario citeturn10search23 | Kart-overlay + “hazard stack” per eiendom |
| Overgang/ESG | Energimerke, taksonomi‑alignment, CSRD‑krav | Energimerking (forskrift + portal) citeturn22search18turn22search22, CSRD-regler & kontroll citeturn19search4turn19search2, taksonomi citeturn19search16turn19search3 | ESG‑score med forklarbarhet/kravmapping, CAPEX‑baner | “EU Taxonomy readiness” + tiltaksliste |
| Verdivurderingsrisiko | AVM‑CI, bias, datakvalitet | Transaksjoner, matrikkel/bygg, plan, energimerke | Model risk management: drift/bias, backtest, CI‑kalibrering | “Confidence cone” + avvik mot takst |
| Norske sær-risikoer | Fellesgjeld, tvangssalg, olje-/regionsjokk | Borettslagstruktur (andel/eier), domstol tvangssalg-proxy citeturn20search8, SSB/BR konkurser citeturn20search1turn20search5 | Kaskade‑modell for fellesgjeld, stress-scenario “Rogaland olje” (makro‑proxy), tvangssalgsrabatt‑justering | “Borettslag‑sårbarhetskort” + tvangssalg‑monitor |

### Analytikk- og modellbibliotek

#### Automatiserte verdivurderinger (AVM) for Norge

En norsk AVM må ta høyde for:
Juridisk boligtype: eierseksjon vs borettslagsandel (andel kan innebære fellesgjeld og andre rettigheter/pliktsett gjennom borettslagslova). citeturn8search0turn8search1  
Datatilgang: matrikkel/byggdata og tinglyst omsetning (SSB) gir bred dekning, mens høykvalitets “features” ofte krever avtaler. citeturn20search3turn6search13

Anbefalt AVM‑stack:
Hedonisk base: log‑pris ~ areal + byggeår + standard + beliggenhetsfaktorer + etasjeposisjon + energimerke + plan/hensynssoner  
Moderne ML: gradient boosting / random forest / deep tabular for ikke‑linearitet  
Geospatial embedding: “micro‑location” med grid/POI/tidsreise (tilgjengelighet)  
Robust CI: konform prediksjon eller quantile regression for å gi konfidensintervall som kan brukes i kreditt/kapital

Norske “må‑features” i praksis:
fellesgjeld‑justert totalpris (der mulig), energimerke (pliktig ved salg/utleie) citeturn22search6turn22search18, og planstatus (NAP) citeturn22search11.

#### Porteføljeanalyse: stress og scenarioer relevant for Norge

Rente- og kredittsyklus:
Koble styringsrente (Norges Bank) og NIBOR/Nowa (pengemarked) til cap rates og diskonteringsrenter. citeturn23search12turn23search9  
Bruk yieldtabeller fra markedsaktører til å lage “prime yield vs funding cost”‑indikator (carry‑gap). citeturn4search4turn4search32

Likviditet:
Transaksjonsvolumer (SSB) + “days on market” fra private/annonserte data → likviditetsscore. citeturn20search3turn5search2

Kreditt/insolvens:
Konkursstatistikk (SSB) og Konkursregisteret (BR) som makro- og bransjeindikator. citeturn20search1turn20search5  
ITU/UTT som mikro‑signal for betalingspress (der lovlig tilgang/bruk). citeturn20search6turn20search18

#### Kontantstrømmodellering og skatt

Eiendomsskatt:
Modellér kommunal eiendomsskatt med lovgrunnlag + kommunale satser. citeturn22search1turn22search33  
Skatteetaten beskriver hvordan skattemeldingsgrunnlag kan inngå i eiendomsskatt i noen kommuner. citeturn22search9

Formuesverdi (næringseiendom):
Skatteetaten har egne regler og satser (kalkulasjonsfaktor m.m.) for formuesverdsettelse av næringseiendom; relevant for private/institusjoner som vurderer formueskatt/rapportering. citeturn5search0turn5search27

### Norske risikodashboards og indikatorer

#### Makro-dashboard (Norge)

Kjerneindikatorer (oppdateres automatisk):
Styringsrente (Norges Bank) citeturn23search22turn23search12  
Pengemarkedsrenter (NIBOR via NoRe) citeturn23search9turn23search5  
Valuta (Norges Bank) citeturn23search16  
Boligtransaksjoner/volum (SSB eiendomsomsetning) citeturn20search3  
Konkursrate (SSB/BR) citeturn20search1turn20search5

#### Property-level scorecard (Norge)

Minsteinnhold for institusjonelt scorecard:
Juridisk status: eierseksjon / andel / festetomt (tomtefesteloven) citeturn8search1turn9search0  
Heftelser/servitutter: tinglysing/servituttlova citeturn9search1turn9search3  
Planstatus: reguleringsformål, utnyttelse, hensynssoner (NAP) citeturn22search11  
Energimerke og energikrav: energimerkeforskriften + TEK17 som “minimumskrav” referanse citeturn22search18turn18search0  
Klimarisiko: flom/skred (NVE), havnivå (Kartverket), radon (DSA/NGU) citeturn23search20turn10search14turn10search7  
Fellesgjeld‑profil (for borettslag): modellert internt basert på tilgjengelige data og brukerinnhentet info, med borettslagslova som juridisk ramme citeturn8search0

#### Dash-wireframes per persona

> Wireframes er skisser (ikke UI-design), ment å beskrive informasjonsarkitektur.

**Bank/CRE-kreditt (underwriter)**
```text
[Search: gnr/bnr | adresse | orgnr | bygg-id ]      [Alert bell: covenant | pant | konkurs | ITU/UTT]

COLLATERAL OVERVIEW (1 side)
- Juridisk: eierseksjon/andel/feste
- Grunnbok: pant (prioritet), servitutter, heftelser
- Verdi: AVM (P50/P10/P90) + siste comps + takst-upload
- Rente: NIBOR/Nowa exposure + hedge gap
- Klima: flom/skred/havnivå/radon (score + kart)
- Plan: reguleringsstatus + risiko for omregulering
- Leie: DSCR, WAULT, top tenants + PD

Right panel:
- "Explain score" (top 10 drivere)
- Dokumentpakke (PDF) + audit trail
```

**Pensjon/liv (portefølje og ESG)**
```text
PORTFOLIO HOME
- KPI: IRR/NOI, yield, gearing, VaR, climate PML, taxonomy alignment
- Heatmap: Norge -> region -> kommune
- Lease ladder + refinancing ladder
- ESG: energy label distribution + retrofit pipeline + CSRD readiness

Drilldown: Asset -> "EU Taxonomy evidence" tab (kilder, dokumentasjon)
```

**PE/fonds (deal screening)**
```text
DEAL PIPELINE
- Opportunities list (score: price/yield, risk-adjusted return, plan risk, climate)
- Comps panel (transactions + rent/yields)
- DCF builder (scenario templates)
- "What changed since yesterday" (rates, plan updates, tenant events)

Export: IC memo pack + data room checklist
```

**Eiendomsbesitter/utvikler**
```text
ASSET OPS
- Tenant health: arrears proxy, sector risk, bankruptcy signals
- CAPEX plan: TEK/energy gaps + retrofit ROI
- Plan & permits: NAP plan status + upcoming hearings
- Klima: mitigation actions checklist
- Ops tickets link (FDV integration)

Project view: pipeline of rehab/newbuild + scenario on rent/yield
```

**Regulator/offentlig analyse**
```text
SYSTEM MONITOR
- Housing & CRE stress indicators (volume, price momentum, defaults proxies)
- Region dashboard (municipality-level)
- Climate vulnerability cross-tabs
- Data provenance + disclosure controls (privacy-safe aggregates)

Download: standardized indicator series + methodology notes
```

#### Risk Factor Library (utdrag)

| Faktor | Kategori | Norsk kilde | Oppdatering | Default vekt (eksempel) |
|---|---|---|---|---|
| Styringsrente | Renter | Norges Bank (policy rate/Datatorg API) citeturn23search12turn23search22 | Daglig | 0,12 |
| NIBOR 3M/6M | Renter | NoRe/Finans Norge citeturn23search9turn23search5 | Daglig | 0,10 |
| NOK/EUR | Marked/valuta | Norges Bank valutakurser (API) citeturn23search16turn23search0 | Daglig | 0,05 |
| Eiendomsomsetning volum | Likviditet | SSB eiendomsomsetning citeturn20search3 | Måned/kvartal (avh. tabell) | 0,08 |
| Konkursrate | Kreditt/makro | SSB konkurser + BR konkursregister citeturn20search1turn20search5 | Kvartal + løpende | 0,06 |
| Flomfareklasse | Klima | NVE farekart (WMS/WFS) citeturn23search20 | Periodisk (kartoppdatering) | 0,07 |
| Skredfareklasse | Klima | NVE farekart (WMS/WFS) citeturn23search20 | Periodisk | 0,07 |
| Havnivå/stormflo | Klima | Kartverket Se havnivå API citeturn10search14turn10search29 | Daglig/varsler + scenario | 0,04 |
| Radon aktsomhet | Helse/bygg | DSA/NGU WMS citeturn10search7 | Sjeldnere | 0,02 |
| Energimerke (A–G) | ESG/overgang | Energimerkeforskriften + Enova/NVE system citeturn22search18turn22search22 | Ved endring | 0,06 |
| Planstatus (uavklart/vedtatt) | Regulatorisk | NAP (Kartverket/DiBK) citeturn22search11turn22search23 | Løpende/døgnlig | 0,08 |
| Tvangssalg‑rate (proxy) | Kreditt/marked | Oslo tingrett nøkkeltall citeturn20search8 | Årlig/periodisk | 0,03 |

> Vekter er illustrerende; i en institusjonell plattform bør de kalibreres per segment (bolig vs kontor vs logistikk) og per region.

## Regelverk, compliance og operasjonell styring

### Eiendomsrett og tinglysing

**Tinglysing / grunnbok:**
Tinglysingsloven regulerer registrering og rettsvirkning av tinglysing. citeturn9search1  
Servituttlova regulerer særretter over fremmed eiendom (servitutter som veirett, båtfeste osv.). citeturn9search3

**Matrikkel:**
Matrikkellova regulerer eiendomsregistrering og har formål å sikre tilgang til viktige eiendomsopplysninger gjennom et ensartet register (matrikkelen). citeturn9search2turn9search6

**Boligjuridikk:**
Burettslagslova (borettslag) citeturn8search0  
Eierseksjonsloven (eierseksjoner/eierleiligheter) citeturn8search1  
Tomtefesteloven (feste/leie av grunn) citeturn9search0  
Husleieloven (leie av husrom) citeturn8search3  
Plan- og bygningsloven (planlegging og byggesaksbehandling) citeturn8search2

### Byggkrav og energi: TEK17 og energimerking

Tekniske minimumskrav til byggverk følger av byggteknisk forskrift (TEK17). citeturn18search0turn18search2  
Energikrav og dokumentasjon er dermed en reell finans-/verdirisiko i rehabiliterings- og utviklingscaser.

Energimerking er regulert i energimerkeforskriften, der Enova forvalter systemet og NVE fører tilsyn. citeturn22search18turn22search14

### Personvern, AML, DORA og sky/outsourcing

**GDPR/personvern og eiendomsdata:**
Kartverket presiserer at eiendomsdata inneholder personopplysninger og at virksomheter må ha lovlig behandlingsgrunnlag; tilgang reguleres gjennom utleveringsforskriften. citeturn6search13turn6search26  
Dette betyr: plattformen må ha **tilgangsstyring per datakilde og kunde**, og i mange tilfeller levere **aggregerte/avidentifiserte visninger** til brukere uten lovlig grunnlag.

**AML (hvitvasking):**
Hvitvaskingsloven (lov 2018-06-01-23) setter rammer for forebygging/avdekking av hvitvasking og terrorfinansiering. citeturn22search0turn22search4  
For eiendomsplattformer som brukes i transaksjoner, betyr dette at onboarding, tilgang, logging og transaksjonsmonitorering kan bli en del av produktkrav (særlig mot meglere/bank).

**DORA (digital operasjonell motstandsdyktighet):**
Finanstilsynet beskriver at DORA er gjennomført i DORA‑loven og trådte i kraft 1. juli 2025, med krav til styring av IKT-risiko, hendelser, testing og tredjepartsrisiko. citeturn19search1turn19search14  
En leverandør til finanssektoren bør derfor levere “DORA-ready” funksjoner: hendelseslogg, SLA/OLA, tredjepartsregister, sikkerhetskontroller, og revisjonsvennlig dokumentasjon.

**Utkontraktering/IKT (før og etter DORA) + sky:**
Finanstilsynets ICT‑regulasjoner og europeiske sky‑retningslinjer peker på styrebehandling av outsourcing, risikoanalyse og kontroll av utkontrakterte ICT‑aktiviteter. citeturn11search18turn11search10  
Finanstilsynet viser også til at DORA erstatter IKT-forskriften for mange foretak fra 1. juli 2025. citeturn19search14

**Norsk eID og API-sikring:**
Maskinporten brukes for maskin‑til‑maskin autentisering og scope‑styring for flere offentlige API-er. citeturn11search0turn11search8  
ID‑porten støtter OAuth2/OIDC‑flyter for brukerstyrt datadeling i offentlig sektor. citeturn11search1  
Selv om en kommersiell “terminal” typisk bruker BankID/enterprise IAM, er Maskinporten/ID‑porten relevant der du integrerer mot offentlige datatjenester som krever dette.

#### Regulatory Compliance Checklist (utdrag)

| Regelverk/krav | Impact på plattform | Tiltak | Tid/ansvar |
|---|---|---|---|
| Utleveringsforskriften (tilgang til grunnbok/matrikkel) | Tilgangsstyrt/rollebasert innsyn i personopplysninger | Implementer “source‑level entitlements”, logging, dataminimering; kontraktfest behandlingsgrunnlag per kunde citeturn6search13turn6search26 | Før data‑onboarding (Legal + Security) |
| Tinglysingsloven | Korrekt tolkning av rettigheter/heftelser | Normaliser dokumenttyper, prioritet, historikk; lag “legal facts”-modul citeturn9search1 | MVP+ |
| Matrikkellova | Korrekt eiendoms- og bygningsidentitet | “Golden ID” + kvalitetstester og endringshåndtering citeturn9search2 | MVP |
| Plan- og bygningsloven + NAP | Planstatus påvirker verdi/risiko | Integrer NAP + planbestemmelser; varsling på planendring/høring citeturn22search11turn8search2 | Fase 2 |
| TEK17 | Energikrav/material- og klima‑krav påvirker CAPEX | Regelmotor for TEK‑relevante checks pr. byggkategori citeturn18search0turn18search2 | Fase 2–3 |
| Energimerkeforskriften | Energimerke som datapunkt og compliance | Innhent energiattestdata lovlig; lag energimerke‑QA og audit trail citeturn22search18turn22search14 | Fase 1–2 |
| Eigedomsskattelova | Kommunal skatt i DCF og risiko | Kommune-satsbibliotek + beregningsmodul citeturn22search1turn22search33 | Fase 2 |
| Hvitvaskingsloven | Relevans for KYC/monitorering | KYC/KYB-workflow, logging, rettighetsstyring citeturn22search0 | Fase 2 (hvis megler/bank) |
| DORA (for finanskundene) | Krav til leverandørstyring og motstandsdyktighet | Drift/beredskap, hendelseshåndtering, tredjepartsregister, revisjonsspor citeturn19search1turn19search0 | Fase 1–2 (grunnmur) |
| CSRD/taksonomi | ESG-rapportering og kontroll | ESRS-mapping, sporbarhet, “evidence pack”; støtte for “stopp-klokken”/overgangsregler citeturn19search2turn19search4turn19search3 | Fase 3 |

## Teknisk arkitektur og implementeringsplan

### Teknisk løsningsarkitektur

Prinsipp: **datakatalog + rettighetsmotor + risikomotor** før fancy UI.

#### Arkitekturdiagram

```text
Norske datakilder
  - Kartverket (grunnbok/matrikkel; avtale/entitlements)
  - SSB PxWebApi (åpen)
  - Norges Bank API (åpen)
  - NVE/MET/NGU/DSA (kart/klima)
  - NAP/plan (Kartverket/DiBK/Geonorge)
  - BR (enhet/konkurs/utlegg) + Maskinporten
  - Private: Eiendomsverdi, Ambita, megler/yield, ESG
        |
        v
Inntak & kvalitet (batch + streaming)
  - Connectors (API/WMS/WFS/fil)
  - Data contracts + schema registry
  - Geospatial normalization (EUREF89 / EPSG:25833)
  - PII classification + entitlements
        |
        v
Lagring
  - Data Lake (rå + kuratert)
  - Warehouse (fakta/dimensjoner)
  - PostGIS (geometri + raster/tiles)
  - Time series store (renter, indeks, pris)
  - Graph store (eierskap/konsern/leietaker)
        |
        v
Analytikk & risikomotor
  - AVM service + model registry
  - Risk scoring (market/credit/climate/ESG/legal)
  - Scenario/stresstest (Monte Carlo)
  - NLP for norske dokumenter (planbestemmelser, kontrakter)
        |
        v
API-lag
  - API Gateway + auth (BankID/enterprise IAM; Maskinporten for enkelte kilder)
  - Query API (fast + ad hoc)
  - Exports (IC memo, regulator pack)
        |
        v
Terminal-UI (web)
  - Dashboards pr persona
  - Kartvisning (basemap + temalag)
  - Alerting & watchlists
  - Audit trail & source citations
```

#### Databaser og nøkkelvalg

Geospatial:
Bruk PostGIS og standardiser SRID til EPSG:25833 som “warehouse SRID” (samsvar med NVE/default og Geonorge‑anbefalinger). citeturn23search20turn23search4

Time series:
Renter og makroserier: Norges Bank API (policy rate/Nowa/valuta) citeturn23search12turn23search0 + NIBOR (NoRe) citeturn23search9

Graph:
Eierskap/konsern og leietakerrelasjoner: BR enhetsdata + interne kundedata. citeturn21search32

Security-by-design:
Kildenivå‑rettigheter (grunnbok/matrikkel), PII‑klassifisering, og “audit trail” for alle beregninger som brukes i kreditt/rapportering. citeturn6search13turn19search4

### Implementeringsroadmap

Roadmapen under er mappet til brukerens ønskede faser, men konkretisert som leveransepakker som reduserer risiko tidlig.

#### Implementerings-Gantt (forenklet)

| Periode | Milepæler | Kritiske avhengigheter |
|---|---|---|
| Måneder 1–6 (MVP) | SSB + Norges Bank + NVE grunnintegrasjoner; geospatial grunnmur (EPSG:25833); Oslo bolig AVM v1; 1 pilotkunde; audit trail v1 | SSB PxWebApi v2 drift/limiter citeturn21search8; Norges Bank API citeturn23search12; NVE karttjenester citeturn23search20 |
| Måneder 7–12 (Core) | NAP planmodul; næringsmodul (yield/leie); porteføljeanalyse; API marketplace v0; multi‑region DR i Norge | NAP standardisering/tilgang citeturn22search11turn22search23; skyregionvalg (Azure Norway) citeturn17view0 |
| Måneder 13–24 (Advanced) | ML‑AVM v2, klimarisiko PML, “real‑time” overvåking (konkurs/utlegg) der relevant; stresstestbibliotek | BR ITU/UTT + Maskinporten citeturn20search6turn11search0; Klimaservicesenter data citeturn10search23 |
| 36+ måneder | Full “Nordic” arkitektur, cross‑country modellramme, institusjonelle investorverktøy | Google Cloud Norge-region status kan endre seg; planlegg uten å avhenge av det citeturn13view0turn15search13 |

#### Team-sammensetning (minimum for institusjonell kvalitet)

Kritiske roller (rekkefølge):
Dataarkitekt (geospatial + master data), backend lead (microservices), sikkerhets-/compliance lead (DORA/GDPR), kvant/ML lead (AVM + risk models), produktsjef (bank/pensjon workflow), og “data partnerships” lead (Kartverket/kommersiell data).

Merk: For finanskunder må leverandørstyring og operasjonell motstandsdyktighet være på plass tidlig pga DORA‑krav. citeturn19search1turn19search14

### API-integrasjonsprioritering

#### API Integration Priority Matrix

| Integrasjon | Verdi | Kompleksitet | Kost | Prioritet |
|---|---:|---:|---:|---|
| SSB PxWebApi v2 | Svært høy (grunnindikatorer) | Lav–middels | Gratis | P0 citeturn21search0turn21search8 |
| Norges Bank åpne data API | Høy (renter/valuta) | Lav | Gratis | P0 citeturn23search12turn23search0 |
| NVE WMS/WFS hazard layers | Høy (klima/risiko) | Middels (geo) | Ofte gratis | P0 citeturn23search20 |
| NAP (plan-/reguleringsdata) | Høy (regulatorisk/verd) | Middels | Varierer | P1 citeturn22search11turn22search23 |
| MET Frost API | Middels (ekstremvær/feature store) | Middels | Gratis | P1 citeturn10search1turn10search5 |
| BR enhetsdata API (åpne data) | Høy (motpart/konsern) | Lav | Gratis | P1 citeturn21search32 |
| BR konkurs/ITU/UTT + Maskinporten | Høy (early warning) | Høy (tilgang/regel) | Varierer | P2 citeturn20search6turn11search0 |
| Kartverket grunnbok/matrikkel API (avtale) | Svært høy (legal truth) | Høy (tilgang/PII) | Betalt/avtale | P2 citeturn10search21turn6search13 |
| Energimerkeportal (Enova/NVE) | Middels–høy (ESG) | Middels (juridisk/teknisk) | Varierer | P2 citeturn22search18turn22search22 |
| Private markedsdata (yield/leie/deals) | Svært høy (næring) | Middels | Betalt | P2–P3 citeturn4search4turn4search2turn6search16 |

## Konkurranse og forretningsmodell

### Konkurranselandskap

Norge har flere sterke nisjeaktører, men det finnes et tydelig gap for en integrert risiko-/analytikkterminal med institusjonell kontroll (audit trail, modellstyring, geospatial risiko som standardfunksjon).

Lokale aktører (eksempler med tydelig posisjonering):
Eiendomsverdi: bred markedsdatabase og “sanntidsbilde” av prisene. citeturn6search16  
Ambita/Infoland: eiendomsinfo, plandata og integrasjonstjenester. citeturn6search5turn6search12  
Visma Property Solutions: beslutnings-/styringsverktøy for næringseiendom. citeturn6search3turn6search28  
Placepoint: “arbeidsflate” som samler offentlige/private data for beslutninger. citeturn6search22  
Megler- og researchmiljø (Malling, DNB Næringsmegling, Newsec, CBRE): markedsrapporter, yields og analyser. citeturn4search0turn5search17turn4search4turn4search32

> Om “Ovius” og “GENA.no”: i åpne kilder identifiseres ikke entydig en norsk eiendomsplattform med dette navnet. I denne rapporten er derfor Visma Property Solutions og Placepoint brukt som konkrete eksempler på norske plattformer i “arbeidsflate/forvaltning”-kategorien. citeturn6search3turn6search22

#### Competitive Positioning Map

| Player | Styrker | Svakheter | Indikativ pris | Målsegment |
|---|---|---|---|---|
| Eiendomsverdi | Sterk dekning, profesjonelle verktøy, prisbilde citeturn6search16 | Primært data/verdi – ikke full risiko-/compliance-motor | Ikke offentlig | Bank, megler, proff |
| Ambita/Infoland | Offisiell dokumentflyt + integrasjoner citeturn6search5turn6search12 | Ikke “portfolio risk terminal” | Ikke offentlig | Megler, bank, forvaltning |
| Visma Property Solutions | Forvaltning/styring næring citeturn6search3turn6search28 | Ikke primært et tverrmarked “terminal”-produkt | Ikke offentlig | Forvaltere/eiere |
| Placepoint | Datakontekst og arbeidsflate citeturn6search22 | Avhenger av datapartnerskap; risiko‑modell dybde varierer | Ikke offentlig | Eiendom/utvikling |
| Newsec/Malling/DNB/CBRE (research) | Markedskontekst, yields, segmentinnsikt citeturn4search4turn4search0turn5search17turn4search32 | Ikke integrert data+modell+workflow; ofte rapportformat | Rapport/abonnement | Investorer/bank/megler |
| MSCI/CoStar/Green Street/Altus (internasjonalt) | Institusjonell standard, benchmark | Norge-dekning ofte begrenset; integrasjon med norske registre | Høy | Multinasjonale |

### Business model og prising

Et “Bloomberg for eiendom” blir troverdig når:
produktet reduserer tid i due diligence, forbedrer kreditt/IC‑beslutninger, og leverer compliance‑klar dokumentasjon.

Forslag til tiers (Norge-spesifikt):
Tier Base (utvikler/megler): markedsdashboard + comps + plan/klima grunnkart  
Tier Pro (forvalter/utvikler): leie/DCF + plan/ESG + alerts  
Tier Institutional (bank/pensjon/PE): full risikomotor + modellstyring + API + audit packs  
Tier Regulator (spesial): aggregerte indikatorer + metodikk + eksport

Betalingsvilje:
Bloomberg‑benchmark (~24k USD/år) er en referanse i finans, men eiendomsterminalen må typisk prises lavere per sete i Norge i tidlig fase – og høyere for enterprise‑funksjoner (API, compliance, datalisenser). (Pris er modellantakelse, ikke offentlig markedstall.)

#### Business Model Canvas (Norge)

| Blokk | Norge-spesifikk utforming |
|---|---|
| Kundesegmenter | Banker (DNB/SpareBank 1), pensjon/liv, PE/fond, utviklere/eiere, meglere, offentlige analysebrukere |
| Verdiforslag | “Single source of truth” for eiendom + risikoscore + plan/klima/ESG + audit‑klar dokumentasjon |
| Kanaler | Direkte B2B-salg, partnerskap med dataleverandører, pilot med 1 institusjon |
| Kunderelasjon | Onboarding + data governance workshops; “model governance” rapporter; support SLA |
| Inntektsstrømmer | Abonnementsseter + enterprise minimum + API‑bruk + profesjonelle tjenester |
| Nøkkelressurser | Datapartnerskap (Kartverket/privat), geospatial stack, modellregister, compliance |
| Nøkkelaktiviteter | Datainnhenting, kvalitetskontroll, modellering, sikkerhet, dashboard UX |
| Partnere | Kartverket/Geonorge/NAP, SSB, Norges Bank, NVE/MET/NGU, BR; private (Eiendomsverdi/Ambita/yield‑aktører) |
| Kostnader | Datalisenser, skylagring i Norge, sikkerhet/revisjon, FoU/ML, salgsapparat |

### Femårig finansmodell (eksempel, base-case)

**Antakelser (for enkel planlegging):**
Salg i “land and expand”: 1–2 piloter → 3–6 institusjoner → 10+  
ARPU per sete øker med funksjonsnivå og datalisenser  
Enterprise minimum for bank/pensjon dekker datalisenser og compliance

> Tallene under er illustrative (forretningsplan), ikke markedstall.

| År | Banker (ARR) | Pensjon/liv (ARR) | PE/fond (ARR) | Utviklere/eiere (ARR) | Meglere/andre (ARR) | Totalt ARR |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3,0 MNOK | 1,5 MNOK | 0,8 MNOK | 0,7 MNOK | 0,3 MNOK | 6,3 MNOK |
| 2 | 6,0 MNOK | 3,0 MNOK | 2,0 MNOK | 1,5 MNOK | 0,8 MNOK | 13,3 MNOK |
| 3 | 10,0 MNOK | 5,0 MNOK | 3,5 MNOK | 2,5 MNOK | 1,5 MNOK | 22,5 MNOK |
| 4 | 15,0 MNOK | 7,0 MNOK | 5,0 MNOK | 4,0 MNOK | 2,5 MNOK | 33,5 MNOK |
| 5 | 20,0 MNOK | 9,0 MNOK | 6,5 MNOK | 5,5 MNOK | 3,5 MNOK | 44,5 MNOK |

Kostnadsdrivere:
Data-lisenser (grunnbok/matrikkel og private markedsdata), sikkerhet og revisjon (særlig mot finans pga DORA), samt geospatial lagring/tiles. DORA‑krav og tredjepartsrisiko vil også påvirke leveransemodell for finanskundene. citeturn19search1turn11search22

## Bibliografi

Kartverket / Geonorge:
Kartverket – Eiendomsdata (tilgang, utleveringsforskriften) citeturn6search13turn6search26  
Kartverket – Grunnbok tjeneste‑API dokumentasjon citeturn10search21  
Kartverket – Se havnivå og API for vannstandsdata citeturn10search14turn10search29  
Kartverket – Forvaltning og distribusjon av plandata / NAP citeturn22search11turn22search23  
Geonorge – Kartprojeksjoner og anbefalte koordinatsystemer (EUREF89/UTM EPSG) citeturn23search4  
Geonorge – Plan datasett citeturn22search35

SSB:
SSB – PxWebApi v2 og brukerveiledning (rate limits) citeturn21search0turn21search8  
SSB – Eiendomsomsetning (tinglyste transaksjoner) citeturn20search3  
SSB – Boliger (boligbestand) citeturn20search11turn20search15  
SSB – Konkurser (offisiell statistikk) citeturn20search1

Norges Bank og pengemarked:
Norges Bank – API for åpne data / Datatorg citeturn23search0turn23search12turn23search7  
Norges Bank – Valutakurser og publiseringstid citeturn23search16  
NoRe / Finans Norge – NIBOR administrasjon og rammeverk citeturn23search9turn23search19turn23search5

NVE/MET/klima:
NVE – Koordinatsystem for karttjenester (EPSG:25833) citeturn23search20  
MET – Frost API citeturn10search1turn10search5  
Klimaservicesenter – klimaframskrivninger citeturn10search23turn10search0

Energimerking/ESG:
Lovdata – Energimerkeforskriften citeturn22search18  
NVE – energimerking og tilsyn citeturn22search2turn22search14  
Enova – energimerkeportal citeturn22search22turn22search26  
Finanstilsynet – kontroll med bærekraftsrapportering (CSRD) citeturn19search4  
Regjeringen – bærekraftsrapportering/overgangsregler (“stopp‑klokken”) citeturn19search2  
Regjeringen/Finanstilsynet – taksonomi og forenklinger citeturn19search16turn19search3turn19search5

Lovverk (Lovdata):
Plan- og bygningsloven citeturn8search2  
TEK17 (byggteknisk forskrift) citeturn18search0  
Husleieloven citeturn8search3  
Burettslagslova citeturn8search0  
Eierseksjonsloven citeturn8search1  
Tomtefesteloven citeturn9search0  
Tinglysingsloven citeturn9search1  
Servituttlova citeturn9search3  
Eigedomsskattelova citeturn22search1  
Hvitvaskingsloven citeturn22search0  
DORA‑loven citeturn19search0turn19search1

Offentlig digital infrastruktur:
Digdir – Maskinporten (API-konsumentguide) citeturn11search0  
Digdir – ID‑porten (OAuth2/OIDC) citeturn11search1