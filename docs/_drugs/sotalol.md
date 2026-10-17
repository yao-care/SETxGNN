---
layout: default
title: Sotalol
parent: Endast modellprediktion (L5)
nav_order: 399
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Sotalol: predikterad ny indikation Sick sinus-syndrom 2, autosomalt dominant (evidensnivå L5). Ursprunglig indikation: Förmaksflimmer (enligt kunskapsgrafen"
monitor_inn: "sotalol"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation", "obsolete susceptibility to ischemic stroke"]
---

# Sotalol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

# Sotalol: Från förmaksflimmer till sick sinus-syndrom 2, autosomalt dominant

---

## Sammanfattning

Sotalol är ett antiarytmikum (klass III) med betablockerande effekt. Enligt kunskapsgrafen har det använts mot **förmaksflimmer**. TxGNN-modellen förutsäger att det kan vara effektivt mot **sick sinus-syndrom 2, autosomalt dominant**, men det finns **inga kliniska prövningar och ingen publicerad litteratur** som stöder detta. Förutsägelsen är rent beräkningsbaserad. Dessutom är sick sinus-syndrom en känd kontraindikation för sotalol, vilket gör kopplingen svår att motivera.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Förmaksflimmer (enligt kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Sick sinus-syndrom 2, autosomalt dominant |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 3 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för rapporten. Sotalol är dock allmänt känt som ett klass III-antiarytmikum och en betablockerare. Det förlänger repolarisationen, sänker sinusfrekvensen och bromsar överledningen i AV-noden. Effekten vid förmaksflimmer är väl etablerad.

Sick sinus-syndrom 2 (autosomalt dominant) är en störning i sinusknutans funktion, ofta kopplad till varianter i generna *HCN4* eller *SCN5A*. Modellen verkar ha kopplat ihop de två sjukdomarna eftersom båda är rytmstörningar med överlappande biologiska nätverk.

Mekanistiskt är kopplingen dock **svår att försvara som en nytta**. Sotalol bromsar sinusknutan och AV-ledningen, vilket i princip kan förvärra den bradykardi som kännetecknar sjukdomen. Det höga poängvärdet speglar sannolikt nätverksmönster i grafen och inte en verklig terapeutisk möjlighet. Förutsägelsen bör därför främst läsas som en säkerhetsvarning.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Alla tre godkännanden är indragna, och inget giltigt läkemedel med sotalol som enda substans finns på marknaden.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 11913 | Sotalol Viatris | Tablett | Ej angiven |
| 11152 | Sotacor | Tablett | Ej angiven |
| 12403 | Sotalol Viatris | Tablett | Ej angiven |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (hämtade från kopplingar i kunskapsgrafen, inte från produktresumétext): 
  - Sick sinus-syndrom och familjärt sick sinus-syndrom. Detta gäller direkt den förutsagda indikationen.
  - Långt QT-syndrom (även familjärt) och torsades de pointes
  - Atrioventrikulärt block
  - Astma (inklusive allergisk och intrinsic astma) och andra bronkiella sjukdomar
  - Kaliumbrist
  - Diabetes mellitus och diabetisk ketoacidos
  - Lågt blodtryck
  - Nedsatt njurfunktion
  - Anafylaxi
- **Läkemedelsinteraktioner:** Totalt 289 interaktioner har identifierats. Bland de allvarligaste (nivå "Major") finns:
  - Adrenalin
  - Klaritromycin
  - Pikosulfat
  - Polyetylenglykol (3350 med elektrolyter)

  Många interaktioner av måttlig grad finns också, bland annat med famotidin, atropin, morfin, bupropion, cimetidin, dapagliflozin och kanagliflozin.
- **Övrig säkerhetssignal:** Sotalol förlänger QT-tiden. Kombination med antipsykotika och andra QT-förlängande läkemedel ökar risken för arytmi.

Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar helt stöd från studier (evidensnivå L5). Sotalols effekter på sinusknutan och AV-ledningen talar dessutom emot nytta vid sick sinus-syndrom, som även är en listad kontraindikation. Alla svenska godkännanden är indragna.
- Bland de andra förutsägelserna har indikationen stroke visst indirekt stöd, genom en avslutad fas 3-prövning (NCT00007605, 706 deltagare) om rytmkontroll vid förmaksflimmer. Den undersöker dock inte stroke som utfall, och antikoagulation är fortfarande huvudstrategin för strokeprevention.

**För att gå vidare krävs:**
- Hämta och granska produktresumén för sotalol (varningar och kontraindikationer) från Läkemedelsverket.
- Hämta verkningsmekanismdata från DrugBank för en fullständig mekanistisk analys.
- Genomför en säkerhetsbedömning som tar hänsyn till kontraindikationen vid sick sinus-syndrom.
- Utvärdera om en mer relevant förutsagd indikation (till exempel med indirekt kliniskt stöd) ska prioriteras i stället.
- Eventuell vidare undersökning bör börja med prekliniska eller mekanistiska studier innan någon klinisk prövning övervägs.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

