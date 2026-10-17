---
layout: default
title: Acetazolamide
parent: Endast modellprediktion (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetazolamide: predikterad ny indikation Exercise-inducerad malign hypertermi (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext finns i de svenska godkännandena. Enligt kunska…"
monitor_inn: "acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
---

# Acetazolamide
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

# Acetazolamid: Från absensepilepsi till exercise-inducerad malign hypertermi

---

### Sammanfattning

Acetazolamid är en karbanhydrashämmare som ursprungligen användes vid bland annat absensepilepsi, hjärtsvikt, glaukom och höjdsjuka. TxGNN-modellen förutsäger att det kan vara effektivt mot **exercise-inducerad malign hypertermi**, men förutsägelsen bygger enbart på en grafmodell: **0 kliniska prövningar** och **0 publikationer** stöder den för närvarande. Evidensen är därför mycket svag.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext finns i de svenska godkännandena. Enligt kunskapsgrafen: absensepilepsi, hjärtsvikt, öppenvinkelglaukom, trångvinkelglaukom och höjdsjuka |
| Förutsagd ny indikation | Exercise-inducerad malign hypertermi |
| TxGNN-förutsägelsepoäng | 99,95 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 7 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Det är allmänt känt att acetazolamid hämmar enzymet karbanhydras, vilket påverkar syra-bas-balansen och jonhanteringen i bland annat njurar, ögon och muskler.

En tänkbar men obekräftad koppling är att karbanhydrashämning kan påverka syra-bas-balans och jontransport i muskler. Acetazolamid används vid vissa periodiska förlamningar, vilket ger ett visst biologiskt resonemang. Det finns dock inga belägg för effekt vid malign hypertermi.

Det finns också en betydande oro: acetazolamid kan förvärra metabol acidos, vilket är ett problem under en hypermetabol kris. Den höga poängen speglar sannolikt närhet i kunskapsgrafen snarare än en verklig behandlingseffekt.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Marknadsinformation Sverige

Samtliga sju godkännanden är indragna och inget har en registrerad indikationstext.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 58997 | Diamox (Abboxia AB) | Pulver till injektionsvätska, lösning | Ingen indikationstext registrerad |
| 64710 | Diamox (Orifarm AB) | Pulver till injektionsvätska, lösning | Ingen indikationstext registrerad |
| 4972 | Diamox (Amdipharm Limited) | Pulver till injektionsvätska, lösning | Ingen indikationstext registrerad |
| 52966 | Diamox (Orifarm AB) | Pulver till injektionsvätska, lösning | Ingen indikationstext registrerad |
| 64540 | Diamox (Orifarm AB) | Pulver till injektionsvätska, lösning | Ingen indikationstext registrerad |

Utöver dessa finns ytterligare två indragna godkännanden: tablett (4971, Amdipharm Limited) och pulver till injektionsvätska (60531, Ebb Medical AB).

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumén): leversvikt och leversjukdom, njursjukdom, hematologisk sjukdom, gallblåsesjukdom, gikt, typ 1- och typ 2-diabetes, diabetisk ketoacidos, andningssvikt, binjurebarksinsufficiens (inklusive Addisons sjukdom och kongenital binjurehyperplasi) samt renal tubulär acidos.
- **Läkemedelsinteraktioner**: 165 interaktioner är registrerade. Bland de viktigaste:
  - **Allvarliga**: acetylsalicylsyra och cisaprid.
  - **Måttliga**: diabetesläkemedel (t.ex. akarbos, acetohexamid, alogliptin, kanagliflozin, dapagliflozin, klorpropamid, albiglutid, dulaglutid), kortikosteroider (betametason, dexametason, beklometason), amfotericin B-preparat samt laxermedel (bisakodyl, ricinolja).
  - **Lindrig**: doxycyklin.
- **Signaler från litteraturen för relaterade tillstånd**: acetazolamid har rapporterats orsaka adynamisk ileus och i ett fall icke-kardiogent lungödem efter intravenös tillförsel. Vid cirros finns risk för hyperammonemi och leverencefalopati.

Produktresumén med varningar och kontraindikationer har inte kunnat hämtas, så se den för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar helt stöd från kliniska prövningar och litteratur (L5), och det finns en tänkbar säkerhetsrisk, bland annat förvärrad metabol acidos under en hypermetabol kris. Dessutom är samtliga svenska godkännanden indragna.

**För att gå vidare krävs:**
- Hämta och granska produktresumén för varningar och kontraindikationer (blockerande dataluckan).
- Komplettera data om verkningsmekanismen, till exempel från DrugBank.
- Genomföra prekliniska studier eller en systematisk litteratursökning om karbanhydrashämning vid malign hypertermi.
- Bedöma kliniskt behov och tillgänglig beredningsform, eftersom inga godkännanden är aktiva i Sverige.
- Notera att förutsägelser på rang 2–10 (bland annat hypertrofisk kardiomyopati och kardiomyopati) inte heller har tillräcklig evidens. Tarmobstruktion har dessutom ett säkerhetssignal mot användning.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

