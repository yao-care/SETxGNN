---
layout: default
title: Histidine
parent: Endast modellprediktion (L5)
nav_order: 224
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Histidine: predikterad ny indikation Gastropares (evidensnivå L5). Ursprunglig indikation: Ingen godkänd indikationstext registrerad"
monitor_inn: "histidine"
predicted_indications: ["gastroparesis (disease)", "sclerosing cholangitis"]
---

# Histidine
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

## Histidin: Från ospecificerad indikation till gastropares
{: .text-alpha }

---

### Sammanfattning

Histidin är en aminosyra som ingår i flera infusionslösningar för parenteral nutrition och i en lösning för kardioplegi/organförvaring. Någon godkänd indikationstext finns inte registrerad i de data som sammanställts för rapporten. TxGNN-modellen förutsäger att histidin kan vara effektivt mot **gastropares**, men det finns **inga kliniska prövningar** och endast **1 publikation** som inte undersöker histidin. Evidensen är därför mycket svag.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen godkänd indikationstext registrerad |
| Förutsagd ny indikation | Gastropares |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 20 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är histidin en essentiell aminosyra och en del av parenterala näringslösningar. Dess användning som näringskomponent är väletablerad, men mekanistiskt är kopplingen till gastropares oklar.

En möjlig indirekt väg är att histidin är prekursor till histamin, som påverkar magsekretion och motilitet. Detta är spekulativt och stöds inte av de data som sammanställts. Den enda publikation som hittats handlar om amyloidpatologi i magen vid ärftlig ATTR-amyloidos och testar inte histidin.

Den höga modellpoängen bör därför tolkas försiktigt. Den är en statistisk förutsägelse, inte ett bevis på effekt.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Preklinisk/klinisk patologistudie (patienter och möss) | Amyloid | Beskriver amyloidpatologi i magsäcken och förlust av nervinnervation i slemhinnan vid ärftlig ATTR-amyloidos. Studien undersöker inte histidin och kopplar det inte till gastropares. |

---

### Marknadsinformation Sverige

Alla 20 godkännanden är indragna. Nedan visas fem av dem. Indikationstext saknas i registret.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 57202 | Corhum | Lösning för kardioplegi/organförvaring | Ej angiven |
| 59088 | Ketosteril | Filmdragerad tablett | Ej angiven |
| 12526 | Glavamin | Infusionsvätska, lösning | Ej angiven |
| 18399 | StructoKabiven Elektrolytfri | Infusionsvätska, emulsion | Ej angiven |
| 10096 | Vamin 18 g N/l elektrolytfri | Infusionsvätska, lösning | Ej angiven |

---

### Säkerhetsaspekter

- **Kontraindikationer i kunskapsgrafen (inte från produkttext):** Modellens kunskapsgraf kopplar histidin till flera tillstånd där läkemedlet kan vara olämpligt. De viktigaste grupperna är:
  - Njursjukdom: kronisk njursjukdom, kronisk njursvikt, njursvikt i slutstadiet, njursten och nefrokalcinos
  - Hjärt-kärlsjukdom: hjärtsjukdom, kammarflimmer och digitalisförgiftning
  - Kalcium- och fosforrubbningar: hyperkalcemi, malignitetsrelaterad hyperkalcemi och sarkoidos
  - Ämnesomsättningssjukdomar: fenylketonuri och andra rubbningar i fenylalaninomsättningen

Dessa uppgifter är inte hämtade från godkänd produktinformation och måste verifieras mot produktresumén.

Information om läkemedelsinteraktioner saknas. Se produktresumén för övrig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellpoäng (evidensnivå L5). Det finns inga kliniska prövningar, och den enda publikationen undersöker inte histidin.
- Samtliga svenska godkännanden är indragna, och mekanism- och säkerhetsdata saknas.

**För att gå vidare krävs:**
- Hämta verkningsmekanismen från DrugBank.
- Hämta varningar och kontraindikationer från produktresumén hos Läkemedelsverket (MPA).
- Göra en systematisk litteratursökning om histidin, histamin och mag-tarmmotilitet.
- Undersöka prekliniska data på histidins effekt på magsäckens tömning.
- Utvärdera administreringsväg och beredningsform för den nya indikationen.

---

### Ytterligare observation: primär skleroserande kolangit (rang 2)

Den näst högst rankade förutsägelsen, skleroserande kolangit (poäng 99,3 %, evidensnivå L4), har flera prekliniska studier. De pekar dock på att histamin-signalering **förvärrar** sjukdomen, och histidin är histaminets prekursor. Mössmodeller utan histidindekarboxylas visar mindre gallgångsskada och fibros. Histidintillförsel skulle därför i teorin kunna vara ofördelaktig. Denna riktning bör behandlas som en säkerhetsfråga och inte som ett terapeutiskt förslag.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

