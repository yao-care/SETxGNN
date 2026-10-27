---
layout: default
title: Glimepiride
parent: Endast modellprediktion (L5)
nav_order: 215
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Glimepiride: predikterad ny indikation Klassiskt stiff person-syndrom (evidensnivå L5). Ursprunglig indikation: Typ 2-diabetes mellitus (enligt kunskapsgrafen"
monitor_inn: "glimepiride"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **9** st
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

## Glimepirid: Från typ 2-diabetes till klassiskt stiff person-syndrom
{: .text-alpha }

---

### Sammanfattning

Glimepirid är ett sulfonureiderivat som ursprungligen används för behandling av typ 2-diabetes mellitus. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **klassiskt stiff person-syndrom**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder denna riktning. Förutsägelsen bygger enbart på modellberäkningar och bedöms som mycket osäker.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Typ 2-diabetes mellitus (enligt kunskapsgrafen; ingen indikationstext finns i de svenska godkännandena) |
| Förutsagd ny indikation | Klassiskt stiff person-syndrom |
| TxGNN-förutsägelsepoäng | 99,7 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 11 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för rapporten. Baserat på allmänt känd information är glimepirid ett sulfonureid som blockerar ATP-känsliga kaliumkanaler i betacellerna i bukspottkörteln och därmed ökar insulinfrisättningen.

Kopplingen till stiff person-syndrom är sannolikt indirekt. Sjukdomen är en autoimmun neurologisk störning med anti-GAD65-antikroppar som påverkar GABA-signalering, och den förekommer ofta tillsammans med typ 2-diabetes och andra autoimmuna former av diabetes. Den höga poängen speglar därför sannolikt närheten mellan sjukdomarna i kunskapsgrafen, inte en terapeutisk mekanism.

Det finns alltså ingen mekanistisk grund för att blockad av K-ATP-kanaler i betaceller skulle lindra stelhet och muskelspasmer vid stiff person-syndrom. Förutsägelsen bör därför ses som en statistisk artefakt snarare än en tillförlitlig hypotes. Samma resonemang gäller även fokalt stiff limb-syndrom, som har identisk poäng.

---

### Marknadsinformation Sverige

Samtliga 11 godkännanden är indragna och inget är för närvarande giltigt. Fem av dem visas nedan. Indikationstext saknas i dessa godkännanden.

| Godkännandenummer | Produktnamn | Beredningsform | Tillverkare | Status |
|---------|------|------|-----------|-----|
| 26270 | Glimepirid Bluefish | Tablett | Bluefish Pharmaceuticals AB | Indraget |
| 22683 | Glimepirid STADA | Tablett | STADA Arzneimittel AG | Indraget |
| 26271 | Glimepirid Bluefish | Tablett | Bluefish Pharmaceuticals AB | Indraget |
| 22681 | Glimepirid Actavis | Tablett | Actavis Group PTC ehf. | Indraget |
| 22679 | Glimepirid Actavis | Tablett | Actavis Group PTC ehf. | Indraget |

---

### Säkerhetsaspekter

- **Sjukdomar som kunskapsgrafen kopplar till kontraindikation**: Njursjukdom, leversjukdom, gallblåsesjukdom, hjärtsvikt, hypofysinsufficiens (inklusive tillväxthormonbrist och hypogonadotrop hypogonadism), osteoporos samt infektionssjukdom. Uppgifterna kommer från kunskapsgrafen och inte från produktresumén, och de bör verifieras.
- **Läkemedelsinteraktioner**: Totalt 599 interaktioner har identifierats. Exempel på måttliga interaktioner:
  - Betablockerare (t.ex. acebutolol), som kan dölja symtom på hypoglykemi
  - Sympatomimetika (t.ex. adrenalin, fenylefrin, pseudoefedrin, salbutamol, formoterol)
  - NSAID-preparat (t.ex. ibuprofen, ketorolak)
  - Histamin-H2-blockerare (famotidin, ranitidin)
  - Hydroklortiazid, acetazolamid, hydrokortison, etinylestradiol
  - Albiglutid, acitretin, nitazoxanid
  - Etanol

  Lätta interaktioner gäller bland annat topikalt hydrokortison och topikalt alklometason.

Uppgifter om varningar och kontraindikationer från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar både kliniskt och mekanistiskt stöd (evidensnivå L5). Dessutom är alla svenska godkännanden indragna, och den troliga förklaringen till den höga poängen är sambandet mellan diabetes och GAD-relaterad autoimmunitet.

**För att gå vidare krävs:**
- Verkningsmekanismen från DrugBank, för att kunna analysera ett eventuellt mekanistiskt samband.
- Varningar och kontraindikationer från produktresumén hos Läkemedelsverket (MPA) för en fullständig säkerhetsbedömning.
- Prekliniska data eller publicerade fallstudier som visar en möjlig effekt vid stiff person-syndrom.
- Bedömning av om andra förutsägelser på listan (t.ex. tiaminresponsivt syndrom, där diabetes ingår i symtombilden) är mer relevanta än den högst rankade. Ingen av dem har dock något kliniskt stöd i nuläget.
- Klargörande av marknadsstatus, eftersom inget giltigt godkännande för glimepirid finns i Sverige.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

