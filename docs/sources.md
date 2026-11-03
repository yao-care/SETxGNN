---
layout: default
title: Datakällor
nav_order: 93
permalink: /sources/
description: "Datakällorna bakom SETxGNN: Läkemedelsverkets läkemedelsregister, TxGNN, ClinicalTrials.gov, PubMed och DrugBank."
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
<tr><td>Registreringsdata</td><td><a href="https://www.lakemedelsverket.se/">Läkemedelsverket (MPA)</a></td><td>Läkemedelsregistret (CSV-export): läkemedel, substanser och registreringsstatus i Sverige</td></tr>
<tr><td>Prediktionsmodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Prediktion av samband mellan läkemedel och sjukdom</td></tr>
<tr><td>Kliniska prövningar</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidensgradering (NCT)</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidensgradering (PMID)</td></tr>
<tr><td>Läkemedelsinformation</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Substansmappning och data om målmolekyler</td></tr>
<tr><td>Interaktioner</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Data om läkemedelsinteraktioner</td></tr>
</tbody>
</table>

---

## Läkemedelsdata för Sverige

| Post | Uppgift |
|------|---------|
| Datamängd | Läkemedelsverkets läkemedelsregister, CSV-export per ATC-huvudgrupp (bland annat fälten MT-nummer och Registreringsstatus) |
| Utgivare | Läkemedelsverket (MPA) |
| Nedladdning | <https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv> (datamängden i Sveriges dataportal: <https://www.dataportal.se/en/datasets/140_5467>) |
| Uppdatering | Hämtas på nytt varje måndag av ett automatiskt arbetsflöde; registreringsstatus (till exempel Godkänd eller Avregistrerad) i läkemedelsrapporterna uppdateras från den nya filen |

---

## Licensiering

Varje källa har sin egen licens — kontrollera den innan du citerar:

- **TxGNN**: akademisk användning; citera Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: offentliga data från amerikanska NIH
- **DrugBank**: icke-kommersiell användning enligt licensvillkoren
- **MPA**: omfattas av villkoren för öppna data hos tillsynsmyndigheten i Sverige

---

## Uppdateringsfrekvens

| Data | Frekvens |
|------|-----------|
| Läkemedelsverkets register | Varje vecka (måndagar, automatiskt) |
| Evidens från prövningar / litteratur | Samlas in på nytt regelbundet |
| Interaktionsdata | Granskas kvartalsvis |

---

## Vetenskaplig citering

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

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
