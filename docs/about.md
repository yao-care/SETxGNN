---
layout: default
title: Om
nav_order: 90
permalink: /about/
description: "SETxGNN är en plattform för prediktion av läkemedelsrepositionering, utvecklad av 藥提醒科技有限公司 (yao.care), byggd på Harvards TxGNN-modell och omfattar läkemedel godkända av MPA i Sverige."
---

# Om

<div class="key-takeaway">
Snabbare evidensvalidering för läkemedelsrepositionering med AI — från prediktion till evidens med en blick.
</div>

---

## Bakgrund

<p class="key-answer" data-question="Vad är SETxGNN?">
<strong>SETxGNN</strong> är en forskningsstödjande plattform för läkemedelsrepositionering, byggd på TxGNN-modellen
som publicerats i <em>Nature Medicine</em> av Zitnik Lab vid Harvard University. Den predikterar
indikationsutvidgning för läkemedel som godkänts av MPA i Sverige. Utöver AI-baserade prediktionspoäng
integrerar plattformen klinisk evidens från ClinicalTrials.gov och PubMed, så att forskare
snabbt kan bedöma hur trovärdig varje prediktion är.
</p>

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

## Vad är läkemedelsrepositionering?

<p class="key-answer" data-question="Vad är läkemedelsrepositionering?">
<strong>Läkemedelsrepositionering</strong> innebär att hitta nya terapeutiska användningsområden för befintliga läkemedel.
Jämfört med att utveckla ett helt nytt läkemedel från grunden — 10 till 15 år och 1&ndash;2 miljarder USD —
tar repositionering 3 till 5 år och 100&ndash;300 miljoner USD, och säkerhetsdata från människa finns redan,
vilket gör risken för misslyckande lägre.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspekt</th><th>Utveckling av nytt läkemedel</th><th>Läkemedelsrepositionering</th></tr>
</thead>
<tbody>
<tr><td>Tid</td><td>10&ndash;15 år</td><td>3&ndash;5 år</td></tr>
<tr><td>Kostnad</td><td>1&ndash;2 miljarder USD</td><td>100&ndash;300 miljoner USD</td></tr>
<tr><td>Säkerhetsdata</td><td>Måste tas fram</td><td>Data från människa finns redan</td></tr>
<tr><td>Risk för misslyckande</td><td>Mycket hög (&gt;90 %)</td><td>Lägre</td></tr>
</tbody>
</table>

---

## Vad är TxGNN?

<p class="key-answer" data-question="Vad är TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> är en djupinlärningsmodell
utvecklad av Zitnik Lab vid Harvard Medical School och publicerad i <em>Nature Medicine</em>.
Den predikterar nya samband mellan läkemedel och sjukdom och är den första grundmodellen för
läkemedelsrepositionering som utformats särskilt för kliniker.
</p>

<blockquote class="expert-quote">
"TxGNN integrerar en kunskapsgraf med 17 080 biomedicinska entiteter och använder grafneurala nätverk
för att lära sig komplexa samband mellan noder och prediktera läkemedels potentiella effekt mot
sällsynta sjukdomar."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Datakällor

<table class="comparison-table">
<thead>
<tr><th>Typ</th><th>Källa</th><th>Beskrivning</th></tr>
</thead>
<tbody>
<tr><td>AI-prediktion</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Harvards prediktionsmodell baserad på kunskapsgraf</td></tr>
<tr><td>Kliniska prövningar</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Globalt register över kliniska prövningar</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Databas över biomedicinsk litteratur</td></tr>
<tr><td>Läkemedelsinformation</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Databas över läkemedel och målmolekyler</td></tr>
<tr><td>Registreringsdata</td><td><a href="https://www.lakemedelsverket.se/">MPA</a></td><td>Läkemedelsgodkännandedata för Sverige</td></tr>
</tbody>
</table>

---

## Vetenskaplig grund

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Omfattning

| Post | Värde |
|------|-------|
| Läkemedelsrapporter | {{ site.drugs.size }} |
| Tillsynsmyndighet | MPA |
| Driftsatta webbplatser | 30 länder / regioner |

---

## Kontakt

- **GitHub Issues**: <https://github.com/yao-care/SETxGNN/issues>
- **Utvecklare**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Produktöversikt**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
