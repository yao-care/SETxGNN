---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

Nu skriver jag rapporten enligt specifikationen för Evidence Pack v4.

---

# Tobramycin: Från Pseudomonas aeruginosa-infektion till exponeringskeratit

## Sammanfattning

Tobramycin är ett aminoglykosidantibiotikum som internationellt är etablerat för behandling av allvarliga infektioner orsakade av gramnegativa bakterier – i synnerhet *Pseudomonas aeruginosa* vid cystisk fibros och bakteriell keratit – men saknar marknadsgodkännande i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **exponeringskeratit** (exposure keratitis), en icke-infektiös hornhinnesjukdom orsakad av ofullständig ögonlocksslutning. Förutsägelsen stöds av **2 kliniska prövningar** och **7 publikationer**, men dessa är samtliga indirekta och evidensnivån bedöms som **L4**, vilket innebär att beslutet för denna indikation är **Avvakta**.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige – tobramycin används internationellt mot gramnegativa bakterieinfektioner (inkl. *Pseudomonas aeruginosa* vid cystisk fibros och bakteriell keratit) |
| Förutsagd ny indikation | Exponeringskeratit (exposure keratitis) |
| TxGNN-förutsägelsepoäng | 99,93% |
| Evidensnivå | L4 – prekliniska studier och mekanismstudier |
| Marknadsstatus i Sverige | Ej marknadsgodkänt |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i Evidence Pack. Baserat på känd farmakologi är tobramycin ett aminoglykosidantibiotikum som hämmar bakteriell proteinsyntes genom att binda till 30S-ribosomala subenheten, vilket orsakar felläsning av mRNA och produktion av dysfunktionella proteiner. Läkemedlet har bevisad klinisk effekt mot *Pseudomonas aeruginosa*, *Staphylococcus aureus* och andra gramnegativa patogener, och tobramycin i ögondroppsform är sedan länge etablerat vid bakteriell keratit.

Exponeringskeratit uppstår när ögonlocket inte kan sluta sig fullständigt – exempelvis vid Graves oftalmopati, facialispares eller vegetativt tillstånd – vilket leder till att hornhinnan torkar ut och utsätts för mekanisk irritation. Sjukdomen är primärt **icke-infektiös** och behandlas i första hand med tårsubstitut, ögonlocksförband och i svårare fall kirurgisk tarsorrafi. Sekundär bakteriell superinfektion är dock en känd komplikation, och det är i detta sammanhang tobramycin hypotetiskt skulle kunna ha en adjuvant roll.

Den mekanistiska kopplingen är alltså svag: tobramycin saknar verkan mot den underliggande hornhinneskadan vid exponeringskeratit och kan som mest fungera som profylax eller behandling av sekundärinfektion. TxGNN-modellens höga poäng förklaras sannolikt av nätverkets statistiska kopplingar mellan korneala sjukdomsentiteter snarare än en direkt biologisk logik – en känd begränsning när "keratit" ingår i sjukdomsnamnet utan att orsaksmekanismen är infektiös.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|--------------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | Ej fas | Okänd | 170 | Utvärderar PRF-membran (Platelet-rich Fibrin) vid fyra ögontillstånd: makulahål, pterygium, hornhinnesår och glaukom efter trabekelektomi. Tobramycin är inte studieläkemedlet och exponeringskeratit ingår inte som målindikation – indirekt koppling via okulär ytsjukdom. |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | Ej fas | Okänd | 40 | Jämför behandlingsmodaliteter vid dendritisk (viral) keratit orsakad av herpes simplex-virus (HSV). Varken tobramycin som primärläkemedel eller exponeringskeratit som målsjukdom – sjukdomsmekanismen (viral) skiljer sig fundamentalt från exponeringskeratit. |

