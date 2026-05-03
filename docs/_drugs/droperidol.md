---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Droperidol
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

TxGNN-pipeline-skillet är laddat. Nu genererar jag den fullständiga utvärderingsrapporten för Droperidol baserat på Evidence Pack.

---

# Droperidol: Från perioperativ sedering till huvudvärksstörningar

## Sammanfattning

Droperidol är ett butyrofenon-antipsykotikum som primärt använts som anestesipremedikation, för att förebygga postoperativt illamående och kräkningar, samt för akut sedering vid agitation. TxGNN-modellen förutsäger att läkemedlet kan vara verksamt mot **10 nya indikationer**, med **huvudvärksstörningar** som den indikation med det starkaste kliniska evidensstödet (evidensnivå L2). Evidensbasen för denna indikation innefattar **1 klinisk prövning** och **20 publikationer**, inklusive systematiska översikter från American Headache Society och Canadian Headache Society.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig användning | Anestesipremedikation, profylax mot postoperativt illamående och kräkningar, akut agitationshantering |
| TxGNN:s högst rankade förutsägelse | Tourette syndrome (TxGNN-poäng: 99,9%) |
| Starkast evidensstödd ny indikation | Huvudvärksstörningar (migrän) |
| TxGNN-förutsägelsepoäng (huvudvärk) | 99,5% |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Droperidol tillhör butyrofenon-klassen och verkar primärt som en **dopamin D₂-receptorantagonist** — samma mekanism som haloperidol, en av klassens mest välkända representanter. Förutom D₂-blockad uppvisar droperidol alfa₁-adrenerg blockad och antiemetiska egenskaper, vilket ger en farmakologiskt bred profil.

Vid migrän och andra primära huvudvärksstörningar hämmar D₂-antagonister dopaminsignalering i det trigeminovaskulära smärtnätverket och reducerar central sensitisering. Det antiemetiska tillägget är kliniskt värdefullt eftersom illamående och kräkningar ofta åtföljer migränanfall. Denna **dubbla verkan** — smärtlindrande och illamåendesupprimerande — ger en mekanistisk motivering som är starkare än för flertalet andra förutsagda indikationer i detta Evidence Pack.

Jämfört med haloperidol (som är indicerat vid Tourette syndrome) har droperidol en betydligt kortare halveringstid (~2 timmar jämfört med ~20 timmar), vilket gör det bättre lämpat för **akuta, episodiska tillstånd** som migränanfall på akutmottagning snarare än för långsiktig underhållsbehandling av kroniska tillstånd.

---

## Alla förutsagda indikationer

TxGNN har förutsagt 10 potentiella nya indikationer för droperidol. Nedan sammanfattas evidensstyrka och rekommendation för samtliga:

| Rank | Indikation | TxGNN-poäng | Evidensnivå | Rekommendation |
|------|-----------|-------------|-------------|----------------|
| 1 | Tourette syndrome | 99,9% | L4 | Avvakta |
| 2 | Tvångsmässigt hårdragningssyndrom (trichotillomania) | 99,9% | L5 | Avvakta |
| 3 | Manisk bipolär affektiv störning | 99,8% | L3 | Avvakta |
| 4 | ADHD, ouppmärksam typ | 99,7% | L5 | Avvakta |
| 5 | Nefrogen SIADH | 99,6% | L5 | Avvakta |
| 6 | ADHD (allmänt) | 99,5% | L5 | Avvakta |
| **7** | **Huvudvärksstörningar** | **99,5%** | **L2** | **Fortsätt med försiktighet** |
| 8 | Vanlig förkylning | 99,5% | L5 | Avvakta |
| 9 | Hypertricos | 99,5% | L5 | Avvakta |
| 10 | Specifika utvecklingsstörningar | 99,4% | L5 | Avvakta |

