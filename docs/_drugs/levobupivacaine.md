---
layout: default
title: Levobupivacaine
parent: Endast modellprediktion (L5)
nav_order: 259
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Levobupivacaine: predikterad ny indikation Gastroduodenit (evidensnivå L5). Ursprunglig indikation: Ej angiven i licensuppgifterna"
monitor_inn: "levobupivacaine"
predicted_indications: ["gastroduodenitis"]
---

# Levobupivacaine
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

## Levobupivakain: Från okänd ursprunglig indikation till gastroduodenit
{: .text-alpha }

---

### Sammanfattning

Levobupivakain är ett långverkande amidlokalanestetikum. Ingen godkänd ursprunglig indikation finns angiven i de data som sammanställts för denna rapport, eftersom indikationstexten saknas i licensuppgifterna. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **gastroduodenit**, men det finns **0 kliniska prövningar** och **0 publikationer** som stöder förutsägelsen, vilket innebär att den enbart bygger på en modellprediktion.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i licensuppgifterna |
| Förutsagd ny indikation | Gastroduodenit |
| TxGNN-förutsägelsepoäng | 99,1 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 (båda indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts. Baserat på allmänt känd information är levobupivakain ett långverkande amidlokalanestetikum som blockerar spänningskänsliga natriumkanaler i nervceller. Det används för att ge lokal bedövning och smärtlindring.

Något säkert samband mellan den ursprungliga användningen och gastroduodenit kan inte styrkas med tillgängliga data. En tänkbar men obekräftad förklaring är att lokalanestetika kan påverka smärtsignalering från inre organ (visceral nociception) eller ha en antiinflammatorisk effekt. Det finns dock inga kliniska eller litteraturbaserade belägg för detta.

Det höga poängvärdet (0,991) kommer från en kunskapsgrafsprediktion och ska tolkas med försiktighet. Det är i sig inget bevis för effekt.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 64618 | Levobupivacaine Molteni | Injektions-/infusionsvätska, lösning | Ej angiven (indragen) |
| 64617 | Levobupivacaine Molteni | Injektions-/infusionsvätska, lösning | Ej angiven (indragen) |

---

### Säkerhetsaspekter

- **Möjliga sjukdomsrelaterade kontraindikationer (från kunskapsgraf, inte från produktresumé)**: njursjukdom, leversjukdom, gallblåsesjukdom, pyouretär, myasthenia gravis (inklusive vuxendebuterad form), sjukdom i neuromuskulära förbindelsen, butyrylkolinesterasbrist samt hjärt- och kärlsjukdom/hjärtsjukdom.
- **Läkemedelsinteraktioner**: totalt 62 kända interaktioner. Exempel på de som klassas som måttliga:
  - Aprepitant
  - Cimetidin
  - Klaritromycin
  - Obetikolsyra
  - Mikonazol
  - Klotrimazol
  - Kobicistat
  - Deferasirox
  - Tiklopidin
  - Fostamatinib
  - Tiabendazol
  - Primakin
  - Lidokain, bensokain och kokain (lokala beredningar) samt lidokain (oftalmologiskt)
- Mindre allvarliga interaktioner förekommer bland annat med dexametason, omeprazol, hyaluronidas och albendazol.

Se produktresumén för fullständig säkerhetsinformation, eftersom uppgifter om varningar och kontraindikationer från etiketten saknas i de sammanställda data.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellprediktion (L5) utan kliniska prövningar eller litteratur. Dessutom saknas giltigt godkännande i Sverige, och verkningsmekanism samt etikettbaserad säkerhetsinformation saknas.

**För att gå vidare krävs:**
- Hämta och granska produktresumén (varningar och kontraindikationer) från Läkemedelsverket.
- Komplettera verkningsmekanismen från DrugBank och analysera det mekanistiska sambandet med gastroduodenit.
- Söka efter och utvärdera kliniska studier och litteratur kring lokalanestetika vid gastroduodenit.
- Bedöma administreringsväg och beredningsform i förhållande till den nya indikationen.
- Gå igenom de 62 läkemedelsinteraktionerna och de kunskapsgrafsbaserade kontraindikationerna.
- Klargöra läkemedlets regulatoriska status, eftersom alla godkännanden är indragna.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

