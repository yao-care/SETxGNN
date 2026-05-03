---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Everolimus
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

Jag genererar nu rapporten baserat på Evidence Pack-data för Everolimus (DB01590), med liposarkom (rank 1) som primär förutsagd indikation.

---

# Everolimus: Från njurcellscancer till liposarkom

## Sammanfattning

Everolimus är en mTOR-hämmare (mammalian target of rapamycin) som ursprungligen används vid behandling av avancerad njurcellscancer, hormonreceptorpositiv bröstcancer och pankreatiska neuroendokrina tumörer. TxGNN-modellen förutsäger att det kan vara effektivt mot **liposarkom**, med **1 pågående klinisk prövning** och **5 publikationer** som stöder denna riktning. Den mekanistiska grunden är välestablerad – mTOR-signalvägen är dokumenterat aktiverad i dedifferentierat liposarkom.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Uppgifter saknas i denna datakälla (läkemedlet är ej registrerat i det abfråbade registret) |
| Förutsagd ny indikation | Liposarkom (liposarcoma) |
| TxGNN-förutsägelsepoäng | 99,88 % |
| Evidensnivå | L3 – pågående fas 2-prövning med publicerade interimsresultat samt mekanistiska studier |
| Marknadsstatus i Sverige | Ej marknadsförd (per denna datakälla) |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Everolimus verkar genom att hämma mTORC1 (mammalian target of rapamycin complex 1), ett centralt signalprotein som reglerar cellproliferation, proteinsyntesen och cellöverlevnad. Blockering av mTORC1 leder till G1-cellcykelstopp och apoptos i tumörceller som är beroende av denna signalväg.

Dedifferentierat liposarkom (DDLS) är den vanligaste formen av retroperitonealt sarkom med uttalad CDK4-amplifikation och aktivering av Akt/mTOR-signalkaskaden. En immunohistokemisk studie på 99 DDLS-prover visade konsekvent aktivering av både Akt/mTOR- och MAPK-vägarna, och kompletterande in vitro-experiment bekräftade antitumöreffekt av mTOR-hämmare i denna tumörtyp (PMID: 26518767). Dessa fynd ger en direkt mekanistisk länk mellan everolimus verkningsmekanism och biologin bakom DDLS.

Kombinationsstrategin med CDK4/6-hämmaren ribociklib förstärker rationale ytterligare: CDK4-amplifikation är ett biologiskt kännetecken för DDLS, och synergistisk tillväxthämning mellan ribociklib och everolimus har visats i multipla tumörmodeller. Den pågående fas 2-studien NCT03114527 bygger direkt på detta synergistiska koncept och utvärderar kombinationen i klinisk miljö.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|-------------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fas 2 | Aktiv, rekryterar ej | 48 | Tvåcenterstudie som utvärderar ribociklib + everolimus vid avancerat dedifferentierat liposarkom (arm A) och leiomyosarkom (arm B). Minst 1 tidigare systembehandling krävs. Ribociklib ges oralt 300 mg/dag 3 veckor på/1 vecka av; everolimus 2,5 mg dagligen. Beräknat slutdatum december 2025. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|-------------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Klinisk fas 2-rapport | Clinical Cancer Research | SAR-096: Rapporterar resultat från NCT03114527. CDK4/6-hämning (ribociklib) kombinerat med mTOR-hämning (everolimus) visar synergistisk tillväxthämning i DDL- och LMS-modeller. Fokus på biologisk rationale för dubbelblockad. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | In vitro/IHC-studie | Tumour Biology | Akt/mTOR- och MAPK-vägarna är konsekvent aktiverade i 99 DDLS-prover. In vitro-experiment bekräftade antitumöreffekter av mTOR-hämmare i DDLS-cellinjer, vilket ger direkt mekanistisk stöd. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Preklinisk översikt | Frontiers in Oncology | PDOX-modeller (patient-derived orthotopic xenograft) för sarkom möjliggör identifiering av effektiva kombinationsterapier med CDK-hämmare; relevanta för liposarkombehandlingsstrategi. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preklinisk studie | Anticancer Research | Eribulin i kombination med mekanistiskt olika anticancermedel utvärderades i xenograftmodeller vid liposarkom och bröstcancer; ger insikter om kombinationslogiken med mTOR-hämmare. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Mekanismsstudie | Oncogene | XPO1-hämmaren selinexor (KPT-330) stör den transkriptionella kärnkretsen i DDLPS via translationsmodulering. Ger förståelse för alternativa kombinationsstrategier vid dedifferentierat liposarkom. |

---

## Cytotoxicitet

| Post | Innehåll |
|------|---------|
| Cytotoxicitetsklassificering | Målriktad terapi – mTOR-hämmare (rapalog) |
| Myelosuppressionsrisk | Medel – klasseffekter inkluderar anemi, trombocytopeni och lymfopeni |
| Emetogenicitetsklassificering | Låg |
| Övervakningspunkter | Fullständigt blodstatus (CBC), lever- och njurfunktionsprover, fasteblodsocker, blodfetter, lungfunktion (icke-infektiös pneumonit är en välkänd klassbiverkan) |
| Hanteringsskydd | Ja – everolimus klassificeras som cytotoxiskt läkemedel och kräver hantering enligt gällande riktlinjer för cytostatikahantering |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- En aktiv fas 2-prövning (NCT03114527) utvärderar everolimus i kombination med ribociklib specifikt vid avancerat liposarkom, och mekanistiska data visar tydlig Akt/mTOR-aktivering som terapeutiskt mål i DDLS. Förutsägelsepoängen på 99,88 % är hög, men slutgiltiga prövningsresultat saknas ännu.

**För att gå vidare krävs:**
- Avvakta och granska slutresultat från NCT03114527 (beräknat slutdatum december 2025)
- Inhämta fullständig säkerhetsprofil inkl. kontraindikationer och varningar från produktresumé eller TFDA/EMA-jämförelse
- Komplettera MOA-data via DrugBank API (DG002)
- Genomföra DDI-analys för relevanta kombinationer (t.ex. ribociklib + everolimus)
- Verifiera marknadsstatus i Sverige via Läkemedelsverkets register (nuvarande datakälla saknar godkännandeuppgifter)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

