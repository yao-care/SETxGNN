---
layout: default
title: Acetylcysteine
parent: Endast modellprediktion (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetylcysteine: predikterad ny indikation Trombotisk sjukdom (thrombotic disease) (evidensnivå L5). Ursprunglig indikation: Bronkit (enligt kunskapsgrafen"
monitor_inn: "acetylcysteine"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "angle-closure glaucoma"]
---

# Acetylcysteine
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

# Acetylcystein: Från bronkit till trombotisk sjukdom

---

## Sammanfattning

Acetylcystein är ett slemlösande läkemedel (mukolytikum) som ursprungligen användes vid luftvägssjukdomar som bronkit och cystisk fibros. Det används också som motgift vid paracetamolförgiftning. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **trombotisk sjukdom**, särskilt trombotisk mikroangiopati (TMA) och trombotisk trombocytopen purpura (TTP). Riktningen stöds av **7 kliniska prövningar** och **20 publikationer**, men ännu saknas redovisade resultat från större prövningar.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Bronkit (enligt kunskapsgrafen; godkänd indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Trombotisk sjukdom (thrombotic disease) |
| TxGNN-förutsägelsepoäng | 99,96 % (rang 398) |
| Evidensnivå | L2 (en avslutad randomiserad fas 2-prövning; fas 3-prövningens resultat är inte redovisade) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 6 (0 giltiga, 6 avregistrerade) |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i databasen. Baserat på känd information är acetylcystein en tiolförening, dess effekt vid luftvägssjukdomar med segt slem är väl dokumenterad, och mekanistiskt kan den vara tillämpbar på trombotiska sjukdomar.

Acetylcystein kan bryta disulfidbindningar. I von Willebrand-faktor (VWF) kan det minska multimerernas förmåga att binda trombocyter. Vid TTP leder brist på enzymet ADAMTS13 till att mycket stora VWF-multimerer ansamlas och bildar blodproppar i de små kärlen. Tanken är att acetylcystein kan ersätta en del av den klyvning som saknas. Detta stöds av prekliniska studier på mus och babian (PMID 28011677).

Acetylcystein har även antioxidativ effekt. Den kan minska den protrombotiska fenotypen vid till exempel njursvikt, där oxidativ stress och cirkulerande vävnadsfaktor är förhöjda. Sambandet till de ursprungliga indikationerna är främst själva molekylens kemiska egenskaper (tiolgrupp, disulfidbrytande effekt), inte en gemensam sjukdomsmekanism. Evidensen är starkast för TMA och TTP och svagare för trombotisk sjukdom i allmänhet.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Fas 3 | Avslutad | 170 | Säkerhet och effekt av acetylcystein vid transplantationsassocierad TMA. Direkt relevant, men resultat redovisas inte i underlaget. |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Fas 2/3 | Aktiv, rekryterar inte | 44 | Enarmad multicenterstudie vid transplantationsassocierad TMA. Förväntas avslutas 2026-12-31, inga resultat ännu. |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Fas 2 | Avslutad | 40 | RENACTIF: randomiserad, dubbelblind, placebokontrollerad cross-over-studie av den trombotiska fenotypen vid njursvikt. Mäter mekanismnära markörer, inte kliniska proppar. |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Tidig fas 1 | Avslutad | 3 | Pilotstudie av intravenös acetylcystein vid misstänkt TTP tillsammans med plasmautbyte. Alltför litet underlag för slutsatser. |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Fas 2 | Okänd | 44 | Högdos-dexametason plus acetylcystein vid nydiagnostiserad immunologisk trombocytopeni (ITP). Indirekt koppling, och kombinationen gör det svårt att isolera effekten av acetylcystein. |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Fas 1/2 | Okänd | 200 | Atorvastatin, acetylcystein och danazol vid steroidresistent eller återfallande ITP. Kombinationsbehandling vid icke-trombotisk sjukdom, låg relevans. |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Tidig fas 1 | Avslutad | 15 | Atorvastatin plus acetylcystein och trombocytantal vid ITP. Liten studie med kombinationsbehandling, låg relevans. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Systematisk översikt | Journal of Clinical Medicine | Granskar acetylcystein vid TTP, där plasmautbyte och immunhämning förbättrat utfallet men refraktär och återfallande sjukdom kvarstår. |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Systematisk översikt | Cureus | Sammanställer acetylcystein som tilläggsbehandling vid TTP, utifrån dess förmåga att reducera disulfidbindningar. |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Kohortstudie | Annals of Hematology | Retrospektiv studie av sambandet mellan acetylcystein och sjukhusdödlighet vid förvärvad TTP. Användningen beskrivs som omstridd. |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preklinisk (mus och babian) | Blood | Acetylcystein prövas i djurmodeller av TTP, med utgångspunkt i behovet av nya behandlingar. |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Översikt | Expert Review of Hematology | Beskriver återanvända läkemedel, bland annat acetylcystein, och nya läkemedel vid immunmedierad TTP. |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Översikt | Blood | Allmän översikt av TTP: ADAMTS13-brist, patofysiologi och behandling. |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Översikt | Journal of Clinical Medicine | Översikt av TTP: patofysiologi, diagnostik och behandling. |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Översikt | Transfusion Clinique et Biologique | Behandling av TTP med plasmautbyte och rituximab, där återfall förekommer hos upp till 40 % av patienterna. |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Översikt | Journal of Infection and Public Health | Acetylcystein vid covid-19, där ett protrombotiskt tillstånd och oxidativ stress diskuteras. |
| [32614622](https://pubmed.ncbi.nlm.nih.gov/32614622/) | 2021 | Översikt | Platelets | Nya trombocythämmande strategier mot VWF och GPIb, med relevans för TMA. |

---

## Marknadsinformation Sverige

Alla sex godkännanden är avregistrerade, och inget giltigt godkännande finns för närvarande. Indikationstext finns inte angiven för något av godkännandena. De fem första visas nedan.

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 22347 | Acetylcystein 1A Farma | Brustablett | Avregistrerad |
| 11537 | Acetylcystein Viatris | Lösning för nebulisator | Avregistrerad |
| 64838 | Acetylcysteine Macure | Koncentrat till infusionsvätska, lösning | Avregistrerad |
| 23596 | Acetylcystein Viatris | Brustablett | Avregistrerad |
| 21646 | Acetylcystein Alternova | Brustablett | Avregistrerad |

---

## Säkerhetsaspekter

Produktresumé med varningar och kontraindikationer ingår inte i de sammanställda uppgifterna. Se produktresumén för fullständig säkerhetsinformation.

- **Tillstånd som kunskapsgrafen kopplar till kontraindikation** (inte hämtat från produkttext): magsår, lågt blodtryck, andningssvikt, astma, bronkialsjukdom och esofagusvaricer.
- **Läkemedelsinteraktioner**: 247 möjliga interaktioner är registrerade. De som är graderade är:
  - Insulin, humant (inhalation, snabbverkande): **måttlig**
  - Aktivt kol: **ringa**
  - De flesta övriga saknar gradering, bland annat omeprazol, pantoprazol, lansoprazol, metformin, glimepirid, morfin, doxycyklin, vankomycin, atropin, prednison och triamcinolon.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Mekanismen är biologiskt rimlig, särskilt för TTP och transplantationsassocierad TMA. Det finns också en avslutad randomiserad fas 2-studie och en avslutad fas 3-studie.
- Inga effektresultat är redovisade från de mest relevanta prövningarna, och den randomiserade studien mäter en mekanismnära markör snarare än kliniska proppar. Därmed kan effekten ännu inte bekräftas.
- Evidensen gäller TMA och TTP, inte trombotisk sjukdom i allmänhet.

**För att gå vidare krävs:**
- Publicerade resultat från NCT03252925 (fas 3) och NCT03636932 (RENACTIF).
- Resultat från NCT07279610 (förväntas avslutas 2026-12-31).
- En avgränsning av målindikationen till TMA eller TTP i stället för "trombotisk sjukdom".
- Randomiserade, kontrollerade studier med kliniska effektmått, till exempel återfall, dödlighet och organskada.
- Fullständig säkerhetsinformation (varningar, kontraindikationer, interaktioner) från produktresumén.
- Klargörande av regulatorisk väg, eftersom alla svenska godkännanden är avregistrerade. Intravenös beredning torde vara relevant för akuta tillstånd.
- Närmare data om verkningsmekanismen, som saknas i databasen.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

