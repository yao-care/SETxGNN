---
layout: default
title: Febuxostat
parent: Måttlig evidens (L3-L4)
nav_order: 189
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
description: "Febuxostat: predikterad ny indikation Renal hypourikemi (hypouricemia, renal) (evidensnivå L4). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Febuxostat
{: .fs-9 }

Evidensnivå: **L4** | Förutsagda indikationer: **3** st
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

## Febuxostat: Renal hypourikemi (hypouricemia, renal)
{: .text-alpha }

---

## Sammanfattning

Febuxostat är en xantinoxidashämmare som ursprungligen användes för att behandla hyperurikemi (förhöjd urinsyranivå). TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **renal hypourikemi**, men underlaget är mycket svagt: **1 klinisk prövning** med oklar koppling till diagnosen och **2 publikationer** (en översikt och en fallrapport). Den höga modellpoängen verkar spegla närhet till urinsyrans metaboliska vägar snarare än en verklig terapeutisk nytta.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Renal hypourikemi (hypouricemia, renal) |
| TxGNN-förutsägelsepoäng | 0.9999 |
| Evidensnivå | L4 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 1 av 1) |
| Antal godkännanden | 1 (giltiga: 1) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Febuxostat är dock känt som en icke-purin, selektiv hämmare av xantinoxidas, som sänker urinsyra i serum.

Vid renal hypourikemi är urinsyranivån redan låg på grund av nedsatt återupptag av urat i njuren (till exempel förlust av funktion i URAT1 eller GLUT9). Ett läkemedel som sänker urinsyra har därför ingen tydlig terapeutisk logik här och kan till och med vara kontraproduktivt. Den enda tänkbara kopplingen är indirekt: en japansk fallrapport från 2023 beskriver att xantinoxidoreduktashämmare övervägts för att förebygga ansträngningsutlöst akut njurskada hos en tonårig fotbollsspelare med familjär renal hypourikemi. Det gäller en annan användning än att behandla själva grundsjukdomen.

Den höga modellpoängen beror sannolikt på att läkemedel och sjukdom ligger nära varandra i nätverket kring urinsyrans metabolism, inte på ett verkligt behandlingssamband.

**Övriga förutsägelser i modellen:** Två ytterligare förutsägelser rankas högt, partiell brist på hypoxantin-guanin-fosforibosyltransferas (HPRT) och Lesch-Nyhans syndrom. Där är mekanismen mer sammanhängande, eftersom sjukdomarna ger överproduktion av urinsyra som xantinoxidashämning kan dämpa. Nyttan skulle dock begränsas till de urinsyrarelaterade symtomen, inte de neurologiska. Dessa nämns bara som kontext, eftersom rapporten gäller den högst rankade förutsägelsen.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fas 4 | Okänd | 100 | Prospektiv kontrollerad studie av hur urinsyrakontroll påverkar stenåterfall och njurfunktion hos patienter med njurstenar och hyperurikemi. Kopplingen till renal hypourikemi och febuxostat kan inte verifieras och bedöms som svag. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Fallrapport | Internal Medicine | 16-årig fotbollsspelare med familjär renal hypourikemi (mutationer i URAT1) och återkommande ansträngningsutlöst akut njurskada. Vätskeintag räckte inte som förebyggande åtgärd, och en xantinoxidoreduktashämmare diskuteras som möjlig profylax. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Översikt | Clinical Rheumatology | Berättande översikt över hypourikemi (serumurat < 2 mg/dl) och dess orsaker. Beskriver inte febuxostat som behandling av tillståndet. |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 56645 | Febuxostat Accord (Accord Healthcare B.V.) | Filmdragerad tablett | Ingen indikationstext angiven (status: godkänd) |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumén): stroke, cerebrovaskulär sjukdom, hjärninfarkt, hjärtinfarkt, koronartrombos och hemoglobinopati.
- **Läkemedelsinteraktioner:** 22 interaktioner identifierades, varav de viktigaste är:
  - **Allvarliga (Major):** merkaptopurin, azatioprin, leflunomid och teriflunomid.
  - **Måttliga (Moderate), urval:** teofyllin, aminofyllin, dyfyllin, oxtrifyllin, metotrexat, tioguanin, klofarabin, epirubicin, trabektedin, pegaspargas, asparaginas, brentuximabvedotin, interferon beta-1a/1b, peginterferon beta-1a och naltrexon.

Säkerhetsuppgifter från produktresumén saknas i underlaget. Se produktresumén för fullständig information om varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Ett urinsänkande läkemedel saknar tydlig terapeutisk logik vid ett tillstånd som redan kännetecknas av låg urinsyra, och evidensen utgörs enbart av en fallrapport och en översikt (L4). Den enda kliniska prövningen handlar om hyperurikemi med njurstenar och stöder inte förutsägelsen.

**För att gå vidare krävs:**
- Verifiering av prövningen NCT04398251 i det ursprungliga registret för att fastställa intervention och utfallsmått.
- Mekanistisk utvärdering av om xantinoxidashämning är relevant för att förebygga ansträngningsutlöst akut njurskada vid renal hypourikemi, samt hur det förhåller sig till risken för ytterligare sänkt urinsyra.
- Kontrollerade studier eller större fallserier som visar effekt och säkerhet.
- Komplettering med varningar och kontraindikationer från produktresumén samt uppgifter om verkningsmekanism från DrugBank.
- Klargörande av den regulatoriska statusen, eftersom det enda svenska godkännandet är avregistrerat.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

