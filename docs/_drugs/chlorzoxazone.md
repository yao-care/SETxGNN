---
layout: default
title: Chlorzoxazone
parent: Endast modellprediktion (L5)
nav_order: 96
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Chlorzoxazone: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Ej angiven i de svenska godkännandena (indikationstexten saknas)"
monitor_inn: "chlorzoxazone"
predicted_indications: ["migraine disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine with brainstem aura", "pulmonary hypertension", "atrophoderma vermiculata", "ulerythema ophryogenesis", "kyphoscoliotic heart disease", "rheumatoid arthritis"]
---

# Chlorzoxazone
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

## Klorzoxazon: Från muskelavslappnande behandling till migrän
{: .text-alpha }

---

## Sammanfattning

Klorzoxazon är ett centralt verkande muskelavslappnande läkemedel. Den ursprungliga godkända indikationen framgår inte av de svenska godkännandena i underlaget. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **migrän** (migraine disorder), med **0 kliniska prövningar** och **3 publikationer** som för närvarande hör till denna riktning. Ingen av publikationerna handlar direkt om migrän, så evidensen är i praktiken endast en modellförutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i de svenska godkännandena (indikationstexten saknas) |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 0,9973 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 3 av 3) |
| Antal godkännanden | 3 (giltiga: 3) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Baserat på känd information är klorzoxazon ett centralt verkande skelettmuskelavslappnande medel. Det beskrivs också som aktivator av kalciumberoende kaliumkanaler (SK/IK).

Det enda tänkbara sambandet med migrän går via jonkanaler. En musstudie (PMID 23115190) visar att aktivatorer av kalciumberoende kaliumkanaler lindrar ataxi orsakad av förstärkta CaV2.1-strömmar. CaV2.1-kanaler är också inblandade i familjär hemiplegisk migrän. Sambandet är därför möjligt men indirekt.

Det saknas belägg för att klorzoxazon i sig behandlar migrän. De hittade artiklarna gäller cerebellär ataxi och yrsel, inte migrän. Modellens höga poäng ska därför tolkas försiktigt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Översikt | Journal of neurology | Översikt av läkemedelsbehandling vid cerebellära och centrala vestibulära sjukdomar. Nämner inte klorzoxazon vid migrän. |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Översikt | Deutsches Arzteblatt international | Behandling och förlopp vid perifer och central yrsel. Vestibulär migrän utgör cirka 11 % av fallen. Ingen koppling till klorzoxazon. |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Prekliniskt (djurmodell) | The Journal of Neuroscience | Aktivatorer av kalciumberoende kaliumkanaler lindrade ataxi hos möss med CaV2.1-mutation. Ger ett indirekt kanalnivålänk. |

Övriga förutsägelser (t.ex. migrän med hjärnstamsaura och reumatoid artrit) saknar likaså direkta studier som stöder klorzoxazon. Den enda med några äldre kliniska rapporter är reumatoid artrit (rang 9), där stödet gäller symtomlindring av muskelsmärta och spasm, inte sjukdomsmodifierande effekt.

---

## Marknadsinformation Sverige

Alla tre godkännanden är indragna. Ingen produkt är för närvarande marknadsförd.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 58677 | Klorzoxazon Evolan | Tablett | Ej angiven |
| 6157 | Paraflex | Tablett | Ej angiven |
| 58609 | Klorzoxazon Orifarm | Tablett | Ej angiven |

---

## Säkerhetsaspekter

- **Möjliga kontraindikationer (från kunskapsgraf, inte från produktresumé)**: leversvikt, leversjukdom, gallblåsesjukdom, missbruk/beroende, läkemedelsorsakad leverskada och paracetamolförgiftning. Dessa bygger på samband i TxGNN:s kunskapsgraf och måste bekräftas mot produktresumén.
- **Läkemedelsinteraktioner**: totalt 72 interaktioner identifierade. De viktigaste:
  - **Allvarliga (Major)**: morfin, liposomalt morfin.
  - **Måttliga (Moderate)**: dronabinol, metoklopramid, nabilon, naltrexon, opium, sibutramin, etanol, prometazin.
  - Flera övriga interaktioner (bl.a. metformin, warfarin, omeprazol, simvastatin, prednison) har okänd allvarlighetsgrad.

Se produktresumén för fullständig information om varningar och kontraindikationer, som saknas i underlaget.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Trots en mycket hög modellpoäng (99,7 %) finns inga kliniska prövningar och ingen litteratur som direkt visar effekt av klorzoxazon vid migrän (evidensnivå L5). Dessutom är alla svenska godkännanden indragna, och varnings- och kontraindikationsdata från produktresumén saknas.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) för varningar, kontraindikationer och ursprunglig indikation.
- Komplettera data om verkningsmekanism, till exempel via DrugBank.
- Genomföra en riktad litteratursökning på klorzoxazon och migrän samt på kaliumkanalaktivatorer vid migrän.
- Vid fortsatt stöd: prekliniska studier i migränmodeller, därefter en liten klinisk pilotstudie.
- Särskilt beakta leverrisk och interaktioner med opioider och alkohol vid framtida utvärdering.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

