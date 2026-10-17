---
layout: default
title: Alla läkemedel
nav_order: 20
permalink: /drugs/
description: "Alla valideringsrapporter för läkemedel och statistik över evidensnivåer i SETxGNN."
---
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}

# Alla läkemedel

{{ listed_drugs.size }} valideringsrapporter för läkemedel

---

## Fördelning av evidensnivåer

| Evidensnivå | Läkemedel | Beskrivning |
|---------|--------|------|
| **L1** | {{ l1_count }} | Flera RCT / systematiska översikter |
| **L2** | {{ l2_count }} | Enstaka RCT / fas 2-prövningar |
| **L3** | {{ l3_count }} | Observationsstudier / stora fallserier |
| **L4** | {{ l4_count }} | Prekliniska / mekanistiska studier |
| **L5** | {{ l5_count }} | Endast modellprediktion |

---

## Fullständig läkemedelslista

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Läkemedel | Evidensnivå | Indikationer |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
