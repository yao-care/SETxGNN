---
layout: default
title: Ciclesonide
parent: Endast modellprediktion (L5)
nav_order: 98
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ciclesonide: predikterad ny indikation Atopiskt eksem (evidensnivå L5). Ursprunglig indikation: Astma, intrinsisk astma, allergisk astma, allergisk rinit…"
monitor_inn: "ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
---

# Ciclesonide
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

# Ciclesonide: Från astma och allergisk rinit till atopiskt eksem

---

### Sammanfattning

Ciclesonide är ett inhalerat kortikosteroid som ursprungligen användes för att behandla astma och allergisk rinit. TxGNN-modellen förutsäger att det kan vara effektivt mot **atopiskt eksem**, men för närvarande finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder denna riktning. Förutsägelsen är därmed enbart beräkningsbaserad.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Astma, intrinsisk astma, allergisk astma, allergisk rinit, vasomotorisk rinit (enligt TxGNN:s kunskapsgraf, eftersom godkända indikationstexter saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Atopiskt eksem |
| TxGNN-förutsägelsepoäng | 99,96 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 9 (samtliga avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det sammanställda underlaget. Baserat på känd information är ciclesonide ett inhalerat kortikosteroid i form av en prodrug. Det aktiveras av esteraser till des-ciclesonide, som verkar som agonist på glukokortikoidreceptorn och har antiinflammatorisk effekt.

Atopiskt eksem är en kronisk inflammatorisk hudsjukdom, och kortikosteroider (lokala eller systemiska) är väletablerad behandling. Den ursprungliga indikationen, allergisk astma och rinit, delar den atopiska, allergiska inflammationen med eksem. En glukokortikoidmedierad mekanism är därför biologiskt rimlig.

Rimligheten är dock teoretisk. Inga studier av ciclesonide vid atopiskt eksem har identifierats, och inhalationsspray är inte en beredningsform som är anpassad för hudbehandling. Poängen 99,96 % är en modellförutsägelse och inte ett bevis på effekt.

Posterna "atopic eczema" och "dermatitis, atopic" (rang 1 och 3) beskriver samma sjukdom och bör slås ihop vid fortsatt granskning.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 64179 | Ciclesonide Orifarm | Inhalationsspray, lösning | Ej angiven (avregistrerad) |
| 21424 | Alvesco | Inhalationsspray, lösning | Ej angiven (avregistrerad) |
| 63699 | Ciclesonide Sandoz | Inhalationsspray, lösning | Ej angiven (avregistrerad) |
| 63698 | Ciclesonide Sandoz | Inhalationsspray, lösning | Ej angiven (avregistrerad) |
| 64178 | Ciclesonide Orifarm | Inhalationsspray, lösning | Ej angiven (avregistrerad) |

Totalt finns 9 godkännanden, och alla är avregistrerade. Tabellen visar de fem första.

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (kommer från TxGNN:s kunskapsgraf och inte från produktresumén): herpes simplex-keratit, binjurebarksinsufficiens, Addisons sjukdom, osteoporos, postmenopausal osteoporos, svampinfektioner, dermatofytos, okulär hypertension, glaukom och parasitinfektioner.
- **Läkemedelsinteraktioner**: totalt 63 interaktioner identifierades. De viktigaste är:
  - **Allvarlig (Major)**: kladribin.
  - **Måttlig (Moderate)**: klaritromycin, mikonazol, kobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, fostamatinib, konivaptan, inhalerat humant insulin och abametapir (lokalt). Flera av dessa är CYP3A4-hämmare, vilket kan öka den systemiska exponeringen för kortikosteroiden.
  - **Lindrig (Minor)**: formoterol, salbutamol och arformoterol.
- **Övrigt**: Kontaktdermatit orsakad av inhalerat budesonid med korsreaktivitet mot ciclesonide (fallrapport, 2012) pekar på en risk för överkänslighet inom kortikosteroidklassen. Vid kronisk bronkit/KOL är inhalerade kortikosteroider förknippade med ökad risk för pneumoni.

För varningar och kontraindikationer enligt produktresumén, se produktresumén, eftersom dessa uppgifter saknas i det sammanställda underlaget.

---

### Andra förutsagda indikationer (kort översikt)

| Förutsagd indikation | Poäng | Evidensnivå | Kommentar |
|------|------|------|------|
| 2-hydroxietylmetakrylat-sensibilisering | 99,76 % | L5 | Kontaktallergi av typ IV. Ingen evidens, och tillståndet är en sensibilisering snarare än en väldefinierad sjukdom. |
| Bronkit | 99,70 % | L4 | Endast en indirekt riktlinje om KOL (PMID [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/), 2015) utan ciclesonide-specifika data. |
| Kontaktdermatit | 99,25 % | L4 | Endast en fallrapport om allergi (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), 2012), som är en säkerhetssignal och inte bevis på nytta. |
| Astmarelaterade egenskaper (mottaglighet) | 99,13 % | L5 | Genetisk egenskap, inte en behandlingsbar indikation. Överlappar sannolikt med den befintliga astmaindikationen. |

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för atopiskt eksem saknar helt kliniska prövningar och litteratur (evidensnivå L5), och verkningsmekanismdata saknas i underlaget. Dessutom är samtliga svenska godkännanden avregistrerade, och produktresumésuppgifter om varningar och kontraindikationer saknas.

**För att gå vidare krävs:**
- Hämta och analysera produktresumén från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket är ett blockerande dataglapp för säkerhetsscreeningen.
- Komplettera verkningsmekanismen från DrugBank.
- Genomföra en systematisk litteratursökning och en sökning efter kliniska prövningar av ciclesonide vid atopiskt eksem.
- Utreda beredningsformens lämplighet, eftersom nuvarande produkter är inhalationssprayer och inte hudberedningar.
- Slå ihop de dubblerade posterna för atopiskt eksem och bedöma risken för kortikosteroidöverkänslighet och systemiska biverkningar.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