> **Viktiga noteringar om lägre rankade förutsägelser:**
> Indikationerna 1–6 och 8–10 saknar direkt klinisk evidens för droperidol specifikt. Tourette syndrome och manisk bipolär affektiv störning har mekanistisk plausibilitet via D₂-antagonism, men droperidols korta halveringstid och parenterala beredningsform lämpar sig inte för långsiktig behandling av dessa kroniska tillstånd. ADHD-indikationerna är farmakologiskt tveksamma — D₂-blockad verkar i motsatt riktning mot ADHD:s etablerade behandlingslogik (dopaminreuptakehämning).

---

## Kliniska prövningar

### Huvudvärksstörningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|--------------|
| [NCT01406860](https://clinicaltrials.gov/study/NCT01406860) | NA | Avslutad i förtid | 19 | Randomiserad dubbelblind studie som jämförde droperidol mot metoklopramid + difenhydramin för primär huvudvärk på akutmottagning. Prövningen avbröts i förtid med alltför få deltagare för definitiva slutsatser. Avbrottsorsak ej publicerad. |

> Inga registrerade kliniska prövningar finns för droperidol vid Tourette syndrome, bipolär manisk fas, trichotillomania, ADHD eller övriga förutsagda indikationer.

---

## Litteraturbevis

### Huvudvärksstörningar (primär indikation)

Urval av de 10 mest relevanta publikationerna, prioriterade efter studiekvalitet:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [25416184](https://pubmed.ncbi.nlm.nih.gov/25416184/) | 2015 | Systematisk översikt / Meta-analys | Annals of Pharmacotherapy | Utvärderade säkerhet och effekt av droperidol specifikt för akut migrän; stöder droperidol som ett giltigt akutalternativ. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematisk översikt | Headache | American Headache Society evidensbedömning av akuta migrän-farmakologier; droperidol ingår bland rekommenderade alternativ. |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematisk översikt | Cephalalgia | Canadian Headache Society systematisk genomgång och rekommendationer för migränbehandling på akutmottagning; droperidol lyfts fram som evidensbaserat alternativ. |
| [21435315](https://pubmed.ncbi.nlm.nih.gov/21435315/) | 2011 | Systematisk översikt | CJEM | Butyrofenoner (inkl. droperidol) ger effektiv migränlindring på akutmottagning; systematisk genomgång av samtlig tillgänglig evidens i ED-kontext. |
| [12552051](https://pubmed.ncbi.nlm.nih.gov/12552051/) | 2003 | RCT | Neurology | Randomiserad dubbelblind placebokontrollerad studie av droperidol vid akut migränanfall; utvärderade "rescue therapy" vid otillräcklig effekt av förstahandspreparat. |
| [11781912](https://pubmed.ncbi.nlm.nih.gov/11781912/) | 2002 | RCT | American Journal of Emergency Medicine | Randomiserad klinisk prövning av intramuskulärt droperidol för akut migrän i community-baserad akutmottagning; stöder klinisk effekt. |
| [9237411](https://pubmed.ncbi.nlm.nih.gov/9237411/) | 1997 | Prospektiv fallserie | Headache | Pilotundersökning av IV droperidol (n=35) vid status migrainosus och refraktär migrän i öppenvårdsinfusionscenter; markant smärtlindring hos majoriteten av patienterna. |
| [10452443](https://pubmed.ncbi.nlm.nih.gov/10452443/) | 1999 | Kontrollerad studie | American Journal of Emergency Medicine | Retrospektiv fallserie av IM droperidol för migränbehandling på suburban akutmottagning; preliminärt stöd för effekt och acceptabel tolerabilitet. |
| [32839811](https://pubmed.ncbi.nlm.nih.gov/32839811/) | 2020 | Narrativ översikt | AJHP | "Reintegrating droperidol into emergency medicine practice" — samlad genomgång av säkerhet, indikationer, effekt och dosering; migrän är en central akutindikation. |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Strukturerad översikt | Headache | Del 2 av 3-delsserie om rescue therapy vid akut migrän; neuroleptika inklusive droperidol analyseras och stöds som effektiva alternativ. |

### Manisk bipolär affektiv störning (sekundär indikation, L3)

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [27976370](https://pubmed.ncbi.nlm.nih.gov/27976370/) | 2016 | Cochrane systematisk översikt | Cochrane Database Syst Rev | Droperidol vid psykosinducerad aggression eller agitation; genomgång av butyrofenoner som farmakologisk tranquilisering vid akuta tillstånd. |
| [15495037](https://pubmed.ncbi.nlm.nih.gov/15495037/) | 2004 | Cochrane systematisk översikt | Cochrane Database Syst Rev | Droperidol vid akut psykos; används i flera länder för snabb farmakologisk lugnande av våldsamt eller agiterat beteende. |
| [321727](https://pubmed.ncbi.nlm.nih.gov/321727/) | 1977 | RCT | Journal of Nervous and Mental Disease | Dubbelblind placebokontrollerad studie (n=41 akut agiterade patienter); IV droperidol 10 mg gav signifikant snabbare agitationskontroll — 6/19 i droperidolgruppen behövde tilläggsbehandling vs. 19/22 i placebogruppen. |
| [9789713](https://pubmed.ncbi.nlm.nih.gov/9789713/) | 1998 | Fallrapporter + litteraturöversikt | Clinical Neuropharmacology | Tre fall av behandlingsrefraktär blandad mani som svarade på oralt droperidol (10–80 mg/dag); minskad agitation, förbättrad sömn och minskat taltempo observerades. Biverkning: dystoni i ett fall. |

---

## Marknadsinformation Sverige

Droperidol saknar för närvarande godkännanden hos Läkemedelsverket och är inte marknadsförd i Sverige. Inga registrerade produkter, godkännandenummer eller godkända indikationer finns att redovisa.

> Eventuell användning i Sverige förutsätter licensansökan eller klinisk prövningstillstånd via Läkemedelsverket.

---

## Säkerhetsaspekter

Specifik säkerhetsinformation i form av strukturerade varningar och kontraindikationer är inte tillgängliga för Sverige i detta Evidence Pack. Baserat på läkemedelsklassen och publicerad litteratur är följande kliniskt relevanta aspekter kända:

- **QTc-förlängning**: Droperidol associeras med dosrelaterad QTc-förlängning och potentiell torsades de pointes. FDA utfärdade en "black box warning" år 2001, vilket kraftigt begränsade användningen i USA under 2000-talet. EKG-kontroll före och efter administrering rekommenderas.
- **Extrapyramidala biverkningar**: Dystoni, akatisi och parkinsonism förekommer, särskilt vid högre doser. Biperiden IV är antidot vid akut dystoni (se PMID 2252483 avseende Thalamonal-kombinationen).
- **Hypotension**: Alfa₁-adrenerg blockad kan orsaka ortostatisk hypotension — kliniskt relevant vid IV-administrering på akutmottagning.
- **Kombination med QTc-förlängande läkemedel**: Bör undvikas med exempelvis klass IA/III-antiarytmika, fluorokinoloner och andra antipsykotika.

> Se produktresumé och gällande FASS-information (vid tillgänglighet via licens) för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Droperidol har ett mekanistiskt välgrundat och kliniskt evidensstött stöd för akut migränbehandling. Evidensbasen inkluderar två publicerade RCT, tre Cochrane-liknande systematiska översikter och formella rekommendationer från internationella huvudvärksorganisationer. Läkemedlet är dock inte marknadsförd i Sverige, och QTc-säkerhetsprofilen kräver strikt patienturval, EKG-monitorering och tydliga kliniska riktlinjer.

**För att gå vidare krävs:**
- Inhämtning av fullständig säkerhetsinformation för Läkemedelsverkets granskning (kontraindikationer, DDI-profil, QTc-riskbedömning)
- Utredning av möjlighet till licens för klinisk användning i Sverige
- Fastställande av optimal dos och administrationssätt (IV vs. IM) baserat på befintliga RCT-data
- Bedömning av droperidols position i förhållande till befintliga alternativ (metoklopramid, sumatriptan, ketorolac) vid akut migränbehandling i Sverige
- Vid positiv utfallsbedömning: samråd med Läkemedelsverket om förutsättningarna för en klinisk prövning eller expanded access-program
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

