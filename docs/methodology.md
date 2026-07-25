---
layout: default
title: Metodik
nav_order: 91
permalink: /methodology/
description: "Så tar SETxGNN fram och validerar prediktioner: prediktion med TxGNN-kunskapsgraf, evidensinsamling, gradering L1-L5 och beslutsrekommendationer."
---

# Metodik

<div class="key-takeaway">
Från AI-prediktion till evidensgradering — varje kandidat har en spårbar grund för sin bedömning.
</div>

---

## Övergripande arbetsflöde

<p class="key-answer" data-question="Hur tar SETxGNN fram sina prediktioner?">
Plattformen använder ett arbetsflöde i fyra steg: TxGNN-kunskapsgrafmodellen predikterar potentiella
samband mellan läkemedel och sjukdom, därefter samlas evidens automatiskt in för varje prediktion,
evidensen graderas från L1 till L5, och slutligen utfärdas en beslutsrekommendation.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-prediktion</strong>: samband mellan läkemedel och sjukdom predikteras med en kunskapsgraf i kombination med grafneurala nätverk.</li>
<li><strong>Evidensinsamling</strong>: för varje prediktion samlas evidens in från ClinicalTrials.gov, PubMed, DrugBank och MPA.</li>
<li><strong>Evidensgradering</strong>: graderas L1 till L5, där L1 är starkast (flera fas 3-RCT) och L5 endast är en modellprediktion.</li>
<li><strong>Beslutsrekommendation</strong>: Go, Proceed, Consider, Explore eller Hold, baserat på evidensnivån.</li>
</ol>

---

## Kriterier för evidensgradering

<table class="comparison-table">
<thead>
<tr><th>Nivå</th><th>Definition</th><th>Klinisk innebörd</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Flera fas 3-RCT / systematiska översikter</td><td>Starkt stöd; klinisk användning kan övervägas</td></tr>
<tr><td><strong>L2</strong></td><td>Enstaka RCT eller flera fas 2-prövningar</td><td>Måttligt stöd; valideringsstudier kan utformas</td></tr>
<tr><td><strong>L3</strong></td><td>Observationsstudier / stora fallserier</td><td>Preliminärt stöd; kräver ytterligare validering</td></tr>
<tr><td><strong>L4</strong></td><td>Prekliniska / mekanistiska studier</td><td>Teoretiskt stöd; långt från klinisk användning</td></tr>
<tr><td><strong>L5</strong></td><td>Endast modellprediktion</td><td>Hypotesstadiet; ännu ingen evidens från människa</td></tr>
</tbody>
</table>

---

## Prediktion med dubbla motorer

Två metoder körs parallellt, och en konfidensetikett anger om de överensstämmer:

| Metod | Hastighet | Precision | Beskrivning |
|--------|-------|-----------|-------------|
| Kunskapsgraf (KG) | Snabb | Lägre | Inferens över DrugBank-relationer och grafstruktur |
| Djupinlärning (DL) | Långsam | Högre | TxGNN grafneurala nätverksmodell |

| Konfidens | Källa | Innebörd |
|------------|--------|---------|
| very_high | KG + DL | Båda metoderna överensstämmer |
| high | Endast DL | Högt poängsatt stöd från djupinlärning |
| medium | Endast KG | Stöd från kunskapsgrafen |

---

## Integration av regulatoriska data

Läkemedelsgodkännandedata för Sverige kommer från MPA. Substansnamn mappas till
DrugBanks vokabulär; substanser som inte kan mappas — växtextrakt, vacciner, hjälpämnen
och annat som inte katalogiserats av DrugBank — utesluts från prediktionen.

---

## Begränsningar

<ol class="actionable-steps">
<li>Prediktionerna är statistiska samband och <strong>innebär inte orsakssamband eller klinisk effekt</strong>.</li>
<li>En L5-bedömning betyder endast modellprediktion, utan stödjande evidens från människa.</li>
<li>Evidensinsamlingen bygger på offentliga databaser; opublicerade eller oindexerade studier fångas inte upp.</li>
<li>Substansmappningen kan missa poster på grund av skillnader i namngivning.</li>
</ol>

---

## Om utvecklaren

Denna plattform utvecklas och drivs av **藥提醒科技有限公司** (yao.care, organisationsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

SETxGNN är Sverige-webbplatsen i företagets produktlinje "TxGNN Drug Repurposing".
Samma system är driftsatt i 30 länder och regioner, vart och ett med namnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN och så vidare) på `{cc}txgnn.yao.care`.
Produktöversikt: <https://www.yao.care/medical/txgnn/>.

Själva TxGNN-modellen utvecklades av Zitnik Lab vid Harvard Medical School och publicerades
i *Nature Medicine*. Denna plattform är det produktionssystem som 藥提醒科技有限公司 har byggt ovanpå den
modellen, och omfattar integration av nationella läkemedelsregistreringsdata, dubbel prediktion med
kunskapsgraf och djupinlärning, evidensgradering från PubMed / ClinicalTrials samt integration med
elektroniska patientjournaler via SMART on FHIR.

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
