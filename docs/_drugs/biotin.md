---
layout: default
title: Biotin
parent: Endast modellprediktion (L5)
nav_order: 62
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Biotin: predikterad ny indikation Dyspepsi (evidensnivå L5). Ursprunglig indikation: Näringsrelaterad biotinbrist (enligt kunskapsgrafen"
monitor_inn: "BIOTIN"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
---

# Biotin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
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

# Biotin: Från näringsrelaterad biotinbrist till dyspepsi

---

### Sammanfattning

Biotin är ett vattenlösligt vitamin som ursprungligen används för att behandla och förebygga **näringsrelaterad biotinbrist**. TxGNN-modellen förutsäger att det kan ha effekt vid **dyspepsi**, men underlaget består enbart av modellens förutsägelse: **inga kliniska prövningar** finns registrerade och den hittade litteraturen (6 publikationer) handlar inte om biotin som behandling mot dyspepsi.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Näringsrelaterad biotinbrist (enligt kunskapsgrafen; svensk godkänd indikationstext saknas) |
| Förutsagd ny indikation | Dyspepsi |
| TxGNN-förutsägelsepoäng | 99,4 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 3 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information fungerar biotin som kofaktor för karboxylaser som deltar i omsättningen av kolhydrater, fett och aminosyror. Dess effekt vid biotinbrist är väletablerad.

Biotinbrist kan ge mag-tarmsymtom som illamående och aptitlöshet. Det ger ett möjligt, men svagt, samband med dyspepsi: biotin kan lindra symtom som beror på brist. Det är dock inte belagt att biotin behandlar funktionell dyspepsi i allmänhet.

Den höga modellpoängen (0,994) ska därför tolkas försiktigt. Ingen av de hittade publikationerna undersöker biotin som behandling av dyspepsi. Mekanismen är i nuläget hypotetisk.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Fallrapport | The Journal of Dermatology | Spädbarn med biotinbrist som fått enbart aminosyrabaserad modersmjölksersättning efter att ha diagnostiserats med dyspepsi som nyfödd. Hudförändringar och håravfall; låga biotinnivåer i serum och urin. Visar brist, inte behandlingseffekt vid dyspepsi. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observationsstudie | International Journal of Molecular Medicine | Endokrina celler i magsäckens antrum hos patienter med IBS. Ingen koppling till biotin. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observationsstudie | World Journal of Gastrointestinal Endoscopy | Endokrina celler i magsäckens oxyntiska slemhinna hos IBS-patienter. Ingen koppling till biotin. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observationsstudie | Journal of Clinical Pathology | Interleukin 10 vid gastrit orsakad av Helicobacter pylori. Ingen koppling till biotin. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Klinisk studie/översikt | Eksperimental'naia i Klinicheskaia Gastroenterologiia | Ett tillskott med prebiotika, vitaminer (inklusive biotin) och mineraler för tarmflorans balans hos patienter med lungsjukdom som fått antibiotika. Biotinets enskilda bidrag går inte att urskilja. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observationsstudie | Kidney International | T-celler i tunntarmen vid IgA-nefropati. Ingen koppling till biotin. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 10237 | Soluvit | Pulver till infusionsvätska, lösning | Avregistrerad |
| 17364 | Cernevit | Pulver till injektions-/infusionsvätska, lösning | Avregistrerad |
| 56261 | Viant | Pulver till infusionsvätska, lösning | Avregistrerad |

Alla tre är injicerbara beredningar. Ingen godkänd indikationstext finns tillgänglig i de sammanställda uppgifterna.

---

### Säkerhetsaspekter

Inga uppgifter från produktresumén finns tillgängliga för varningar, kontraindikationer eller läkemedelsinteraktioner (inga interaktioner hittades).

Kunskapsgrafen anger följande sjukdomstillstånd som är förknippade med kontraindikation. Det är inte hämtat från produkttext och bör verifieras mot den:

- Njursjukdom, nefrokalcinos, njursten (nefrolitiasis) och akut urinsyranefropati
- Hyperparatyreoidism, osteitis fibrosa och hyperkalcemi
- Störningar i fosforomsättningen
- Sarkoidos
- Pyouretär
- Förstoppning
- Lytiska bensmetastaser

Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellpoängen (evidensnivå L5). Det finns inga kliniska prövningar, ingen litteratur som stöder biotin vid dyspepsi, ingen känd verkningsmekanism i underlaget, och alla svenska godkännanden är avregistrerade.

**För att gå vidare krävs:**
- Verkningsmekanismdata från DrugBank för att kunna bedöma ett mekanistiskt samband.
- Säkerhetsinformation från produktresumén (varningar och kontraindikationer), eftersom säkerhetsgranskningen annars inte kan genomföras.
- Litteratursökning riktad mot biotin vid dyspepsi, särskilt hos patienter med påvisad biotinbrist.
- Bedömning av administreringsväg: de tidigare godkända produkterna är endast injicerbara, och en oral beredning skulle behöva utredas.
- Om förutsägelsen ska utredas vidare, en preklinisk eller liten klinisk pilotstudie i en väldefinierad population.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

