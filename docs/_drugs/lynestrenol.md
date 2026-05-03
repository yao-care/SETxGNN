---
layout: default
title: Lynestrenol
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 5
---

# Lynestrenol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **5** st
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

Using `txgnn-pipeline` skill for context — now generating the Swedish evaluation report based on the Evidence Pack.

---

# Lynestrenol: Från syntetiskt gestagen till migrän med eller utan aura

## Sammanfattning

Lynestrenol är ett syntetiskt gestagen (progestogen) som traditionellt används vid gynekologiska tillstånd såsom menstruationsrubbningar och endometrios, men är inte godkänt på den svenska marknaden. TxGNN-modellen förutsäger att det kan vara effektivt vid **migrän med eller utan aura**, via delade genetiska mekanismer mellan epilepsi och migrän (jonkanalsgener som CACNA1A och SCN1A). Evidensunderlaget för denna specifika indikation är begränsat: **0 kliniska prövningar** och **20 publikationer** finns tillgängliga, varav merparten berör epilepsigenetik snarare än Lynestrenols direkta effekt mot migrän.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige – indikationsdata saknas |
| Förutsagd ny indikation | Migrän med eller utan aura |
| TxGNN-förutsägelsepoäng | 99,51% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga direkt Lynestrenol-specifika studier |
| Marknadsstatus i Sverige | Ej på marknaden |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd information är Lynestrenol ett syntetiskt gestagen som binder till progesteronreceptorer och modulerar den hormonella miljön. Dess gynekologiska effekter är välbelagda, men en direkt koppling till migrän saknas i tillgänglig dokumentation.

TxGNN-modellens förutsägelse bygger på att epilepsi och migrän delar genetisk sårbarhet via jonkanalsgener (t.ex. CACNA1A, SCN1A). Den hypotetiska mekanistiska vägen lyder: **Lynestrenol → progesteronreceptorer → neurosteroideffekter → positiv modulering av GABA-A-receptorer → dämpning av kortikal hyperexcitabilitet (CSD)** – vilket är en gemensam patofysiologisk komponent vid migrän med aura. Denna väg är dock höggradigt spekulativ, och det saknas direkta bevis för att Lynestrenol som syntetiskt gestagen producerar tillräckliga neurosteroidmetaboliter (t.ex. allopregnanolon-analoger) in vivo för att uppnå en kliniskt meningsfull GABA-A-effekt.

Det är värt att notera att det vid sidan av denna förutsägelse finns en äldre klinisk rapport (PMID 14091721, år 1963) om Lynestrenol (Orgametril) som profylaktisk behandling mot migrän i allmänhet – med hormonstabilisering (reduktion av östrogendropp) som troligare biologisk mekanism. Detta stärker inte den epilepsi-aura-genetiska väg som driver Rank 1-förutsägelsen, men antyder att ett biologiskt samband mellan Lynestrenol och migränprofylax förtjänar vidare utredning.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Nedanstående 10 publikationer är de mest relevanta ur sökningen (n = 20). Notera att ingen publikation studerar Lynestrenol direkt vid migrän med aura — litteraturen belyser den epilepsi–migrän-genetiska överlappning som driver TxGNN:s förutsägelse.

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [33856647](https://pubmed.ncbi.nlm.nih.gov/33856647/) | 2021 | Översikt | Molecular Neurobiology | Epilepsi och migrän delar genetiska och molekylära mekanismer; gemensamma miljöfaktorer och specifika gener har identifierats som patogena vid båda tillstånden |
| [23294289](https://pubmed.ncbi.nlm.nih.gov/23294289/) | 2013 | Genetisk studie | Epilepsia | Genetisk sårbarhet är delad mellan migrän och epilepsi i EPGP-kohorten, vilket stödjer TxGNN:s modelllogik för denna förutsägelse |
| [34575901](https://pubmed.ncbi.nlm.nih.gov/34575901/) | 2021 | Översikt | Int J Mol Sci | Genomgång av molekylära mål för antiepileptogenesis; inkluderar GABA-relaterade vägar relevanta för mekanismhypotesen |
| [34209535](https://pubmed.ncbi.nlm.nih.gov/34209535/) | 2021 | Översikt | Int J Mol Sci | Neuroinflammation som bidragande faktor vid epilepsi; relevant för den gemensamma patofysiologin vid epilepsi–migrän |
| [17460155](https://pubmed.ncbi.nlm.nih.gov/17460155/) | 2007 | Genetisk länkningsstudie | Neurology | Familjär oksipitotemporallobsepilepsi kopplad till migrän med visuell aura; lokus kartlagt till kromosom 9q — direkt stöd för epilepsi-migrän-aura-kopplingen |
| [24874544](https://pubmed.ncbi.nlm.nih.gov/24874544/) | 2014 | Litteraturöversikt | Neurobiology of Disease | Könsskillnader i anfallskänslighet; hormonella faktorer (inkl. progestogen) diskuteras som modulatorer av epileptogenicitet |
| [16244322](https://pubmed.ncbi.nlm.nih.gov/16244322/) | 2005 | Översikt | Human Molecular Genetics | Sårbarhetsgener för komplex epilepsi; GABA- och jonkanalsmutationer utgör centrala mekanismer |
| [16201993](https://pubmed.ncbi.nlm.nih.gov/16201993/) | 2005 | Översikt | Epilepsia | GABA-A- och glutamatreceptorers roll i kortikal excitabilitet – mekanistisk bakgrund till progesteron/GABA-A-hypotesen |
| [22938964](https://pubmed.ncbi.nlm.nih.gov/22938964/) | 2012 | Bokkapitel/Översikt | Handbook of Clinical Neurology | Genomgång av djurmodeller för epilepsi; patofysiologiska insikter om jonkanalers roll |
| [22266888](https://pubmed.ncbi.nlm.nih.gov/22266888/) | 2011 | Översikt | Seminars in Neurology | Genetik vid epilepsi; polygena faktorer och sårbarhetsgeners bidrag till anfallströskel |

---

## Säkerhetsaspekter

> Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivån är L5 (enbart modellförutsägelse) för indikationen "migrän med eller utan aura". Inga kliniska prövningar eller direkta Lynestrenol-specifika studier stöder denna specifika förutsägelse. Den föreslagna mekanistiska vägen via neurosteroid GABA-A-modulering är plausibel på teoretisk nivå men saknar empiriskt stöd för just Lynestrenol som syntetiskt gestagen.

**För att gå vidare krävs:**
- Hämta och granska produktresumén (SmPC/SPC) för Lynestrenol för verkningsmekanism, varningar och kontraindikationer – särskilt avseende migrän med aura (WHO MEC-klassificering)
- Utföra en systematisk litteratursökning specifikt inriktad på Lynestrenol + migrän, inte enbart epilepsi-migrän-komorbiditet i allmänhet
- Bekräfta om Lynestrenol producerar aktiva neurosteroidmetaboliter (t.ex. allopregnanolon-analoger) in vivo i tillräckliga koncentrationer för GABA-A-modulering
- Utreda om WHO MEC Kategori 4 (kombinerade p-piller kontraindicerade vid migrän med aura) även gäller rent gestagena preparat som Lynestrenol – detta är avgörande för säkerhetsbedömningen
- Överväga att låta Rank 2-indikationen ("migraine disorder", evidensnivå L4) bli primär utredningsriktning, då den 1963 års direkta kliniska rapport (PMID 14091721) ger ett svagare men mer biologiskt trovärdigt underlag
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

