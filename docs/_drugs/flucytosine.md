---
layout: default
title: Flucytosine
parent: Endast modellprediktion (L5)
nav_order: 199
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Flucytosine: predikterad ny indikation Pagets sjukdom i skelettet (bone Paget disease) (evidensnivå L5). Ursprunglig indikation: Ej angiven i godkännandedata"
monitor_inn: "flucytosine"
predicted_indications: ["bone Paget disease"]
---

# Flucytosine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

## Flucytosin: Från ej angiven indikation till Pagets sjukdom i skelettet
{: .text-alpha }

---

## Sammanfattning

Flucytosin är ett svampdödande läkemedel (prodrug som omvandlas till 5-fluorouracil i svampceller). Den ursprungliga godkända indikationen finns inte angiven i de data som sammanställts för denna rapport. TxGNN-modellen (deep learning) förutsäger att läkemedlet kan vara effektivt mot **Pagets sjukdom i skelettet** med en hög poäng (0,9904), men **inga kliniska prövningar och ingen publicerad litteratur** stöder för närvarande denna riktning. Poängen kommer från TxGNN-modellen (deep learning) och kan spegla likheter som modellen lärt sig mellan relaterade sjukdomar, inte biologisk evidens.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i godkännandedata |
| Förutsagd ny indikation | Pagets sjukdom i skelettet (bone Paget disease) |
| TxGNN-förutsägelsepoäng | 0,9904 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 1 av 1) |
| Antal godkännanden | 1 (giltiga: 1) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda data. Utifrån allmänt känd information är flucytosin ett antimykotikum: svampceller tar upp det via cytosinpermeas, och enzymet cytosindeaminas omvandlar det till 5-fluorouracil, som stör svampens RNA- och DNA-syntes.

Sambandet med Pagets sjukdom i skelettet är svagt. Sjukdomen kännetecknas av störd osteoklastaktivitet, ökad benomsättning och oordnad benombyggnad (bland annat via SQSTM1 och RANK/NF-κB-signalering). Humana celler saknar i stort sett cytosindeaminas, så läkemedlets kända verkningsväg kopplar inte tydligt till denna sjukdomsprocess.

Eventuella samband är därför spekulativa, till exempel genom 5-FU-exponering via tarmens mikrobiom eller effekter på osteoklastprekursorer. Inget av detta stöds av data. Den höga modellpoängen bör ses som en hypotes, inte som belägg.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 9337 | Ancotil (Viatris AB) | Infusionsvätska, lösning | Ej angiven |

<!-- review:begin se-row-20261112-flucytosine-1 -->

> **Granskningsrättelse (2026-11-12)**: Ursprungligen stod det: ”9337 (indraget) / Ancotil (Viatris AB) / Infusionsvätska, lösning / Ej angiven” Enligt Läkemedelsverkets registreringsstatus (2026-11-02) har 9337 status Godkänd; tabellen angav det som indraget. Endast statusuppgiften i tabellen har ändrats. Källa: [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-row-20261112-flucytosine-1 -->

---

## Cytotoxicitet

Flucytosin omvandlas till 5-fluorouracil (en fluoropyrimidin), men läkemedlet används som antimykotikum och inte som cancerläkemedel. Av den anledningen ligger fokus här på de toxicitetssignaler som framgår av data.

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Inte klassificerat som antineoplastiskt; fluoropyrimidin-prodrug |
| Myelosuppressionsrisk | Se säkerhetsaspekter nedan (kunskapsgrafen anger benmärgsrelaterade tillstånd som kontraindikationer) |
| Övervakningspunkter | Blodstatus, lever- och njurfunktion, kalium |

Se produktresumén för varningar och försiktighetsåtgärder.

---

## Säkerhetsaspekter

Produktresumédata (varningar och kontraindikationer) saknas i de sammanställda data. Följande information kommer från modellens kunskapsgraf och inte från produkttext, och ska därför tolkas med försiktighet.

- **Möjliga kontraindikationer enligt kunskapsgrafen**:
  - Njursjukdom och leversjukdom
  - Gallblåsesjukdom
  - Blodrelaterade tillstånd: trombocytopeni, leukopeni, agranulocytos, neutropeni (inklusive medfödda former) samt aplastisk anemi
  - Kaliumbrist

- **Läkemedelsinteraktioner**: Totalt 85 interaktioner finns registrerade. Den enda med allvarlig nivå (Major) bland de som listats är:
  - **Deferipron** (allvarlig)

  Exempel på interaktioner av måttlig nivå:
  - Amfotericin B (även lipidkomplex, kolesterylsulfat och liposomal form)
  - Mesalazin, balsalazid, olsalazin och sulfasalazin
  - Aminoglykosider och närliggande antibiotika (kanamycin, neomycin, streptomycin, vancomycin, polymyxin B, bacitracin)
  - Deferasirox, pentamidin, ibuprofen
  - Radiofarmaka: jobenguan (I-131) och strontiumklorid Sr-89

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds endast av en modellpoäng (L5). Det finns inga studier, ingen litteratur och ingen etablerad mekanism, och läkemedlets kända verkan har ingen tydlig koppling till Pagets sjukdom.
- Säkerhetsprofilen är dessutom oklar: produktresumédata saknas, och kunskapsgrafen pekar på risker för benmärg, lever och njurar.

<!-- review:begin se-lic-20261106-flucytosine-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Säkerhetsprofilen är dessutom oklar: produktresumédata saknas, och kunskapsgrafen pekar på risker för benmärg, lever och njurar. Det enda svenska godkännandet är indraget.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 1, varav giltiga: 1; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-flucytosine-1 -->

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) för varningar, kontraindikationer och ursprunglig indikation.
- Komplettera verkningsmekanismdata från DrugBank.
- Genomföra litteratur- och prövningssökning samt prekliniska studier (till exempel på osteoklastmodeller) för att pröva om det finns någon biologisk koppling.
- Bedöma nytta och risk i förhållande till befintliga behandlingar vid Pagets sjukdom, och utreda administreringsväg (flucytosin finns som infusionsvätska) och tillgänglighet på den svenska marknaden.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Det enda svenska godkännandet är indraget” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-12 | Tabell: 1 godkännande (9337) är godkänd, inte indragna | Rättad | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

