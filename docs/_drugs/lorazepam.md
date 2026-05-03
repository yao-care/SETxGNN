---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Lorazepam
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

Jag har granskat Evidence Pack och den tillämpliga TxGNN-pipeline-skickligheten. Lorazepam är inte antineoplastiskt, saknar svenska godkännanden och har L5-evidens för toppindikationen. Jag genererar nu rapporten på svenska enligt rapportformatet v5.

---

# Lorazepam: Från ångestbehandling till trigeminusnervtumör

## Sammanfattning

Lorazepam är ett välkänt benzodiazepinläkemedel som används globalt vid ångeststörningar, sömnstörningar och kramper, men är inte registrerat i Sverige. TxGNN-modellen förutsäger att det kan vara effektivt mot **trigeminusnervtumör (trigeminal nerve neoplasm)** med en poäng på 99,87 %, men denna förutsägelse stöds av **0 kliniska prövningar** och **0 publikationer**. Den höga modellpoängen bedöms sannolikt bero på strukturell likhet i kunskapsgrafen snarare än en reell farmakologisk koppling, och rekommendationen är att avvakta.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige; globalt används lorazepam vid ångest, sömnlöshet och akuta kramper |
| Förutsagd ny indikation | Trigeminusnervtumör (trigeminal nerve neoplasm) |
| TxGNN-förutsägelsepoäng | 99,87 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta underlag. Baserat på känd farmakologi är lorazepam en positiv allosterisk modulator av GABA-A-receptorn: det binder till benzodiazepinbindningsstället och ökar receptorns känslighet för GABA, vilket ökar kloridjonflödet in i neuronen och dämpar neuronal aktivitet i centrala nervsystemet. Effekten är dosberoende och inkluderar ångestlindring, sedation, muskelrelaxation och antikonvulsiv verkan.

Kopplingen mellan GABA-A-modulering och tumörbiologi vid trigeminusnervtumörer är farmakologiskt svagt underbyggd. Trigeminusnervtumörer – typiskt schwannom eller meningeom – uppstår till följd av genetiska förändringar i Schwann-celler eller meningeala celler och drivs av mekanismer såsom NF2-mutationer eller kromosomala avvikelser. Det finns inga etablerade biologiska mekanismer som kopplar GABAerg aktivering till tillväxthämning av perifera nervsheathtumörer.

Den höga TxGNN-poängen (99,87 %) bedöms sannolikt vara ett resultat av så kallat graph embedding-brus: noden för "nervsystemtumörer" i kunskapsgrafen ligger strukturellt nära noder för etablerade benzodiazepinindikationer (epilepsi, ångest, sömnlöshet), utan att detta återspeglar en direkt biologisk länk. Lorazepam kan visserligen ordineras som symtomlindrande tillägg vid tumörrelaterad ångest eller smärtbehandling, men detta utgör inte läkemedelsåteranvändning i egentlig mening.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Lorazepam är inte godkänt för försäljning i Sverige. Inga produktgodkännanden finns registrerade hos Läkemedelsverket (MPA).

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivån är L5 (enbart modellförutsägelse) med noll kliniska prövningar och noll publikationer som direkt stöder lorazepam vid trigeminusnervtumör. Det saknas en biologiskt trovärdig mekanism, och den höga TxGNN-poängen bedöms sannolikt spegla graph embedding-brus snarare än en reell farmakologisk signal.

**För att gå vidare krävs:**
- Identifiering av en plausibel biologisk mekanism som kopplar GABA-A-modulering till trigeminusnervtumörers tillväxt eller överlevnad
- Minst en preklinisk studie (in vitro eller djurmodell) som visar antitumöral effekt hos lorazepam eller en strukturellt besläktad GABA-A-modulator
- Omprövning av alternativa högrankade indikationer med starkare evidens: **insomni (rank 2, L2-evidens, 23 kliniska prövningar och 18 publikationer)** och **mikturationsinducerade kramper (rank 7, L3-evidens, 20 publikationer)** utgör mer lovande kandidater för vidare utredning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

