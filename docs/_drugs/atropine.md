---
layout: default
title: Atropine
parent: Endast modellprediktion (L5)
nav_order: 45
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Atropine: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga godkännandedata"
monitor_inn: "atropine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Atropine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

## Atropin: Från [ej angiven ursprunglig indikation] till migrän
{: .text-alpha }

---

## Sammanfattning

Atropin är ett antikolinergt läkemedel (muskarinantagonist) som i Sverige har haft flera godkännanden som injektionsvätska och ögondroppar. Samtliga godkännanden är numera avregistrerade, och den ursprungliga indikationstexten saknas i det data som sammanställts för rapporten. TxGNN-modellen förutsäger att atropin kan vara effektivt mot **migrän** (poäng 99,6 %), men det finns **inga kliniska prövningar** och endast **prekliniska eller indirekta publikationer**. Evidensen är därför mycket begränsad (nivå L5).

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga godkännandedata |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L5 (endast modellförutsägelse, inga kliniska studier) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 9 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det data som sammanställts. Baserat på allmänt känd information är atropin en icke-selektiv muskarinreceptorantagonist, det vill säga det blockerar acetylkolins effekter på det parasympatiska nervsystemet.

Det finns ett biologiskt rimligt, men indirekt, samband med migrän. Prekliniska studier tyder på att det kolinerga systemet och parasympatiska nervbanor deltar i den neurogena inflammationen i hjärnhinnorna, som tros bidra till migränsmärta. En råttstudie (2024) undersökte hur kolinerg påverkan via mastceller i hjärnhinnan samverkar med migränmekanismer. En annan studie visade att stimulering av det parasympatiska sphenopalatina ganglionet ger plasmaproteinläckage i råttans dura mater. Atropin har dessutom minskat attackrelaterad svettning och tårflöde vid kronisk paroxysmal hemikrani, en besläktad huvudvärkssjukdom.

Bilden är dock inte entydig. För den andra förutsägelsen, migrän med hjärnstammsaura, visar en musstudie att *aktivering* av muskarinreceptorer hämmar kortikal spridande depression (grunden för migränaura). Det talar snarare för att blockad med ett antikolinergt läkemedel kan vara kontraproduktiv. Ingen studie visar direkt att atropin lindrar migrän hos människa.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preklinisk mekanismstudie | Eur J Neurosci | Kolinerg modulering via hjärnhinnans mastceller påverkar neurogen inflammation i en råttmodell för migrän |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preklinisk djurstudie | Exp Neurol | Stimulering av parasympatiskt ganglion ger plasmaproteinläckage i durans kärl hos råtta |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preklinisk djurstudie | J Pharmacol Exp Ther | Centrala kolinerga systemet medverkar i sumatriptans smärtlindrande effekt hos gnagare |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Klinisk observation | Cephalalgia | Systemiskt atropin minskade attackrelaterad svettning, tårflöde och nässekretion vid kronisk paroxysmal hemikrani (4 patienter) |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Översikt | J Appl Toxicol | Beskriver anisodamin, ett atropinderivat, som mindre potent och mindre toxiskt än atropin |
| [31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/) | 2020 | Preklinisk djurstudie | Neuropharmacology | Kolinerg aktivering via muskarinreceptorer hämmar kortikal spridande depression i musens hjärnbark (gäller migrän med hjärnstammsaura) |

Flera övriga träffar i sökningen var inte relevanta för atropin (till exempel topiramatbiverkningar på ögat, ergotaminfarmakologi och en fallrapport om botulinumtoxin) och redovisas inte.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 59083 | Atropine Accord | Injektionsvätska, lösning i förfylld spruta | Avregistrerad |
| 53365 | Atropin Aguettant | Injektionsvätska, lösning i förfylld spruta | Avregistrerad |
| 66778 | Atropine Noridem | Injektionsvätska, lösning | Avregistrerad |
| 9018 | Atropin Viatris | Injektionsvätska, lösning | Avregistrerad |
| 9654 | Atropin Bausch & Lomb | Ögondroppar, lösning i endosbehållare | Avregistrerad |

Visar 5 av 9 godkännanden. Indikationstext finns inte angiven i godkännandedata.

---

## Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Totalt 380 registrerade interaktioner. Exempel på måttliga interaktioner är andra antikolinerga läkemedel (hyoscyamin, aklidinium, amitriptylin, klorfeniramin), opioider (fentanyl, alfentanil, kodein, dihydrokodein, tramadol), botulinumtoxin typ A, galantamin, amantadin, loperamid, acebutolol och etanol. Mindre interaktioner finns med paracetamol och hydroklortiazid.
- **Förväntade antikolinerga biverkningar** (utifrån litteraturgenomgången): påverkan på kognition, hjärtklappning/takykardi, muntorrhet och dimsyn.

Varningar och kontraindikationer från produktresumén saknas i det data som sammanställts. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Trots mycket hög modellpoäng bygger förutsägelsen enbart på prekliniska och indirekta data. Inga kliniska prövningar finns, och ingen studie visar att atropin lindrar migrän hos människa. Dessutom pekar en studie på att muskarinblockad kan vara ogynnsam vid migränaura.
- Alla svenska godkännanden är avregistrerade, och den antikolinerga biverkningsprofilen samt den stora interaktionsbördan talar för försiktighet.

**För att gå vidare krävs:**
- Komplettera produktresumédata (varningar, kontraindikationer, ursprunglig indikation) och verkningsmekanism, vilket är blockerande för säkerhetsbedömningen.
- Fördjupad prekliniska studier som direkt testar atropin eller selektiva muskarinantagonister i migränmodeller, med särskild uppmärksamhet på riktningen i effekten.
- Kliniska pilotstudier (fas 2) endast om prekliniska data är stödjande, och med utvärdering av en lämplig beredningsform eftersom inga nu godkända produkter finns på marknaden.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

