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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Sverige: vad filerna innehåller nu

| Fil | Innehåll nu |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} läkemedel med predikterade indikationer |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} läkemedel med evidensnivå och ursprunglig indikation |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} MedicationKnowledge-resurser (en per läkemedel) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ClinicalUseDefinition-resurser (en per predikterad indikation) |

Återanvändning av den lokala datamängden: [Läkemedelsverket: läkemedelsregistret (CSV-export)](https://www.dataportal.se/en/datasets/140_5467), publicerad av Läkemedelsverket; återanvändning styrs av utgivarens villkor, och webbplatsen ger inga ytterligare rättigheter.

{% if site.data.local_facts.top_licensed.size > 0 %}Läkemedel med flest godkända godkännanden från Läkemedelsverket: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Senaste rättelserna i granskningsloggen: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

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
