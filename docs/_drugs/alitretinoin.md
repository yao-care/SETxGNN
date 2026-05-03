---
layout: default
title: Alitretinoin
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

Tack för kontexten. Nu genererar jag rapporten baserat på Evidence Pack för Alitretinoin.

---

# Alitretinoin: Från kronisk handeksem till akne

## Sammanfattning

Alitretinoin (9-cis-retinsyra) är ett oralt retinoidt läkemedel godkänt i Europa för behandling av svår kronisk handeksem som inte svarar på starka topikala kortikosteroider, men är inte registrerat i Sverige. TxGNN-modellen förutsäger att **akne** är den mest evidensstödda nya indikationen, stödd av **1 klinisk prövning** och **5 publikationer** – och en direkt klinisk jämförelse mellan 9-cis-RA och isotretinoin vid akne finns redan publicerad (PMID 8884148). Notera att den högst rankade TxGNN-förutsägelsen (rang 1: amenorré, poäng 99,99 %) bedöms vara ett falskt positivt signal, eftersom amenorré är en känd biverkning av retinoidbehandling och inte ett terapeutiskt mål.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Kronisk svår handeksem (europeiskt godkännande; ej registrerad i Sverige) |
| Förutsagd ny indikation | Akne (rang 2; rang 1 = amenorré bedöms vara falskt signal) |
| TxGNN-förutsägelsepoäng | 99,92 % |
| Evidensnivå | L3 – Klinisk jämförelsestudie och narrativa översikter |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta – Forskningsfråga |

---

## Varför är denna förutsägelse rimlig?

Detaljerad MOA-data från DrugBank saknas för tillfället, men alitretinoins verkningsmekanism är väl känd i litteraturen: Det är en endogen retinoid (9-cis-retinsyra) som binder och aktiverar **både RAR (α, β, γ) och RXR (α, β, γ)** nukleära receptorer – ett bredare receptortäckningsspektrum än isotretinoin (13-cis-RA), som primärt verkar via RAR-aktivering efter intracellulär isomerisering.

Retinoidernas **sebosuppressiva effekt** via RAR/RXR-aktivering är den välestablerade mekanismen bakom aknebehandling. Aktiveringen hämmar proliferationen av sebocyter och reducerar talgkörtlarnas storlek, vilket direkt motverkar den patofysiologiska grunden för akne. Därutöver dämpar retinoiderna den follikulära inflammationen via nedreglering av IL-1α och TNF-α. Alitretinoins bredare receptorbindningsprofil innebär teoretiskt sett ett minst lika brett effektspektrum som isotretinoin vid denna indikation.

Den direkta kliniska jämförelsen i PMID 8884148 (Ott et al., 1996) visar att 9-cis-RA (alitretinoin) är lika aktiv som 13-cis-RA vid hämning av sebocytproliferation och reduktion av talgkörtelstorleken in vitro och in vivo, vilket ger en mekanistisk brygga från den godkända hudindikationen till akne. Moderna fas 2/3 RCT-data specifikt för alitretinoin vid akne saknas dock helt, och det är det enskilt största hindret för att gå vidare.

> **⚠️ Not om rang 1 (amenorré):** Den högst rankade förutsägelsen (amenorré, TxGNN-poäng 99,99 %) ska tolkas med stor försiktighet. Menstruationsstörningar – inklusive amenorré – är kända biverkningar av retinoidbehandling och drabbar uppskattningsvis 10–20 % av patienterna. TxGNN-modellen kan ha feltolkat biverkningstabellens fenotypsignal som ett terapeutiskt samband i kunskapsgrafen. Amenorré betraktas inte som en reell återanvändningsindikation.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Okänd | 300 | Undersöker om nasal slemhinnertorrhet orsakad av oral retinoidbehandling (isotretinoin) ökar risken för COVID-19-infektion. Studien avser isotretinoin, inte alitretinoin, och frågeställningen gäller infektionsrisk – inte aknebehandling. Låg direkt relevans för denna utvärdering. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [8884148](https://pubmed.ncbi.nlm.nih.gov/8884148/) | 1996 | Klinisk jämförelsestudie | Dermatology | **Direktjämförelse:** 9-cis-RA (alitretinoin) är lika aktiv som 13-cis-RA vid hämning av sebocytproliferation och minskning av talgkörtlarnas storlek. Starkaste evidensen för akneindikationen. |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Narrativ översikt | Clinics in Dermatology | Aktuell genomgång av vitamin A och retinoider i dermatologi. Alitretinoin nämns explicit som ett oralt retinoidt läkemedel i kliniskt bruk; retinoidernas roll vid akne och andra hudsjukdomar sammanfattas. |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Expertöversikt | Skin Pharmacology and Applied Skin Physiology | Retinoiders pleiotropa funktioner och selektiva verkan på hudstrukturer; framtida dermatologiska indikationer diskuteras, inklusive sebosuppressiva tillämpningar. |
| [8884149](https://pubmed.ncbi.nlm.nih.gov/8884149/) | 1996 | Klinisk farmakologistudie | Dermatology | Oral all-trans-retinsyra sänker talgproduktionen hos unga manliga försökspersoner – stödjer retinoidernas generella sebosuppressiva effekt som prediktiv markör för anti-akneaktivitet. |
| [10521699](https://pubmed.ncbi.nlm.nih.gov/10521699/) | 1999 | Mekanistisk grundforskning | Biochimica et Biophysica Acta | Detaljerad genomgång av retinoidbindande proteiner och enzymatisk metabolism; förklarar hur naturliga retinoider som 9-cis-RA aktiverar nukleära receptorer och reglerar epiteliell differentiering. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> Fullständiga varningsuppgifter och kontraindikationer för den svenska/europeiska marknaden (SMPC) saknas i detta datamaterial (Data Gap DG001). Känt från litteraturkontexten är att alitretinoin klassificeras som **teratogen kategori X** och är strikt kontraindicerat under graviditet – detta är en fundamental säkerhetsbegränsning för reproduktivt aktiva patienter och berör direkt akne-populationen.

---

## Slutsats och nästa steg

**Beslut: Avvakta – Forskningsfråga**

**Motivering:**
Biologisk plausibilitet för alitretinoin vid akne är välgrundad – den direkta jämförelsestudien mot isotretinoin (PMID 8884148) och retinoidklassens sebosuppressiva mekanism ger ett trovärdigt mekanistiskt underlag. Den avgörande flaskhalsen är frånvaron av moderna, dedikerade kliniska prövningar specifikt för alitretinoin vid akne, kombinerat med avsaknad av marknadsregistrering i Sverige.

**För att gå vidare krävs:**
- Genomföra en fas 2-studie med alitretinoin (oral, standarddos) vid måttlig–svår akne med aktiv kontrollarm (isotretinoin) för direktjämförelse
- Hämta och granska fullständig SMPC-säkerhetsdata inklusive varningar, kontraindikationer och teratogena risker för tilltänkt population (Data Gap DG001)
- Komplettera MOA-data från DrugBank API (Data Gap DG002)
- Utreda regulatorisk väg för akneindikation inom EU/Sverige, inklusive hantering av graviditetsprevention (PREG-program) i enlighet med befintlig europeisk riskminimeringsstrategi för alitretinoin
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

