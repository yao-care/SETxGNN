---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Miglustat
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

Använde `txgnn-pipeline`-skillet för att bekräfta arbetsflödet. Nu genererar jag rapporten för MIGLUSTAT. Primär indikation att rapportera väljs som **Tay-Sachs sjukdom** (rank 7) — den enda med faktisk klinisk evidens (L2), till skillnad från rank 1–6 och 8–10 som alla är L5/Hold utan stödjande data.

---

# Miglustat: Från Gauchers sjukdom till Tay-Sachs sjukdom

## Sammanfattning

Miglustat (Zavesca®) är ett oralt substratreduktionsterapi-läkemedel (SRT) som internationellt är godkänt för behandling av typ 1 Gauchers sjukdom och Niemann-Pick typ C, men som saknar godkännande i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Tay-Sachs sjukdom** (GM2-gangliosidos), med stöd av **5 kliniska prövningar** och **20 publikationer** som stöder denna riktning. Prediktionspoängen uppgår till 99,75 % och evidensnivån bedöms som **L2**, baserat på ett publicerat randomiserat kontrollerat försök och en systematisk översikt, om än med inkonsekventa effektresultat.

---

## Snabböversikt

| Post | Innehåll |
|---|---|
| Ursprunglig indikation | Gauchers sjukdom typ 1 (internationellt godkänd indikation; ej registrerad i Sverige) |
| Förutsagd ny indikation | Tay-Sachs sjukdom (GM2-gangliosidos) |
| TxGNN-förutsägelsepoäng | 99,75 % |
| Evidensnivå | L2 – 1 publicerat RCT + 1 systematisk översikt |
| Marknadsstatus i Sverige | Ej godkänd i Sverige |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

För närvarande saknas fullständig MOA-data i evidenspaketet. Baserat på publicerad litteratur (bl.a. PMID 12808890) är Miglustat en iminosocker (N-butyl-deoxynojirimycin, NB-DNJ) som verkar som en kompetitiv hämmare av enzymet **glukosylceramidsyntas** (UDP-glukos:ceramid glukosyltransferas). Genom att blockera det första glycosyleringssteget i glykosfingolipidsyntes minskar läkemedlet bildningen av glukosylceramid och efterföljande komplexa glykosfingolipider — detta är kärnan i SRT-strategin. Vid Gauchers sjukdom minskar denna mekanism ansamlingen av glukosylceramid i makrofagernas lysosomer.

Tay-Sachs sjukdom orsakas av brist på β-hexosaminidas A (HEXA-genmutation), vilket leder till att gangliosid GM2 ansamlas i nervcellers lysosomer. Eftersom GM2-gangliosid syntetiseras **nedströms glukosylceramid** i samma glykosfingolipidmetabolomväg, kan Miglustat teoretiskt minska flödet av GM2-förstadier från den proximala punkten och därigenom lindra den lysosomala substratbördan. Denna SRT-logik gäller i princip för alla GM2-gangliosidoser, inkl. Tay-Sachs och Sandhoffs sjukdom.

