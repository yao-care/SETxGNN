---
layout: default
title: Måttlig evidens (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Kandidater för läkemedelsrepositionering med L3-L4 i SETxGNN, som stöds av observationell eller preklinisk evidens."
---

# Måttlig evidens (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med preliminär evidens som kräver ytterligare validering
</p>

---

## Kriterier

| Nivå | Definition | Klinisk innebörd |
|-------|------------|------------------|
| **L3** | Observationsstudier / stora fallserier | Preliminärt stöd; kräver ytterligare validering |
| **L4** | Prekliniska / mekanistiska studier | Teoretiskt stöd; långt från klinisk användning |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} läkemedel)

| Läkemedel | Indikationer | Länk |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Visa rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} läkemedel)

| Läkemedel | Indikationer | Länk |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Visa rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
