---
layout: default
title: Calcifediol
parent: Endast modellprediktion (L5)
nav_order: 76
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Calcifediol: predikterad ny indikation Obsolete vitamin D deficiency (föråldrad term för D-vitaminbrist) (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext angiven i godkännandena. Enlig…"
monitor_inn: "calcifediol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "hereditary hypophosphatemic rickets", "vitamin D-dependent rickets"]
---

# Calcifediol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

# Kalcifediol: Från hyperkalcemi och rakit till D-vitaminbrist

## Sammanfattning

Kalcifediol (25-hydroxivitamin D3) är den cirkulerande föregångaren till aktivt D-vitamin (kalcitriol). Läkemedlet kopplas i kunskapsgrafen till bensjukdomar och mineralomsättningsstörningar, bland annat rakit, osteomalaci, hypofosfatemi och renal osteodystrofi. TxGNN-modellen förutsäger att det kan vara effektivt mot **D-vitaminbrist** (en föråldrad ontologipost), men det finns **inga kliniska prövningar** och **ingen litteratur** för just den indikationen. För alternativa förutsagda indikationer finns endast **2 översiktsartiklar** som indirekt stöd.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext angiven i godkännandena. Enligt kunskapsgrafen: hyperkalcemi, nefrokalcinos, fosfatomsättningsstörning, hypofosfatemi, rakit, osteomalaci och renal osteodystrofi |
| Förutsagd ny indikation | Obsolete vitamin D deficiency (föråldrad term för D-vitaminbrist) |
| TxGNN-förutsägelsepoäng | 99,99 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 (båda indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är kalcifediol den direkta föregångaren till kalcitriol och den vedertagna markören för D-vitaminstatus. Dess effekt vid rakit och osteomalaci är väl känd, och mekanistiskt kan den vara tillämpbar på D-vitaminbrist.

Den mycket höga poängen (0,9999) speglar sannolikt att D-vitaminbrist ligger nära de ursprungliga indikationerna (rakit, osteomalaci) i kunskapsgrafen, snarare än att det finns oberoende evidens. Termen är dessutom föråldrad i ontologin. Poängen bör därför tolkas med försiktighet.

Bland de övriga förutsägelserna är **D-vitaminberoende rakit** mekanistiskt mest intressant:

- **D-vitaminberoende rakit typ 1B** orsakas av brist på 25-hydroxylas (CYP2R1). Kalcifediol kringgår detta enzymblock, vilket ger en direkt och biologiskt stark logik. Typ 1A (brist på 1-alfahydroxylas) skulle inte ha nytta, eftersom den kräver kalcitriol.
- **Ärftlig hypofosfatemisk rakit** drivs av njurarnas fosfatförlust (ofta FGF23-medierad). Standardbehandlingen är fosfat plus aktivt D-vitamin, och kalcifediol är därför sannolikt inte primär behandling.
- **Renal tubulär acidos** kan ge sekundär bensjukdom. Kalcifediol skulle i bästa fall vara ett komplement mot benkomplikationer, inte behandla själva tubulusdefekten.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen litteratur finns för den högst rankade indikationen. För de övriga förutsagda indikationerna finns följande:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Översikt | Nutrients | Beskriver olika typer av rakit och behandling med D-vitamin och analoger (bl.a. kalcitriol). Indirekt stöd för ärftlig hypofosfatemisk rakit. |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Översikt/kliniskt fall | Journal of Bone and Mineral Research | Beskriver D-vitaminberoende rakit typ 1B (25-hydroxylasbrist, CYP2R1) hos 7 patienter från 2 familjer. Indirekt stöd. |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 59064 | Rayaldee (indraget) | Depotkapsel, mjuk | Ingen indikationstext angiven |
| 64724 | Defevix (indraget) | Kapsel, mjuk | Ingen indikationstext angiven |

---

## Säkerhetsaspekter

**Kontraindikationer enligt kunskapsgrafen** (ej hämtade från produktresumétext): njursjukdom, pyouretär, sarkoidos, hyperkalcemi, nefrokalcinos, fosfatomsättningsstörning, njursten (inklusive genetisk benägenhet kopplad till SLC26A1), akut urat-nefropati, hyperfosfatemi, hypervitaminos och arteriosclerosis obliterans.

**Läkemedelsinteraktioner** (57 identifierade, de viktigaste nedan):

- **Allvarliga (Major):** kolekalciferol, kalcitriol, burosumab
- **Måttliga (Moderate), urval:**
  - Tiazider: hydroklortiazid, bendroflumetiazid, klortalidon, klortiazid
  - Antiepileptika och barbiturater: fosfenytoin, karbamazepin, amobarbital, butalbital, butabarbital
  - Gallsyrabindare: kolestyramin, kolesevelam, kolestipol
  - Övrigt: aluminiumhydroxid, digitoxin, kalcipotriol och kalcitriol (topikala)

Se produktresumén för fullständig säkerhetsinformation, varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den högst rankade förutsägelsen (D-vitaminbrist) bygger enbart på modellen (L5), är en föråldrad term och saknar både prövningar och litteratur. Dessutom är båda svenska godkännandena indragna.
- D-vitaminberoende rakit typ 1B är den mest lovande riktningen mekanistiskt (L4), men stödet är indirekt och bör ses som en forskningsfråga.

**För att gå vidare krävs:**
- Produktresumé från Läkemedelsverket med varningar och kontraindikationer, eftersom säkerhetsscreening inte kan genomföras utan dem.
- Verkningsmekanismdata från DrugBank.
- Systematisk litteratursökning och sökning efter kliniska prövningar för kalcifediol vid bekräftad D-vitaminberoende rakit typ 1B.
- Bedömning av beredningsform och administreringsväg samt av risken för hyperkalcemi och nefrokalcinos hos njursjuka patienter.
- Klargörande av om en ny eller aktuell marknadsföring i Sverige är möjlig, givet att godkännandena är indragna.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

