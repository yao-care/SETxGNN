---
layout: default
title: Tetracaine
parent: Endast modellprediktion (L5)
nav_order: 420
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Tetracaine: predikterad ny indikation Akrodermatit chronica atrophicans (evidensnivå L5). Ursprunglig indikation: Dermatit (enligt TxGNN-kunskapsgrafen"
monitor_inn: "tetracaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
---

# Tetracaine
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

## Tetrakain: Från dermatit till akrodermatit chronica atrophicans
{: .text-alpha }

---

### Sammanfattning

Tetrakain (tetrakain, INN: tetracaine) är ett lokalanestetikum som i datakällan är kopplat till dermatit som ursprunglig indikation. TxGNN-modellen förutsäger att det kan vara effektivt mot **akrodermatit chronica atrophicans** (en sen hudmanifestation av borrelia), men det finns **inga kliniska prövningar och ingen litteratur** som stöder denna förutsägelse. Förutsägelsen är enbart modellbaserad.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Dermatit (enligt TxGNN-kunskapsgrafen; ingen godkänd indikationstext finns i de svenska godkännandena) |
| Förutsagd ny indikation | Akrodermatit chronica atrophicans |
| TxGNN-förutsägelsepoäng | 99,93 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 3 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Tetrakain är ett lokalanestetikum av estertyp och verkar i allmänhet genom att blockera natriumkanaler i nerver. Dess effekt vid lokal smärtlindring är väl känd, men mekanistiskt finns inget känt samband med behandling av dermatit som sjukdom.

Akrodermatit chronica atrophicans är en sen hudmanifestation av borreliainfektion (Lyme) och behandlas med antibiotika. Tetrakain saknar antimikrobiell och sjukdomsmodifierande verkan, så ett rimligt mekanistiskt samband kan inte påvisas. Den höga poängen speglar sannolikt närhet i kunskapsgrafen till hudsjukdomar snarare än en verklig behandlingseffekt.

Bland övriga förutsägelser (t.ex. neonatal dermatomyosit, bronkit, irritabel tarm) saknas likaså stöd av studier. För akne keloid finns endast studier av tetrakain som bedövning vid lasergbehandling, och för cauda equina-syndrom beskriver litteraturen tetrakain som en möjlig orsak till skadan, inte som behandling.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

*Kommentar:* Den enda prövningen i materialet gäller en annan förutsagd indikation (akne keloid): [NCT02372786](https://clinicaltrials.gov/study/NCT02372786), fas 4, avslutad, 30 deltagare. Den jämförde lidokain/tetrakain-kräm med lidokain/prilokain-kräm för smärtlindring vid laserbehandling av acne keloidalis nuchae och tatueringsborttagning. Den undersöker bedövning vid ingreppet, inte behandling av sjukdomen.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 10080 | Tetrakain Bausch & Lomb | Ögondroppar, lösning i endosbehållare | Ingen indikationstext tillgänglig (indraget) |
| 22468 | Rapydan | Medicinskt plåster | Ingen indikationstext tillgänglig (indraget) |
| 57835 | Mekostest 36 | Plåster för provokationstest | Ingen indikationstext tillgänglig (indraget) |

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte produkttext): epilepsi, njursjukdom, leversjukdom, gallblåsesjukdom, hjärtsjukdom och hjärt-kärlsjukdom, plötsligt hjärtstopp, hjärtledningsstörningar, andningssvikt, myasthenia gravis och andra sjukdomar i nerv-muskelövergången, butyrylkolinesterasbrist, hypertyreos (inklusive Graves sjukdom och tyreotoxikos), samt ögonsjukdomar såsom uveit, irissjukdom, sjukdom i ciliarkroppen, ögoninfektioner och konjunktivit.
- **Läkemedelsinteraktioner** (32 identifierade, de viktigaste nedan):
  - *Allvarliga:* nitrit (salpetersyrlighet) och liposomalt bupivakain.
  - *Måttliga:* andra lokalanestetika (lidokain, bensokain, kokain, proparakain, oxibuprokain, cinkokain), bensodiazepiner (alprazolam, klordiazepoxid, klobazam, klonazepam, diazepam, estazolam), sulfasalazin och sulfametoxazol.
  - *Lindrig:* hyaluronidas.
- **Neurotoxicitet vid intratekal användning:** Litteraturen i materialet beskriver fall av cauda equina-syndrom efter spinalbedövning med tetrakain. Detta är en säkerhetssignal och inte en terapeutisk nytta.

Produktresumé med varningar och kontraindikationer har inte kunnat hämtas; se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en grafmodell (evidensnivå L5) och saknar både kliniska prövningar, litteratur och en rimlig verkningsmekanism. Tetrakain har dessutom inga aktiva godkännanden i Sverige i dag.

**För att gå vidare krävs:**
- Hämta verkningsmekanismen från DrugBank och bedöm om något mekanistiskt samband finns.
- Hämta och granska produktresumén (varningar och kontraindikationer) från Läkemedelsverket.
- Prekliniska eller kliniska data som visar effekt vid den förutsagda sjukdomen.
- Bedöma administreringsväg och beredningsform, då nuvarande godkännanden (ögondroppar, plåster) är indragna.
- Överväga om någon av de andra förutsagda indikationerna (t.ex. smärtlindring vid dermatologiska ingrepp) vore mer realistisk än den högst rankade.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

