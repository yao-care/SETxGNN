---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Axitinib
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

Använder `txgnn-pipeline` för kontexten. Nu genererar jag rapporten baserat på Evidence Pack.

---

# Axitinib: Från njurcellscancer till RCC med Xp11.2-translokation/TFE3-genfusion

## Sammanfattning

Axitinib är en selektiv tyrosinkinashämmare som riktar sig mot VEGFR-1, -2 och -3, godkänd i flera länder för behandling av avancerat njurcellscancer (mRCC). TxGNN-modellen förutsäger att det kan vara effektivt mot **njurcellscancer associerad med Xp11.2-translokationer/TFE3-genfusioner** – en sällsynt molekylär subtyp som framför allt drabbar barn och unga vuxna. Förutsägelsen stöds för närvarande av **1 pågående klinisk fas 2-prövning** som specifikt inkluderar denna patientgrupp.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Avancerat/metastaserande njurcellscancer (mRCC) |
| Förutsagd ny indikation | Njurcellscancer associerad med Xp11.2-translokation/TFE3-genfusion |
| TxGNN-förutsägelsepoäng | 99,90 % |
| Evidensnivå | L2 – 1 aktiv fas 2-prövning med direkt koppling till subtypen |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Axitinib är en andra generationens oral tyrosinkinashämmare med hög selektivitet mot VEGFR-1, -2 och -3. Dess inhibitoriska koncentration (IC₅₀) för VEGFR-familjen är upp till tio gånger lägre än för äldre preparat som sunitinib och sorafenib. Läkemedlets kärnmekanism är att blockera tumörens angiogenessignal – nybildning av blodkärl som tumören behöver för att växa och metastasera.

Vid njurcellscancer med Xp11.2-translokation/TFE3-genfusion bildas fusionsproteiner med transkriptionsfaktorn TFE3 till följd av kromosombrott på Xp11.2. Dessa fusionsproteiner uppregulerar VEGF-A-uttrycket och aktiverar MET/mTOR-signalering, vilket gör VEGFR-hämning till en biologiskt rationell behandlingsstrategi. Subtypen utgör mer än 40 % av njurcellscancer hos barn men förekommer även hos unga vuxna.

Den kliniska plausibiliteten stärks ytterligare av att axitinib redan visat robust effekt vid konventionellt RCC i pivotala studier (AXIS, KEYNOTE-426, JAVELIN Renal 101), och att den pågående fas 2-prövningen NCT03595124 explicit rekryterar patienter med TFE/translokations-RCC i alla åldersgrupper, inklusive pediatrisk population. Behandlingsramverket för etablerat RCC kan därigenom utvidgas till denna sällsynta subtyp.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Fas 2 | Aktiv, ej rekryterande | 15 | Randomiserad prövning som jämför axitinib + nivolumab mot nivolumab monoterapi vid inoperabelt eller metastaserat TFE/translokations-RCC. Inkluderar alla åldersgrupper. Axitinib verkar genom att blockera enzymer nödvändiga för tumörtillväxt. Beräknad avslutning november 2026. |

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande för denna specifika subtyp.

---

## Marknadsinformation Sverige

Axitinib är för närvarande **inte registrerat i Sverige**. Inga godkännanden finns registrerade hos Läkemedelsverket.

> Notera: Axitinib (Inlyta®) är godkänt av FDA (2012) och EMA för behandling av avancerat njurcellscancer efter tidigare behandling. En introduktion på den svenska marknaden kräver separat ansökan till Läkemedelsverket/MPA.

---

## Cytotoxicitet

Axitinib är ett antineoplastiskt läkemedel (VEGFR-tyrosinkinashämmare) avsett för cancerbehandling.

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Målriktad terapi – selektiv VEGFR-tyrosinkinashämmare (TKI), ej konventionell cytotoxisk kemoterapi |
| Myelosuppressionsrisk | Låg till medel; TKI-klass orsakar sällan allvarlig benmärgssuppression jämfört med konventionell kemoterapi |
| Emetogenicitetsklassificering | Låg till medel (oral TKI; illamående förekommer men är sällan av hög grad) |
| Övervakningspunkter | Blodtryck (hypertension är vanlig biverkan), tyreoideafunktion (hypo- och hypertyreoidism), leverfunktion (ASAT/ALAT), fullständigt blodstatus, njurfunktion |
| Hanteringsskydd | Oral beredning (tablett); standardrutiner för hantering av orala antineoplastiska läkemedel tillämpas |

---

## Säkerhetsaspekter

Fullständig säkerhetsbedömning kunde inte genomföras på grund av saknad produktinformation för den svenska marknaden (se datagap DG001).

> Se produktresumén (SmPC) för fullständig information om varningar, kontraindikationer och säkerhetsdata.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Axitinib har en välgrundad verkningsmekanism för VEGFR-driven njurcancer, och TFE3-fusionsproteinets roll i VEGF-A-uppregulering ger en tydlig biologisk koppling till denna subtyp. En pågående fas 2-prövning (NCT03595124) ger direkt klinisk evidens, men det lilla urvalet (n=15) och frånvaron av publicerade resultat motiverar ett avvaktande förhållningssätt tills fullständiga data föreligger.

**För att gå vidare krävs:**
- Invänta slutresultat från NCT03595124 (beräknad avslutning november 2026)
- Inhämta och granska fullständig SmPC/produktresumé för formell säkerhetsbedömning (datagap DG001)
- Komplettera MOA-data via DrugBank för fördjupad mekanismanalys (datagap DG002)
- Utvärdera pediatrisk dosering och långtidssäkerhet (tillväxt, kardiovaskulär uppföljning) separat för barn och unga vuxna
- Vid bekräftad klinisk evidens: inleda registreringsprocess hos Läkemedelsverket/MPA
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

