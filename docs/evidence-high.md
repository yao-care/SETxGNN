---
layout: default
title: Hög evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Kandidater för läkemedelsrepositionering med L1-L2 i SETxGNN, som stöds av kliniska prövningar eller systematiska översikter."
---

# Hög evidens (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater som kan prioriteras för klinisk utvärdering
</p>

---

## Kriterier

| Nivå | Definition | Klinisk innebörd |
|-------|------------|------------------|
| **L1** | Flera fas 3-RCT / systematiska översikter | Starkt stöd; klinisk användning kan övervägas |
| **L2** | Enstaka RCT eller flera fas 2-prövningar | Måttligt stöd; valideringsstudier kan utformas |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} läkemedel)

| Läkemedel | Indikationer | Länk |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Visa rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} läkemedel)

| Läkemedel | Indikationer | Länk |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Visa rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
