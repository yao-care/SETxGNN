---
layout: default
title: Balsalazide
parent: Endast modellprediktion (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Balsalazide: predikterad ny indikation Gikt (evidensnivå L5). Ursprunglig indikation: Ulcerös kolit, inflammatorisk tarmsjukdom (enligt kunskapsgrafen"
monitor_inn: "balsalazide"
predicted_indications: ["gout", "congenital hypotrichosis with juvenile macular dystrophy", "ankylosing spondylitis", "rheumatoid arthritis", "rheumatoid vasculitis", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease", "polyarticular juvenile rheumatoid arthritis", "anus disease"]
---

# Balsalazide
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

# Balsalazid: Från ulcerös kolit till gikt

---

## Sammanfattning

Balsalazid är en prodrug till 5-aminosalicylsyra (5-ASA) och användes ursprungligen för att behandla ulcerös kolit och inflammatorisk tarmsjukdom. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **gikt**, men det finns **0 kliniska prövningar** och **0 publikationer** som stöder förutsägelsen. Den är därmed enbart en modellförutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ulcerös kolit, inflammatorisk tarmsjukdom (enligt kunskapsgrafen; godkännandets indikationstext saknas) |
| Förutsagd ny indikation | Gikt |
| TxGNN-förutsägelsepoäng | 99,75 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 1 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Balsalazid är dock en prodrug av 5-ASA, som verkar antiinflammatoriskt lokalt i tjocktarmen. Dess effekt vid ulcerös kolit är väletablerad.

Gikt orsakas av att urinsyrakristaller aktiverar NLRP3-inflammasomen och utlöser en kraftig inflammation i lederna. Ett samband med 5-ASA:s antiinflammatoriska egenskaper är möjligt men **spekulativt**. 5-ASA tas dessutom upp dåligt i blodet, vilket försvagar resonemanget ytterligare, eftersom gikt kräver effekt i lederna och inte i tarmen.

Förutsägelsen bör därför tolkas försiktigt. Den höga poängen visar modellens mönster i kunskapsgrafen, inte biologiskt eller kliniskt belägg.

### Övriga förutsägelser

De närmast följande förutsägelserna har likartade poäng (99,4–99,7 %) och likaså enbart evidensnivå L5. Några har ett något tydligare biologiskt samband med tarm–led-axeln:

| Förutsagd indikation | Poäng | Bedömning |
|------|------|------|
| Ankyloserande spondylit | 99,71 % | Forskningsfråga: delad IBD–spondyloartrit-axel, men aminosalicylater har begränsad effekt vid axial sjukdom |
| Reumatoid artrit | 99,64 % | Forskningsfråga: sulfasalazin är etablerat, men effekten tillskrivs sulfapyridin, som balsalazid saknar |
| Inflammatorisk spondylopati | 99,53 % | Forskningsfråga: överlappar med spondyloartropatier, indirekt stöd |
| Polyartikulär juvenil reumatoid artrit | 99,43 % | Forskningsfråga: indirekt stöd via sulfasalazin, pediatriska data saknas |
| Analsjukdom | 99,41 % | Forskningsfråga: icke-specifik term, måste preciseras (t.ex. proktit) |
| Reumatoid vaskulit, kongenital hypotrikos med juvenil makuladystrofi, hypermobilitet i svansbenet, Kümmells sjukdom | 99,2–99,7 % | Avvakta: ingen rimlig mekanism |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 14325 | Colazid (Almirall S.A.) | Kapsel, hård | Indraget |

Det finns inga giltiga godkännanden i Sverige för närvarande.

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumén): njursjukdom, pyouréter (var i urinledaren), pylorusstenos.
- **Läkemedelsinteraktioner**: totalt 196 interaktioner identifierade. De viktigaste i urvalet:
  - **Allvarlig (Major)**: humant immunglobulin G (intravenöst)
  - **Måttlig (Moderate)**, bland annat:
    - NSAID-preparat: ketorolak, ibuprofen, celecoxib
    - Njurpåverkande läkemedel: amfotericin B (inklusive lipidkomplex och kolesterylsulfat), foskarnet, aciklovir, gallium nitrat
    - Antibiotika: amikacin (inklusive liposomal form), amoxicillin, ampicillin, azitromycin, doxycyklin, bacitracin, fosfomycin
    - Övriga: azatioprin, acetohexamid

Eftersom informationen från produktresumén saknas bör man även se produktresumén för fullständiga varningar och försiktighetsåtgärder.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för gikt bygger enbart på en modellpoäng utan kliniska prövningar eller publikationer, och den biologiska rimligheten är låg, bland annat på grund av 5-ASA:s dåliga upptag i blodet. Dessutom är läkemedlets enda svenska godkännande indraget.

**För att gå vidare krävs:**
- En systematisk litteratursökning om aminosalicylater vid gikt, och i första hand vid ankyloserande spondylit, reumatoid artrit och inflammatorisk spondylopati, där tarm–led-sambandet är starkare.
- Uppgifter om verkningsmekanism från DrugBank.
- Varningar och kontraindikationer från produktresumén.
- Prekliniska data om balsalazid eller 5-ASA och NLRP3-inflammasomen.
- Klargörande av marknadsläget, eftersom godkännandet är indraget och beredningsformen är avsedd för lokal effekt i tarmen.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

