---
layout: default
title: Nedladdningar
nav_order: 94
permalink: /downloads/
description: "Öppna data att ladda ned från SETxGNN: FHIR-resurser, prediktionsresultat och sökindex."
---

# Nedladdningar

<div class="key-takeaway">
Prediktionerna publiceras i FHIR R4-format, redo att integreras med journalsystem.
</div>

---

## FHIR-resurser

Denna webbplats publicerar prediktioner som FHIR R4-resurser, som kan användas direkt av SMART on FHIR-appar:

| Resurs | Sökväg | Beskrivning |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Kapacitetsdeklaration för FHIR-servern |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Läkemedelsresurser |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Predikterade indikationer |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alla prediktioner samlade |

---

## Sökindex

`/data/search-index.json` tillhandahåller ett sökindex över läkemedel och indikationer för att bygga ditt eget
sökgränssnitt.

---

## Användarvillkor

<ol class="actionable-steps">
<li>Data på denna webbplats är <strong>endast avsedda som forskningsreferens</strong> och får inte användas som underlag för medicinska beslut.</li>
<li>Vid citering, ange SETxGNN (藥提醒科技有限公司) som källa och citera den ursprungliga TxGNN-artikeln.</li>
<li>Vidareanvända data omfattas fortfarande av licensvillkoren för varje ursprunglig källa (se <a href="{{ '/sources/' | relative_url }}">Datakällor</a>).</li>
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
