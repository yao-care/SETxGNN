---
layout: default
title: "Prediktioner f\u00f6r L\u00e4kemedelsrepositionering \u2014 Sverige"
nav_order: 1
description: "AI-baserade prediktioner för ny användning av läkemedel i Sverige. Evidensbaserad analys av godkända läkemedel för möjliga nya användningsområden."
permalink: /
---

# Prediktioner för ny användning av läkemedel — Sverige

Detta projekt använder TxGNN, ett grafneuralt nätverk, för att prediktera möjliga nya terapeutiska användningsområden för läkemedel som är godkända i Sverige.

**Ansvarsfriskrivning**: Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning. Alla prediktioner om läkemedelsrepositionering kräver klinisk validering före tillämpning.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Sverige: vad webbplatsen omfattar

Webbplatsen publicerar rapporter om **{{ site.data.drug_stats.total_drugs }}** läkemedel i registreringsdata från [MPA](https://www.lakemedelsverket.se/) (Sverige).

### Läkemedelsdata för Sverige

| Post | Uppgift |
|------|---------|
| Datamängd | Läkemedelsverkets läkemedelsregister, CSV-export per ATC-huvudgrupp (bland annat fälten MT-nummer och Registreringsstatus) |
| Utgivare | Läkemedelsverket (MPA) |
| Nedladdning | <https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv> (datamängden i Sveriges dataportal: <https://www.dataportal.se/en/datasets/140_5467>) |
| Uppdatering | Hämtas på nytt varje måndag av ett automatiskt arbetsflöde; registreringsstatus (till exempel Godkänd eller Avregistrerad) i läkemedelsrapporterna uppdateras från den nya filen |

Detaljer: [Datakällor]({{ '/sources/' | relative_url }}).

Rapporter per evidensnivå:

| Evidensnivå | Rapporter | Andel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

### Läkemedel med högst evidensnivå på webbplatsen

| Läkemedel | Evidensnivå |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Acetylcysteine](/drugs/acetylcysteine/) | L2 |
| [Bupropion](/drugs/bupropion/) | L2 |
| [Diazepam](/drugs/diazepam/) | L2 |
| [Fludarabine](/drugs/fludarabine/) | L2 |

<!-- local-home:end -->

## Om utvecklaren

Denna plattform utvecklas och drivs av **藥提醒科技有限公司** (yao.care). Se sidan
<a href="{{ '/about/' | relative_url }}">Om</a> för fullständig bakgrund om företaget och metoden.
