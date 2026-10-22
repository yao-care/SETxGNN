---
layout: default
title: Metodik
nav_order: 91
permalink: /methodology/
description: "Så tar SETxGNN fram och validerar prediktioner: prediktion med TxGNN-modellen (djupinlärning), evidensinsamling, gradering L1-L5 och beslutsrekommendationer."
---

# Metodik

<div class="key-takeaway">
Från AI-prediktion till evidensgradering — varje kandidat har en spårbar grund för sin bedömning.
</div>

---

## Övergripande arbetsflöde

<p class="key-answer" data-question="Hur tar SETxGNN fram sina prediktioner?">
Plattformen använder ett arbetsflöde i fyra steg: TxGNN-modellen (djupinlärning) predikterar potentiella
samband mellan läkemedel och sjukdom, därefter samlas evidens automatiskt in för varje prediktion,
evidensen graderas från L1 till L5, och slutligen utfärdas en beslutsrekommendation.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-prediktion</strong>: samband mellan läkemedel och sjukdom predikteras av TxGNN-modellen (djupinlärning: ett grafneuralt nätverk tränat på en biomedicinsk kunskapsgraf).</li>
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

## Så tas prediktionerna fram

TxGNN:s djupinlärningsmodell (DL) poängsätter varje läkemedel–sjukdom-par. Därefter tas indikationer och kontraindikationer bort som redan finns registrerade för läkemedlet i TxGNN:s kunskapsgraf (KG), så läkemedelssidorna visar bara nya predikterade indikationer med en poäng på minst 0,99 (högst 10 per läkemedel).

| Steg | Roll |
|------|------|
| Djupinlärning (DL) | TxGNN:s grafbaserade neurala nätverk poängsätter varje läkemedel–sjukdom-par |
| Kontroll av känd användning (KG) | Tar bort indikationer och kontraindikationer som redan finns i kunskapsgrafen; de räknas inte som nya prediktioner |
| Insamling av evidens | Söker i ClinicalTrials.gov och PubMed för varje återstående prediktion och tilldelar en evidensnivå (L1–L5) |

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
modellen, och omfattar integration av nationella läkemedelsregistreringsdata, prediktion med djupinlärning där användning som redan finns i kunskapsgrafen är utesluten, evidensgradering från PubMed / ClinicalTrials samt integration med
elektroniska patientjournaler via SMART on FHIR.

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
