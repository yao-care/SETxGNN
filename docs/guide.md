---
layout: default
title: Användarguide
nav_order: 92
permalink: /guide/
description: "Användarguide för SETxGNN: hur du slår upp läkemedel, läser evidensnivåer och tolkar rekommendationer."
---

# Användarguide

<div class="key-takeaway">
Kontrollera evidensnivån först, sedan rekommendationen, och läs därefter källitteraturen.
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

## Slå upp ett läkemedel

<ol class="actionable-steps">
<li>Använd sökrutan högst upp på sidan (generiska substansnamn ger bättre träffar än varumärkesnamn).</li>
<li>Eller bläddra i den fullständiga listan på <a href="{{ '/drugs/' | relative_url }}">Alla läkemedel</a>.</li>
<li>Du kan också bläddra efter evidensnivå: <a href="{{ '/evidence-high/' | relative_url }}">hög</a>, <a href="{{ '/evidence-medium/' | relative_url }}">måttlig</a>, <a href="{{ '/evidence-low/' | relative_url }}">endast modellprediktion</a>.</li>
</ol>

---

## Läsa en rapport

<p class="key-answer" data-question="Vad betyder evidensnivåerna L1 till L5?">
Varje läkemedelsrapport listar predikterade nya indikationer, och varje indikation har en evidensnivå
från L1 till L5. <strong>L1 betyder att flera randomiserade kontrollerade fas 3-prövningar redan stöder den; L5 betyder
endast modellprediktion, utan evidens från människa.</strong> Fullständiga kriterier finns på sidan
<a href="{{ '/methodology/' | relative_url }}">Metodik</a>.
</p>

| Om du ser | Det betyder | Föreslagen åtgärd |
|-----------|----------|------------------|
| L1 / L2 | Det finns evidens från kliniska prövningar | Granska käll-NCT och PMID-posterna |
| L3 / L4 | Observationell eller preklinisk evidens | Betrakta som ett forskningsuppslag |
| L5 | Endast modellprediktion | Endast hypotesgenerering; inte för kliniskt bruk |

---

## Citering och spårbarhet

Varje evidensuppgift i en rapport har en spårbar identifierare:

- **NCT-nummer**: länkar till registreringen på ClinicalTrials.gov
- **PMID**: länkar till posten i PubMed
- **DrugBank-ID**: länkar till läkemedels- och målmolekyldata

Läs källitteraturen för att bekräfta sammanhanget innan du citerar någon slutsats från denna plattform.

---

## Vanliga frågor

<p class="key-answer" data-question="Kan prediktionerna användas kliniskt?">
<strong>Nej.</strong> Prediktionerna på denna plattform är forskningsuppslag, inte kliniska råd. All
klinisk tillämpning av läkemedelsrepositionering måste genomgå fullständig validering i kliniska prövningar och
regulatorisk granskning.
</p>

<p class="key-answer" data-question="Varför hittar jag inte ett visst läkemedel?">
En substans måste kunna mappas till DrugBanks vokabulär för att ingå i prediktionen. Växtextrakt,
vacciner, hjälpämnen och andra poster som inte katalogiserats av DrugBank visas inte på denna plattform.
</p>

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
