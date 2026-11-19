---
layout: default
title: Måttlig evidens (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "54 läkemedel på evidensnivå L3–L4 på webbplatsen (Sverige), t.ex. Acitretin, Alprazolam, Calcipotriol, med viktigaste predikterade indikation, godkännanden från Läkemedelsverket och granskningslogg för vart och ett."
---

# Måttlig evidens (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Sidan visar **{{ site.data.evidence_tier_facts.medium.count }}** av de **{{ site.data.drug_stats.total_drugs }}** läkemedel som har en publicerad rapport på webbplatsen ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Medianandel på L3–L4 över de 30 TxGNN-webbplatserna: {{ site.data.evidence_tier_facts.medium.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Den här webbplatsen ligger över medianen.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Den här webbplatsen ligger under medianen.{% else %}Den här webbplatsen ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
I de lokala uppgifterna (godkännanden från Läkemedelsverket) har **{{ site.data.evidence_tier_facts.medium.with_current }}** av dessa läkemedel minst ett godkända godkännande, **{{ site.data.evidence_tier_facts.medium.none_current }}** har godkännanden men inget godkända, och **{{ site.data.evidence_tier_facts.medium.without_data }}** finns inte i de lokala uppgifterna. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** har poster i granskningsloggen (rättelser av godkännandeuppgifter på läkemedelssidan). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** har en predikterad indikation som ingen annan TxGNN-webbplats anger för samma läkemedel.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Med godkännanden men inget godkända: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definition av alla nivåer: [Metodik]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} läkemedel)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Läkemedel | Nivå | Viktigaste predikterade nya indikation | godkännanden från Läkemedelsverket: godkända / totalt | Granskningslogg | Bara på den här webbplatsen |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} läkemedel)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Läkemedel | Nivå | Viktigaste predikterade nya indikation | godkännanden från Läkemedelsverket: godkända / totalt | Granskningslogg | Bara på den här webbplatsen |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
