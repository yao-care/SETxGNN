---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

Använder `txgnn-pipeline` för att generera en strukturerad läkemedelsåteranvändningsrapport för det svenska TxGNN-projektet (Se-deployment).

---

# Oxaliplatin: Från kolorektalcancer till malignt pleuralt mesoteliom

## Sammanfattning

Oxaliplatin är ett tredje generationens platinabaserat kemoterapiläkemedel med bevisad synergistisk aktivitet mot kolorektalcancer. TxGNN-modellen förutsäger att det kan vara effektivt mot **malignt pleuralt mesoteliom (MPM)** med en förutsägelsepoäng på 99,68 %. Förutsägelsen stöds av **6 kliniska prövningar** och **20 publikationer**, varav flera direkt har utvärderat oxaliplatin i kombinationsregimer specifikt för MPM.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Kolorektalcancer |
| Förutsagd ny indikation | Malignt pleuralt mesoteliom |
| TxGNN-förutsägelsepoäng | 99,68 % |
| Evidensnivå | L2 – 1 avslutad fas 2-prövning med direkt relevans |
| Marknadsstatus i Sverige | Inte marknadsfört |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Oxaliplatin är en platinakoordinationsförening med en DACH-bärligand (1,2-diaminocyklohexan). Läkemedlet binder kovalent till DNA och bildar intrastrand-crosslinks – framför allt 1,2-d(GpG)-addukter – samt interstrand-crosslinks, vilket blockerar DNA-replikation och transkription och utlöser apoptos. En central egenskap är att dessa DACH-bundna addukter i lägre grad känns igen av mismatch-reparationsproteiner jämfört med cisplatins addukter, vilket kan övervinna viss platinaresistens.

Sambandet mellan kolorektalcancer och malignt pleuralt mesoteliom bygger på en delad biologisk sårbarhet: mesoteliomceller, i synnerhet den epiteloida subtypen, uppvisar dokumenterat nedsatt kapacitet för nukleotidexcisionsreparation (NER) – den primära cellulära mekanism som reparerar platinaorsakade DNA-skador. Denna NER-defekt gör MPM-celler särskilt känsliga för oxaliplatins DNA-tvärbindningar, och utgör den biologiska grunden för att GEMOX-regimen (Gemcitabin + Oxaliplatin) och kombinationen Raltitrexed + Oxaliplatin specifikt har utforskats i MPM-studier.

