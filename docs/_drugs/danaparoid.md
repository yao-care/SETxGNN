---
layout: default
title: Danaparoid
parent: Endast modellprediktion (L5)
nav_order: 122
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Danaparoid: predikterad ny indikation Glanzmanns trombasteni (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga data"
monitor_inn: "danaparoid"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome"]
---

# Danaparoid
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

# Danaparoid: Från (ej angiven indikation) till Glanzmanns trombasteni

---

### Sammanfattning

Danaparoid (varumärke Orgaran) är ett antikoagulerande heparinoid. I de data som sammanställts för denna rapport finns ingen godkänd indikation angiven för den svenska licensen. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Glanzmanns trombasteni**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder förutsägelsen. Den mekanistiska bedömningen talar dessutom emot den, eftersom ett blödningshämmande läkemedel behövs vid detta tillstånd, inte ett antikoagulerande.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga data |
| Förutsagd ny indikation | Glanzmanns trombasteni |
| TxGNN-förutsägelsepoäng | 99,9 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 1 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är danaparoid ett heparinoid som främst hämmar faktor Xa via antitrombin. Dess effekt är att minska blodets koagulation.

Glanzmanns trombasteni är en blödningssjukdom som beror på att trombocyternas receptor integrin alfa-IIb/beta-3 saknas eller fungerar dåligt. Patienterna har alltså redan en ökad blödningsbenägenhet.

Det finns därför **ingen rimlig mekanistisk koppling**. Den höga poängen (99,9 %) beror sannolikt på att läkemedlet och sjukdomen ligger nära varandra i kunskapsgrafen, eftersom båda hör till koagulation och trombocyter. Ett antikoagulerande läkemedel förväntas förvärra blödningsrisken, så förutsägelsen kan likna en kontraindikation snarare än en behandlingsmöjlighet.

Övriga förutsägelser med liknande poäng (primär frisättningsstörning i trombocyter, pseudo-von Willebrands sjukdom, blödningsbenägenhet vid kollagenreceptordefekt, konstitutionell trombocytopeni med blödning samt Scotts syndrom) har samma problem: ingen evidens och en mekanism som sannolikt verkar åt fel håll.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 11720 (indraget) | Orgaran | Injektionsvätska, lösning | Ingen indikationstext tillgänglig |

Innehavare: Viatris Limited.

---

### Säkerhetsaspekter

**Läkemedelsinteraktioner**: Totalt 139 interaktioner finns registrerade. Bland de som ingår i underlaget är följande av allvarlig (Major) grad, i första hand läkemedel som också ökar blödningsrisken:
- Acetylsalicylsyra
- Ibuprofen
- Ketorolak
- Abciximab
- Alteplas
- Akalabrutinib
- Deferasirox
- Trastuzumabemtansin
- Ibritumomabtiuxetan
- Tositumomab (I-131)

Måttliga (Moderate) interaktioner finns bland annat med fenfluramin, sibutramin, aliskiren, amilorid, celekoxib, sugammadex och radioaktivt jod (I-123, I-131).

Se produktresumén för information om varningar och kontraindikationer, som inte ingår i underlaget.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en grafbaserad modell utan stöd från kliniska prövningar eller litteratur. Läkemedlets antikoagulerande verkan skulle sannolikt förvärra blödningsrisken vid Glanzmanns trombasteni, så säkerhetsrisken är betydande. Dessutom är det enda svenska godkännandet indraget.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket för att få varningar, kontraindikationer och godkänd indikation (blockerande dataglapp).
- Hämta verkningsmekanismdata från DrugBank.
- Genomföra en litteratur- och prövningssökning som kan visa om det finns någon biologisk grund för användning vid trombocytfunktionsstörningar.
- Bedöma om förutsägelsen i själva verket är en kontraindikationssignal, och granska övriga förutsägelser med samma mönster.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

