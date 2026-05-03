---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 1
---

# Sumatriptan
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

Använder **txgnn-pipeline** för att säkerställa rätt rapportformat för detta TxGNN Sweden-projekt. Nu genererar jag rapporten utifrån Evidence Pack-data.

---

# Sumatriptan: Från migrän till migrän med hjärnstamsaura

## Sammanfattning

Sumatriptan är ett välkänt akutläkemedel mot migrän som verkar som selektiv agonist vid 5-HT₁B/1D-receptorer och vars effekt vid vanlig migrän är väletablerad. TxGNN-modellen förutsäger att sumatriptan kan vara effektivt mot **migrän med hjärnstamsaura (MBA)**, en specifik undergrupp av migrän med aura som engagerar hjärnstam eller bilateral kortex. Förutsägelsen stöds av **18 publikationer** – varav 2 randomiserade kliniska prövningar och 1 systematisk översikt – men saknar kliniska prövningar specifikt utformade för MBA-undergruppen.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Akutbehandling av migrän (välkänd klinisk indikation; inga produkter registrerade i systemet) |
| Förutsagd ny indikation | Migrän med hjärnstamsaura |
| TxGNN-förutsägelsepoäng | 99,74 % |
| Evidensnivå | L3 – Systematisk översikt och observationsstudier |
| Marknadsstatus i Sverige | Ej registrerad (0 godkända produkter i systemet) |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta datapaket. Baserat på känd information är sumatriptan en selektiv 5-HT₁B/1D-receptoragonist. Läkemedlet dämpar migränanfall via två parallella mekanismer: inhibering av det trigeminovaskulära systemet (via 5-HT₁D) och konstriktion av intrakraniella blodkärl (via 5-HT₁B), vilket sammantaget minskar frisättningen av vasoaktiva neuropeptider från peritrigeminal dura.

Migrän med hjärnstamsaura (MBA, tidigare benämnd basilär migrän) delar grundläggande patofysiologi med övriga migränformer med aura – aurafenomenen drivs av cortical spreading depression (CSD) eller hjärnstamsdysfunktion. Den 5-HT₁D-medierade trigeminala inhibitionen bör teoretiskt vara verksam även vid MBA. Historiskt uppstod kontraindikationen mot triptaner vid MBA av oro för att 5-HT₁B-aktivering av arteria basilaris skulle kunna framkalla posterior cirkulationsischemi. Internationella Huvudvärksällskapet (IHS) mjukade dock upp denna restriktiva hållning i klassificeringsrevisionen 2013 och omdöpte tillståndet till just "migrän med hjärnstamsaura" för att minska stigmat kring behandling.

TxGNN-modellens höga förutsägelsepoäng (99,74 %) speglar sannolikt det starka sambandet i kunskapsgrafen mellan sumatriptan och migrän som helhet, snarare än en specifik validering av MBA-undergruppen. Bristen på MBA-dedikerade randomiserade kliniska prövningar innebär att effekt- och säkerhetsgränserna för just denna subtyp – framför allt avseende posteriorcirkulationsrisk – ännu inte är kvantifierade.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Dubbelblind RCT (n=100) jämförde ingefärspulver med sumatriptan vid akut migrän utan aura; likvärdig smärtlindrande effekt observerades i de två armarna. |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Tidig administration av sumatriptan förhindrade PACAP38-inducerade migränanfall; understryker värdet av tidigt insatt triptan­behandling. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematisk översikt | Headache | American Headache Society:s uppdaterade evidensutvärdering av akuta migrän­läkemedel; sumatriptan klassificeras med stark evidens (nivå A) för akutbehandling. |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Klinisk analys | Neurology | Sumatriptans effektivitet var signifikant reducerad vid migrän med aura jämfört med migrän utan aura – direkt relevant för MBA-undergruppen. |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Dubbelblind placebokontrollerad parallellgruppsstudie av sumatriptan 200 mg oral vid akut migrän med aura; effektgraden i öppna förstudier uppgick till 70–85 %. |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Klinisk studie | Neurology | Undersökte subkutant sumatriptan i relation till migränaura; ger insikt om triptaners påverkan på aurafasen och tidpunktens betydelse. |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Granskning | Cephalalgia | Detaljerad genomgång av sumatriptans 5-HT₁-receptoragonism, trigeminal inhibering och peritrigeminal kärlmekanism baserat på samtliga publicerade prövningar vid den tidpunkten. |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Klinisk studie | JAMA Neurology | PET-studie undersökte om sumatriptan penetrerar CNS och binder centrala 5-HT₁B-receptorer under pågående migränanfall; ger mekanistisk information om centralt kontra perifert verkningssätt. |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Läkemedelsgranskning | Expert Review of Neurotherapeutics | Subkutan sumatriptan (Sumavel DosePro) godkänt för akut migrän med/utan aura och klusterhuvudvärk; subkutan administrering visas vara snabbast och mest effektiv administreringsväg. |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Granskning | Handbook of Clinical Neurology | Status migrainosus som erkänd komplikation till migrän med/utan aura (>72 timmar); behandlingsprinciper och sjukvårdsbörda sammanfattas, triptaner ingår i behandlingsarsenalen. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensnivån är L3 – sumatriptans effekt vid MBA saknar dedikerade randomiserade kliniska prövningar, och säkerhetsgränserna för posteriorcirkulationsischemi vid denna specifika subtyp är inte kvantifierade trots att IHS 2013 mjukade upp den historiska kontraindikationen. TxGNN:s höga poäng reflekterar generell migränassociation snarare än MBA-specifik validering.

**För att gå vidare krävs:**
- Genomförande av en MBA-specifik fas II RCT med sumatriptan för att fastställa effekt och säkerhet
- Prospektiv insamling av säkerhetsdata avseende posterior cirkulationsischemi hos MBA-patienter behandlade med sumatriptan
- Inhämtning av fullständig produktresumé (SmPC) för komplett säkerhetsprofil: kontraindikationer, varningar och läkemedelsinteraktioner
- Genomgång av uppdaterade riktlinjer i ljuset av IHS 2013-revisionen och eventuella nyare meta­analyser om triptaner vid aura­subtyperna
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

