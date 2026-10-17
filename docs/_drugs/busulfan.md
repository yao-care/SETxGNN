---
layout: default
title: Busulfan
parent: Endast modellprediktion (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Busulfan: predikterad ny indikation Myelodysplastiskt syndrom (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext angiven i de svenska godkännandena"
monitor_inn: "BUSULFAN"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "simian immunodeficiency virus infection"]
---

# Busulfan
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

# Busulfan: Från ospecificerad ursprunglig indikation till myelodysplastiskt syndrom

---

### Sammanfattning

Busulfan är ett alkylerande cytostatikum som i Sverige har haft godkännanden som tablett (Myleran) och som koncentrat till infusionsvätska (Busulfan Zentiva). Båda godkännandena är numera avregistrerade, och någon godkänd indikationstext finns inte i de data som sammanställts för rapporten.
TxGNN-modellen förutsäger att läkemedlet kan vara användbart vid **myelodysplastiskt syndrom (MDS)**, med **36 kliniska prövningar** och **20 publikationer** i underlaget. Användningen gäller främst konditionering inför allogen stamcellstransplantation, inte busulfan som enskild sjukdomsmodifierande behandling.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext angiven i de svenska godkännandena |
| Förutsagd ny indikation | Myelodysplastiskt syndrom |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L2 (för MDS: fas 2-prövningar och en avslutad fas 3-prövning där busulfan ingår i en jämförande konditionering; se anmärkning nedan) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 2 |
| Rekommenderat beslut | Fortsätt med försiktighet |

*Anmärkning om evidensnivå:* Enligt de data som sammanställts för rapporten klassas MDS som L2. Flera avslutade fas 2-prövningar och två randomiserade fas 3-studier i litteraturen (bland annat en studie som jämför G-CSF, decitabin och busulfan-cyklofosfamid med enbart busulfan-cyklofosfamid) stöder användningen. Busulfan ingår dock alltid som del av en kombination.

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Baserat på känd information är busulfan ett bifunktionellt alkylerande läkemedel som skapar tvärbindningar i DNA och därigenom slår ut blodbildande celler i benmärgen (myeloablation).

Vid MDS är benmärgen sjuk och producerar defekta blodceller. Allogen stamcellstransplantation är den enda potentiellt botande behandlingen. Inför transplantationen behövs konditionering som tar bort den sjuka märgen och skapar utrymme för donatorns friska stamceller. Busulfan är en ryggrad i flera sådana regimer, ofta tillsammans med fludarabin, klofarabin, kladribin eller cyklofosfamid.

Sambandet är därför mekanistiskt rimligt, men det handlar om en roll som konditioneringsmedel och inte om behandling av sjukdomen med enbart busulfan.

---

### Kliniska prövningar

Ett urval av de mest relevanta prövningarna för MDS (totalt 36 registrerade):

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Fas 2 | Aktiv, rekryterar ej | 116 | Venetoklax plus tidssekvenserad busulfan, kladribin och fludarabin före donatorstamcellstransplantation vid AML och MDS |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Fas 2 | Avslutad | 34 | Dosreducerad konditionering med busulfan och klofarabin före allogen transplantation |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Fas 2 | Avslutad | 200 | Intravenöst busulfan med fludarabin före allogen transplantation vid AML och MDS |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Fas 2/3 | Rekryterar | 324 | Venetoklax tillagt till fraktionerad busulfanregim vid högrisk-AML och MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Fas 2/3 | Okänd | 242 | G-CSF + decitabin + busulfan/cyklofosfamid jämfört med G-CSF + decitabin + busulfan/fludarabin vid högrisk-MDS |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Fas 3 | Avslutad | 570 | Treosulfan-baserad konditionering jämförd med dosreducerad busulfan vid AML eller MDS hos patienter som inte tål standardkonditionering |
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Fas 3 | Avslutad | 240 | Busulfan-TBI jämfört med cyklofosfamid-TBI vid avancerat MDS eller MDS-relaterad AML |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Fas 2 | Avslutad | 68 | Busulfan, fludarabin och ATG med azacitidin vid högrisk-MDS och äldre AML-patienter |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Fas 2 | Okänd | 59 | Konditionering med fludarabin, busulfan och melfalan vid MDS |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | Ej tillämpligt | Rekryterar | 138 | Randomiserad jämförelse av venetoklax plus BUCY och standard-BUCY vid högrisk-AML och MDS |

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (fas 3) | The Lancet. Haematology | Treosulfan plus fludarabin jämfört med dosreducerat busulfan plus fludarabin hos äldre patienter med AML eller MDS |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (fas 3) | The Lancet. Haematology | G-CSF, decitabin och busulfan-cyklofosfamid jämfört med busulfan-cyklofosfamid för att minska återfall vid MDS |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT (fas 2) | Transplantation and Cellular Therapy | Två fraktioneringsscheman av myeloablativt busulfan med fludarabin och kladribin vid AML eller MDS |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Kohort (slutanalys av randomiserad studie) | American Journal of Hematology | Treosulfan jämfört med dosreducerat busulfan vid AML och MDS hos äldre patienter |
| [38197938](https://pubmed.ncbi.nlm.nih.gov/38197938/) | 2024 | Kohort (fas 1) | Blood Advances | Underhållsbehandling med venetoklax/azacitidin efter Ven/FluBu2-konditionering vid högrisk-MDS/AML |
| [40901473](https://pubmed.ncbi.nlm.nih.gov/40901473/) | 2025 | Kohort | Frontiers in Immunology | Ruxolitinib och decitabin plus busulfan-cyklofosfamid för att förebygga återfall |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Registerstudie | Bone Marrow Transplantation | Fludarabin/busulfan jämfört med busulfan/cyklofosfamid som myeloablativ konditionering vid MDS |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Registerstudie | Transplantation and Cellular Therapy | Myeloablativ jämfört med dosreducerad Flu/Bu vid MDS |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematisk översikt och metaanalys | Frontiers in Oncology | Långtidsutfall för treosulfan- jämfört med busulfanbaserad konditionering vid MDS och AML |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Översikt | American Journal of Hematology | Allogen transplantation är den enda potentiellt botande behandlingen vid MDS och myelofibros |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 5013 | Myleran | Filmdragerad tablett | Ingen indikationstext angiven (avregistrerad) |
| 57476 | Busulfan Zentiva | Koncentrat till infusionsvätska, lösning | Ingen indikationstext angiven (avregistrerad) |

---

### Cytotoxicitet

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Konventionell cytotoxisk (bifunktionellt alkylerande medel) |
| Myelosuppressionsrisk | Hög. Myeloablation är den avsedda effekten vid konditionering. |
| Emetogenicitetsklassificering | Se produktresumén för varningar och försiktighetsåtgärder |
| Övervakningspunkter | Blodstatus (särskilt trombocyter och neutrofiler), lever- och njurfunktion, samt lungfunktion. Läkemedelsnivåer (riktad dosering) används i flera av prövningarna. |
| Hanteringsskydd | Hantering enligt gällande föreskrifter för cytotoxiska läkemedel |

---

### Säkerhetsaspekter

- **Sjukdomar där kontraindikation anges i kunskapsgrafen** (härledd från TxGNN:s kunskapsgraf, inte från produkttext): epilepsi, trombocytopeni, neutropeni, agranulocytos, anemi (inklusive makrocytär anemi), Fanconis anemi, lungfibros, hyperglykemi, svampinfektioner, infektionssjukdomar och kaliumbrist.
- **Läkemedelsinteraktioner** (100 identifierade; de viktigaste):
  - **Allvarlig:** metronidazol
  - **Måttlig:** aprepitant, mikonazol
  - **Lindrig:** levofloxacin
  - Flera ytterligare interaktioner har okänd allvarlighetsgrad, bland annat amfotericin B, vankomycin, protonpumpshämmare, kortikosteroider och antiemetika.
- **Långsiktiga risker:** litteraturen beskriver ökad risk för sekundär malignitet efter busulfan samt långtidskomplikationer efter busulfanbaserad konditionering hos barn.

Övrig säkerhetsinformation: se produktresumén.

---

### Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Stödet för MDS är relativt starkt, med flera avslutade fas 2-prövningar och randomiserade fas 3-studier. Busulfan ingår dock alltid i en kombinationsregim, och användningen är konditionering inför transplantation. Dessutom saknar läkemedlet för närvarande giltiga svenska godkännanden, och uppgifter om varningar och kontraindikationer från produkttexten saknas.

**För att gå vidare krävs:**
- Hämta och granska produktresumén från Läkemedelsverket för varningar och kontraindikationer.
- Bekräfta verkningsmekanismen via DrugBank.
- Bedöma om en ny svensk ansökan eller användning av ett annat tillgängligt busulfanpreparat är aktuell, eftersom båda godkännandena är avregistrerade.
- Utvärdera busulfans specifika bidrag jämfört med andra konditioneringsmedel (till exempel treosulfan) i jämförande studier.
- Bedöma resultaten från pågående randomiserade prövningar (till exempel NCT04708054) när de avslutats.

**Övriga förutsagda indikationer (kort):**
- **Aregenerativ anemi / benmärgssvikt** (L1): stöds av en fas 3-prövning och många fas 2-prövningar, men evidensen är mestadels från blandade hematologiska populationer.
- **Refraktär cytopeni hos barn** (L2) och **HIV-infektion** (L3): busulfan används som konditioneringsmedel, inte som antiviralt läkemedel. Evidensen är begränsad.
- **Oklassificerat MDS** (L3) har endast äldre litteratur. **Partiell deletion av kromosom 5q, kongenital hypokrom anemi med ringsideroblaster, neuroutvecklingsstörning, seborroisk keratos och SIV-infektion** saknar studier och är endast modellförutsägelser; ingen rimlig mekanistisk koppling har identifierats.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

