---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

Med hjälp av `txgnn-pipeline`-skickligheten som bakgrund, genererar jag nu rapporten baserat på Evidence Pack JSON:

---

# Zolmitriptan: Från migrän till migrän med hjärnstamsaura

## Sammanfattning

Zolmitriptan är ett selektivt serotonin 5-HT1B/1D-receptoragonist (triptan) som används för akut behandling av migränanfall. TxGNN-modellen förutsäger med en poäng på 99,99 % att läkemedlet kan vara effektivt mot **migrän med hjärnstamsaura** (tidigare kallad "basilär migrän"), en migränsubtyp där hjärnstamssymtom dominerar aurafasen. Förutsägelsen stöds av **0 registrerade kliniska prövningar** för den specifika subtypen, men av **19 publikationer** — inklusive systematiska översikter, metaanalyser och RCT:er — som dokumenterar triptan-klassens effekt vid migrän med aura.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Akut behandling av migränanfall (välkänd triptan-indikation; ej registrerat i Sverige) |
| Förutsagd ny indikation | Migrän med hjärnstamsaura |
| TxGNN-förutsägelsepoäng | 99,99 % |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Zolmitriptan är ett selektivt 5-HT1B/1D-receptoragonist som verkar längs den trigeminovaskulära signalvägen. Läkemedlet hämmar frisättningen av pro-inflammatoriska neuropeptider — framför allt CGRP (calcitonin gene-related peptide) och substans P — från trigeminusnervsändarna, och orsakar samtidigt vasokonstriktion av patologiskt utvidgade intrakraniella blodkärl. Till skillnad från äldre triptaner verkar zolmitriptan både centralt och perifert på trigeminusaktiveringen, vilket ger en bredare hämningsprofil.

Migrän med hjärnstamsaura (IHS-klassificeringen 2013 ersatte det tidigare begreppet "basilär migrän") delar samma trigeminusaktiverade patofysiologi som vanlig migrän med aura. Den historiska kontraindikationen mot triptaner vid denna subtyp grundades på teoretisk oro för vasokonstriktion i basilärkärlsgebiet, men 2015 omvärderade AHS/IHS-riktlinjerna dessa restriktioner och konstaterade att risken troligen hade överskattats — behandlingsresponsen förväntas vara jämförbar med övrig auramigrän.

Mekanistiskt är förutsägelsen välmotiverad: den patofysiologiska kärnan är densamma, och zolmitriptans centrala verkningsmekanism gör det särskilt relevant för migränsubtyper med hjärnstamsinvolvering. Individuell riskbedömning avseende hjärnstams-vaskulär effekt bör dock fortfarande genomföras, och den specifika subtypen saknar dedikerade prövningar.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande specifikt för migrän med hjärnstamsaura.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Klinisk studie | Headache | Rapporterar direkt användning av triptaner vid basilär migrän och migrän med prolongerad aura med prominenta neurologiska hjärnstamssymtom — mest direkt relevant för den förutsagda indikationen |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematisk översikt / Riktlinje (Tier 1) | Headache | American Headache Society:s uppdaterade evidensbedömning av farmakologiska akutbehandlingar för migrän; omvärderar triptan-klassens indikationsbredd |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Komparativ RCT / Metaanalys (Tier 1) | The Journal of Headache and Pain | Metaanalys jämför frovatriptan mot zolmitriptan, rizatriptan och almotriptan specifikt vid migrän med aura; utvärderar effekt under huvudvärksfasen |
| [15581383](https://pubmed.ncbi.nlm.nih.gov/15581383/) | 2004 | RCT (Tier 1) | CNS Drugs | Zolmitriptan 5 mg ODT vid akut migränbehandling; påvisade snabb smärtlindring inom 45 minuter och varaktigt behandlingssvar vid 2 timmar |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | Dubbelblind RCT, subgruppsanalys | Neurological Sciences | Frovatriptan vs. zolmitriptan 2,5 mg vid migrän med aura; cross-over-design med direkt jämförelse i aura-subpopulation |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | Randomiserad studie | Cephalalgia | Triptan-effekt vid migrän med tidig kutan allodyni; signifikant smärtreduktion vid tidig behandling med zolmitriptan i aurapatienter |
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | Dubbelblind RCT (TEENZ-studien) | Headache | Zolmitriptan nässpray 5 mg vid akut migrän hos ungdomar 12–17 år; smärtfrihet vid 2 timmar som primärt utfall |
| [9399016](https://pubmed.ncbi.nlm.nih.gov/9399016/) | 1997 | Fas 2/3 klinisk studie (Tier 2) | Cephalalgia | Tolerabilitetsprofil för zolmitriptan baserad på >3 000 patienter; fastställer säkerhetsprofilen i bred klinisk population inklusive doser 0,5–50 mg |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Systematisk översikt | Frontiers in Neurology | Behandlingsalternativ vid vestibulär migrän — en besläktad migränsubtyp med hjärnstamssymtom; summerar evidens för triptaner i hjärnstamsrelaterade migränformer |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Narrativ översikt (Tier 2) | Expert Opinion on Pharmacotherapy | Genomgång av zolmitriptans prekliniska farmakologi, RCT-data och kliniska tillämpningar; bekräftar selektiv 5-HT1B/1D-mekanism och dubbel central/perifer verkan |

---

## Marknadsinformation Sverige

Zolmitriptan är **inte registrerat i Sverige**. Inga produktgodkännanden finns registrerade hos Läkemedelsverket, och ingen produktresumé (SmPC) är tillgänglig för den svenska marknaden.

> **Notering:** Zolmitriptan (varumärke Zomig) är godkänt i ett flertal länder inom EU, USA och UK för akut migränbehandling i dosberedningsformerna oral tablett, munsönderfallande tablett och nässpray. Ansökan om godkännande för den svenska/europeiska marknaden behöver hanteras via EMA eller Läkemedelsverket.

---

## Säkerhetsaspekter

Se produktresumén (SmPC från ett godkänt land, exempelvis EMA SmPC för Zomig) för fullständig säkerhetsinformation avseende varningar, kontraindikationer och läkemedelsinteraktioner. Dokumenterade säkerhetsdata för Sverige saknas i det aktuella evidenspaketet.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
TxGNN förutsäger med utomordentligt hög poäng (99,99 %) att zolmitriptan är verksamt vid migrän med hjärnstamsaura. Evidensnivån L2 stöds av systematiska översikter och RCT:er för triptan-klassen vid migrän med aura, samt av ett starkt mekanistiskt stöd — men dedikerade prövningar specifikt för subtypen "migrän med hjärnstamsaura" saknas, och läkemedlet är inte registrerat i Sverige.

**För att gå vidare krävs:**
- Inhämtning av fullständig säkerhetsinformation från gällande SmPC (t.ex. EMA SmPC för Zomig) avseende kontraindikationer, varningar och läkemedelsinteraktioner
- Specifik riskbedömning av hjärnstams-vaskulär effekt vid zolmitriptan-behandling för denna subtyp
- Litteratursökning efter nyare prövningar (post-2015) specifikt designade för "migraine with brainstem aura" efter IHS-klassificeringens omarbetning
- Regulatorisk strategi för registrering i Sverige via Läkemedelsverket eller EMA
- Konsultation med neurologisk/huvudvärksmedicinsk expertis angående klinisk lämplighet och patientval
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

