---
layout: default
title: Sevoflurane
parent: Endast modellprediktion (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sevoflurane: predikterad ny indikation Prinzmetals angina (evidensnivå L5). Ursprunglig indikation: Ej angiven i de data som sammanställts för rapporten (indikationstext…"
monitor_inn: "sevoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
---

# Sevoflurane
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

# Sevofluran: Från allmän anestesi (inhalationsnarkos) till Prinzmetals angina

## Sammanfattning

Sevofluran är en inhalationsanestetika (narkosgas) som har använts för att söva patienter vid kirurgi. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Prinzmetals angina** (poäng 99,8 %), men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder denna riktning. Förutsägelsen bygger enbart på modellen.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i de data som sammanställts för rapporten (indikationstexten saknas för alla godkännanden) |
| Förutsagd ny indikation | Prinzmetals angina |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 6 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Sevofluran är en flyktig anestetika som i allmänhet anses förstärka GABA-A-receptorer och påverka andra jonkanaler. Dess effekt vid generell anestesi är väletablerad, men något mekanistiskt samband med Prinzmetals angina är inte belagt i underlaget.

Ett möjligt, men spekulativt, samband är att flyktiga anestetika kan ha kärlvidgande effekter och påverka kalciumkanaler i kärlens glatta muskulatur. Prinzmetals angina orsakas av kramp i kranskärlen (koronar vasospasm), så en sådan effekt skulle kunna vara relevant i teorin.

Samtidigt är sevofluran en inhalationsgas som ges under övervakning vid narkos. Långvarig eller upprepad användning vid en kronisk sjukdom är opraktisk. Det finns heller inga studier som visar nytta. Förutsägelsen bör därför ses som en hypotes och inte som ett belägg.

---

## Marknadsinformation Sverige

Alla sex godkännanden är indragna och inget är i dagsläget giltigt. Indikationstexten saknas i de data som sammanställts.

| Godkännandenummer | Produktnamn | Beredningsform | Tillverkare | Status |
|---------|------|------|-----|-----------|
| 64635 | Sevorane | Inhalationsånga, vätska | Orifarm AB | Indraget |
| 60134 | Sevorane | Inhalationsånga, vätska | Orifarm AB | Indraget |
| 22339 | Sevofluran Baxter | Inhalationsånga, vätska | Baxter Medical AB | Indraget |
| 67689 | Sevorane | Inhalationsånga, vätska | Orifarm AB | Indraget |
| 12332 | Sevorane | Inhalationsånga, vätska | AbbVie AB | Indraget |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgraf (inte produktresumé)**: Modellens kunskapsgraf kopplar sevofluran till följande tillstånd där läkemedlet bör undvikas eller användas med stor försiktighet: epilepsi, njursjukdom, leversjukdom, gallblåsesjukdom, lågt blodtryck, malign hypertermi (inklusive ansträngningsutlöst), pseudotumor cerebri, förhöjt intrakraniellt tryck, muskeldystrofi (Duchennes och Beckers), pyouretär samt proteinuri.
- **Läkemedelsinteraktioner**: Totalt 146 interaktioner har identifierats. Exempel på **allvarliga (Major)** interaktioner:
  - Adrenalin (epinefrin)
  - Dolasetron
  - Cisaprid

  Exempel på **måttliga (Moderate)** interaktioner: famotidin, morfin, klaritromycin, levofloxacin, ondansetron, palonosetron och exenatid. Metronidazol har en **lindrig (Minor)** interaktion.

Uppgifter om varningar och kontraindikationer från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för Prinzmetals angina bygger enbart på modellen (evidensnivå L5), utan kliniska prövningar eller litteratur. Dessutom är samtliga svenska godkännanden indragna, och läkemedlets användning som narkosgas passar dåligt för en kronisk kärlsjukdom.

**För att gå vidare krävs:**
- Hämta och granska produktresumén för varningar och kontraindikationer.
- Komplettera verkningsmekanismen (t.ex. via DrugBank).
- Genomföra prekliniska studier eller mekanismstudier av effekter på koronar vasospasm.
- Bedöma administreringsväg och praktisk genomförbarhet för en kronisk indikation.

---

## Övriga förutsagda indikationer (kort översikt)

Modellen förutsäger även andra indikationer. För ingen av dem finns kliniskt stöd för behandlingseffekt.

| Rang | Förutsagd indikation | TxGNN-poäng | Evidensnivå | Kommentar |
|------|------|------|------|------|
| 2 | Tourettes syndrom | 99,5 % | L5 | Ingen evidens; mekanistiskt avlägset |
| 3 | Fibromyalgi | 99,4 % | L4 | Endast en fallrapport om narkoshantering (PMID [26419112](https://pubmed.ncbi.nlm.nih.gov/26419112/)) |
| 4 | Tendinit | 99,4 % | L4 | Nio perioperativa narkosstudier, ingen behandlingsstudie |
| 5 | Myositis fibrosa | 99,4 % | L5 | Ingen evidens |
| 6 | Idiopatisk granulomatös myosit | 99,4 % | L5 | Identisk poäng som rang 5, möjligen en grafartefakt |
| 7 | Nefrogent syndrom med olämplig antidures | 99,4 % | L5 | Inget rimligt mekanistiskt samband |
| 8 | Trikotillomani | 99,3 % | L5 | Ingen evidens |
| 9 | Migrän | 99,2 % | L4 | Endast en studie om narkos vid MR hos barn (PMID [31852450](https://pubmed.ncbi.nlm.nih.gov/31852450/)) |
| 10 | Inklusionskroppsmyosit | 99,1 % | L4 | Endast en fallrapport om narkoshantering (PMID [27247916](https://pubmed.ncbi.nlm.nih.gov/27247916/)) |

Publikationerna för fibromyalgi, tendinit, migrän och inklusionskroppsmyosit beskriver narkos under kirurgi eller undersökningar. Ingen av dem visar att sevofluran behandlar sjukdomen.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

