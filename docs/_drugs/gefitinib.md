---
layout: default
title: Gefitinib
parent: Endast modellprediktion (L5)
nav_order: 213
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
description: "Gefitinib: predikterad ny indikation Fibromatos i tandköttet (fibromatosis, gingival) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Gefitinib
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **9** st
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

## Gefitinib: Fibromatos i tandköttet (fibromatosis, gingival)
{: .text-alpha }

---

### Sammanfattning

Gefitinib är en EGFR-tyrosinkinashämmare som ursprungligen används för att behandla icke-småcellig lungcancer (NSCLC). TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **fibromatos i tandköttet (gingival fibromatos)**, men för denna förutsägelse finns **inga kliniska prövningar och ingen publicerad litteratur**. Förutsägelsen bygger enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Fibromatos i tandköttet (fibromatosis, gingival) |
| TxGNN-förutsägelsepoäng | 0.9989 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Gefitinib är dock allmänt känt som en selektiv hämmare av EGFR-tyrosinkinas, och dess effekt vid EGFR-muterad NSCLC är väl belagd.

Ett tänkbart samband är att EGFR/ErbB-signalering bidrar till fibroblastproliferation, vilket skulle kunna vara relevant vid fibrös överväxt i tandköttet. Detta är dock **spekulativt och oprövat**. Den höga poängen kommer från TxGNN-modellen (deep learning) och kan spegla likheter som modellen har lärt sig mellan relaterade sjukdomar, inte biologisk evidens. Ingen studie har undersökt gefitinib vid denna sjukdom.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 56625 | Gefitinib STADA (STADA Arzneimittel AG) | Filmdragerad tablett | Ingen indikationstext tillgänglig (godkänd) |
| 56936 | Gefitinib Accord (Accord Healthcare B.V.) | Filmdragerad tablett | Ingen indikationstext tillgänglig (godkänd) |

---

### Cytotoxicitet

Gefitinib är ett antineoplastiskt läkemedel (indikation: lungcancer). Det är en **målriktad terapi** (EGFR-tyrosinkinashämmare), inte ett konventionellt cytotoxiskt läkemedel.

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Målriktad terapi (EGFR-tyrosinkinashämmare) |
| Myelosuppressionsrisk | Se produktresumén för varningar och försiktighetsåtgärder |
| Emetogenicitetsklassificering | Se produktresumén för varningar och försiktighetsåtgärder |
| Övervakningspunkter | Leverfunktion och andningsstatus (se säkerhetsaspekter nedan) |
| Hanteringsskydd | Se produktresumén för varningar och försiktighetsåtgärder |

---

### Säkerhetsaspekter

- **Sjukdomar där kunskapsgrafen anger kontraindikation** (inte hämtat från produktresumé): leversjukdom, gallblåsesjukdom, interstitiell lungsjukdom, lungfibros och postinflammatorisk lungfibros.
- **Läkemedelsinteraktioner**: Totalt identifierades 100 interaktioner. De flesta av de visade är av måttlig svårighetsgrad:
  - Syrahämmande läkemedel: famotidin, ranitidin, cimetidin, nizatidin samt protonpumpshämmare (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol)
  - Aprepitant, klaritromycin, mikonazol, klotrimazol, dexametason, naltrexon, troglitazon
  - Kalcitriol och glimepirid har oklar svårighetsgrad
- **Litteraturbaserade säkerhetssignaler**: Publikationer i underlaget beskriver gefitinibrelaterad pneumonit/interstitiell lungsjukdom (inklusive ett dödsfall), hudtoxicitet, QT-förlängning och ett fall av återkommande hjärtinfarkt. Detta överensstämmer med kontraindikationerna ovan.

Varningar och kontraindikationer från produktresumén saknas i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen har evidensnivå L5 utan kliniska prövningar eller litteratur, och något stöd för en EGFR-driven mekanism vid gingival fibromatos saknas. Dessutom är samtliga svenska godkännanden avregistrerade.

**Övriga förutsägelser i utvärderingen (alla utan stöd för äkta återanvändning):**
- *Fibrom i lunga, hamartom i lunga, inklusionskroppsmyopati med tidig Pagets sjukdom, Leukomelanoderma-syndromet, junktional epidermolysis bullosa*: endast modellförutsägelser (L5). Vid junktional epidermolysis bullosa är användning mekanistiskt oroande, eftersom gefitinib ofta ger hudtoxicitet.
- *Carcinom i lunghilus och pulmonary sulcus-neoplasm*: i praktiken en utvidgning av den befintliga NSCLC-indikationen snarare än äkta återanvändning (L4, endast ett fallrapport respektive en översikt).
- *Benign lungneoplasm och lungcancer av germinalcellstyp*: litteraturen gäller malign NSCLC eller solida tumörer i allmänhet, inte dessa tillstånd. Den enda prövningen (NCT00068497, fas I, 40 deltagare) gäller huvud-halscancer eller NSCLC och är endast löst relevant.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata (t.ex. via DrugBank) och produktresumétexter om varningar och kontraindikationer från Läkemedelsverket
- Prekliniska studier (t.ex. fibroblastmodeller) som testar om EGFR-hämning påverkar fibros i tandköttet
- Fallserier eller prövningar vid gingival fibromatos innan en klinisk bedömning görs
- Klargöra regulatorisk status, eftersom 2 giltiga godkännanden av 2 finns i Sverige
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

