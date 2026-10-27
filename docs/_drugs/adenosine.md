---
layout: default
title: Adenosine
parent: Endast modellprediktion (L5)
nav_order: 17
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Adenosine: predikterad ny indikation Obsolete bundle branch block (grenblock, föråldrad term) (evidensnivå L5). Ursprunglig indikation: Ventrikulär takykardi (enligt kunskapsgrafen"
monitor_inn: "adenosine"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
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

## Adenosin: Från ventrikulär takykardi till grenblock (föråldrad term i ontologin)
{: .text-alpha }

---

### Sammanfattning

Adenosin är ett läkemedel mot hjärtrytmrubbningar. Enligt kunskapsgrafen användes det ursprungligen vid **ventrikulär takykardi**. TxGNN-modellen förutsäger att det kan vara effektivt mot **"obsolete bundle branch block"** (en föråldrad ontologipost för grenblock), men det finns **inga kliniska prövningar och ingen publicerad litteratur** som stöder detta. Förutsägelsen är en ren modellberäkning och bedöms sannolikt vara en artefakt.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ventrikulär takykardi (enligt kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Obsolete bundle branch block (grenblock, föråldrad term) |
| TxGNN-förutsägelsepoäng | 99,94 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 2 (båda avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts. Adenosin verkar dock i hjärtat genom att aktivera A1-receptorer, vilket påverkar ledningen i AV-knutan. Det används vid utredning och akut behandling av vissa arytmier, men inte som behandling av ledningsblock.

Den höga poängen är svår att motivera kliniskt. Grenblock är en ledningsstörning i kammaren, nedanför AV-knutan, och en direkt behandlingsrationale för adenosin syns inte. Termen är dessutom markerad som föråldrad, vilket tyder på en gammal ontologipost snarare än ett eget kliniskt tillstånd. Det mest sannolika är att poängen beror på att adenosin i grafen ligger nära noder för hjärtats ledningssystem och arytmier.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 19361 | Adenosin Life Medical (Evolan Pharma AB) | Injektions-/infusionsvätska, lösning | Avregistrerad |
| 67173 | Adenosin Macure (Macure Healthcare Limited) | Injektions-/infusionsvätska, lösning | Avregistrerad |

Ingen godkänd indikationstext finns tillgänglig för dessa godkännanden. Ingen av produkterna har något giltigt godkännande i dag.

---

### Säkerhetsaspekter

Uppgifter om varningar och kontraindikationer från produktresumén saknas. Se produktresumén för säkerhetsinformation.

- **Kontraindikationer enligt kunskapsgrafen** (ej hämtade från produkttext): kroniskt obstruktiv lungsjukdom (KOL), astma, aortastenos, mitralisstenos, lågt blodtryck, akut kranskärlssyndrom, kranskärlssjukdom, AV-block, sjuk sinusknuta (sick sinus syndrome), perikardit, lungemfysem och andningssvikt.
- **Läkemedelsinteraktioner:** Totalt 138 interaktioner är kända. Bland de viktigaste:
  - **Allvarliga (Major):** cisaprid, dolasetron, papaverin.
  - **Måttliga (Moderate):** famotidin, klaritromycin, granisetron, levofloxacin, ondansetron, palonosetron.

---

### Ytterligare förutsägelse: katekolaminerg polymorf ventrikulär takykardi (CPVT)

Modellens andra förutsägelse, **CPVT** (poäng 99,42 %), har något mer stöd och bedöms som evidensnivå **L4** med rekommendationen "Forskningsfråga".

- **Mekanism:** CPVT orsakas av kalciumläckage från sarkoplasmatiska retikulum, vilket ger triggade arytmier. Adenosin (och ATP) kan via A1-receptorer motverka beta-adrenerg stimulering och sänka cAMP. Det ger en rimlig mekanism för att avbryta bidirektionell kammartakykardi.
- **Klinisk evidens:** Endast en fallrapport, [PMID 18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) (2008, *Heart Rhythm*), där ATP avbröt bidirektionell kammartakykardi hos en CPVT-patient. Övriga träffar är översikter, prekliniska studier och diagnostiska sammanhang, utan visad behandlingseffekt av adenosin. Inga kliniska prövningar är registrerade.
- **Begränsningar:** Adenosin har mycket kort halveringstid och kan därför bara avbryta akuta episoder, inte förebygga nya. Det kan dessutom i vissa situationer vara proarytmiskt. Standardbehandlingen (betablockerare, flekainid, vänstersidig kardiell sympatisk denervering, ICD) är fortsatt grunden.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den förutsagda indikationen (grenblock) saknar all klinisk och publicerad evidens, är en föråldrad ontologipost och har ingen tydlig mekanistisk koppling till adenosin. Båda svenska godkännandena är dessutom avregistrerade.

**För att gå vidare krävs:**
- Uppgifter om varningar och kontraindikationer från produktresumén, samt verkningsmekanism från DrugBank.
- Klinisk validering av om en relevant, aktuell sjukdomsdefinition finns för den förutsagda indikationen.
- Om CPVT ska följas upp: systematisk litteraturgenomgång och kontrollerade studier som visar nytta utöver standardbehandling.
- Klarhet i om en ny marknadsföring i Sverige är aktuell, eftersom inga giltiga godkännanden finns.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

