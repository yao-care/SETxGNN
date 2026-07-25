---
layout: default
title: Datakällor
nav_order: 93
permalink: /sources/
description: "Datakällorna bakom SETxGNN: registreringsdata från MPA, TxGNN, ClinicalTrials.gov, PubMed och DrugBank."
---

# Datakällor

<div class="key-takeaway">
Varje slutsats går att spåra tillbaka till en offentlig datakälla — ingenting är en svart låda.
</div>

---

## Översikt över källor

<table class="comparison-table">
<thead>
<tr><th>Typ</th><th>Källa</th><th>Används till</th></tr>
</thead>
<tbody>
<tr><td>Registreringsdata</td><td><a href="https://www.lakemedelsverket.se/">MPA</a></td><td>Lista över godkända läkemedel och substanser för Sverige</td></tr>
<tr><td>Prediktionsmodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Prediktion av samband mellan läkemedel och sjukdom</td></tr>
<tr><td>Kliniska prövningar</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidensgradering (NCT)</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidensgradering (PMID)</td></tr>
<tr><td>Läkemedelsinformation</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Substansmappning och data om målmolekyler</td></tr>
<tr><td>Interaktioner</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Data om läkemedelsinteraktioner</td></tr>
</tbody>
</table>

---

## Licensiering

Varje källa har sin egen licens — kontrollera den innan du citerar:

- **TxGNN**: akademisk användning; citera Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: offentliga data från amerikanska NIH
- **DrugBank**: icke-kommersiell användning enligt licensvillkoren
- **MPA**: omfattas av villkoren för öppna data hos tillsynsmyndigheten i Sverige

---

## Uppdateringsfrekvens

| Data | Frekvens |
|------|-----------|
| Registreringsdata | Enligt tillsynsmyndighetens publicering |
| Evidens från prövningar / litteratur | Samlas in på nytt regelbundet |
| Interaktionsdata | Granskas kvartalsvis |

---

## Vetenskaplig citering

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Om utvecklaren

Denna plattform utvecklas och drivs av **藥提醒科技有限公司** (yao.care, organisationsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

SETxGNN är Sverige-webbplatsen i företagets produktlinje "TxGNN Drug Repurposing".
Samma system är driftsatt i 30 länder och regioner, vart och ett med namnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN och så vidare) på `{cc}txgnn.yao.care`.
Produktöversikt: <https://www.yao.care/medical/txgnn/>.

Själva TxGNN-modellen utvecklades av Zitnik Lab vid Harvard Medical School och publicerades
i *Nature Medicine*. Denna plattform är det produktionssystem som 藥提醒科技有限公司 har byggt ovanpå den
modellen, och omfattar integration av nationella läkemedelsregistreringsdata, dubbel prediktion med
kunskapsgraf och djupinlärning, evidensgradering från PubMed / ClinicalTrials samt integration med
elektroniska patientjournaler via SMART on FHIR.

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
