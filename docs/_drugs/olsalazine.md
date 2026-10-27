---
layout: default
title: Olsalazine
parent: Endast modellprediktion (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Olsalazine: predikterad ny indikation Myelodysplastiskt syndrom (evidensnivå L5). Ursprunglig indikation: Ej angiven (indikationstexten saknas i de svenska godkännandena)"
monitor_inn: "olsalazine"
predicted_indications: ["myelodysplastic syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "partial deletion of the long arm of chromosome 5", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
---

# Olsalazine
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

## Olsalazin: Från ej angiven ursprunglig indikation till myelodysplastiskt syndrom
{: .text-alpha }

---

### Sammanfattning

Olsalazin är en prodrug-dimer av 5-aminosalicylsyra (5-ASA, mesalazin) som verkar lokalt i tjocktarmen. Dess ursprungliga godkända indikation finns inte angiven i de data som sammanställts för rapporten. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **myelodysplastiskt syndrom** (poäng 99,9 %), men **inga kliniska prövningar och ingen litteratur** stöder för närvarande denna riktning. Förutsägelsen bygger enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven (indikationstexten saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Myelodysplastiskt syndrom |
| TxGNN-förutsägelsepoäng | 99,9 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 2 (båda avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är olsalazin en prodrug som delas av tarmbakterier i kolon till två molekyler 5-ASA, och systemisk exponering är minimal. Läkemedlet används vid inflammatorisk tarmsjukdom, men den ursprungliga indikationen är inte bekräftad i de data som sammanställts.

Kopplingen till myelodysplastiskt syndrom (MDS) vilar enbart på grafbaserad förutsägelse. Man kan spekulera i att 5-ASA har antiinflammatoriska eller antioxidativa effekter, till exempel via NF-kB-modulering, men det är inte prövat för olsalazin.

Det finns också skäl till försiktighet: aminosalicylater är i sällsynta fall förknippade med benmärgstoxicitet. Det talar emot förutsägelsen, särskilt eftersom MDS är en sjukdom med nedsatt benmärgsfunktion.

De övriga förutsägelserna ligger nära MDS i grafen: odifferentierat MDS, refraktär cytopeni hos barn, partiell deletion av långa armen på kromosom 5, aregenerativ anemi och ringsideroblastisk anemi. De utgör därför inte oberoende evidens. Förutsägelserna om håravfall (hypotrichosis simplex, kongenital hypotrichosis med milia, alopeci, diffus alopecia areata) saknar också en trolig mekanism och speglar sannolikt likheter i grafen.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation | Status |
|---------|------|------|-----------|------|
| 11586 | Dipentum | Kapsel, hård | Ej angiven | Avregistrerad |
| 12026 | Dipentum | Tablett | Ej angiven | Avregistrerad |

Innehavare för båda: Atnahs Pharma Netherlands B.V.

---

### Säkerhetsaspekter

**Läkemedelsinteraktioner:** Totalt 105 interaktioner identifierades. Nedan visas ett urval.

- **Allvarliga (Major):**
  - Humant immunglobulin G (intravenöst)
  - Humant botulinum-neurotoxin A/B-immunglobulin
  - Cidofovir
  - Jotalaminsyra
- **Måttliga (Moderate):** bland annat azatioprin, cisplatin, klofarabin, NSAID (ketorolak, ibuprofen, celecoxib, diklofenak), aminoglykosider (amikacin), amfotericin B, aciklovir, bacitracin, kapreomycin, kolistimetat, ibandronat och klorpropamid. Många av dessa är kopplade till risk för påverkan på njurarna.

**Viktigt för MDS-spåret:** Aminosalicylater har i sällsynta fall rapporterats ge benmärgstoxicitet och aplastisk anemi. Det är en avgörande säkerhetsfråga hos patienter med redan nedsatt blodbildning.

Se i övrigt produktresumén för varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modell (L5) utan stödjande prövningar eller litteratur, och läkemedlets systemiska exponering är låg. Risken för benmärgstoxicitet talar dessutom emot användning vid MDS.
- Båda svenska godkännandena är avregistrerade, och den ursprungliga indikationen samt varningar och kontraindikationer saknas i underlaget.

**För att gå vidare krävs:**
- Bekräfta ursprunglig indikation, verkningsmekanism, varningar och kontraindikationer från produktresumén och DrugBank.
- Genomför en systematisk litteratursökning och prekliniska studier (till exempel cellmodeller för benmärg eller MDS) för att pröva om det finns någon biologisk grund.
- Utvärdera om systemisk exponering är tillräcklig för att nå benmärgen, och väg mot risken för hematologisk toxicitet.
- Överväg att prioritera förutsägelser med bättre stöd, eftersom flera av de övriga är starkt korrelerade med MDS-förutsägelsen.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

