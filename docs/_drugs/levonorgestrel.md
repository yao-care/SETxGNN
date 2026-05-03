---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
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

Jag använder `txgnn-pipeline`-skillet för vägledning och genererar nu rapporten baserat på Evidence Pack:et.

---

# Levonorgestrel: Från hormonell antikonception till aknebehandling

## Sammanfattning

Levonorgestrel är ett syntetiskt gestagen (19-nor progestin) som primärt används i hormonella preventivmedel — inklusive kombinerade p-piller, intrauterin spiral och subderma implantat. TxGNN-modellen förutsäger att det kan vara effektivt mot **akne**, med **5 kliniska prövningar** och **20 publikationer** som för närvarande stöder denna riktning. Evidensen är starkast för levonorgestrel i kombination med etinylestradiol i orala preventivmedel, och mekanismen är biologiskt plausibel men kontextberoende.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Hormonell antikonception (preventivmedel) |
| Förutsagd ny indikation | Akne (acne disease) |
| TxGNN-förutsägelsepoäng | 99,88% |
| Evidensnivå | L3 – Observationsstudier och kliniska studier |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Levonorgestrel tillhör 19-nortestosteronserien och besitter uttalad gestagenaktivitet kombinerat med viss androgenaktivitet. Det binder till androgenreceptorer i talgkörtlarna och kan teoretiskt stimulera talgproduktion — vilket i sin tur kan förvärra akne. Denna androgenicitet är en grundläggande egenskap som skiljer levonorgestrel från antiandrogena progestiner som drospirenon och klormadinon.

I klinisk praxis används levonorgestrel emellertid nästan alltid i kombination med etinylestradiol (EE) i kombinerade p-piller. I detta kombinationsformat motverkas den androgena effekten: östrogen höjer nivåerna av könshormonbindande globulin (SHBG), vilket sänker mängden fritt testosteron i blodet. Nettoresultatet är reducerade biologiskt tillgängliga androgener och potentiell förbättring av akne — ett samband som bekräftats i minst en randomiserad placebokontrollerad studie (PMID 12196750).

