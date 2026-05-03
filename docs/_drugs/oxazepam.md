---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 1
---

# Oxazepam
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

Använder **txgnn-pipeline** för att generera en strukturerad läkemedelsåteranvändningsrapport, och följer **Läkemedelsåteranvändning Utvärderingsrapport Prompt v5** för format och svenska sektionsrubriker.

---

# Oxazepam: Från ångestbehandling till insomni

## Sammanfattning

Oxazepam är ett bensodiazepinpreparat som traditionellt används vid ångestsyndrom och alkoholabstinenssyndrom. TxGNN-modellen förutsäger att det kan vara effektivt mot **insomni**, med **0 registrerade kliniska prövningar** och **11 publikationer** – varav 2 randomiserade kontrollerade studier – som för närvarande stöder denna riktning. Förutsägelsepoängen på 99,86 % är exceptionellt hög och är väl underbyggd av oxazepams etablerade verkningsmekanism via GABA-A-receptorn.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ångestsyndrom och alkoholabstinens (bensodiazepinklass) |
| Förutsagd ny indikation | Insomni |
| TxGNN-förutsägelsepoäng | 99,86 % |
| Evidensnivå | L1 (minst 2 randomiserade kontrollerade studier) |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Oxazepam är en positiv allosterisk modulator av GABA-A-receptorn – det vill säga ett klassiskt bensodiazepinpreparat. Genom att förstärka den GABAerga hämmande signalöverföringen i centrala nervsystemet producerar oxazepam tydliga sömnframkallande effekter: förkortad insomningstid, förlängd total sömntid och minskat antal nattliga uppvaknanden.

Kopplingen till insomni är direkt och välmotiverad. Insomni karakteriseras patofysiologiskt av ett tillstånd av överaktivering (hyperarousal) – förhöjd kortikal aktivitet, ökad sympatikustonus och störd dygnsrytm. Förstärkning av GABA-A-receptorn motverkar exakt detta tillstånd. Oxazepam har dessutom en relativt kort halveringstid jämfört med äldre bensodiazepiner som diazepam och flurazepam, vilket minskar risken för kvarstående dagtrötthet och residualsedation.

TxGNN-förutsägelsepoängen på 0,9986 återspeglar styrkan i den mekanistiska länken: modellen identifierar oxazepam som en av de starkaste kandidaterna för insomnibehandling, i full samklang med klinisk litteratur som sedan 1984 dokumenterat effekt vid sömnstörningar.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | The American Journal of Psychiatry | Oxazepam och flurazepam förbättrade polysomnografiska sömnmått hos 14 patienter med kronisk insomni; oxazepam orsakade inte dagtrötthet till skillnad från flurazepam |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | The Annals of Pharmacotherapy | Oxazepam jämfördes med melatonin för ångest och sömnkvalitet hos STEMI-patienter efter PCI; bensodiazepiner var effektiva men förenade med biverkningsrisk |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Systematisk översikt | Archives of Gerontology and Geriatrics | Genomgång av sömnmedels effektivitet och säkerhet hos patienter över 70 år med insomni och samsjuklighet, inklusive demens och depression |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Farmakoepidemologi | PeerJ | Långtidsanvändning av bensodiazepiner och z-läkemedel hos äldre kopplad till hög ålder, kvinnligt kön samt psykiatrisk och somatisk samsjuklighet |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Klinisk riktlinje | Journal of Clinical and Experimental Hepatology | Handläggning av alkoholabstinenssyndrom vid leversjukdom; insomni anges som ett tidigt abstinenssymtom som bensodiazepiner inklusive oxazepam adresserar |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Farmakokinetisk översikt | Expert Opinion on Drug Metabolism & Toxicology | Genomgång av farmakokinetiken hos anxiolytika inklusive bensodiazepiner; relevant för dosoptimering vid sömnindikation |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Klinisk observation | JAMA | Abstinenssyndrom vid byte från långverkande till kortverkande bensodiazepin (oxazepam ersatte diazepam); belyser oxazepams korta halveringstid och kliniska farmakokinetisk profil |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Narrativ översikt | Psychiatrische Praxis | Behandling av beteendemässiga och psykologiska symtom vid demens (BPSD) i DACH-regionen; bensodiazepiner inklusive oxazepam används vid sömnstörningar i denna patientgrupp |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Oxazepam uppvisar en exceptionellt hög TxGNN-förutsägelsepoäng (99,86 %) för insomni, starkt underbyggd av den välkända GABA-A-mekanismen. Två randomiserade kontrollerade studier och flera systematiska översikter och observationsstudier bekräftar klinisk relevans, vilket motiverar evidensnivå L1. Avsaknaden av registrering i Sverige och ofullständiga säkerhetsdata kräver dock kompletterande åtgärder innan vidare beslut.

**För att gå vidare krävs:**
- Inhämtning av fullständig säkerhetsinformation: produktresumé (SmPC), kontraindikationer och varningar saknas i nuvarande datakälla
- Genomförande av läkemedelsinteraktionsanalys (DDI-data ej tillgänglig)
- Regulatorisk utredning: oxazepam är ej registrerat i Sverige – formell ansökan om marknadsgodkännande eller licens krävs vid eventuell klinisk användning
- Bedömning av beroendepotential och ändamålsenliga förskrivningsbegränsningar; bensodiazepiner klassificeras som narkotika i Sverige (förteckning IV)
- Klargörande av ursprunglig godkänd indikation via TFDA-dokumentation (hämtning av officiellt godkänd indikationstext)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

