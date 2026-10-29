---
layout: default
title: "Prediktioner f\u00f6r L\u00e4kemedelsrepositionering \u2014 Sverige"
nav_order: 1
description: "AI-baserade prediktioner för ny användning av läkemedel i Sverige. Evidensbaserad analys av godkända läkemedel för möjliga nya användningsområden."
permalink: /
---

# Prediktioner för ny användning av läkemedel — Sverige

This project uses the TxGNN graph neural network to predict potential new therapeutic uses for medicines approved in Sweden.

**Disclaimer**: This content is for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before application.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Sverige: vad webbplatsen omfattar

Webbplatsen publicerar rapporter om **{{ site.data.drug_stats.total_drugs }}** läkemedel i registreringsdata från [MPA](https://www.lakemedelsverket.se/) (Sverige).

Rapporter per evidensnivå: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Läkemedel med högst evidensnivå på webbplatsen

| Läkemedel | Evidensnivå |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Docetaxel](/drugs/docetaxel/) | L1 |
| [Progesterone](/drugs/progesterone/) | L1 |
| [Tiotropium](/drugs/tiotropium/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Terbutaline](/drugs/terbutaline/) | L1 |

<!-- local-home:end -->

## Om utvecklaren

Denna plattform utvecklas och drivs av **藥提醒科技有限公司** (yao.care, organisationsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

SETxGNN är Sverige-webbplatsen i företagets produktlinje "TxGNN Drug Repurposing".
Samma system är driftsatt i 30 länder och regioner, vart och ett med namnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN och så vidare) på `{cc}txgnn.yao.care`.
Produktöversikt: <https://www.yao.care/medical/txgnn/>.

Själva TxGNN-modellen utvecklades av Zitnik Lab vid Harvard Medical School och publicerades
i *Nature Medicine*. Denna plattform är det produktionssystem som 藥提醒科技有限公司 har byggt ovanpå den
modellen, och omfattar integration av nationella läkemedelsregistreringsdata, prediktion med djupinlärning där användning som redan finns i kunskapsgrafen är utesluten, evidensgradering från PubMed / ClinicalTrials samt integration med
elektroniska patientjournaler via SMART on FHIR.
