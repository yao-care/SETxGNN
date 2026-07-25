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
