---
noindex: true
sitemap: false
layout: default
title: Linagliptin
parent: Endast modellprediktion (L5)
nav_order: 81
evidence_level: L5
indication_count: 0
last_modified_at: 2026-10-30
predicted_indications: []
---

# Linagliptin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **0** st
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

## Linagliptin: Läkemedel mot typ 2-diabetes — inga repositioneringskandidater identifierade
{: .text-alpha }

---

## Sammanfattning

Linagliptin (DB08882) är en väletablerad DPP-4-hämmare som ursprungligen godkändes för behandling av typ 2-diabetes. TxGNN-modellen gav dock **inga förutsagda nya indikationer** för detta läkemedel i det nuvarande underlaget. Bedömningen kan inte gå vidare till analys på indikationsnivå förrän förutsägelseflödet har körts om och evidensdata har fyllts i.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Typ 2-diabetes (DPP-4-hämmarklassen) |
| Förutsagd ny indikation | Ingen identifierad (predicted_indications: tom) |
| TxGNN-förutsägelsepoäng | Ej tillämpligt |
| Evidensnivå | L5 — endast modellprediktion; inget resultat returnerades |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 13 av 13) |
| Antal godkännanden | 13 (giltiga: 13) |
| Rekommenderat beslut | **Avvakta** |

---

## Varför är denna förutsägelse rimlig?

Ingen repositioneringsförutsägelse finns i det nuvarande underlaget. Fältet `predicted_indications` är tomt, vilket betyder att TxGNN-modellen antingen inte gav någon rankad utdata för Linagliptin, eller att flödet inte slutfördes för denna kandidat.

Även data om verkningsmekanism är markerade som en datalucka. Utifrån kunskap om läkemedelsklassen är Linagliptin en selektiv, kompetitiv hämmare av dipeptidylpeptidas-4 (DPP-4), som förlänger verkan av inkretinhormonerna (GLP-1 och GIP) och därmed stimulerar glukosberoende insulinfrisättning. Huruvida denna mekanism kan överföras till andra indikationer (t.ex. icke-alkoholisk fettleversjukdom, hjärtsvikt, njurskydd) är en rimlig hypotes som har undersökts i publicerad litteratur — men **det finns för närvarande ingen modellbaserad förutsägelse att bedöma**.

Utan en förutsägelse från TxGNN kan denna rapport inte göra resonemang på indikationsnivå, kartläggning av kliniska prövningar eller koppling till litteratur.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande — det finns ingen förutsagd indikation att koppla evidens till.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande — det finns ingen förutsagd indikation att förankra en litteraturgenomgång i.

---

## Marknadsinformation Sverige

Inga godkännanden registrerade i det nuvarande datasetet. Sökningen mot TFDA (sök-ID: 1) gav 0 resultat, och inga godkännandeposter finns i `taiwan_regulatory.licenses`.

> **Obs:** Linagliptin finns kommersiellt tillgängligt på flera marknader under varumärken som Tradjenta (Boehringer Ingelheim / Eli Lilly). Att poster saknas här kan bero på en datalucka i den aktuella körningen snarare än på att läkemedlet faktiskt saknas på marknaden. Korskontroll mot databaserna hos Läkemedelsverket (MPA) och TFDA rekommenderas.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> Alla säkerhetsfält (viktiga varningar, kontraindikationer, läkemedelsinteraktioner) returnerades som dataluckor eller tomma i detta underlag. Sökningen efter läkemedelsinteraktioner gav `not_found` med 0 registrerade interaktioner.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
TxGNN-förutsägelseflödet gav inga kandidatindikationer för Linagliptin, vilket gör det omöjligt att bedöma möjligheten till repositionering. Ingen poängsättning, evidenstriangulering eller säkerhetskartläggning kan genomföras i detta skede.

**För att gå vidare krävs:**

- **Kör om TxGNN-förutsägelseflödet** för DB08882 och kontrollera att `predicted_indications` innehåller minst en poängsatt kandidat
- **Hämta verkningsmekanismdata** från DrugBanks API (datalucka DG002) för att möjliggöra resonemang från mekanism till indikation
- **Hämta varningar och kontraindikationer ur TFDA:s produktresumé** (datalucka DG001, blockerar för närvarande säkerhetsscreening S1)
- **Verifiera marknadsstatus** direkt mot Läkemedelsverket (MPA, Sverige) och TFDA (Taiwan) — den nuvarande uppgiften om 0 godkännanden stämmer inte med känd global tillgänglighet
- **Kör om sökningen efter läkemedelsinteraktioner** med en alternativ källa (t.ex. DrugBanks interaktionsendpoint eller Drugs@FDA), eftersom den nuvarande sökningen gav `not_found`
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