> **Notering:** Båda prövningarna bedöms ha grad C-relevans. Inga kliniska prövningar av tobramycin specifikt vid exponeringskeratit är registrerade.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Fallrapport | Oxford Medical Case Reports | Bakteriell keratit orsakad av multiresistent *Shewanella algae* hos en patient i vegetativt tillstånd som inte kunde sluta ögonen voluntärt – kliniskt scenario direkt analogt med exponeringskeratit med sekundär bakteriell komplikation. |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Fallrapport | Ophthalmology | *Bacillus cereus*-keratit kopplad till kontaktlinsbärande – illustrerar hur hornhinnesårbarhet kan leda till opportunistisk bakteriell infektion, vilket är relevant för exponeringskeratitens komplikationsbild. |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Fallrapport | Eye & Contact Lens | Bilateral MRSA-keratit efter PRK – belyser vikten av antibiotikaprofylax vid procedurer som komprometterar hornhinnans barriärfunktion. |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Retrospektiv fallserie | Polish Journal of Veterinary Sciences | Okulär toxoplasmos hos 105 katter behandlad med kombinationsregim innehållande tobramycin – veterinärkontext med begränsad translationsbarhet till human exponeringskeratit. |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro-studie | Current Eye Research | Jämförande cytotoxicitetsanalys av fyra aminoglykosider (neomycin, gentamicin, tobramycin, amikacin) på odlade kaninhornhinneepitelceller. Tobramycin uppvisade lägst epitelcytotoxicitet bland de testade aminoglykosiderna – relevant för säkerhetsbedömning vid lokal användning. |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Laboratoriestudie | Nippon Ganka Gakkai Zasshi | MIC och post-antibiotisk effekt för ögondroppsantibiotika mot isolat från infektiös keratit i Japan – tobramycin ingår i jämförelsen och visar god aktivitet mot vanliga keratitpatogener. |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Fallrapport | Eye Science | Paracentralt kornealt dell hos patient med Graves oftalmopati – direkt kopplat till exponeringskeratit-mekanismen (exoftalmus och ofullständig ögonlocksslutning), men rapporten fokuserar på diagnos snarare än antibiotikabehandling. |

---

## Marknadsinformation Sverige

Tobramycin saknar marknadsgodkännande i Sverige. Det finns inga registrerade produkter i det svenska läkemedelsregistret (Läkemedelsverket). Eventuell klinisk användning kräver licensansökan eller import via nationellt undantagsförfarande.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Exponeringskeratit är en icke-infektiös tillstånd där tobramycin saknar primär terapeutisk verkningsmekanism; läkemedlet kan som mest ha en adjuvant roll vid sekundär bakteriell superinfektion, inte som behandling av grundsjukdomen. L4-evidensnivån bygger uteslutande på indirekta fallrapporter och in vitro-studier utan en enda klinisk prövning riktad mot denna indikation, vilket är otillräckligt för att motivera vidare utredning i nuläget.

**För att gå vidare krävs:**
- Prospektiv klinisk prövning som specifikt utvärderar tobramycin (eller bredspektrum-aminoglykosid) som profylax mot sekundärinfektion vid exponeringskeratit
- Verkningsmekanism-data (DrugBank MOA, datagap DG002) för att bättre bedöma mekanistisk relevans
- Säkerhets- och kontraindikationsdata (datagap DG001) innan säkerhetsinitialvärdering (S1) kan genomföras
- Tydligare definition av indikationsgränsen: är målet primärbehandling, adjuvant antibiotikaprofylax, eller specifik patientsubgrupp med kombinerad bakteriell superinfektion?

> **Not om bredare kontext:** Bland samtliga 10 förutsagda indikationer uppvisar **extern otit** (rank 3, L3) och **post-bacterial disorder/CF-Pseudomonas** (rank 5, L1) väsentligt starkare evidens och bättre mekanistisk koppling till tobramycins kända antibakteriella profil. Dessa indikationer kan lämpa sig bättre för fortsatt utredning om läkemedlet ska prioriteras.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

