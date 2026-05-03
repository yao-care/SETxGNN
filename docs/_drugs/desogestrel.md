---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

Ingen specifik rapport-skrivningsinstruktion hittades i pipeline-skillet — systemprompten innehåller alla nödvändiga riktlinjer. Jag genererar nu rapporten enligt Evidence Pack:

---

# Desogestrel: Från preventivmedel till amenorré

## Sammanfattning

Desogestrel är ett tredje generationens progestin som globalt används som aktiv komponent i kombinerade p-piller (COC) och gestagenpiller (POP) för att förhindra graviditet – dock saknas godkännande i Sverige. TxGNN-modellen förutsäger att det kan vara effektivt mot **amenorré**, med **2 kliniska prövningar** och **16 publikationer** som för närvarande stöder denna riktning. Evidensen är dock till övervägande del indirekt: befintliga studier undersöker primärt desogestrels preventiveffekt, och amenorré förekommer som sekundärt utfall eller biverkningsprofil snarare än primärt behandlingsmål.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej registrerat i Sverige; globalt godkänt som preventivmedel (COC/POP) |
| Förutsagd ny indikation | Amenorré (amenorrhea disease) |
| TxGNN-förutsägelsepoäng | 99,96 % |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd information är Desogestrel ett syntetiskt progestin (gestanderivat) med utpräglat låg androgen aktivitet; det ingår i kombinerade p-piller (COC, t.ex. Marvelon/Mercilon) och som ensamt verksamt ämne i gestagenpiller (POP 75 µg, t.ex. Cerazette). Dess preventiva effekt vid reproduktiv ålder är väl dokumenterad sedan 1980-talet.

Sambandet mellan preventivmedelsanvändning och amenorré är biologiskt plausibelt på flera nivåer. I COC-format tillhandahåller desogestrel (kombinerat med etinylöstradiol) cyklisk exogen progesteron/östrogenstimulering som kan inducera regelbunden endometrieavstötning och därigenom återställa ett menstruationsmönster vid funktionell hypotalamisk amenorré (FHA, t.ex. idrottaramenorré) eller PCOS-relaterad oligoamenorré. I POP-format (75 µg desogestrel) hämmar läkemedlet ovulation och kan paradoxalt nog orsaka amenorré hos vissa användare genom kontinuerlig progestinexponering utan östrogen.

Det är viktigt att notera att COC vid FHA ger hormonellt stöd utan att åtgärda den underliggande störningen i hypotalamus-hypofys-gonadaxeln. Desogestrels specifika bidrag i amenorrébehandling – till skillnad från östrogen-progestin-kombinationens gemensamma farmakologiska effekt – är inte isolerat klarlagt i befintlig litteratur, vilket begränsar evidensnivån.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Fas 3 | Avslutad | 121 | Undersöker hormon- och kroppssammansättningsförändringar hos unga idrottare med och utan menstruationsavbrott samt om transdermal eller oral östrogen ökar bentäthet vid idrottaramenorré (FHA). COC med desogestrel kan ingå som interventionsarm, men den primära forskningsfrågan är fettreglering av reproduktionsfunktion – inte specifik desogestrel-behandling av amenorré. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Fas 4 | Okänd | 42 | Jämför långtidseffekter (59 veckor) av vaginal och oral kombinerade p-piller på androgenproduktion, insulinmetabolism, lipidprofil och hs-CRP hos PCOS-patienter. Amenorré är inte primärt utfall; relevant som bakgrundsdata för desogestrel vid hormonella menstruationsrubbningar. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Klinisk observationsstudie | Gynecological Endocrinology | Jämför blödningsprofil hos kvinnor med kardiovaskulära riskfaktorer som använder drospirenon 4 mg vs. desogestrel 0,075 mg. Desogestrel-gruppen uppvisade sämre cyklisk kontroll inkl. hög amenorréfrekvens, vilket belyser desogestrels direkta koppling till amenorré som biverkningsprofil. |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | RCT | Br J Obstet Gynaecol | Jämförelse av Mercilon (20 µg EE + 150 µg desogestrel) och Marvelon/Desolett (30 µg EE + 150 µg desogestrel) avseende tillförlitlighet, cyklisk kontroll och biverkningsprofil. Visar att lägre östrogendos ökar risken för oregelbunden blödning och amenorré. |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Cochrane systematisk översikt | Cochrane Database Syst Rev | Systematisk genomgång av 20 µg vs. >20 µg östrogen i COC. Relevant för att förstå hur desogestrel-innehållande lågdosformuleringar påverkar blödningsmönster och amenorréincidens. |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Cochrane systematisk översikt | Cochrane Database Syst Rev | Tidigare version av ovanstående Cochrane-översikt. Understryker att lägre östrogendos i COC är associerad med mer oregelbunden blödning och förhöjd amenorréfrekvens. |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Klinisk studie | J Reprod Med | Utvärderar hur minskande doser etinylöstradiol påverkar bentäthet hos unga kvinnor med hypotalamisk oligoamenorré som behandlas med COC. Direkt relevant för amenorrébehandling med östrogen-progestin-kombinationer innehållande desogestrel. |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Farmakodynamisk studie | Acta Obstet Gynecol Scand Suppl | Utvärderar androgenicitet hos progestogener med fokus på desogestrel. Kopplar desogestrels låga androgenicitet till minskat acne, hirsutism och amenorréliknande bild jämfört med testosteronderiverade progestogener. |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Klinisk observationsstudie | Am J Obstet Gynecol | Genomgång av tolerabilitetsprofilen för desogestrel/EE COC. Beskriver icke-preventiva hälsofördelar inkl. reducerad dysmenorré och effekt på menstruationsmönster. |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Översikt | Obstet Gynecol Surv | Genomgång av de tre nya progestogenerna desogestrel, norgestimat och gestoden; betonar lägre hormondoser och förbättrad tolerabilitetsprofil inkl. effekter på menstruationscykeln. |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Översikt | Br Med Bull | Genomgång av COC-säkerhet och -effektivitet med fokus på dosreduktion och klinisk hantering; relevant bakgrund för desogestrels roll i reglering av menstruationscykeln. |
| [1604074](https://pubmed.ncbi.nlm.nih.gov/1604074/) | 1992 | Översikt | Rev Med Liège | Allmän genomgång av hormonell preventivmedel; kontextualiserar desogestrel bland moderna tredje generationens progestogener. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- TxGNN-förutsägelsepoängen är mycket hög (99,96 %) och den mekanistiska länken till amenorré är biologiskt rimlig, men befintliga kliniska prövningar saknar amenorré som primärt utfall och studiedesignen är heterogen. Evidensnivån L2 grundar sig på indirekt fas 3-data, vilket inte är tillräckligt för en direkt rekommendation om återanvändning för amenorréindikationen.

**För att gå vidare krävs:**
- Prospektiv klinisk prövning med amenorré (FHA, PCOS-relaterad oligoamenorré eller sekundär amenorré) som primärt utfall, med desogestrel POP (75 µg) eller desogestrel/EE COC som specificerad intervention
- Precisering av vilken amenorréétiologi och läkemedelsformulering (COC vs. POP) som är den primära kandidaten – dessa har skilda verkningsmekanismer och säkerhetsprofiler
- Fullständig säkerhetsdatainhämtning: varningar, kontraindikationer och läkemedelsinteraktioner saknas i nuvarande evidenspaket och måste kompletteras innan klinisk bedömning kan genomföras
- Registreringsbedömning: desogestrel-innehållande produkter är ej marknadsförda i Sverige; registrering eller licensiering måste utredas för eventuell klinisk prövning på svensk mark
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

