---
layout: default
title: Alteplase
parent: Endast modellprediktion (L5)
nav_order: 25
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Alteplase: predikterad ny indikation Posterolateral hjärtinfarkt (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext finns i de svenska godkännandena. Enligt kunska…"
monitor_inn: "alteplase"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
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

# Alteplas: Från lungemboli och hjärtinfarkt till posterolateral hjärtinfarkt

---

## Sammanfattning

Alteplas (Actilyse) är ett trombolytiskt läkemedel som enligt kunskapsgrafen ursprungligen används vid bland annat hjärtinfarkt, lungemboli och ischemisk stroke. TxGNN-modellen förutsäger att det kan vara effektivt mot **posterolateral hjärtinfarkt**, men **inga kliniska prövningar och ingen publicerad litteratur** har hittats för just denna diagnos. Förutsägelsen är i praktiken en undertyp av en redan etablerad indikation, inte en egentlig ny användning.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext finns i de svenska godkännandena. Enligt kunskapsgrafen: lungemboli, hjärtinfarkt, kranskärlstrombos och stroke |
| Förutsagd ny indikation | Posterolateral hjärtinfarkt |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 (endast modellförutsägelse, inga studier för denna diagnos) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 5 (samtliga avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Baserat på känd information är alteplas en rekombinant vävnadsplasminogenaktivator (tPA). Den omvandlar plasminogen till plasmin på fibrinytan och löser därigenom upp blodproppar. Effekten vid hjärtinfarkt är väl dokumenterad, och mekanistiskt kan den vara tillämpbar på posterolateral hjärtinfarkt.

Posterolateral hjärtinfarkt beskriver var i hjärtmuskeln infarkten sitter, inte en annan sjukdomsmekanism. Orsaken är i regel en propp i ett kranskärl, och proppupplösningen fungerar likadant oavsett infarktområde. Den höga poängen speglar därför sannolikt släktskapet med den övergripande diagnosen hjärtinfarkt, inte självständig evidens för just denna undertyp. Detsamma gäller den närliggande diagnosen posteroinferior hjärtinfarkt, som fick samma poäng.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Alla fem godkännanden är avregistrerade, och ingen indikationstext finns angiven i dem.

| Godkännandenummer | Produktnamn | Beredningsform | Tillverkare | Status |
|---------|------|------|-----------|-----------|
| 68998 | Actilyse | Pulver och vätska till injektions-/infusionsvätska, lösning | Orifarm AB | Avregistrerad |
| 68997 | Actilyse | Pulver och vätska till injektions-/infusionsvätska, lösning | Orifarm AB | Avregistrerad |
| 49994 | Actilyse | Pulver och vätska till injektions-/infusionsvätska, lösning | Orifarm AB | Avregistrerad |
| 44422 | Actilyse | Pulver till injektions-/infusionsvätska, lösning | Boehringer Ingelheim International GmbH | Avregistrerad |
| 11137 | Actilyse | Pulver och vätska till injektions-/infusionsvätska, lösning | Boehringer Ingelheim International GmbH | Avregistrerad |

---

## Säkerhetsaspekter

**Läkemedelsinteraktioner:** 140 interaktioner är registrerade. De viktigaste är främst läkemedel som påverkar blodets koagulation eller trombocytfunktion, där blödningsrisken kan öka.

- **Allvarliga (Major):** abciximab, apixaban, fondaparinux, anisindion, acalabrutinib, deferasirox, ibritumomab tiuxetan, tositumomab (även I-131-märkt)
- **Måttliga (Moderate):** acetylsalicylsyra, ibuprofen, ketorolak (även ögonpreparat), fluvoxamin, fosinopril, aminokapronsyra, aprotinin, fenfluramin, dexfenfluramin, sibutramin

Varnings- och kontraindikationsdata saknas i det underlag som sammanställts. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen avser en anatomisk undertyp av hjärtinfarkt, som redan är en etablerad indikation för alteplas, och det finns ingen självständig evidens för just posterolateral hjärtinfarkt.
- Alla svenska godkännanden är avregistrerade och saknar indikationstext, så ingen aktuell marknadsföring eller godkänd användning kan bekräftas i Sverige.

**För att gå vidare krävs:**
- Verifiering av gällande indikationer och status för alteplas i Sverige, till exempel via produktresumé och MPA, eftersom godkännandena saknar indikationstext och är avregistrerade.
- Hämtning av produktresumé med varningar och kontraindikationer.
- Hämtning av detaljerad verkningsmekanismdata från DrugBank.
- Bedömning av om undertypen tillför något utöver den redan etablerade hjärtinfarktindikationen. Om inte bör fokus flyttas till kandidater med mer evidens.
- Av de övriga förutsagda indikationerna har **trombofili** (en pågående fas 2-prövning, NCT05540834, samt fallrapporter) och **kranskärlsstenos** (bland annat en dubbelblind randomiserad studie, PMID 8299637, och flera kliniska studier) mer underlag. Båda är dock fortfarande på forskningsfrågenivå. Evidensen för kranskärlsstenos rör huvudsakligen hjärtinfarkt och instabil angina, och modern praxis föredrar PCI.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

