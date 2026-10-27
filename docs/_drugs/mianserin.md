---
layout: default
title: Mianserin
parent: Endast modellprediktion (L5)
nav_order: 291
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Mianserin: predikterad ny indikation Benign paroxysmal torticollis hos spädbarn (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext finns i de svenska godkännandena. Enligt kunska…"
monitor_inn: "mianserin"
predicted_indications: ["benign paroxysmal torticollis of infancy", "dysthymic disorder", "agoraphobia", "Ohdo syndrome and variants", "melancholia", "neurotic disorder"]
---

# Mianserin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

## Mianserin: Från unipolär depression till benign paroxysmal torticollis hos spädbarn
{: .text-alpha }

---

### Sammanfattning

Mianserin är ett tetracykliskt antidepressivt läkemedel som ursprungligen användes för att behandla unipolär depression, endogen depression, egentlig depression och ångestsyndrom.
TxGNN-modellen förutsäger att det kan vara effektivt mot **benign paroxysmal torticollis hos spädbarn**, med mycket hög modellpoäng (99,5 %) men **0 kliniska prövningar** och **0 publikationer** som stöder just denna riktning. Förutsägelsen är därför enbart en beräkningsmässig hypotes.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext finns i de svenska godkännandena. Enligt kunskapsgrafen: unipolär depression, endogen depression, egentlig depression och ångestsyndrom |
| Förutsagd ny indikation | Benign paroxysmal torticollis hos spädbarn |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast återkallade godkännanden |
| Antal godkännanden | 9 (alla återkallade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är mianserin ett tetracykliskt antidepressivt läkemedel vars effekt vid depression är väl dokumenterad. Farmakologiska data visar att mianserin binder till flera serotoninreceptorer (5-HT1B, 5-HT2A, 5-HT2B, 5-HT2C, 5-HT6, 5-HT7), alfa-1-adrenoreceptorer (1A, 1B, 1D), LPA1-receptorn och noradrenalintransportören (NET).

Benign paroxysmal torticollis hos spädbarn är en barnneurologisk sjukdom som ofta kopplas till kanalopati (bland annat CACNA1A) och står nära migränspektrumet. Mianserins blockad av 5-HT2-receptorer och dess antihistaminerga effekt ger endast en spekulativ koppling till detta tillstånd.

Det finns alltså inget stöd i kliniska prövningar eller litteratur. Den höga poängen är en modellprediktion. Att målgruppen är spädbarn och att läkemedlet saknar giltigt godkännande i Sverige ökar dessutom säkerhetsfrågorna.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 65740 | Mianserin Ebb | Filmdragerad tablett | Ingen indikationstext tillgänglig (återkallat) |
| 58086 | Mianserin Viatris | Filmdragerad tablett | Ingen indikationstext tillgänglig (återkallat) |
| 12850 | Mianserin Viatris | Filmdragerad tablett | Ingen indikationstext tillgänglig (återkallat) |
| 56510 | Mianserin 2care4 | Filmdragerad tablett | Ingen indikationstext tillgänglig (återkallat) |
| 12014 | Mianserin Viatris | Filmdragerad tablett | Ingen indikationstext tillgänglig (återkallat) |

Totalt finns 9 godkännanden, alla återkallade. Ytterligare fyra godkännanden (58008, 57435, 65741 och 12015) visas inte här.

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Interaktionsfrågan slutfördes och gav 11 poster. Dessa är farmakologiska målstrukturer och inte interaktioner med andra läkemedel. De viktigaste är serotoninreceptorerna 5-HT1B, 5-HT2A, 5-HT2B, 5-HT2C, 5-HT6 och 5-HT7, alfa-1-adrenoreceptorerna (1A, 1B, 1D), LPA1-receptorn och noradrenalintransportören (NET). Inga interaktionsnivåer är angivna.

Uppgifter om varningar och kontraindikationer saknas. Se produktresumén för fullständig säkerhetsinformation. Eftersom den föreslagna patientgruppen är spädbarn krävs särskilt noggrann säkerhetsbedömning.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellpoängen. Det finns inga kliniska prövningar, ingen litteratur och ingen etablerad mekanistisk koppling. Läkemedlet saknar dessutom giltigt godkännande i Sverige och den tänkta patientgruppen är spädbarn.

**För att gå vidare krävs:**
- Hämta och granska produktresumén (varningar och kontraindikationer), vilket i nuläget blockerar säkerhetsbedömningen.
- Komplettera verkningsmekanismdata från DrugBank.
- Genomföra en riktad litteraturgenomgång om mianserin och paroxysmala rörelsestörningar eller migränspektrumet hos barn.
- Utvärdera säkerhet och lämplighet hos barn före varje vidare prekliniskt eller kliniskt arbete.

---

### Alternativa kandidater värda att notera

Andra förutsägelser har starkare litteraturstöd, men de ligger nära mianserins ursprungliga depressionsindikationer och är därför i praktiken inte någon verklig återanvändning:

| Förutsagd indikation | Poäng | Evidensnivå | Kommentar |
|------|------|------|------|
| Neurotisk sjukdom | 99,0 % | L3 | Mest mianserinspecifik litteratur, bland annat jämförande studier mot klomipramin och imipramin |
| Melankoli | 99,2 % | L4 | Motsvarar endogen depression, alltså nära en befintlig indikation |
| Neurotisk depression | 99,2 % | L4 | Föråldrad diagnosterm, indirekt evidens |
| Dysthymi | 99,4 % | L4 | Endast metaanalys på läkemedelsklassnivå |
| Agorafobi | 99,4 % | L4 | Ingen direkt evidens för mianserin |
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

