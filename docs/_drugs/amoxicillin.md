---
layout: default
title: Amoxicillin
parent: Endast modellprediktion (L5)
nav_order: 33
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Amoxicillin: predikterad ny indikation Hyperamylasemi (evidensnivå L5). Ursprunglig indikation: Urinvägsinfektion (enligt kunskapsgrafen"
monitor_inn: "amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **8** st
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

## Amoxicillin: Från urinvägsinfektion till hyperamylasemi
{: .text-alpha }

---

### Sammanfattning

Amoxicillin är ett betalaktamantibiotikum som ursprungligen användes mot bakteriella infektioner, bland annat urinvägsinfektion, öroninflammation, streptokockinfektion och bakteriell lunginflammation. TxGNN-modellen förutsäger att det kan vara effektivt mot **hyperamylasemi**, men för denna förutsägelse finns **inga kliniska prövningar** och **ingen publicerad litteratur**. Förutsägelsen bygger enbart på modellen och bör därför tolkas med stor försiktighet.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Urinvägsinfektion (enligt kunskapsgrafen; indikationstext saknas i det svenska godkännandet) |
| Förutsagd ny indikation | Hyperamylasemi |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 1 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Det är dock känt att amoxicillin är ett betalaktamantibiotikum som hämmar bakteriers cellväggssyntes, och att effekten vid bakteriella infektioner är väl belagd.

Hyperamylasemi är ett biokemiskt fynd, en förhöjd amylasnivå i blodet, och inte en bakteriell infektion. Det finns därför inget känt antibakteriellt målmolekyl som kan förklara en effekt. Den höga poängen (99,6 %) är sannolikt en följd av närhet mellan noder i kunskapsgrafen och inte av en verklig biologisk koppling.

Sammantaget går det inte att identifiera någon rimlig mekanistisk koppling mellan amoxicillins ursprungliga användning och den förutsagda nya indikationen.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 60758 | Xilmac | Pulver till injektions-/infusionsvätska, lösning | Indikationstext saknas (godkännandet är indraget) |

Tillverkare: MACURE PHARMA ApS. Det enda godkännandet är indraget, och ingen giltig produkt finns på den svenska marknaden.

---

### Säkerhetsaspekter

**Kontraindikationer enligt kunskapsgrafen** (hämtade från relationer i kunskapsgrafen, inte från produktresumé):
- Lever- och gallsjukdomar: leversvikt, leversjukdom, kolestas (inklusive benign recidiverande och familjär intrahepatisk kolestas), gallblåsesjukdom
- Njursjukdom
- Hjärtrytmrubbningar: långt QT-syndrom, torsades de pointes, ventrikulär takykardi
- Porfyri (inklusive ärftlig porfyri)
- *Clostridioides difficile*-kolit och nekrotiserande enterokolit hos nyfödda
- Myasthenia gravis och sjukdomar i neuromuskulära synapsen
- Osteoporos (inklusive postmenopausal) och benfraktur
- Infektiös mononukleos och kroniskt Epstein–Barr-virussyndrom
- Pyoureter

Dessa poster ska tolkas med försiktighet eftersom de kommer från en kunskapsgraf och inte från officiell produktinformation.

**Läkemedelsinteraktioner** (271 interaktioner identifierade; ett urval av de viktigaste):
- **Allvarliga (Major):** metotrexat, levande kolera­vaccin (*Vibrio cholerae* CVD 103-HgR)
- **Måttliga (Moderate):** doxycyklin, minocyklin, demeklocyklin, etinylestradiol, estradiol, anisindion, dikumarol, balsalazid, entekavir, mykofenolatmofetil, probiotika (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*), indium-111-oxikinolin
- **Lindriga (Minor):** allopurinol, amilorid, azitromycin, klaritromycin, erytromycin

Varningar och kontraindikationer från produktresumén finns inte tillgängliga i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen är enbart modellbaserad (L5) utan kliniska prövningar eller litteratur, och någon rimlig mekanistisk koppling mellan en antibakteriell betalaktam och hyperamylasemi saknas. Dessutom är det enda svenska godkännandet indraget.

**För att gå vidare krävs:**
- Verkningsmekanism från DrugBank för att kunna göra en ordentlig mekanistisk analys
- Varningar och kontraindikationer från produktresumén (Läkemedelsverket) för säkerhetsbedömning
- Prekliniska eller kliniska data som visar en koppling mellan amoxicillin och hyperamylasemi
- Ett tydligt biologiskt resonemang för hur amoxicillin skulle kunna påverka amylasnivåer, i stället för att enbart förlita sig på grafbaserad förutsägelse

**Kompletterande observation om andra förutsägelser:** Bland de övriga förutsagda indikationerna är *septicemisk pest* den enda med biologisk rimlighet (Yersinia pestis är en gramnegativ bakterie). Evidensen består dock av prekliniska och in vitro-studier, och standardbehandling utgörs av aminoglykosider, fluorokinoloner och tetracykliner, så amoxicillin är inte en stark kandidat där heller.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

