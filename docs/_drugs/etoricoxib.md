---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

Jag har hämtat `txgnn-pipeline`-skillet för kontext. Nu genererar jag rapporten baserat på Evidence Pack för ETORICOXIB.

---

# Etoricoxib: Från muskuloskeletal smärta till migrän

---

## Sammanfattning

Etoricoxib är en selektiv COX-2-hämmare inom NSAID-klassen som internationellt används för behandling av artrit, ankyloserande spondylit och akut muskuloskeletal smärta – men som i dagsläget saknar godkännande och marknadsföring i Sverige. TxGNN-modellen förutsäger med mycket hög säkerhet (**99,9 %**) att etoricoxib kan vara verksamt vid **migrän**, den högst rankade av tio utvärderade nya indikationer. Evidensunderlaget för just denna indikation är dock begränsat – det finns varken kliniska prövningar eller direkta publikationer som specifikt stöder etoricoxib vid migrän, vilket innebär att förutsägelsen i nuläget enbart vilar på modellens slutledning (L5).

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Ej registrerat i Sverige; internationellt godkänt för artrit, ankyloserande spondylit och akut muskuloskeletal smärta |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,9 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga direkta studier |
| Marknadsstatus i Sverige | Ej marknadsfört |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Etoricoxib verkar genom selektiv hämning av cyklooxygenas-2 (COX-2)-enzymet. Detaljerad MOA-data saknas i detta datapaket, men utifrån etablerad farmakologi: etoricoxib tillhör den selektiva COX-2-hämmande NSAID-klassen och reducerar prostaglandinsyntesen utan att i kliniska doser nämnvärt påverka COX-1. Det ger en teoretisk fördel vad gäller gastrointestinal tolerabilitet jämfört med icke-selektiva NSAID som indometacin.

Kopplingen till migrän är biologiskt plausibel. COX-2-hämning minskar syntesen av prostaglandin E2 (PGE2), en central förmedlare av perifer och central smärtsensibilisering samt neuroinflammation längs den trigeminovaskulära smärtaxeln – den patofysiologiska kärnan i migränattacker. Minskad PGE2-produktion kan i teorin dämpa den neurogena inflammation och centrala sensibilisering som driver och förlänger migränepisoder.

Ytterligare stöd för mekanistisk rimlighet ges av att etoricoxib delar grundläggande prostanoidhämmande verkningsmekanism med indometacin – ett väletablerat NSAID med bevisad effekt vid ett brett spektrum av indometacinresponsiva primära huvudvärkssyndrom. Inom detta Evidence Pack visar den lägre rankade indikationen *headache disorder* (rank 9) faktiskt L3-evidens, med direkta fallserier och case reports om etoricoxib vid indomethacin-responsiva tillstånd – vilket indirekt stärker den övergripande mekanistiska trovärdigheten. Direkta kliniska data specifikt för etoricoxib vid migrän saknas dock helt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande för etoricoxib vid migrän.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande som direkt undersöker etoricoxib vid migrän.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> **Notering:** Etoricoxib är inte godkänt i Sverige och saknar produktresumé hos Läkemedelsverket (MPA). Som selektiv COX-2-hämmare är läkemedlet internationellt associerat med förhöjd kardiovaskulär risk, njurpåverkan och risk för vätskeretention. Detaljerade varningsdata och kontraindikationer bör inhämtas via DrugBank (DB01628) och EMA:s produktinformation innan vidare utvärdering.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots ett TxGNN-förutsägelsepoäng på 99,9 % saknas helt kliniska prövningar och direkta publikationer för etoricoxib specifikt vid migrän. Evidensnivån är L5 – lägsta möjliga – vilket innebär att förutsägelsen inte kan utgöra grund för klinisk tillämpning. Därtill är etoricoxib ej registrerat i Sverige, vilket lägger till ett regulatoriskt hinder vid eventuell klinisk prövning.

**För att gå vidare krävs:**
- Utökad litteratursökning med breddade söktermer (inkl. migrän, trigeminovaskulär smärta, PGE2, COX-2 och primär huvudvärk)
- Identifiering av befintliga kliniska prövningar för etoricoxib vid migränrelaterade tillstånd i internationella register (ClinicalTrials.gov, ICTRP, EudraCT)
- **Prioritera parallell utredning av indikationen *headache disorder* (rank 9, L3-evidens, 2 kliniska prövningar + 5 publikationer)** som ett mer omedelbart kliniskt värdefullt spår med befintligt evidensunderlag
- Inhämta fullständig säkerhetsprofil via DrugBank API (MOA, kontraindikationer, DDI) och EMA:s produktresumé
- Regulatorisk bedömning hos Läkemedelsverket för eventuell klinisk prövning eller licensansökan i Sverige
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