Mekanismen är alltså dubbelriktad och helt beroende av formuleringskontext: enbart levonorgestrel (progestin-only) riskerar att förvärra akne via androgenreceptorstimulering, medan kombinationen EE/LNG kan förbättra akne via SHBG-medierad androgenreduktion. Användningsscenariot måste därför avgränsas tydligt innan klinisk tillämpning kan rekommenderas.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Avslutad | 131 | Undersökte kontinuerlig oral antikonception (innehållande levonorgestrel) kombinerat med doxycyklin för att minska oplanerade blödningar. Doxycyklin används kliniskt vid aknebehandling; studien ger direkt jämförande data för LNG-innehållande p-piller i akne-relevant kontext. |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Avslutad | 101 498 | Stor prospektiv kohortstudie jämförde nomegestrolacetat/estradiol-OC mot LNG-innehållande kombinerade p-piller avseende kortvariga och långvariga säkerhetsutfall; akne är sannolikt inkluderat som biverkningsändpunkt och ger robust realtidsdata. |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Fas 2 | Avslutad | 100 | Randomiserad dubbelblind placebokontrollerad studie av gestrinone-implantat (19-nortestosteronderivat, likt LNG) vid endometrios-relaterad bäckensmärta. Androgenrelaterade biverkningar inklusive akne kan ha dokumenterats systematiskt. |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Avbruten | 44 | Studie av LNG-IUS för prevention av endometriecancer hos överviktiga kvinnor. Avbruten i förtid (N=44). Studiebeskrivningen nämner akne explicit som biverkan vid orala gestagener, vilket motiverade val av IUS-formulering. |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Fas 2 | Okänd | 60 | Pilotstudie av LNG-IUS (Mirena) kontra megestrol vid atypisk endometriehyperplasi hos fertilitetsbevarande kvinnor. Begränsad direkt relevans för akne; dokumenterar LNG-IUS biverkningsprofil. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatology | Randomiserad placebokontrollerad studie av lågdos-OC (EE 20 µg/LNG 100 µg) vid måttlig akne. Visade förbättring av biokemiska androgenitetsmarkörer och klinisk akne — starkaste direkta evidensen för EE/LNG vid akneindikation. |
| [10717776](https://pubmed.ncbi.nlm.nih.gov/10717776/) | 1999 | Klinisk studie | Contraception | Multicenterstudie jämförde EE 20 µg/LNG med EE 20 µg/annat gestagen; påvisade divergerande effekter på SHBG och fritt testosteron, med direkta implikationer för akneoutcome beroende av progestinval. |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Systematisk översikt | Drugs | EE/klormadinon var signifikant effektivare än EE/LNG 0,03/0,15 mg vid mild till måttlig papulopustulär ansiktsakne. Bekräftar att EE/LNG är aktivt mot akne men inte optimalt jämfört med antiandrogena gestagener. |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Översikt | Am J Medicine | Genomgång av androgenicitet hos 19-nortestosteron-progestiner. Levonorgestrel identifieras som androgenaktiv — grundläggande mekanistisk referens för aknekopplingen. |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Översikt | J Women's Health | Jämförelse av drospirenon mot MPA, levonorgestrel och mikroniserat progesteron. Drospirenon minskar akne och hirsutism via antiandrogen effekt, medan LNG saknar denna egenskap — kontextualiserar LNG:s begränsning. |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Översikt | Am J Clin Dermatology | Akne, hirsutism och seborre som pilosebaceösa störningar vid hyperandrogenemi. Hormonella OC med antiandrogen effekt diskuteras som behandling; LNG-baserade OC nämns i jämförelse. |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Cochrane-översikt | Cochrane Database Syst Rev | Systematisk Cochrane-översikt av LNG-IUS vid endometriehyperplasi. Dokumenterar biverkningsprofil inklusive androgenrelaterade effekter såsom akne vid systemisk absorption. |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Översikt | Semin Reprod Med | Genomgång av LNG-IUS:ens endometrieeffekter och kliniska profil. Androgena biverkningar inklusive akne och håravfall nämns i biverkningsavsnittet — relevant för riskprofil. |
| [2403935](https://pubmed.ncbi.nlm.nih.gov/2403935/) | 1990 | Översikt | Fertility Sterility | Diskuterar lipider, kardiovaskulär sjukdom och OC. Androgenicitet hos progestiner och deras metaboliska konsekvenser behandlas; bakgrundskontext för LNG:s biverkningsprofil. |
| [1773615](https://pubmed.ncbi.nlm.nih.gov/1773615/) | 1991 | Översikt | Contraception | Jämförelse av LNG-IUD (20 µg/dag) med koppar-IUD över 5 år (N=1 821). Biverkningsprofil inklusive androgenrelaterade effekter dokumenteras systematiskt. |

---

## Marknadsinformation Sverige

Levonorgestrel har inga registrerade godkännanden i Sverige enligt tillgänglig data i detta Evidence Pack (0 licenser).

> **Notering:** Globalt är levonorgestrel ett av de mest använda gestagener och finns godkänt i ett stort antal länder under varumärken som Mirena® (IUS), Jadelle® (implantat) och Norlevo® (akutpreventivmedel). Avsaknaden av svenska licensdata i detta pack bör verifieras mot MPA:s läkemedelsdatabas innan slutsatser dras om faktisk marknadsstatus.

---

## Säkerhetsaspekter

Specifik säkerhetsdata (varningar, kontraindikationer och läkemedelsinteraktioner) saknas i detta Evidence Pack.

> Se produktresumén (SmPC) för säkerhetsinformation.

> **Klinisk notering:** Baserat på etablerad klinisk kunskap inkluderar välkända risker med levonorgestrel-innehållande kombinerade p-piller: venös tromboembolism (VTE) — särskilt vid samtidig rökning och ålder >35 år; androgenrelaterade biverkningar såsom akne, hirsutism och humörförändringar; samt kontraindikationer vid känd trombofili, aktiv leversjukdom och hormonsensitiv malignitet. Dessa bör bekräftas via officiell SmPC innan vidare bedömning.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Det finns en biologiskt plausibel och partiellt kliniskt studerad mekanism för levonorgestrel (i kombination med etinylestradiol) vid aknebehandling, understödd av L3-evidens. Mekanismen är dock kontextberoende och dubbelriktad — formulering och kombination med östrogen är avgörande för om effekten är gynnsam eller negativ vid akne.

**För att gå vidare krävs:**
- Tydlig avgränsning av behandlingsscenario: kombinerat p-piller (EE/LNG) kontra progestin-only-formulering (LNG-IUS, implantat, minipiller)
- Hämtning av fullständig SmPC och officiella varnings-/kontraindikationsdata (data gap DG001)
- Bekräftelse av verkningsmekanism via DrugBank API (data gap DG002)
- Verifiering av faktisk marknadsstatus i Sverige via MPA:s läkemedelsdatabas
- Identifiering av ytterligare direkta RCT-data specifikt för EE/LNG vid akneindikation för att kunna höja evidensnivån från L3 mot L2
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