Kopplingen till ursprungsindikationen är stark: båda tillstånden är lysosomala inlagringssjukdomar med rubbad glykosfingolipidmetabolism, och SRT-rationalet delas. Prekliniska data i Tay-Sachs-musmodeller visade att NB-DNJ förhindrade GM2-ansamling i hjärnan (PMID 9103204). I klinisk praxis har dock efficacy-data visat sig vara inkonsekventa — det enda publicerade RCT (Shapiro et al., 2009) nådde inte sitt primära effektmått, och ett Fas 3-program avbröts.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---|---|---|---|---|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fas 3 | Avslutad | 10 | Farmakokinetik, säkerhet och tolerabilitet hos patienter med infantil GM2-gangliosidos (Tay-Sachs/Sandhoff). Signifikant Miglustat-koncentration påvisades i cerebrospinalvätska; primärt fokus var PK/säkerhet snarare än klinisk efficacy. |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fas 2 | Avslutad | 5 | Farmakokinetik och tolerabilitet vid enkla och upprepade doser hos juvenila GM2-gangliosidospatienter. Bekräftade PK-profil och acceptabel tolerabilitet; extremt litet urval. |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fas 3 | Avbruten | 30 | Effektutvärdering av Miglustat vid infantil Tay-Sachs och Sandhoffs sjukdom. Planerad avslutning september 2025; avbruten med ej angiven orsak i källdata — viktigt att utreda om avbrottet berodde på utebliven effekt, säkerhetssignal eller rekryteringsproblem. |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fas 4 | Avbruten | 16 | Syner-G: kombinationsterapi med Miglustat och ketogen diet vid infantil/juvenil gangliosidos. Avbröts med ofullständig rekrytering; kombinationsregimen visade sig svår att genomföra i praktiken. |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Fas 2 | Rekryterar | 21 | Långtidssäkerhet och effekt av Nizubaglustat (AZ-3102) hos GM2-gangliosidos- och NPC-patienter, inkl. en kohort som övergår från stabil Miglustat-behandling. Startdatum: februari 2026; pågår till 2030. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|---|---|---|---|---|
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematisk översikt | European Journal of Neurology | Systematisk genomgång av Miglustat-studier vid GM2-gangliosidos. Inkonsekventa resultat konstaterades; viss sjukdomsstabilisering kan förekomma vid sen-debut-former, men övertygande efficacy vid infantila former saknas. |
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | 12-månaders randomiserat, kontrollerat försök + 24 månaders förlängt öppet program. Utvärderade säkerhet och effekt vid GM2-gangliosidos. Det primära effektmåttet uppnåddes inte; viss kognitiv stabilisering observerades i undergrupper. |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Översikt | International Journal of Molecular Sciences | Kliniska egenskaper, patofysiologiska aspekter och aktuella behandlingsalternativ vid GM2-gangliosidos. Ger bred referensram för sjukdomsmekanismer och rollen för SRT. |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Översikt | Frontiers in Physiology | Nya terapistrategier vid Tay-Sachs, inkl. SRT, genterapi, enzymersättning och kombinationsbehandlingar. Placerar Miglustat i kontext av ett växande behandlingslandskap. |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Klinisk studie | Neurology | SRT med Miglustat hos 2 infantila Tay-Sachs-patienter. Neurologisk försämring kunde inte stoppas, men makrocefali förhindrades och signifikant läkemedelskoncentration i CSF påvisades — bevisar CNS-penetrans. |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Pilotstudie | Journal of Inherited Metabolic Disease | Neurokognitiv testning vid sen-debut Tay-Sachs (LOTS). Utforskade kognitiv funktion som terapeutiskt utfallsmått — relevant underlag för framtida studiedesign. |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Observationsstudie | Molecular Genetics and Metabolism | Kartläggning av klinisk tidslinje vid infantil gangliosidos. SRT med Miglustat prövades men begränsades av gastrointestinala biverkningar; inga godkända behandlingar finns för infantila former. |
| [12803928](https://pubmed.ncbi.nlm.nih.gov/12803928/) | 2003 | Preklinisk studie | Philosophical Transactions of the Royal Society B | SRT med NB-DNJ (Miglustat) i musmodeller av Tay-Sachs, Sandhoff och Fabrys sjukdom. Visade efficacy hos juvenila/adulta former; infantila former kräver tillägg av enzymförstärkning för meningsfullt resultat. |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Preklinisk studie | Science | Grundläggande studie: NB-DNJ förhindrade lysosomal GM2-inlagring i Tay-Sachs-möss och minskade antalet lagringsbelastade nervceller. Etablerade det biologiska rationalet för SRT vid GM2-gangliosidos. |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Läkemedelsprofil | Current Opinion in Investigational Drugs | Historisk översikt av Miglustat: EU-godkänt för Gauchers sjukdom 2002, under utveckling för Tay-Sachs, Fabrys sjukdom och Niemann-Pick typ C. Ger kontext för SRT-strategins ursprung och spridning. |

---

## Marknadsinformation Sverige

Miglustat är **inte godkänt i Sverige**. Inga registrerade godkännanden eller produktlicenser föreligger (totalt: 0). Läkemedlet marknadsförs i andra länder (EU, USA) under varumärkesnamnet Zavesca® för Gauchers sjukdom och Niemann-Pick typ C. För enskilda svenska patienter kan behandling eventuellt möjliggöras via Läkemedelsverkets licensförfarande.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Det finns ett välgrundat mekanistiskt rationale och ett historik av kliniska prövningar för Miglustat vid Tay-Sachs sjukdom, men det enda publicerade RCT nådde inte sitt primära effektmått och ett Fas 3-program avbröts av oklara skäl. Läkemedlet kan ha en begränsad roll vid sen-debut-former, men otvetydig klinisk efficacy — särskilt vid infantila former — är ännu inte fastställd.

**För att gå vidare krävs:**
- Utredning av avbrottsorsak för NCT03822013 (Fas 3) — om avbrottet berodde på efficacy-misslyckande är det ett avgörande negativt tecken
- Subgruppsanalys: är efficacy-signalen starkare för juvenil/sen-debut än infantil form?
- Konsultation med specialist i lysosomala inlagringssjukdomar för klinisk relevansavvägning
- Inhämtning av fullständig produktresumé och varningsinformation för säkerhetsbedömning
- Bevakning av NCT07399704 (Nizubaglustat-studie) som inkluderar patienter som tidigare behandlats med Miglustat — kan ge indirekt jämförelsedata
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

