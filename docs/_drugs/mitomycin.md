---
layout: default
title: Mitomycin
parent: Endast modellprediktion (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mitomycin: predikterad ny indikation Osteoklastisk jättecellstumör i pankreas (evidensnivå L5). Ursprunglig indikation: Pankreasadenokarcinom (enligt kunskapsgrafen"
monitor_inn: "MITOMYCIN"
predicted_indications: ["osteoclastic giant cell tumor of pancreas", "solid pseudopapillary carcinoma of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
---

# Mitomycin
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

## Mitomycin: Från pankreasadenokarcinom till osteoklastisk jättecellstumör i pankreas
{: .text-alpha }

---

### Sammanfattning

Mitomycin är ett cytostatikum som i den data som sammanställts för denna rapport är kopplat till behandling av pankreasadenokarcinom. TxGNN-modellen förutsäger att det kan vara effektivt mot **osteoklastisk jättecellstumör i pankreas**, en sällsynt histologisk variant av pankreascancer. Det finns **inga kliniska prövningar** och **inga publikationer** som stöder just denna förutsägelse, så underlaget består enbart av modellens förutsägelse.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Pankreasadenokarcinom (enligt kunskapsgrafen; godkännandena i Sverige saknar indikationstext) |
| Förutsagd ny indikation | Osteoklastisk jättecellstumör i pankreas |
| TxGNN-förutsägelsepoäng | 99,86 % |
| Evidensnivå | L5 (endast modellförutsägelse, inga studier) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 3 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts. Baserat på känd information är mitomycin ett cytostatikum som verkar genom att tvärbinda DNA, och dess effekt vid pankreasadenokarcinom är den indikation som kunskapsgrafen kopplar till läkemedlet. Mekanistiskt kan det därför vara tillämpbart på en närbesläktad tumörtyp.

Osteoklastisk jättecellstumör i pankreas är en sällsynt histologisk variant av duktalt pankreasadenokarcinom. Eftersom tumören delar ursprung med den ursprungliga indikationen är ett gemensamt cytotoxiskt angreppssätt rimligt. Det finns dock inga studier eller publikationer som styrker kopplingen.

Flera andra förutsagda indikationer ligger nära varandra i poäng (99,8–99,9 %) och är i huvudsak varianter av pankreascancer. De flesta saknar också helt kliniskt underlag.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 45894 | Mitomycin Substipharm | Pulver till injektions-/infusionsvätska, lösning | Indragen |
| 45895 | Mitomycin Substipharm | Pulver och vätska till intravesikal lösning | Indragen |
| 50421 | Mitomycin medac | Pulver och vätska till intravesikal lösning | Indragen |

Ingen godkänd indikationstext finns registrerad för dessa godkännanden.

---

### Cytotoxicitet

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Konventionell cytotoxisk (DNA-tvärbindande alkylerande antibiotikum) |
| Myelosuppressionsrisk | Hög. Kunskapsgrafen kopplar läkemedlet till trombocytopeni, leukopeni och anemi. |
| Emetogenicitetsklassificering | Se produktresumén |
| Övervakningspunkter | Blodstatus (trombocyter, leukocyter, hemoglobin), njurfunktion, tecken på hemolytiskt uremiskt syndrom |
| Hanteringsskydd | Hantera enligt gällande föreskrifter för cytotoxiska läkemedel. Se produktresumén för detaljer. |

---

### Säkerhetsaspekter

**Möjliga kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé):
- Njursjukdom
- Trombocytopeni, koagulationsrubbningar, anemi (inklusive makrocytär anemi) och leukopeni
- Hemolytiskt uremiskt syndrom (inklusive typiskt)
- Hjärtsvikt (kongestiv hjärtsvikt)
- Stomatit
- Pyouretär

**Läkemedelsinteraktioner** (100 interaktioner identifierade, de viktigaste nedan):

| Interagerande läkemedel | Nivå |
|------|------|
| Deferipron | Allvarlig |
| Samarium (153Sm) lexidronam | Allvarlig |
| Palifermin | Måttlig |
| Strontiumklorid Sr-89 | Måttlig |
| Fostamatinib | Måttlig |
| Levofloxacin | Mindre |

Övriga listade interaktioner (bland annat warfarin, dexametason och omeprazol) har okänd allvarlighetsgrad.

Produktresuméns varningar och kontraindikationer har inte kunnat inhämtas och måste kontrolleras separat.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellen (L5), utan kliniska prövningar eller direkt litteratur. Dessutom är alla svenska godkännanden indragna, och produktresuméns säkerhetsdata saknas.

**För att gå vidare krävs:**
- Hämta produktresumé med varningar och kontraindikationer från Läkemedelsverket (MPA) för att kunna göra en säkerhetsbedömning.
- Komplettera verkningsmekanismen från DrugBank.
- Göra en systematisk litteratursökning efter mitomycin vid sällsynta pankreastumörer, särskilt de varianter som liknar duktalt adenokarcinom.
- Bedöma administreringsväg och beredningsform, eftersom de svenska godkännandena gällde injektion och intravesikal användning.
- Tänk på att den närmast jämförbara indikationen, den ursprungliga pankreascancern, redan är ansluten till läkemedlet, så ett nytt tillämpningsområde är inte tydligt avgränsat.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

