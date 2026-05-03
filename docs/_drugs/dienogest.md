---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Dienogest
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

# Dienogest: Från endometrios till amenorré

---

## Sammanfattning

Dienogest är ett fjärde generationens progestin (gestagen) som primärt används för behandling av endometrios, bland annat under varumärket Visanne. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt vid **amenorré** (utebliven menstruation), med **4 kliniska prövningar** och **6 publikationer** som för närvarande finns tillgängliga. Det är dock viktigt att notera att samtliga identifierade studier rör endometrios – amenorré förekommer i dessa som en farmakologisk biverkning hos 30–50 % av patienterna snarare än som ett behandlingsmål, vilket kraftigt begränsar förutsägelsens kliniska tillämpbarhet.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Endometrios (klinisk kontext; inga godkännanden registrerade i Sverige) |
| Förutsagd ny indikation | Amenorré |
| TxGNN-förutsägelsepoäng | 99,71 % |
| Evidensnivå | L4 – Mekanismstudier och observationsdata |
| Marknadsstatus i Sverige | Inte godkänt |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i Evidence Pack. Baserat på tillgänglig klinisk och farmakologisk information är Dienogest ett fjärde generationens progestin med hög selektivitet för progesteronreceptorn och minimal androgen aktivitet. Det är godkänt för behandling av endometrios i flera länder och verkar primärt genom att hämma endometriets tillväxt och supprimera LH-peak, vilket skapar en hypöstrogen miljö som bromsar ektopisk endometrievävnad.

Kopplingen till amenorré är farmakologisk snarare än terapeutisk: Dienogest orsakar amenorré hos 30–50 % av patienterna som en direkt effekt av endometriell atrofi och ovulationshämning. Amenorré är alltså en väldokumenterad biverkning av läkemedlet – inte en indikation. Om målet vore att "behandla amenorré med Dienogest" vore mekanismriktningen omvänd: läkemedlet *inducerar* det tillstånd det förväntas behandla.

TxGNN-modellens höga poäng (99,71 %) förklaras sannolikt av stark statistisk samförekomst mellan Dienogest och amenorré i träningsdata, utan att modellen kan skilja på biverkning och terapeutisk effekt. Detta är ett känt begränsningsproblem i kunskapsgrafsbaserade modeller, som kan ge vilseledande höga poäng när ett läkemedel frekvent associeras med ett tillstånd – oavsett kausalitetens riktning.

---

## Kliniska prövningar

> **Obs:** Nedanstående prövningar avser behandling av endometrios. Amenorré förekommer i dessa som sekundär observationspunkt eller biverkning – inte som primär indikation.

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Avslutad | 968 | Verklighetsstudie av Visanne (Dienogest) vid endometrios i klinisk rutinpraxis; amenorré ingick som sekundär observationspunkt för biverkningsprofilen. |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fas 3 | Rekryterar | 290 | Randomiserad öppen Fas 3-studie som jämför Indinol Forto® och Visanne vid endometrios; non-inferiority-design. Amenorré kan förekomma som sekundär endpoint. |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Avslutad | 895 | Prospektiv observationsstudie av Dienogest hos asiatiska kvinnor med endometrios; utvärderar livskvalitet och långsiktig biverkningsprofil, inklusive amenorré. |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Aktiv, ej rekryterande | 138 | Jämför progestin + transdermal östradiol (Dienogest vs. drospirenon) vid endometrios; studien syftar till att *hantera* Dienogest-inducerad amenorré och lågestrogensymtom med add-back-terapi, inte att behandla amenorrésjukdom. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematisk översikt + Bayesiansk metaanalys | BMC Pharmacology & Toxicology | Sammanfattar biverkningar av Dienogest vid endometrios och adenomyos; amenorré identifieras som en av de vanligaste biverkningarna med hög förekomst. |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Farmakologisk studie | European Journal of Contraception & Reproductive Health Care | Hög inhibitionskvot och transformationsindex för Dienogest 2 mg; understryker att induktion av amenorré är en central farmakologisk effekt vid endometriosterapi, inte ett behandlingsmål i sig. |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Prospektiv observationsstudie | Reproductive Sciences | Långtidssäkerhet och effekt av Dienogest vid ovarialendometriom (n=514, >12 månader); amenorré dokumenterad som biverkning vid långtidsanvändning. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrativ översikt | Reviews in Endocrine & Metabolic Disorders | Genomgång av hormonella behandlingar vid endometrios; belyser östrogenberoende och progesteronresistens som centrala patogenetiska mekanismer bakom effekten av progestiner som Dienogest. |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Fallrapport | Medicine | Fallrapport om ovariegranulosacelltumör vid PCOS; begränsad direkt relevans för Dienogest-amenorré-sambandet. |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Klinisk/bilddiagnostisk studie | Journal of Pediatric and Adolescent Gynecology | 3D-modellering och VR-visualisering vid Müllerska anomalier; obstruktiva anomalier kan orsaka amenorré, men studien saknar koppling till Dienogest. |

---

## Marknadsinformation Sverige

Dienogest saknar godkännanden hos Läkemedelsverket (MPA). Läkemedlet är för närvarande inte registrerat på den svenska marknaden för någon indikation.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- TxGNN-modellens höga förutsägelsepoäng (99,71 %) för amenorré bedöms vara ett modellartefakt orsakat av statistisk samförekomst: Dienogest *orsakar* amenorré som biverkning hos 30–50 % av patienterna, men är inte avsett att *behandla* amenorrésjukdom. Mekanismriktningen är omvänd, och ingen av de fyra identifierade kliniska prövningarna studerar Dienogest som behandling mot amenorré.

**För att gå vidare krävs:**
- Verifiering av klinisk frågeställning – om syftet är terapeutisk induktion av amenorré (t.ex. vid endometrios eller adenomyos) finns redan etablerad evidens, men detta utgör inte en ny indikation
- Inhämtning av fullständig säkerhetsinformation: MOA-data, varningar och kontraindikationer från DrugBank och produktresumé (FASS/SmPC)
- Ansökan om marknadsgodkännande i Sverige hos Läkemedelsverket med fullständig dokumentation om läkemedlet ska introduceras på den svenska marknaden
- Alternativt: Utvärdering av **Rang 3-kandidaten – bröstfibrocystisk sjukdom** (TxGNN-poäng: 99,60 %, evidensnivå L4, beslutsstadium S1 – "Research Question"), som har ett mer biologiskt välgrundat mekanismsamband baserat på Dienogest's antiöstrogena effekter i bröstvävnad, och bättre förutsättningar för klinisk vidareutveckling
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

