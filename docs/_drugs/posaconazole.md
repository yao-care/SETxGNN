---
layout: default
title: Posaconazole
parent: Endast modellprediktion (L5)
nav_order: 357
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: predikterad ny indikation Pneumocystosis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Posaconazole
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

## Posaconazole: Pneumocystosis
{: .text-alpha }

---

### Sammanfattning

Posakonazol är ett azolbaserat svampmedel som ursprungligen användes mot flera svampinfektioner, bland annat aspergillos, candidiasis, kokcidioidomykos och histoplasmos. TxGNN-modellen förutsäger att det kan vara effektivt mot **pneumocystos** med mycket hög modellpoäng, men i de data som sammanställts för rapporten finns **ingen studie som direkt stöder detta**: en enda klinisk prövning (som gäller ett annat läkemedel) och fem publikationer, varav ingen är en kontrollerad studie av posakonazol mot pneumocystos.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Pneumocystosis |
| TxGNN-förutsägelsepoäng | 0.9977 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 8 av 8) |
| Antal godkännanden | 8 (giltiga: 8) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Baserat på allmän kunskap är posakonazol ett triazolbaserat svampmedel som hämmar svampens enzym lanosterol 14-alfa-demetylas (CYP51). Därmed blockeras bildningen av ergosterol, en viktig byggsten i svampens cellmembran.

Den ursprungliga indikationsgruppen består av svamp­infektioner där denna mekanism är väl belagd. Pneumocystos är också en svampinfektion i lungorna, vilket förklarar att modellen placerar den nära de övriga indikationerna.

Mekanismen är dock **svagt tillämpbar** här. *Pneumocystis jirovecii* saknar i stort sett ergosterol i sina membran och använder främst kolesterol och andra steroler, så azolernas primära målstruktur saknas i stort sett. Den höga modellpoängen speglar sannolikt närhet till andra svampindikationer i nätverket snarare än en verklig farmakologisk grund.

---

### Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fas 3 | Avslutad | 602 | Studerar rezafungin (ett echinokandin, inte posakonazol) som förebyggande behandling mot invasiva svampinfektioner efter allogen blod- och benmärgstransplantation, jämfört med standardregim. Ger ingen direkt evidens för posakonazol. |

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Riktlinje | The Lancet. Infectious diseases | Uppdaterade brittiska rekommendationer för diagnostik av allvarliga svampinfektioner, där icke-odlingsbaserade metoder dominerar. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Riktlinje | Zhonghua jie he he hu xi za zhi | Kinesiska riktlinjer för diagnostik och behandling av invasiva lungsvampinfektioner, särskilt hos patienter utan nedsatt immunförsvar. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Översikt | Swiss medical weekly | Översikt över invasiv candidiasis, aspergillos, kryptokockos och pneumocystispneumoni. Nämner att profylax med posakonazol minskat invasiva svampinfektioner hos högriskpatienter med blodcancer. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Översikt (farmakokinetik) | Clinical pharmacokinetics | Genomgång av hur svampmedel tränger in i lungornas epitelvätska. Visar skillnader mellan beredningsformer och substanser. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Retrospektiv kohortstudie | Transplant infectious disease | Beskriver infektionskomplikationer vid akut graft-versus-host-sjukdom efter levertransplantation. |

---

### Marknadsinformation Sverige

Samtliga åtta godkännanden är indragna. Ingen indikationstext är registrerad. Fem av dem listas nedan.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 62638 | Posaconazole Abacus Medicine | Oral suspension | Ej angiven |
| 55779 | Posaconazole STADA | Oral suspension | Ej angiven |
| 58657 | Posaconazole Sandoz | Enterotablett | Ej angiven |
| 57715 | Posaconazole STADA | Enterotablett | Ej angiven |
| 65035 | Posaconazole Vivanta | Enterotablett | Ej angiven |

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Totalt 269 interaktioner är identifierade. Bland de mest betydelsefulla (allvarlig nivå) finns:
  - Loperamid
  - Triamcinolon
  - Budesonid

  Flera måttliga interaktioner gäller bland annat protonpumpshämmare och H2-blockerare (omeprazol, rabeprazol, famotidin, ranitidin, cimetidin), kortikosteroider (hydrokortison, dexametason, betametason), aprepitant, klaritromycin och saxagliptin.

Varnings- och kontraindikationsdata saknas i de sammanställda uppgifterna. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den höga modellpoängen stöds inte av någon direkt klinisk eller mekanistisk evidens, och posakonazols verkningsmekanism är svagt kopplad till *Pneumocystis*, som saknar ergosterol. Dessutom är alla svenska godkännanden indragna.

**För att gå vidare krävs:**
- Hämta produktresumé och komplettera uppgifter om varningar och kontraindikationer (blockerande dataluckor för säkerhetsscreening)
- Komplettera data om verkningsmekanism från DrugBank
- Prekliniska eller kliniska data som direkt visar effekt av posakonazol mot *Pneumocystis jirovecii*
- Jämförelse med etablerad behandling och profylax (t.ex. trimetoprim-sulfametoxazol)
- Bedömning av administreringsvägar, eftersom uppgifter om detta saknas
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

