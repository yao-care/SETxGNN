---
layout: default
title: Bupivacaine
parent: Endast modellprediktion (L5)
nav_order: 70
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Bupivacaine: predikterad ny indikation Akrodermatit chronica atrophicans (evidensnivå L5). Ursprunglig indikation: Dermatit (enligt kunskapsgrafen"
monitor_inn: "bupivacaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
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

# Bupivakain: Från dermatit till akrodermatit chronica atrophicans

---

## Sammanfattning

Bupivakain är ett lokalanestetikum av amidtyp. I den kunskapsgraf som ligger till grund för förutsägelsen är dess ursprungliga indikation **dermatit**. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **akrodermatit chronica atrophicans** med en hög modellpoäng (99,2 %). Det finns dock **inga kliniska prövningar och ingen litteratur** som stöder förutsägelsen, och något mekanistiskt samband har inte kunnat påvisas.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Dermatit (enligt kunskapsgrafen; godkännandena i Sverige saknar indikationstext) |
| Förutsagd ny indikation | Akrodermatit chronica atrophicans |
| TxGNN-förutsägelsepoäng | 99,2 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 15 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Det är allmänt känt att bupivakain blockerar spänningsstyrda natriumkanaler i nervceller och därigenom hämmar nervledning. Effekten är lokal smärtlindring.

Akrodermatit chronica atrophicans är den sena hudmanifestationen av borreliainfektion och behandlas med antibiotika. Ett lokalanestetikum påverkar varken infektionen eller den underliggande vävnadsförändringen. Något mekanistiskt samband är därför inte etablerat.

Den höga poängen (0,992) är sannolikt en grafbaserad förutsägelse som drivs av läkemedlets koppling till hudsjukdomar (dermatit) i kunskapsgrafen. Den bör inte tolkas som ett tecken på klinisk effekt.

Övriga förutsägelser med liknande höga poäng stöds inte heller av data:

| Förutsagd indikation | Poäng | Kommentar |
|---|---|---|
| Neonatal dermatomyosit | 99,1 % | Immunmedierad sjukdom. Bupivakain kan i bästa fall ge symtomlindring, och lokalanestetikas muskeltoxicitet talar emot användning vid myosit. |
| Sekundär interstitiell lungsjukdom hos barn vid bindvävssjukdom | 99,1 % | Inflammation och fibros påverkas inte av natriumkanalblockad. |
| Amyopatisk dermatomyosit | 99,0 % | Immunmedierad hudsjukdom. Ingen effekt förväntas på den underliggande immunpatologin. |

---

## Marknadsinformation Sverige

Alla 15 godkännanden är indragna och ingen indikationstext finns registrerad. De fem första visas nedan.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 60203 | Bupivacaine Noridem | Injektionsvätska, lösning | – |
| 57563 | Pankaine Spinal tung | Injektionsvätska, lösning | – |
| 9999 | Marcain spinal tung | Injektionsvätska, lösning | – |
| 8613 | Marcain | Injektionsvätska, lösning | – |
| 10255 | Marcain spinal | Injektionsvätska, lösning | – |

---

## Säkerhetsaspekter

**Läkemedelsinteraktioner** (56 registrerade, de viktigaste visas):
- Aprepitant (måttlig)
- Morfin, liposomalt (måttlig)
- Övriga identifierade interaktioner saknar graderad allvarlighet, bland annat pantoprazol, omeprazol, lansoprazol, vankomycin, atropin, kortikosteroider (triamcinolon, prednison, prednisolon, hydrokortison, dexametason), simvastatin, kaliumklorid, ondansetron, metoklopramid och naloxon.

**Sjukdomar där kunskapsgrafen anger kontraindikation** (inte hämtat från produktresumétext): bland annat hypertoni, leversvikt, leversjukdom, njursjukdom, epilepsi, svår KOL, andningssvikt, kranskärlssjukdom, hjärtinfarkt, förmaksflimmer, hjärtledningsrubbning, plötsligt hjärtstopp, hypotyreos, diabetes, diabetesketoacidos, inflammatorisk tarmsjukdom, benign prostatahyperplasi, trångvinkelglaukom, hemoglobinopati, kaliumbrist och substansberoende.

Varnings- och kontraindikationstext från produktresumén saknas i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en grafbaserad modell (evidensnivå L5) utan kliniska prövningar eller publikationer. Dessutom saknas ett rimligt mekanistiskt samband, och samtliga svenska godkännanden är indragna.

**För att gå vidare krävs:**
- Hämta och analysera produktresumé (varningar och kontraindikationer) från Läkemedelsverket, eftersom säkerhetsscreening inte kan genomföras utan dessa data.
- Komplettera verkningsmekanismdata, till exempel via DrugBank.
- Genomföra en systematisk litteratur- och prövningssökning för akrodermatit chronica atrophicans och bupivakain.
- Bedöma om en mekanistisk hypotes (till exempel symtomlindring av smärta eller klåda) är klinisk relevant, annars bör förutsägelsen avskrivas.
- Klargöra administreringsväg och beredningsform, eftersom befintliga beredningar är injektionsvätskor för spinal eller infiltrationsanvändning.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

