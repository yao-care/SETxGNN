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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Sverige: data bakom webbplatsen

Webbplatsen publicerar rapporter om **{{ site.data.drug_stats.total_drugs }}** läkemedel i registreringsdata från [MPA](https://www.lakemedelsverket.se/) (Sverige).

Datamängd: [Läkemedelsverket: läkemedelsregistret (CSV-export)](https://www.dataportal.se/en/datasets/140_5467); laddas ned och jämförs automatiskt varje vecka (måndagar). Detaljer: [Datakällor]({{ '/sources/' | relative_url }}).

Rapporter per evidensnivå:

| Evidensnivå | Rapporter | Andel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

<!-- site-data:end -->

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
