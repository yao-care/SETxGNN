---
layout: default
title: Mupirocin
parent: Endast modellprediktion (L5)
nav_order: 307
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "MUPIROCIN"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Mupirocin: predikterad ny indikation Pleural empyema (disease) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Mupirocin
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

## Mupirocin: Pleural empyema (disease)
{: .text-alpha }

---

## Sammanfattning

Mupirocin är ett lokalt verkande antibiotikum som ursprungligen användes för att behandla hudinfektioner av typen impetigo och bullös impetigo. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **pleurempyem**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** i de data som sammanställts för denna rapport. Förutsägelsen är därför enbart en modellberäkning och bör tolkas med stor försiktighet.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Pleural empyema (disease) |
| TxGNN-förutsägelsepoäng | 0.9949 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 1 av 1) |
| Antal godkännanden | 1 (giltiga: 1) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Det finns ingen detaljerad verkningsmekanismdata i de sammanställda uppgifterna. Utifrån allmän farmakologisk kunskap hämmar mupirocin bakteriens isoleucyl-tRNA-syntetas och verkar främst mot grampositiva kocker som *Staphylococcus aureus* (inklusive MRSA) och *Streptococcus pyogenes*. Dessa bakterier är också vanliga orsaker till pleurempyem, vilket ger en möjlig antibakteriell logik bakom förutsägelsen.

Det finns dock ett stort praktiskt hinder. Mupirocin är ett lokalt läkemedel med försumbar systemisk upptagning, eftersom det snabbt omvandlas till den inaktiva metaboliten monsyra. Det kan inte nå verksamma koncentrationer i pleurahålan via någon etablerad administreringsväg. Det höga poängvärdet (0,9949) ska därför ses som ett beräkningsresultat och inte som ett tecken på klinisk användbarhet.

Den näst högst rankade förutsägelsen, punktformad epitelial keratokonjunktivit (poäng 0,9910), har likaså svag grund. Mupirocins effekt mot stafylokocker kan vara relevant bara för den bakteriella delmängden, och läkemedlet saknar antiviral effekt. Tillgängliga beredningar är avsedda för hud eller näsa och är inte godkända för ögonen, så tolerans och säkerhet i ögat är inte klarlagda.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 11808 (avregistrerad) | Bactroban (GlaxoSmithKline AB) | Salva | Ingen indikationstext tillgänglig |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen**: Dermatit. Uppgiften kommer från samband i kunskapsgrafen och inte från produktresumétext.
- **Läkemedelsinteraktioner**: Interaktionsdatabasen visar 100 registrerade läkemedelspar, men allvarlighetsgraden är klassad som "okänd" för samtliga. Bland de listade läkemedlen finns kalcitriol, klotrimazol, morfin, metformin, pantoprazol, omeprazol, sukralfat, vankomycin, laktulos, triamcinolon, prednison och simvastatin. Ingen av dessa kan i nuläget bedömas som kliniskt betydelsefull.

Se produktresumén för fullständig säkerhetsinformation om varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellberäkning (evidensnivå L5) utan stöd från kliniska prövningar eller litteratur.
- Mupirocin är ett lokalt läkemedel utan relevant systemisk exponering, vilket gör att nå pleurahålan i praktiken omöjligt med nuvarande beredningar.

<!-- review:begin se-lic-20261106-mupirocin-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Mupirocin är ett lokalt läkemedel utan relevant systemisk exponering, vilket gör att nå pleurahålan i praktiken omöjligt med nuvarande beredningar. Dessutom är det enda svenska godkännandet avregistrerat.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 1, varav giltiga: 1; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-mupirocin-1 -->

**För att gå vidare krävs:**
- Hämta och granska produktresumén för varningar och kontraindikationer, eftersom säkerhetsdata saknas i nuläget.
- Komplettera uppgifter om verkningsmekanism från DrugBank.
- Utvärdera administreringsväg och beredningsform: en systemisk eller intrapleural beredning skulle krävas, med prekliniska data om farmakokinetik och säkerhet.
- Genomföra litteratur- och prövningssökning för pleurempyem och stafylokockrelaterade ögoninfektioner.
- Överväga etablerade systemiska antibiotika som jämförelsealternativ, eftersom dessa redan används vid pleurempyem.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Dessutom är det enda svenska godkännandet avregistrerat” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

