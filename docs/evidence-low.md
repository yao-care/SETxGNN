---
layout: default
title: Endast modellprediktion (L5)
nav_order: 23
permalink: /evidence-low/
description: "L5-kandidater i SETxGNN: endast modellprediktion, ännu utan klinisk evidens eller litteraturstöd."
---

# Endast modellprediktion (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Sidan visar **{{ pd_m }}** av de **{{ site.data.drug_stats.total_drugs }}** läkemedel som har en publicerad rapport på webbplatsen ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definition av nivåerna: [Metodik]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med endast modellprediktion och ännu ingen evidens från människa
</p>

---

## Kriterier

| Nivå | Definition | Klinisk innebörd |
|-------|------------|------------------|
| **L5** | Endast modellprediktion | Hypotesstadiet; ännu ingen evidens från människa |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ l5_drugs.size }} läkemedel)

| Läkemedel | Indikationer | Länk |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Visa rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
