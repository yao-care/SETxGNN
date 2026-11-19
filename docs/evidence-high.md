---
layout: default
title: Hög evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "27 läkemedel på evidensnivå L1–L2 på webbplatsen (Sverige), t.ex. Bendamustine, Busulfan, Clomipramine, med viktigaste predikterade indikation, godkännanden från Läkemedelsverket och granskningslogg för vart och ett."
---

# Hög evidens (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Sidan visar **{{ site.data.evidence_tier_facts.high.count }}** av de **{{ site.data.drug_stats.total_drugs }}** läkemedel som har en publicerad rapport på webbplatsen ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Medianandel på L1–L2 över de 30 TxGNN-webbplatserna: {{ site.data.evidence_tier_facts.high.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Den här webbplatsen ligger över medianen.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Den här webbplatsen ligger under medianen.{% else %}Den här webbplatsen ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
I de lokala uppgifterna (godkännanden från Läkemedelsverket) har **{{ site.data.evidence_tier_facts.high.with_current }}** av dessa läkemedel minst ett godkända godkännande, **{{ site.data.evidence_tier_facts.high.none_current }}** har godkännanden men inget godkända, och **{{ site.data.evidence_tier_facts.high.without_data }}** finns inte i de lokala uppgifterna. **{{ site.data.evidence_tier_facts.high.with_reviews }}** har poster i granskningsloggen (rättelser av godkännandeuppgifter på läkemedelssidan). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** har en predikterad indikation som ingen annan TxGNN-webbplats anger för samma läkemedel.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Med godkännanden men inget godkända: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definition av alla nivåer: [Metodik]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater som kan prioriteras för klinisk utvärdering
</p>

Vilka av dessa läkemedel har evidens från prövningar för sin förutsagda nya indikation, och hur många registrerade prövningar citeras? Se [Läkemedel i Sverige med evidens från kliniska prövningar för en ny indikation]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Kriterier

| Nivå | Definition | Klinisk innebörd |
|-------|------------|------------------|
| **L1** | Flera fas 3-RCT / systematiska översikter | Starkt stöd; klinisk användning kan övervägas |
| **L2** | Enstaka RCT eller flera fas 2-prövningar | Måttligt stöd; valideringsstudier kan utformas |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} läkemedel)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Läkemedel | Nivå | Viktigaste predikterade nya indikation | godkännanden från Läkemedelsverket: godkända / totalt | Granskningslogg | Bara på den här webbplatsen |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} läkemedel)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Läkemedel | Nivå | Viktigaste predikterade nya indikation | godkännanden från Läkemedelsverket: godkända / totalt | Granskningslogg | Bara på den här webbplatsen |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