Den mekanistiska logiken är direkt bekräftad i klinisk forskning: fas 2-prövningar visar påvisad aktivitet för oxaliplatin i kombinationsregimer som förstalinjebehandling vid MPM. Därtill inducerar oxaliplatin immunogen celldöd genom calreticulin-exponering på cellytan, vilket skapar ett biologiskt rationale för synergistisk kombination med checkpointhämmare – ett alltmer centralt behandlingsparadigm vid MPM.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|--------------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Fas 2 | Avslutad | 29 | Oxaliplatin + Gemcitabin som första- eller andralinjeterapi vid malign pleural eller peritoneal mesoteliom; direkt högkvalitativ evidens för kombinationens responsfrekvens och tolerabilitet |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Fas 2 | Okänd | 29 | Bortezomib + Oxaliplatin (VELCADE + ELOXATIN) hos tidigare behandlade MPM-patienter; max 6 cykler; tumörrespons utvärderades med CT-scanning var 8:e vecka |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Okänd | 1 000 | Internationellt multicenterdokumentationsregister för trycksatt intraperitoneal aerosolkemoterapi (PIPAC/PITAC) vid maligna pleural- och peritonealsjukdomar; oxaliplatin är ett vanligt PIPAC-läkemedel och ger verkliga användningsdata |
| [NCT07532902](https://clinicaltrials.gov/study/NCT07532902) | Fas 1 | Rekryterar | 60 | BMS-986504 i kombination med standardvård vid metastatiska MTAP-deleterade solida tumörer; standardvård kan inkludera platinabaserade regimer |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Fas 1 | Rekryterar | 345 | NX-1607 (CBL-B-hämmare) doseskalering i avancerade maligniteter med bred basket-design som eventuellt inkluderar mesoteliomkohort |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Fas 2-prövning | Journal of Clinical Oncology | Raltitrexed + Oxaliplatin i 70 MPM-patienter (55 kemonaiva, 15 förbehandlade); kombinationen visade klinisk aktivitet i MPM, en av de viktigaste primärstudierna |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Fas 2-prövning | Clinical Lung Cancer | Multicenterstudie GEMOX (Gemcitabin 1 000 mg/m² + Oxaliplatin 80 mg/m²) i 25 MPM-patienter, dag 1 och 8 per 21-dagarscykel; utvärderar klinisk aktivitet |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Fas 2-prövning | Journal of Occupational Medicine and Toxicology | Oxaliplatin ± Gemcitabin hos MPM-patienter förbehandlade med pemetrexed; ger andralinjeevidens för kombinationsanvändning |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Fas 2-prövning | Tumori | Pilotstudie Oxaliplatin + Raltitrexed vid inoperabel MPM; bygger vidare på fas 1-aktivitetsfynd; tidig klinisk bekräftelse |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Fas 2-prövning | Lung Cancer | Vinorelbine + Oxaliplatin som förstalinjebehandling i MPM; 21-dagarscykler upp till 6 cykler; rapporterar responsfrekvens och tolerabilitetsprofil |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Fas 2-prövning | Lung Cancer | Raltitrexed + Oxaliplatin som andralinjeterapi i MPM; 14 patienter, ingen objektiv respons uppnåddes – kombinationen inaktiv i andralinjeinställning; viktig negativ evidens |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Översikt | International Journal of Molecular Sciences | Oxaliplatin, cisplatin och pemetrexed undersökta för immunmodulerande egenskaper i MPM; oxaliplatin bedöms lovande för kombination med checkpointhämmare på grund av immunogenicitet |
| [10936465](https://pubmed.ncbi.nlm.nih.gov/10936465/) | 2000 | Översikt | Critical Reviews in Oncology/Hematology | Oxaliplatins kliniska aktivitetsprofil; brett tumörspektrum; DACH-liganden ger unik adduktsignatur och gynnsam säkerhetsprofil jämfört med cisplatin |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Översikt | British Journal of Cancer | Sammanfattning av kliniska prövningar i MPM-kemoterapi; platinabaserade kombinationer och antifolater mer lovande än konventionella cytotoxiska regimer |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Översikt | Seminars in Oncology | Antifolaters roll i MPM; raltitrexed/oxaliplatin och pemetrexed/cisplatin framhålls som de starkaste kombinationerna i tillgänglig fas 2-data |

---

## Marknadsinformation Sverige

Oxaliplatin är för närvarande **inte marknadsfört i Sverige**. Inga produktgodkännanden är registrerade (totalt 0 licenser).

---

## Cytotoxicitet

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Konventionell cytotoxisk – tredje generationens platinaanalog med DACH-bärligand (alkylerande/DNA-tvärbindande verkningsmekanism) |
| Myelosuppressionsrisk | Medel – trombocytopeni och neutropeni förekommer; generellt mildare benmärgspåverkan än cisplatin |
| Emetogenicitetsklassificering | Medel – antiemetisk profylax rekommenderas inför varje administrering |
| Övervakningspunkter | Fullständigt blodstatus (CBC) inför varje cykel; lever- och njurfunktion; neurologisk bedömning (kumulativ perifer sensorisk neuropati är den dosbegränsande toxiciteten) |
| Hanteringsskydd | Ja – beredning och administrering kräver skyddsåtgärder i enlighet med gällande cytotoxikahanteringsföreskrifter |

---

## Säkerhetsaspekter

Se produktresumén (SmPC) för fullständig säkerhetsinformation avseende varningar, kontraindikationer och läkemedelsinteraktioner.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Oxaliplatin uppvisar stark biologisk plausibilitet och direkt klinisk fas 2-evidens för behandling av malignt pleuralt mesoteliom via NER-defektmekanismen. Avsaknaden av svenska godkännanden samt ofullständig säkerhetsdokumentation motiverar ett strukturerat och försiktigt tillvägagångssätt.

**För att gå vidare krävs:**
- **Säkerhetsgranskning**: Hämta och analysera produktresumé (SmPC) från EMA eller Läkemedelsverket för att kartlägga kontraindikationer och viktigaste varningar
- **MOA-verifiering**: Komplettera DrugBank API-sökning för fullständig farmakodynamisk profil inklusive kända resistensmekanismer
- **Regulatorisk kartläggning**: Utred möjligheter för klinisk prövning eller licensansökan i Sverige i samråd med Läkemedelsverket
- **Subtypselektion**: Definiera huruvida studiedesignen ska fokusera på epiteloid MPM (bäst förväntad respons på grund av NER-defekt) eller en bredare MPM-population
- **Kombinationsstrategi**: Välj optimal kombinationspartner – Gemcitabin (GEMOX-regimen, starkast direkt evidens) eller immunterapi (för att utnyttja oxaliplatins immunogena celldödseffekt) – samt administreringsväg (systemisk IV kontra lokoregional HIPEC/PIPAC)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

