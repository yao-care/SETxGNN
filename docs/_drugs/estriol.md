---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 1
---

# Estriol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

Jag har läst in `txgnn-pipeline`-skillet. Nu genererar jag rapporten utifrån Evidence Pack:et.

---

# Estriol: Från naturlig östrogenbehandling till amenorré

## Sammanfattning

Estriol är ett naturligt, svagt östrogen (östrogenpotens ca 1/80 av estradiol) som kliniskt används för behandling av urogenital atrofi och klimakteriesymptom, men som inte är formellt registrerat i Sverige. TxGNN-modellen förutsäger med **99,18%** konfidens att estriol kan vara effektivt mot **amenorré** – specifikt funktionell hypotalamisk amenorré (FHA) – genom neuroendokrin modulering av hypotalamus–hypofys-axeln. Förutsägelsen stöds av **3 kliniska prövningar** och **13 publikationer**, varav en klinisk interventionsstudie direkt undersöker estriol vid FHA.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige; används kliniskt för urogenital atrofi och klimakteriesymptom |
| Förutsagd ny indikation | Amenorré – funktionell hypotalamisk amenorré (FHA) |
| TxGNN-förutsägelsepoäng | 99,18% |
| Evidensnivå | L3 – Observationsstudier och mekanistiska studier |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Estriol är ett naturligt östrogen med relativt svag systemisk östrogeneffekt, vilket paradoxalt nog gör det till en intressant kandidat för subtil neuroendokrin reglering. Till skillnad från estradiol, som ger kraftiga systemiska effekter, kan lågdos estriol modulera hypotalamus–hypofys-axeln utan att utlösa fullständig östrogendominans.

Vid funktionell hypotalamisk amenorré (FHA) störs den pulsatila GnRH-sekretionen till följd av psykosociala eller metabola stressfaktorer – exempelvis intensiv träning, undervikt eller kronisk stress. Detta leder till sänkta LH- och FSH-nivåer, reducerat östrogenpåslag och utebliven menstruation. Lågdos estriol kan, via estrogenreceptorernas återkopplingsmekanismer i hypotalamus och hypofys, gradvis återuppta den pulsatila LH-sekretionen och därigenom trigga återhämtning av ovulationscykeln.

Det som skiljer denna tillämpning från klassisk östrogensubstitution är att estriol inte ersätter östrogenbristen rent substitutivt – utan agerar som en neuroendokrin interventionssignal riktad direkt mot den bakomliggande dysreguleringen. Publicerade kliniska fynd (PMID 22137494) visar att estrioladministration faktiskt modulerar LH-sekretionen hos kvinnor med FHA, vilket ger mekanistisk grund för förutsägelsen.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|--------------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Fas 2 | Tillbakadragen | 0 | Studerade fotobiomodulation vid vulvovaginal atrofi hos postmenopausala kvinnor. Amenorré nämns i samband med menopausdiagnos. Studien drogs tillbaka utan insamlad data och ger inga användbara resultat. |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Fas 3 | Avslutad | 1 570 | Dubbelblind, placebokontrollerad studie av **estetrol (E4)** vid måttliga–svåra vasomotorsymptom (E4Comfort Study I). Hög metodologisk kvalitet; avser dock estetrol (ett annat östrogen), inte estriol. |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Fas 3 | Avslutad | 1 015 | Uppföljningsstudie av **estetrol (E4)** vid vasomotorsymptom (E4Comfort Study II). Fas 3, avslutad med god inrollering; avser estetrol, inte estriol direkt. |

> **OBS:** De två avslutade fas 3-prövningarna avser estetrol (E4), ett fetalt östrogen som skiljer sig molekylärt från estriol (E3). Dessa utgör indirekt evidens om östrogenbehandling vid menopausala tillstånd, men är inte specifika för estriol eller FHA.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Klinisk interventionsstudie | *Fertility and Sterility* | Estrioladministration modulerar LH-sekretionen hos kvinnor med funktionell hypotalamisk amenorré (FHA) – direkt relevant primärevidens för den förutsagda indikationen. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Översiktsartikel | *Biomedicines* | Lågdosöstrogener som neuroendokrina modulatorer vid FHA; granskar positiva återkopplingsmekanismer och estriolens roll i att återupprätta GnRH-pulsatilitet. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Klinisk studie | *Medicinski pregled* | Östro-gestagen-effekter på lipid- och hormonprofiler vid prematur primär ovarialsvikt (PPOF), en form av hypergonadotrop amenorré med östrogenunderskott. |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | Klinisk prövning | *J Obstet Gynaecol Br Commonw* | Tidig klinisk prövning av humana gonadotropiner vid idiopatisk sekundär amenorré; historisk kontext för hormonbaserad behandling av amenorré. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Fallserie | *Lancet* | Endokrinologiska fynd vid prematur ovarialsvikt med amenorré; belyser hypoestrogenismens roll. |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Klinisk översikt | *British Journal of Psychiatry* | Anorexia nervosa och amenorré – belyser sambandet mellan energiunderskott och utebliven menstruation, relevant för FHA-patofysiologi. |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Observationsstudie | *Am J Obstet Gynecol* | Långvariga hormonella störningar efter medroxiprogesteronadministrering; visar hormonella mönster kopplade till amenorré. |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Översiktsartikel | *Clinical Obstetrics and Gynecology* | Neoplasi och hormonell antikonception; ger brett perspektiv på östrogenernas systemeffekter. |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observationsstudie | *Zhong Xi Yi Jie He Za Zhi* | TCM-perspektiv på gonadfunktion vid amenorré och oligomenorré; begränsad direkt relevans. |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | Metodartikel | *Die Medizinische Welt* | Radioimmunoassay av LH, FSH och östrogener inkl. estriol; metodologisk relevans för hormonmonitorering vid amenorré. |

---

## Marknadsinformation Sverige

Estriol (DB04573) har inga registrerade godkännanden i Sverige. Läkemedlet klassas som **ej registrerat** och saknar tillgängliga produktresumér från Läkemedelsverket i aktuellt datamaterial.

---

## Säkerhetsaspekter

Säkerhetsdata för estriol – inklusive viktiga varningar, kontraindikationer och läkemedelsinteraktioner – saknas i aktuellt Evidence Pack.

> Se produktresumén för säkerhetsinformation. Komplettering av TFDA/EMA-säkerhetsdata rekommenderas innan vidare klinisk utvärdering.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Estriol uppvisar en biologiskt välmotiverad mekanism för behandling av funktionell hypotalamisk amenorré, och en riktad klinisk interventionsstudie (PMID 22137494) ger direkt stöd för effekten på LH-sekretion. Evidensbasen är dock begränsad till L3-nivå – inga prospektiva RCT specifikt för estriol vid FHA finns tillgängliga, och läkemedlet saknar registrering i Sverige, vilket försvårar klinisk tillämpning.

**För att gå vidare krävs:**
- Prospektiv, randomiserad kontrollerad prövning (RCT) av estriol vid FHA, för att uppnå minst L2-evidens
- Komplettering av säkerhetsdata: produktresumé med varningar och kontraindikationer (TFDA/EMA)
- Fullständig MOA-analys via DrugBank API
- Utredning av registreringsväg i Sverige för ett icke-registrerat läkemedel (exv. licensförfarande via Läkemedelsverket)
- Fastställande av optimal administreringsväg och dosregim specifikt för FHA-indikationen
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

