---
layout: default
title: Palonosetron
parent: Måttlig evidens (L3-L4)
nav_order: 336
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-28
description: "Palonosetron: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L4). Ursprunglig indikation: Ej angiven i tillgängliga data"
monitor_inn: "palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Evidensnivå: **L4** | Förutsagda indikationer: **4** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

## Palonosetron: Från ej angiven ursprunglig indikation till migrän
{: .text-alpha }

---

### Sammanfattning

Palonosetron är en 5-HT3-receptorantagonist. Den ursprungliga indikationen finns inte angiven i de data som har sammanställts för denna rapport, men substansen används i regel mot illamående och kräkningar. TxGNN-modellen (deep learning) förutsäger att palonosetron kan vara effektivt mot **migrän** (poäng 0,9974), men det finns **inga kliniska prövningar** och bara **en fallrapport**, som dessutom beskriver att palonosetron *orsakar* migränliknande huvudvärk. Evidensen för förutsägelsen är därför mycket svag.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga data |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 0,9974 |
| Evidensnivå | L4 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 6 av 6) |
| Antal godkännanden | 6 (giltiga: 6) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Palonosetron är dock allmänt känt som en 5-HT3-receptorantagonist, och eftersom serotonin är inblandat i migränens patofysiologi är ett samband tänkbart.

Den enda litteratur som kopplas till migrän pekar dock åt motsatt håll. Fallrapporten från 2011 beskriver migränliknande huvudvärk som en biverkning av palonosetron, och huvudvärk är en känd biverkning av 5-HT3-antagonister. Modellens höga poäng bygger alltså på grafbaserad närhet, inte på stöd för behandlingseffekt.

De övriga förutsägelserna (migrän med hjärnstammsaura, migränrelaterad genetisk känslighet, atrofodermi vermiculata och ulerythema ophryogenes) har ingen eller bara indirekt evidens. Migrän med hjärnstammsaura är sannolikt en följd av närheten till den allmänna migränprofilen. De två hudsjukdomarna saknar identifierad koppling till 5-HT3-blockad. Känslighet för migrän är en genetisk benägenhet snarare än en behandlingsbar indikation.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Fallrapport | Canadian Journal of Anaesthesia | Beskriver migränliknande huvudvärk orsakad av palonosetron, alltså en säkerhetssignal och inte ett tecken på nytta. |

Kliniska prövningar: inga relaterade kliniska prövningar är registrerade för närvarande.

En översikt från 2026 om QT-förlängning vid antiemetika ([42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/), European Heart Journal – Cardiovascular Pharmacotherapy) är kopplad till en annan migränrelaterad förutsägelse. Den är relevant för säkerhet (risk för QT-förlängning) men ger inget effektstöd vid migrän.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 52912 | Palonosetron Reig Jofre | Injektionsvätska, lösning | Indragen |
| 52932 | Palonosetron Fresenius Kabi | Injektionsvätska, lösning | Indragen |
| 61378 | Palonosetron Kalceks | Injektionsvätska, lösning | Indragen |
| 52849 | FERANT | Injektionsvätska, lösning | Indragen |
| 52834 | Palonosetron STADA | Injektionsvätska, lösning | Indragen |

Ytterligare ett godkännande (52850, Palonosetron Macure) finns, också indraget. Inga indikationstexter finns registrerade.

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Totalt 398 interaktioner har identifierats. Exempel på interaktioner av allvarlig (major) grad:
  - Fentanyl, alfentanil, tramadol och dextrometorfan
  - Almotriptan och sumatriptan
  - Amiodaron, amisulprid, amitriptylin och anagrelid
- Exempel på måttliga interaktioner: abirateron, kodein, dihydrokodein, famotidin, formoterol, adenosin, salbutamol, alfuzosin, propofol och loperamid.
- **Övrig säkerhetssignal**: Huvudvärk/migränliknande huvudvärk (fallrapport) och risk för QT-förlängning vid antiemetika (översikt från 2026).

För varningar och kontraindikationer, se produktresumén.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den höga modellpoängen stöds inte av någon klinisk prövning, och den enda relevanta litteraturen visar att palonosetron kan framkalla migränliknande huvudvärk. Dessutom är alla svenska godkännanden indragna.

**För att gå vidare krävs:**
- Hämta produktresumé med varningar och kontraindikationer (blockerande dataluckor för säkerhetsgranskning).
- Komplettera verkningsmekanismen och den ursprungliga indikationen från DrugBank.
- Genomföra en systematisk litteratursökning efter prekliniska eller kliniska data om 5-HT3-antagonister vid migrän.
- Bedöma om förutsägelsen är meningsfull, eftersom litteraturen tyder på motsatt effekt.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

