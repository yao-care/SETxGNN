---
layout: default
title: "Läkemedel med prövningsevidens för en ny indikation"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Läkemedel i Läkemedelsverkets register vars av TxGNN förutsagda nya indikation har evidens från kliniska prövningar (L1-L2): indikation, nivå, prövningar."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「se rapporten」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Förutsagd ny indikation" | split: "|" -%}
{%- assign lev_labels = "Evidensnivå" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Läkemedel i Sverige med evidens från kliniska prövningar för en ny indikation

<p class="key-answer" data-question="Vilka läkemedel i Sverige har evidens från kliniska prövningar för en ny indikation?">
<strong>{{ trial_drugs.size }}</strong> av de {{ listed.size }} läkemedlen med en SETxGNN-rapport har en ny indikation som TxGNN förutsagt med evidensnivå <strong>L1 eller L2</strong> ({{ l1.size }} på L1, {{ l2.size }} på L2), det vill säga att evidens från kliniska prövningar har hittats (randomiserade prövningar, fas 2–3-prövningar eller systematiska översikter).
</p>

Läkemedlen kommer från [Läkemedelsverkets](https://www.lakemedelsverket.se/) läkemedelsregister (registreringsstatus, till exempel Godkänd eller Avregistrerad, visas i varje rapport); listan återspeglar läkemedelsrapporterna, senast uppdaterade {{ latest_date }}.

<div class="key-takeaway">
Evidens från prövningar för en förutsagd indikation bevisar inte effekt. Varje kandidat nedan <strong>kräver fortfarande klinisk validering</strong> och myndighetsprövning före all klinisk användning.
</div>

---

## Läkemedel med evidens från prövningar (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Läkemedel</th><th>Förutsagd ny indikation</th><th>Evidensnivå</th><th>Citerade registrerade prövningar (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}se rapporten{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(med förbehåll)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Så läser du listan

- **Evidensnivå** följer webbplatsens [kriterier]({{ '/evidence-high/' | relative_url }}): L1 = Flera fas 3-RCT / systematiska översikter; L2 = Enstaka RCT eller flera fas 2-prövningar. ”(med förbehåll)” betyder att rapporten reserverar sig kring nivån; läs anmärkningen i rapporten innan du förlitar dig på den.
- **Förutsagd ny indikation** är huvudförutsägelsen i varje rapport. Indikationer och kontraindikationer som redan finns i TxGNN:s kunskapsgraf är uteslutna, men vissa förutsägelser kan ändå överlappa en etablerad användning; rapporten förklarar det när det gäller.
- **Citerade registrerade prövningar** räknar de ClinicalTrials.gov-nummer (NCT) som citeras i rapporten. Rapporterna citerar ett urval av de prövningar som hittats; 0 betyder att rapporten inte citerar någon registrerad prövning, och avsnittet om litteraturevidens visar grunden för nivån.
- Alla nivåer och hela metoden finns under [Hög evidens (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Alla läkemedel]({{ '/drugs/' | relative_url }}) och [metod]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
