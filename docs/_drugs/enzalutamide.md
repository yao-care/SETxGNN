---
layout: default
title: Enzalutamide
parent: Endast modellprediktion (L5)
nav_order: 165
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Enzalutamide: predikterad ny indikation Prostate cancer/brain cancer susceptibility (genetisk känslighet för… (evidensnivå L5). Ursprunglig indikation: Prostatacancer (godkännandetexterna i det samma…"
monitor_inn: "enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Enzalutamide
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

# Enzalutamid: Från prostatacancer till genetisk känslighet för prostata-/hjärncancer

---

### Sammanfattning

Enzalutamid är en androgenreceptorhämmare som ursprungligen används vid **prostatacancer**. TxGNN-modellen förutsäger att det kan vara effektivt mot **"prostate cancer/brain cancer susceptibility"** (genetisk känslighet för prostata- och hjärncancer), med en mycket hög modellpoäng på 99,7 %. För denna förutsägelse finns dock **inga kliniska prövningar och ingen publicerad litteratur**, så evidensen består enbart av modellens förutsägelse.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Prostatacancer (godkännandetexterna i det sammanställda underlaget saknar indikationstext, så uppgiften kommer från kunskapsgrafen) |
| Förutsagd ny indikation | Prostate cancer/brain cancer susceptibility (genetisk känslighet för prostata-/hjärncancer) |
| TxGNN-förutsägelsepoäng | 99,7 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 10 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i underlaget. Enzalutamid är dock allmänt känt som en androgenreceptorhämmare. Den blockerar att receptorn flyttas in i cellkärnan, att den binder till DNA och att den rekryterar samverkande proteiner. Effekten vid prostatacancer är väl belagd, och mekanistiskt skulle androgenberoende tumörer kunna vara tillgängliga för samma angreppssätt.

Den höga poängen beror troligen på att kunskapsgrafen kopplar enzalutamid starkt till prostatacancer. "Prostate cancer/brain cancer susceptibility" är ett **genetiskt känslighetsfenotyp** och inte en sjukdom som behandlas direkt. Det finns därför inget självständigt stöd för en behandlingseffekt, och särskilt inte för hjärncancer.

Förutsägelsen bör alltså tolkas som en artefakt av grafens närhet till prostatacancer och inte som en biologiskt underbyggd ny indikation.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

Samtliga 10 godkännanden är avregistrerade. Det finns inga giltiga godkännanden för enskilda preparat eller kombinationer. De fem första visas nedan. Alla är filmdragerade tabletter, och indikationstext saknas i underlaget.

| Godkännandenummer | Produktnamn | Beredningsform | Tillverkare | Status |
|---------|------|------|-----------|------|
| 66243 | Enzalutamide Teva | Filmdragerad tablett | TEVA GmbH | Avregistrerad |
| 64679 | Enzalutamide Sandoz | Filmdragerad tablett | Sandoz A/S | Avregistrerad |
| 68137 | Enzalutamide Zentiva | Filmdragerad tablett | Zentiva k.s. | Avregistrerad |
| 68138 | Enzalutamide Zentiva | Filmdragerad tablett | Zentiva k.s. | Avregistrerad |
| 64920 | Enzalutamide STADA | Filmdragerad tablett | STADA Arzneimittel AG | Avregistrerad |

---

### Cytotoxicitet

Enzalutamid används mot cancer, men är en hormonell, målriktad behandling och inte ett klassiskt cytostatikum.

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Målriktad (hormonell) terapi, androgenreceptorhämmare |
| Myelosuppressionsrisk | Se produktresumén för varningar och försiktighetsåtgärder |
| Emetogenicitetsklassificering | Se produktresumén för varningar och försiktighetsåtgärder |
| Övervakningspunkter | Se produktresumén för varningar och försiktighetsåtgärder |
| Hanteringsskydd | Se produktresumén för varningar och försiktighetsåtgärder |

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Totalt 571 interaktioner är registrerade. Exempel:
  - **Allvarliga (Major)**: bupropion, dolasetron, eliglustat.
  - **Måttliga (Moderate)**, ett urval: omeprazol, rabeprazol, famotidin, hydrokortison, dexametason, aprepitant, klaritromycin, loperamid, empagliflozin, linagliptin, saxagliptin.

Varningar och kontraindikationer enligt produktresumé ingår inte i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen har hög modellpoäng men ingen klinisk eller publicerad evidens (L5). Måldiagnosen är dessutom ett genetiskt känslighetsfenotyp och inte en behandlingsbar sjukdom.
- Alla svenska godkännanden är avregistrerade, vilket också behöver kontrolleras.

**För att gå vidare krävs:**
- En tydligare definition av vilken sjukdomsenhet som faktiskt avses och om den är behandlingsbar.
- Prekliniska eller kliniska data som visar en androgenreceptorberoende mekanism vid den aktuella diagnosen, särskilt för hjärncancer.
- Verkningsmekanismdata (t.ex. via DrugBank) och produktresumé med varningar och kontraindikationer.
- Verifiering av marknadsstatus, eftersom alla godkännanden är avregistrerade trots att läkemedlet är etablerat vid prostatacancer.
- Fokus på de bättre underbyggda kandidaterna. Kategorin "male reproductive organ cancer" överlappar med den ursprungliga indikationen och har fas 3-studier, men är ingen ny indikation. Möjligt värde ligger i nya kombinationer och patientgrupper, till exempel äldre patienter eller kombination med mevrometostat.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

