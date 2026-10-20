---
layout: default
title: Rabeprazole
parent: Endast modellprediktion (L5)
nav_order: 373
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Rabeprazole: predikterad ny indikation Smouldering systemisk mastocytos (evidensnivå L5). Ursprunglig indikation: Ingen godkänd indikationstext finns i svenska licensdata. Enligt kuns…"
monitor_inn: "rabeprazole"
predicted_indications: ["lymphoadenopathic mastocytosis with eosinophilia"]
---

# Rabeprazole
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

# Rabeprazol: Från peptisk ulcussjukdom och gastroesofageal refluxsjukdom till smouldering systemisk mastocytos

---

## Sammanfattning

Rabeprazol är en protonpumpshämmare som i den data som sammanställts för denna rapport är kopplad till syrarelaterade sjukdomar i magtarmkanalen, bland annat peptisk ulcussjukdom, gastroesofageal refluxsjukdom och Zollinger-Ellisons syndrom. Dessutom finns mastocytos och systemisk mastocytos bland läkemedlets kända indikationer i kunskapsgrafen.
TxGNN-modellen förutsäger att det kan vara effektivt mot **smouldering systemisk mastocytos**, men det finns **0 kliniska prövningar** och **0 publikationer** som stöder denna riktning. Förutsägelsen bygger enbart på modellen.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen godkänd indikationstext finns i svenska licensdata. Enligt kunskapsgrafen: peptisk ulcussjukdom, gastroesofageal refluxsjukdom, esofagit, duodenalsår, Zollinger-Ellisons syndrom m.fl. |
| Förutsagd ny indikation | Smouldering systemisk mastocytos |
| TxGNN-förutsägelsepoäng | 99,4 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 (båda indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på allmän kunskap är rabeprazol en protonpumpshämmare, och dess effekt på syrarelaterade sjukdomar är väl känd. Mekanistiskt kan den vara tillämpbar vid symtom från magsyraöverproduktion vid mastocytos. Denna koppling bygger på allmän kunskap om protonpumpshämmare och har inte kunnat verifieras i den data som sammanställts.

Vid mastocytos frisätter mastceller histamin, vilket kan driva upp magsyraproduktionen. Rabeprazol har redan mastocytos och systemisk mastocytos bland sina indikationer i kunskapsgrafen. Smouldering systemisk mastocytos är en undertyp av systemisk mastocytos, och den höga poängen (0,994) speglar sannolikt just denna närhet i grafen.

Den troliga rollen är symtomlindring av syrarelaterade magtarmbesvär, inte behandling av den underliggande sjukdomen i form av en klonal mastcellssjukdom. Inga studier eller publikationer har lämnats som visar en sjukdomsspecifik effekt.

**Ytterligare förutsägelse (rang 2):** Lymfadenopatisk mastocytos med eosinofili (poäng 99,3 %) har samma typ av koppling och samma begränsningar. En eventuell nytta skulle gälla symtomlindring av syrarelaterade besvär, inte lymfadenopati eller eosinofili som kännetecknar denna undertyp. Heller inte här finns några studier eller publikationer.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation | Status |
|---------|------|------|-----------|------|
| 14696 | Pariet | Enterotablett | Ingen indikationstext angiven | Indragen |
| 14697 | Pariet | Enterotablett | Ingen indikationstext angiven | Indragen |

Tillverkare: Eisai AB. Ingen av produkterna har ett giltigt godkännande i Sverige idag.

---

## Säkerhetsaspekter

- **Sjukdomar som i kunskapsgrafen är kopplade till kontraindikation** (hämtat från kunskapsgrafen, inte från produktresumétext): leversjukdom, gallblåsesjukdom, osteoporos, postmenopausal osteoporos och benfraktur.
- **Läkemedelsinteraktioner:** Totalt 486 interaktioner har identifierats. Exempel på de som klassats som stora (Major):
  - Acalabrutinib
  - Atazanavir

  Exempel på måttliga (Moderate) interaktioner: amikacin, amfetamin, amfotericin B (flera beredningar), aprepitant, armodafinil, bosutinib, apalutamid och tiaziddiuretika (bendroflumetiazid, benztiazid).

  Exempel på lindrig (Minor) interaktion: acetylsalicylsyra, axitinib.

  Listan är ett urval av de första posterna och är inte fullständig.

Varnings- och kontraindikationstext från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds enbart av modellen (L5), utan kliniska prövningar eller litteratur. Den troliga nyttan är begränsad till symtomlindring av syrarelaterade besvär och gäller inte själva mastocytosen.
- Rabeprazol saknar dessutom giltigt godkännande i Sverige, och produktresumédata för säkerhetsbedömning saknas.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) och sammanställa varningar och kontraindikationer. Detta är ett blockerande datagap för säkerhetsgranskning.
- Hämta verkningsmekanismdata från DrugBank för att kunna analysera den mekanistiska kopplingen.
- Genomföra litteratursökning och sökning efter kliniska prövningar om protonpumpshämmare vid (smouldering) systemisk mastocytos.
- Klargöra om rabeprazol är tillgängligt i Sverige, eftersom båda godkännandena är indragna, samt om andra protonpumpshämmare redan används för samma symtom.
- Bedöma de kontraindikationsrelaterade sjukdomarna i kunskapsgrafen (osteoporos och benfraktur), särskilt relevant eftersom osteoporos är vanligt vid systemisk mastocytos.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

