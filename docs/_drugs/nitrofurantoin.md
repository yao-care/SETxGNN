---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

Använder `txgnn-pipeline`-skillet för kontext kring rapportgenerering. Nu genererar jag rapporten baserat på Evidence Pack:

---

# Nitrofurantoin: Från urinvägsinfektion till reumatoid artrit

## Sammanfattning

Nitrofurantoin är ett antibiotikum som klassiskt används för behandling av urinvägsinfektioner (UVI). TxGNN-modellen förutsäger att läkemedlet kan vara verksamt mot **reumatoid artrit**, med **0 kliniska prövningar** och **12 publikationer** som belyser detta samband. Den tillgängliga litteraturen stödjer dock inte ett terapeutiskt samband – texterna handlar i stället om Nitrofurantoin som orsak till biverkningar hos RA-patienter, vilket tyder på ett kunskapsgrafsbaserat samlöpningsfel snarare än en verklig återanvändningshypotes.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Urinvägsinfektion (antibiotikum; ej registrerat i Sverige) |
| Förutsagd ny indikation | Reumatoid artrit |
| TxGNN-förutsägelsepoäng | 99,89% |
| Evidensnivå | L5 – Enbart modellförutsägelse |
| Marknadsstatus i Sverige | Ej godkänt för försäljning |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Nitrofurantoin är ett nitrofuranderivat med antibakteriell verkningsmekanism. Detaljerade MOA-data är inte tillgängliga i detta underlag, men det är välkänt att läkemedlet verkar primärt genom att skada bakteriernas DNA och enzymsystem via reaktiva intermediärer som bildas efter intracellulär reduktion. Läkemedlet saknar känd immunmodulerande eller antiinflammatorisk aktivitet – de egenskaper som normalt krävs för behandling av reumatoid artrit.

Sambandet som TxGNN har identifierat är i praktiken ett **samlöpningsartefakt i kunskapsgrafen**. Litteraturen där Nitrofurantoin och RA förekommer tillsammans handlar antingen om (1) Nitrofurantoin som orsak till allvarliga lungbiverkningar – läkemedelsinducerad lungfibros – hos RA-patienter som redan använder immunsuppressiva läkemedel som Metotrexat, eller (2) att RA-patienter på grund av immunsuppressiv behandling löper ökad risk för urinvägsinfektioner och därigenom exponeras för Nitrofurantoin. Ingen av dessa kopplingar utgör ett terapeutiskt argument.

Det finns dessutom en säkerhetsmässigt kritisk faktor mot denna användning: Nitrofurantoin är kontraindicerat vid nedsatt njurfunktion (CrCl < 30–45 mL/min), ett vanligt tillstånd hos äldre RA-patienter och vid samsjuklighet med autoimmun njurpåverkan. Läkemedlet är alltså inte bara overksamt mot RA – det kan vara skadligt för den tilltänkta patientgruppen.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled case series | Scientific Reports | Studie av antibiotikaanvändning och RA-skov (CPRD GOLD, n = 31 992). Nitrofurantoin ingår i gruppen undersökta antibiotika – inga terapeutiska fynd för RA. |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Fallrapport | Cureus | 94-årig kvinna med RA behandlad med Metotrexat, sedan Nitrofurantoin för UVI – utvecklade irreversibel lungfibros. Nitrofurantoin framträder som biverkningsorsak, inte som behandling av RA. |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Översikt | Saudi Medical Journal | Genomgång av läkemedelsinducerad lungfibros; Nitrofurantoin identifieras som orsakande medel. RA nämns som predisponerande grundsjukdom, inte som indikation. |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Översikt | La Revue du praticien | Läkemedelsinducerad interstitiell lungsjukdom; Nitrofurantoin ingår i listan av antibiotika som kan utlösa tillståndet. |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Retrospektiv kohortstudie | Chest | 57 RA-patienter inlagda för interstitiell lungfibros – studerar RA-komplikation, Nitrofurantoin ej terapeutisk agent. |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Fallrapport | Cureus | Autoimmun hepatit; Nitrofurantoin listas som potentiell utlösare av läkemedelsinducerad leversjukdom i differentialdiagnostiken. |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Fallrapport | Revue de pneumologie clinique | Guldbehandlingsutlöst pneumoni hos RA-patient med CD4-alveoliter; Nitrofurantoin nämns i jämförelsesammanhang. |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Klinisk studie | Acta Medica Scandinavica | Korttidsbehandling med Nitrofurantoin vid bakteriuri hos medelålders kvinnor – rendodlad UVI-indikation, inget RA-samband. |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Fallrapport | Annales de dermatologie et de venereologie | Läkemedelsinducerad sialaddenit med fenylbutazon; Nitrofurantoin nämns bland andra kända utlösare av tillståndet. |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Översikt | Der Internist | Alveoliter och lungfibros – Nitrofurantoin ingår i översikten av utlösande ämnen. |

---

## Marknadsinformation Sverige

Nitrofurantoin har inga registrerade godkännanden i Sverige och är för närvarande inte tillgängligt på den svenska marknaden (0 licenser).

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
TxGNN-förutsägelsen för Nitrofurantoin vid reumatoid artrit är en artefakt av kunskapsgrafsbaserad samlöpning, inte ett tecken på terapeutisk potential. Det saknas biologiskt plausibelt mekanistiskt samband – Nitrofurantoin är ett antibiotikum utan immunmodulerande eller antiinflammatoriska egenskaper – och den tillgängliga litteraturen dokumenterar läkemedlet som en biverkningsorsak snarare än som en behandlingsform vid RA.

**För att gå vidare krävs:**
- Identifiering av ett biologiskt plausibelt mekanistiskt samband mellan Nitrofurantoin och RA-patofysiologi (saknas i dagsläget)
- Prekliniska data (in vitro/in vivo) som visar antiinflammatorisk eller immunmodulerande aktivitet
- Säkerhetsutvärdering avseende lungfibrosrisk vid kronisk Nitrofurantoin-användning hos RA-patienter, särskilt vid samtidig Metotrexat-behandling
- Kartläggning av njurfunktionsprofilen hos målpopulationen (känd kontraindikation vid CrCl < 30–45 mL/min)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

