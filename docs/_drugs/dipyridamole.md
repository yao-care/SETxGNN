---
layout: default
title: Dipyridamole
parent: Endast modellprediktion (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dipyridamole: predikterad ny indikation Prinzmetals angina (evidensnivå L5). Ursprunglig indikation: Förmaksflimmer (de svenska godkännandena saknar indikationstext…"
monitor_inn: "dipyridamole"
predicted_indications: ["stroke disorder", "thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
---

# Dipyridamole
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

## Dipyridamol: Från förmaksflimmer till Prinzmetals angina
{: .text-alpha }

---

## Sammanfattning

Dipyridamol är ett trombocythämmande och kärlvidgande läkemedel. Enligt de data som sammanställts för rapporten är dess ursprungliga indikation **förmaksflimmer**. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt vid **Prinzmetals angina** (vasospastisk angina), men det finns **inga kliniska prövningar** och bara **10 publikationer**, varav ingen visar behandlingsnytta. Flera av dem pekar snarare mot en möjlig risk.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Förmaksflimmer (de svenska godkännandena saknar indikationstext, så uppgiften kommer från läkemedlets indikationskoppling i kunskapsgrafen) |
| Förutsagd ny indikation | Prinzmetals angina |
| TxGNN-förutsägelsepoäng | 99,99 % (rank 292) |
| Evidensnivå | L4 (endast indirekta data, huvudsakligen om diagnostisk användning och mekanism) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 3 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Det finns ingen detaljerad verkningsmekanismdata i läkemedelsdatabasen. Enligt den sammanställda analysen hämmar dipyridamol återupptaget av adenosin och fosfodiesteras. Det höjer adenosinhalten utanför cellerna och vidgar kranskärlen. Det är också skälet till att läkemedlet används som farmakologiskt belastningsmedel vid myokardscintigrafi och ekokardiografi.

Kopplingen till Prinzmetals angina är därför i första hand indirekt. Båda tillstånden gäller kranskärlens funktion, och modellen har sannolikt fångat denna likhet. Förmaksflimmer och vasospastisk angina är dock olika sjukdomar, och någon direkt koppling mellan den ursprungliga och den nya indikationen har inte kunnat styrkas.

Mekanismen talar dessutom delvis emot nytta. Kärlvidgning med dipyridamol kan ge "coronary steal", där blodflödet fördelas bort från redan sjuka områden. Publicerade data visar också att kranskärlsspasm kan utlösas när dipyridamolbelastning avbryts med aminofyllin hos patienter med variantangina. Den biologiska rimligheten är alltså låg till måttlig, och risken kan vara större än nyttan.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Klinisk observation | Japanese Circulation Journal | 26 patienter med vilo-angina (13 med Prinzmetals angina) fick bland annat propranolol, diltiazem, dipyridamol 50 mg, atropin och fenoxibensamin. Propranolol var verkningslöst och tenderade att förvärra anfallen. Sammanfattningen är avkortad och visar inte dipyridamols effekt. |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Liten klinisk studie | American Journal of Cardiology | Studerade om avbrytande av dipyridamolbelastning med aminofyllin kan utlösa kranskärlsspasm hos 36 inneliggande patienter. Visar en provokationsmekanism, inte behandlingsnytta. |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Kohortstudie | British Heart Journal | 25 patienter med ST-höjning vid arbetsprov och olika svar på dipyridamoltest. Diagnostisk användning. |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Kohortstudie | Zhonghua Xin Xue Guan Bing Za Zhi | Jämför kliniska drag vid typisk och atypisk kranskärlsspasm. Ingen uppgift om dipyridamol som behandling. |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Diagnostisk studie | Journal of the American College of Cardiology | Ökad ekogenicitet i övergående rörelsestörd hjärtmuskel som ekokardiografiskt tecken på ischemi. Diagnostiskt fynd. |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Översikt | Circulation | Patofysiologisk grund för icke-invasiv utvärdering av kranskärlsförträngning, bland annat med dipyridamol. |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostisk studie | Japanese Circulation Journal | Dipyridamolbelastning med talliumscintigrafi hos 38 patienter med kranskärlssjukdom gav 66 % diagnostisk träffsäkerhet. Ingen behandlingseffekt. |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Prognosstudie | Revista Portuguesa de Cardiologia | Treårsprognos hos patienter med misstänkt kranskärlssjukdom och normal dipyridamol-talliumscintigrafi. Diagnostisk användning. |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Fallrapport | Clinical Nuclear Medicine | Patient med migrän, astma och dokumenterad variantangina samt ischemi vid belastning. Diskuterar "hjärtmigrän" och ingen behandlingseffekt. |
| [14060538](https://pubmed.ncbi.nlm.nih.gov/14060538/) | 1963 | Fallrapport | Naika (Internal Medicine) | Fall av variantform av angina pectoris. Ingen sammanfattning tillgänglig. |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 66506 | Pyranistole | Depotkapsel, hård | Ej angiven |
| 47980 | Dipyridamol Alternova | Depotkapsel, hård | Ej angiven |
| 46282 | Diprasorin | Kapsel med modifierad frisättning, hård | Ej angiven |

Alla tre godkännanden är avregistrerade, och för närvarande finns inget giltigt godkännande i Sverige.

---

## Säkerhetsaspekter

- **Kontraindikationer (från kunskapsgraf, inte från produktresumé)**: Kopplingar finns till bland annat njursjukdom, leversjukdom, gallblåsesjukdom, trombocytopeni, magsår, lågt blodtryck, gikt, akut kranskärlssyndrom, hjärtinfarkt, blödarsjuka (hemofili), olika anemiformer, Reye syndrom och Alzheimers sjukdom. Dessa uppgifter måste verifieras mot produktresumén innan de används kliniskt.
- **Läkemedelsinteraktioner**: Totalt 321 interaktioner är registrerade. De som är graderade som måttliga är **dexfenfluramin**, **sibutramin** och **fenfluramin**. Bland interaktionerna med okänd allvarlighetsgrad finns acetylsalicylsyra, omeprazol, pantoprazol, lansoprazol, cimetidin, metformin, glimepirid, rosiglitazon, simvastatin, morfin, prednison, vankomycin och amfotericin B.
- **Specifik risk vid vasospastisk angina**: Kärlvidgning och "coronary steal" kan försämra blodflödet, och kranskärlsspasm kan utlösas när dipyridamolbelastning avbryts.

Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsepoängen är mycket hög, men det finns inga kliniska prövningar och ingen litteratur som visar behandlingsnytta vid Prinzmetals angina. Mekanismen kan dessutom vara ofördelaktig vid kranskärlsspasm.
- Alla svenska godkännanden är avregistrerade, och säkerhetsdata från produktresumén saknas.

**För att gå vidare krävs:**
- Produktresumé med varningar och kontraindikationer för säkerhetsbedömning.
- Prekliniska eller kliniska data som visar att dipyridamol minskar eller åtminstone inte ökar vasospastiska anfall.
- Granskning av om risken för "coronary steal" och spasm väger över möjlig nytta.
- Klargörande av den ursprungliga indikationen, eftersom de svenska godkännandena saknar indikationstext.

Observera att samma data visar betydligt starkare stöd (evidensnivå L1, bland annat ESPRIT-studien och metaanalyser) för **sekundärprevention efter stroke och TIA**. Det är dock en redan etablerad användning och inte ny återanvändning.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

