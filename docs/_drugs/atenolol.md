---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **9** st
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

Skill lastad. `txgnn-pipeline` innehåller inga specifika instruktioner för rapportgenerering — arbetsflödet och formatet är redan fullt definierat i systempromten. Jag går vidare och genererar rapporten baserat på Evidence Pack.

---

# Atenolol: Från akut hjärtinfarkt till posterolateral hjärtinfarkt

---

## Sammanfattning

Atenolol är en kardioselektiv β1-adrenerg blockerare (betablockerare) med välbelagd effekt vid akut hjärtinfarkt, bland annat bekräftad i den stora ISIS-1-studien (n ≈ 16 000). TxGNN-modellen förutsäger att det kan vara effektivt mot **posterolateral hjärtinfarkt** (posterolateral myocardial infarction), en anatomisk subtyp av akut MI. Förutsägelsen stöds av ett mycket högt TxGNN-poäng på **99,87 %** och stark mekanistisk plausibilitet, men direkta kliniska prövningar och publikationer specifikt för denna anatomiska subtyp saknas för närvarande.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige |
| Förutsagd ny indikation | Posterolateral hjärtinfarkt (posterolateral myocardial infarction) |
| TxGNN-förutsägelsepoäng | 99,87 % |
| Evidensnivå | L4 – Mekanistiska studier / indirekt klassextrapolering |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i datakällan. Baserat på känd information är atenolol en β1-selektiv adrenerg antagonist som blockerar β1-receptorer i hjärtat och i de juxtaglomerulära cellerna i njuren. Effekten inkluderar sänkt hjärtfrekvens (negativ kronotrop), minskad kontraktilitet (negativ inotrop) och reducerat minutvolym – vilket sammantaget minskar hjärtmuskulaturens syreförbrukning och begränsar ischemisk skada.

Posterolateral hjärtinfarkt är en anatomisk subtyp av akut MI som drabbar vänster kammares posterolaterala vägg, typiskt försörjd av höger koronärartären (RCA) eller den cirkumflexa artären. Den grundläggande patofysiologin – ischemisk myokardskada till följd av otillräcklig syretillförsel – är identisk med alla MI-subtyper. β1-blockad minskar hjärtats syrebehov, bromsar infarktutbredning och reducerar risken för maligna arytmier under det akuta skedet såväl som vid sekundärprevention.

ISIS-1 är en landmärkesstudie som påvisade signifikant mortalitetsminskning med intravenöst atenolol vid akut MI. Posterolateral MI är en anatomisk avgränsning – inte en skild patofysiologisk entitet – varför mekanismen och den terapeutiska logiken är fullt tillämpbar. Att direkta prövningar saknas för just denna subtyp beror sannolikt på att klassiska RCT och registerdata traditionellt inte stratifierar efter exakt infarktlokal.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
TxGNN-förutsägelsepoängen är mycket hög (99,87 %) och mekanistisk plausibilitet är stark – β1-blockad vid akut MI är väletablerat i storskaliga RCT. Posterolateral MI är dock en anatomisk subtyp för vilken direkta prövningsdata saknas, och den fullständiga säkerhetsprofilen i denna specifika population behöver verifieras innan vidare åtgärder.

**För att gå vidare krävs:**
- Inhämta detaljerad verkningsmekanismdata (MOA) via DrugBank API (DB00335)
- Hämta och granska produktresumé (SmPC) för att fastställa kontraindikationer och viktiga varningar
- Genomföra systematisk litteratursökning av β-blockerare vid anatomiska MI-subtyper (posterolateral, posteroinferior, septal)
- Bedöma interaktioner med övriga hjärtläkemedel (antikoagulantia, trombocythämmare, antiarytmika)
- Konsultera kardiolog för klinisk relevans- och genomförbarhetsbedömning av registreringsstrategi i Sverige
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

