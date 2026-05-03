---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 1
---

# Isoniazid
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

Jag använder `txgnn-pipeline`-skillet för kontexten och genererar nu rapporten baserat på Evidence Pack-data.

---

# Isoniazid: Från tuberkulos till konjunktivit

## Sammanfattning

Isoniazid är ett välkänt antimykobakteriellt läkemedel som sedan decennier utgör hörnstenen i behandlingen av *Mycobacterium tuberculosis*-infektioner. TxGNN-modellen förutsäger att det kan vara verksamt mot **konjunktivit** (ögonkatarr), med **1 klinisk prövning** och **20 publikationer** som delvis stöder denna riktning. Det samlade evidensunderlaget är dock begränsat och avser nästan uteslutande **tuberkulös konjunktivit** – inte konjunktivit i allmänhet.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Tuberkulos (välkänd klinisk standardindikation; inga svenska registreringsdata tillgängliga) |
| Förutsagd ny indikation | Konjunktivit |
| TxGNN-förutsägelsepoäng | 99,4% |
| Evidensnivå | L4 |
| Marknadsstatus i Sverige | Inte registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata i Evidence Pack. Baserat på känd farmakologi är isoniazid ett prokymedicinerat antibiotikum mot mykobakterier: det aktiveras av katalas-peroxidasenzymet KatG inne i *M. tuberculosis* och bildar en reaktiv metabolit som hämmar InhA (enoyl-ACP-reduktas). Det blockerar därigenom biosyntesen av mykolsyror – en essentiell komponent i mykobakteriernas cellvägg – och leder till bakteriedöd. Denna mekanism är strikt specifik för mykobakterier och saknar känd effekt mot andra patogener som orsakar konjunktivit.

Sambandet mellan isoniazid och konjunktivit är välkänt men smalt avgränsat: läkemedlet förekommer i behandlingen av **tuberkulös konjunktivit** – ett ovanligt tillstånd där *M. tuberculosis* direkt infekterar bindhinnan – samt vid fliktenulär keratokonjunktivit som uppstår som en hypersensitivitetsreaktion mot tuberkulosantigener. Äldre studier har även visat positiv effekt av isoniazidprofylax på fliktenulär keratokonjunktivit i högendemiska populationer.

Det är viktigt att understryka att "konjunktivit" som diagnoskategori innefattar viral, bakteriell (icke-tuberkulos) och allergisk konjunktivit, för vilka isoniazid saknar mekanistiskt stöd. TxGNN:s höga poäng speglar troligtvis strukturella kopplingar i kunskapsgraferna mellan tuberkulos och tuberkulös konjunktivit, snarare än en bred återanvändningspotential över hela diagnosgruppen.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Fas 3 | Avslutad | 490 | Jämför biverkningsprofilen för 3HP- vs 1HP-regimen (båda innehåller isoniazid) vid behandling av latent tuberkulos. Konjunktivit förekommer eventuellt som biverkningsfynd snarare än som behandlingsmål – prövningen ger inget direkt stöd för isoniazid som behandling mot konjunktivit. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Interventionsstudie | Am Rev Respir Dis | Isoniazidprofylax vid fliktenulär keratokonjunktivit bland eskimåer i Alaska. Det starkaste direkta stödet för isoniazid mot tuberkulos-associerad konjunktivit i litteraturen. |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Övrigt | Ann Oculistique | Lokal behandling med isoniazid vid okulär tuberkulos; stödjer lokalt/systemiskt bruk mot tuberkulös ögonsjukdom inklusive konjunktivit. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Fallrapport | Medicine | Pediatrisk fliktenulär keratokonjunktivit associerad med primär sinonasal tuberkulos; behandlades med anti-TB-regim inkluderande isoniazid med gott utfall. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Fallrapport | Middle East Afr J Ophthalmol | Tuberkulös konjunktivit i anoftalmisk ögonhåla hos 27-årig kvinna med tidigare miliar-TB; belyser TB:s ovanliga ögonmanifestation. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Fallrapport | Cornea | *M. tuberculosis* presenterat som kroniskt rött öga med konjunktival infektion; behandlad med standardiserad anti-TB-terapi. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Fallserie | Oftalmologia | 28 fall av tuberkulös keratokonjunktivit inkl. 13 pediatriska; alla med positiv tuberkulintest och röntgenologiska TB-fynd; behandlade med anti-TB. |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Fallrapport | Can J Ophthalmol | Konjunktival fliktion som tidig markör för förestående klinisk tuberkulos; understryker vikten av tidig anti-TB-behandling inklusive isoniazid. |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Fallrapport | Clin Pediatrics | Oväntat fall av konjunktivit hos ungdom; belyser mykobakteriell etiologi som differentialdiagnos vid atypisk konjunktivit. |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Fallserie | Arch Ophthalmol | Primär tuberkulos i bindhinnan; tidiga dokumenterade fall av konjunktivalt tuberkulosengagemang behandlade med anti-TB-regim. |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Fallrapport | Rev Rhum Engl Ed | Isoniazid vid refraktär artropati efter intravesikal BCG-terapi; isoniazids roll vid BCG-relaterade komplikationer (inkl. konjunktivit i Reiter-liknande syndrom) diskuteras. |

---

## Marknadsinformation Sverige

Isoniazid är inte registrerat i Sverige enligt tillgängliga data – inga godkännandenummer eller produkter har hittats i den genomsökta databasen. Läkemedlet kan förekomma som licensläkemedel eller i kombinationspreparat som inte indexerats i nuvarande datakälla.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots en mycket hög TxGNN-förutsägelsepoäng (99,4%) baseras det samlade evidensunderlaget enbart på fallrapporter och äldre interventionsstudier (L4) – samtliga avgränsade till **tuberkulös konjunktivit**. Eftersom isoniazid saknar verkningsmekanism mot icke-mykobakteriella konjunktivitorsakar är återanvändningspotentialen smal och redan delvis integrerad i befintliga TB-behandlingsriktlinjer; det rör sig i praktiken om ett erkänt, men smalt, tillämpningsområde snarare än en ny indikation.

**För att gå vidare krävs:**
- Specificering av om satsningen avser enbart **tuberkulös konjunktivit** (befintlig indikation inom TB-vård) eller bredare konjunktivitetiologier (saknar mekanistiskt stöd)
- Genomgång av isoniazids regulatoriska status i Sverige via MPA/FASS för att fastställa om licensmöjlighet föreligger
- Systematisk översikt eller metaanalys av isoniazid vid okulär tuberkulos för att höja evidensnivån från L4 till L3 eller högre
- Verifiering av säkerhetsprofil (biverkningar, kontraindikationer, läkemedelsinteraktioner) via FASS eller WHO:s produktresumé
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

