---
layout: default
title: Levocabastine
parent: Endast modellprediktion (L5)
nav_order: 260
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Levocabastine: predikterad ny indikation Allergisk urtikaria (evidensnivå L5). Ursprunglig indikation: Atopisk konjunktivit…"
monitor_inn: "levocabastine"
predicted_indications: ["allergic urticaria", "rosacea conjunctivitis"]
---

# Levocabastine
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

# Levocabastin: Från atopisk konjunktivit till allergisk urtikaria

---

## Sammanfattning

Levocabastin är en histamin H1-receptorantagonist som ursprungligen användes mot allergiska ögonåkommor (atopisk, papillär och vernal konjunktivit) som ögondroppar och som nässpray. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **allergisk urtikaria**. Evidensen är svag: inga kliniska prövningar och **3 publikationer**, varav ingen studerar urtikaria direkt.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Atopisk konjunktivit, papillär konjunktivit och vernal konjunktivit (enligt kunskapsgrafen; godkännandenas indikationstext är tom) |
| Förutsagd ny indikation | Allergisk urtikaria |
| TxGNN-förutsägelsepoäng | 99,2 % |
| Evidensnivå | L4 (indirekt evidens från klassfarmakologi och allergenprovokationsstudie vid allergisk rinit) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 3 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Data om verkningsmekanism saknas i den insamlade informationen. Utifrån etablerad farmakologi är levocabastin en selektiv H1-receptorantagonist. Vid allergisk urtikaria driver histamin, via H1-receptorer i hudens små blodkärl och sensoriska nerver, bildandet av kvaddlar och rodnad. H1-blockad är därför mekanistiskt rimlig, och andra antihistaminer är förstahandsbehandling vid urtikaria.

Kopplingen till den ursprungliga indikationen är att båda tillstånden är histaminmedierade allergiska reaktioner. Förutsägelsen bygger dock på läkemedelsklassen och inte på levocabastin självt.

Det finns en viktig begränsning. Levocabastin har bara funnits som lokala beredningar (ögondroppar och nässpray) med låg systemisk exponering. Det finns därför ingen etablerad administreringsväg eller dos för att behandla urtikaria, och förenlighet med beredningsform och administreringsväg är inte utredd.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [8938880](https://pubmed.ncbi.nlm.nih.gov/8938880/) | 1996 | Klinisk provokationsstudie (randomiserad, dubbelblind, placebokontrollerad, cross-over) | Rhinology | 22 patienter med allergisk rinit. Levocabastin nässpray minskade nysningar signifikant (p < 0,001) och även rinorré efter nasal allergenprovokation. Gäller allergisk rinit, inte urtikaria. |
| [1685361](https://pubmed.ncbi.nlm.nih.gov/1685361/) | 1991 | Översikt | Clinical pharmacokinetics | Sammanfattar farmakokinetik och farmakodynamik för andra generationens H1-antagonister vid allergisk rinokonjunktivit och kronisk urtikaria. Allmän klassinformation. |
| [42585211](https://pubmed.ncbi.nlm.nih.gov/42585211/) | 2026 | Deskriptiv farmakovigilansanalys | PLoS ONE | Jämför biverkningsprofiler för azelastin och levocabastin i WHO:s databas VigiAccess. Ger säkerhetskontext, inte effektdata. |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 11504 | Livostin (McNeil Sweden AB) | Nässpray, suspension | Ingen indikationstext angiven (indraget) |
| 61691 | Livostin (Ebb Medical AB) | Nässpray, suspension | Ingen indikationstext angiven (indraget) |
| 11328 | Livostin (McNeil Sweden AB) | Ögondroppar, suspension | Ingen indikationstext angiven (indraget) |

---

## Säkerhetsaspekter

- **Läkemedelsinteraktioner**: En farmakologisk koppling till NTS2-receptorn (NTSR2) har registrerats, men affinitetsdata som styrker den saknas och ingen allvarlighetsgrad är angiven. Den har oklar klinisk betydelse.

Se i övrigt produktresumén för varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den höga modellpoängen stöds inte av direkt evidens. Det finns inga kliniska prövningar, ingen litteratur om urtikaria och endast indirekta data från allergisk rinit.
- Dessutom är alla svenska godkännanden indragna, och de lokala beredningarna har låg systemisk exponering, vilket gör användning vid urtikaria praktiskt osäker.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket för varningar och kontraindikationer, vilket är ett blockerande datagap för säkerhetsbedömningen.
- Komplettera data om verkningsmekanism och bekräfta H1-profilen.
- Utreda om det finns en lämplig beredningsform och administreringsväg samt dos för systemisk eller kutan behandling.
- Överväga prekliniska studier eller en pilotstudie vid urtikaria. Jämför mot etablerade antihistaminer som redan är godkända för indikationen.

---

*Sekundär förutsägelse (rang 2): reumatisk/rosacea-konjunktivit (poäng 99,2 %, evidensnivå L5, beslut Avvakta). Mekanismkopplingen är spekulativ eftersom okulär rosacea främst drivs av meibomska körtlars dysfunktion, lock- och mikrobfaktorer samt medfödd inflammation, med högst liten roll för histamin. Inga studier finns.*
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

