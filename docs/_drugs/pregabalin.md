---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

Using the `txgnn-pipeline` skill as context — this is a Swedish TxGNN deployment report. Generating the Swedish evaluation report from the Evidence Pack now.

---

# Pregabalin: Från neuropatisk smärta till tendinit

## Sammanfattning

Pregabalin är ett gabapentinoid-läkemedel godkänt internationellt för behandling av neuropatisk smärta och partiell epilepsi. TxGNN-modellen förutsäger att det kan vara effektivt mot **tendinit** (seninflammation), men evidensbasen är begränsad – inga kliniska prövningar är registrerade och **6 publikationer** ger endast indirekt stöd via studier på postoperativ smärta vid senkirurgi. Den mekanistiska kopplingen bedöms som svag och nuvarande evidens motiverar inte vidare klinisk prioritering.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Neuropatisk smärta, partiell epilepsi |
| Förutsagd ny indikation | Tendinit |
| TxGNN-förutsägelsepoäng | 99,7% |
| Evidensnivå | L4 – Prekliniska/mekanismstudier |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är Pregabalin ett gabapentinoid (GABA-analog) som verkar genom att hämma α2δ-subenheten hos spänningskänsliga kalciumkanaler (VGCC), vilket minskar presynaptisk frisättning av smärtmediatorer som glutamat, noradrenalin och substans P. Dess effekt vid neuropatisk smärta och epilepsi är väl dokumenterad, och mekanistiskt kan den vara tillämpbar på smärtkomponenten vid tendinit.

Tendinit är en lokal inflammatorisk och degenerativ sensjukdom. Det finns ett indirekt samband med Pregabalins verkningsområde: läkemedlet kan lindra den kroniska smärta och centrala sensitisering som uppstår vid svår eller långvarig tendinit via α2δ VGCC-hämning. Däremot saknas direkt verkningsmekanism mot tendinitens kärnpatologi – lokal inflammation, kollagennedbrytning och senvävnadsreparation påverkas inte av detta läkemedel.

Sammantaget bedöms den mekanistiska kopplingen som svag. TxGNN-förutsägelsen drivs sannolikt av grafens nodnärhet inom muskuloskeletala sjukdomsnoder snarare än en stark direkt farmakologisk länk till tendinit.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | *Arthroscopy* | Perioperativ oral pregabalin gav likvärdiga smärtpoäng som interscalenusblockad efter artroskopisk rotatorkuffreparation |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT | *J Orthop Sci* | Pregabalin visade opioidbesparande effekt efter artroskopisk rotatorkuffkirurgi; evidensen för multimodalt regim är motstridande och begränsad |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Fallrapport/Översikt | *Praxis* | Fluorokinolonassocierad funktionsnedsättning med tendinopati efter ciprofloxacin – pregabalin är ej studieobjektet |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Fallrapport | *Pain Practice* | Posterior femoral kutan nervneuropati orsakad av hamstringstendinit vid maratonlöpning; pregabalin nämns som potentiellt behandlingsalternativ för den neuropatiska smärtkomponenten |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Ledare | *Arthroscopy* | Piriformissyndrom behandlat med neurolys och piriformissenfriläggning – pregabalin inte primärt utvärderat |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Djurstudie | *Adv Pharmacol Pharm Sci* | Växtextrakt mot vincristin-inducerad perifer neuropati hos råttor; pregabalin används som aktivt jämförelseläkemedel, inte som primärt studieobjekt |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Pregabalins α2δ VGCC-hämmande mekanism saknar direkt koppling till tendinitens kärnpatologi. Befintlig litteratur stöder inte pregabalin som specifik behandling mot tendinit – de tillgängliga publikationerna rör postoperativ smärta vid senkirurgi eller är fallrapporter där pregabalin inte är primärt utvärderat. Inga kliniska prövningar är registrerade och evidensnivå L4 motiverar inte vidare klinisk prioritering för denna indikation.

**För att gå vidare krävs:**
- Riktade prekliniska studier som undersöker pregabalins direkta effekt på seninflammation och senvävnadsreparation
- Prospektiva kliniska studier för kronisk tendinit med neuropatisk eller central smärtkomponent
- Fullständig säkerhetsinformation (SmPC) för Pregabalin från Läkemedelsverket
- Bekräftelse av Pregabalins faktiska marknadsstatus i Sverige (datakvaliteten för 0 godkännanden bör verifieras)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

