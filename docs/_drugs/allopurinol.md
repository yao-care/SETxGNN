---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

Jag har identifierat `txgnn-pipeline`-skillet som relevant för denna uppgift. Nu genererar jag rapporten baserat på Evidence Pack för Allopurinol.

---

# Allopurinol: Från gikt och hyperurikemi till hepatisk porfyri

## Sammanfattning

Allopurinol är ett välkänt läkemedel som ursprungligen användes för behandling av gikt och hyperurikemi genom hämning av enzymet xantinoxidas (XO), vilket minskar produktionen av urinsyra i kroppen. TxGNN-modellen förutsäger att allopurinol kan vara effektivt mot **hepatisk porfyri**, baserat på en hypotetisk förmåga att hämma 5-aminolevulinsyrasyntas (ALAS) – det hastighetsbegränsande enzymet i hembiosyntesen. Evidensstödet är för närvarande begränsat till **2 publikationer** av typen hypotesstudier och djurstudier, utan några registrerade kliniska prövningar.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Gikt och hyperurikemi |
| Förutsagd ny indikation | Hepatisk porfyri (hepatic porphyria) |
| TxGNN-förutsägelsepoäng | 99,95% |
| Evidensnivå | L4 – Mekanismstudier och djurstudier |
| Marknadsstatus i Sverige | Ej registrerat i Sverige |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Allopurinol är en potent hämmare av xantinoxidas (XO), ett enzym som katalyserar det sista steget i purinkatabolismen och omvandlar hypoxantin och xantin till urinsyra. Denna mekanism är väl etablerad och utgör grunden för allopurinols användning vid gikt. Utöver XO-hämning har det i litteraturen lyfts fram hypoteser om att allopurinol även kan påverka 5-aminolevulinsyrasyntas (ALAS) i levern – det hastighetsbegränsande enzymet i hembiosyntesen.

Hepatisk porfyri karaktäriseras av en dysreglerad överaktivering av ALAS, vilket leder till ansamling av toxiska porfyrinprekursorer – aminolevulinsyra (ALA) och porfobilinogen (PBG) – i levern. Akuta porfyrianfall utlöses av faktorer som svält, hormoner och vissa läkemedel, och är associerade med kraftig induktion av ALAS sekundärt till uttömning av den regulatoriska hempoolen. Om allopurinol kan dämpa ALAS-aktiviteten, finns en teoretisk möjlighet att reducera prekursoransamlingen och förhindra eller mildra akuta anfall.

Kopplingen är mekanistiskt motiverad men stöds hittills enbart av en hypotesartikel (Badawy 2019) och en äldre djurstudie (Morgan & Badawy 1992) som inte direkt undersöker allopurinol mot hepatisk porfyri. Det saknas kliniska prövningar, varför evidensnivån bedöms till L4.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypotes/Mekanistisk översikt | Medical Hypotheses | Föreslår att metabolisk targetering av lever-ALAS via hämning av hemets utnyttjande av tryptofan 2,3-dioxygenase (TDO) kan utgöra en ny terapistrategi vid akuta hepatiska porfyrier; ger indirekt stöd för ALAS-hämning som behandlingsprincip. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Djurstudie | Biochemical Pharmacology | Undersökte karbamazepins effekter på hemmetabolism i råttlever via ALAS-induktion och tryptofanpyrolas-medierad hempoolförändring; belyser ALAS-reglering som mekanism vid läkemedelsexacerbation av porfyri. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensunderlaget begränsar sig till mekanistiska hypoteser och en indirekt djurstudie från 1992. Det finns inga kliniska prövningar som direkt undersökt allopurinol för hepatisk porfyri, och den föreslagna ALAS-hämmande mekanismen saknar experimentell bekräftelse i porfyrimodeller.

**För att gå vidare krävs:**
- In vitro- och djurmodellstudier som direkt bekräftar allopurinols effekt på ALAS-aktivitet i leverkontext vid hepatisk porfyri
- Säkerhetsgenomgång baserad på fullständig produktresumé (SmPC), med särskild uppmärksamhet på allopurinol hypersensitivity syndrome (DRESS/TEN) och potentiella läkemedelsinteraktioner relevanta för porfyripatienter
- Litteratursökning avseende eventuella fallrapporter eller observationella fynd om allopurinol vid porfyri
- Övervägande av proof-of-concept-studie (fas 1/2) om mekanistiska studier ger tillräckligt förstärkt stöd
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

