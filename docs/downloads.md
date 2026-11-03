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

Denna plattform utvecklas och drivs av **藥提醒科技有限公司** (yao.care). Se sidan
<a href="{{ '/about/' | relative_url }}">Om</a> för fullständig bakgrund om företaget och metoden.

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
