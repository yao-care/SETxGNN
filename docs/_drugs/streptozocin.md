---
layout: default
title: Streptozocin
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Streptozocin
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

Jag har granskat TxGNN-pipeline-skillet. Nu genererar jag rapporten baserat på Evidence Pack:et.

---

# Streptozocin: Från pankreatisk neuroendokrin tumör till recidiverande-remitterande multipel skleros

## Sammanfattning

Streptozocin (STZ) är ett cytotoxiskt alkyleringsmedel som internationellt används för behandling av metastaserande pankreatiska neuroendokrina tumörer (isletcellscancer). TxGNN-modellen förutsäger att det potentiellt kan vara effektivt mot **recidiverande-remitterande multipel skleros (RRMS)**, med **0 kliniska prövningar** och **1 publikation** som för närvarande stöder denna riktning. Evidensen är på lägsta möjliga nivå (L5), och den enda tillgängliga publikationen berör fingolimod i en diabetesdjurmodell – inte STZ som MS-behandling – vilket tyder på att förutsägelsen sannolikt är ett falskt positivt resultat orsakad av grafnärhet i kunskapsgrafen.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Pankreatisk isletcellscancer (neuroendokrin tumör) – ej godkänd i Sverige |
| Förutsagd ny indikation | Recidiverande-remitterande multipel skleros |
| TxGNN-förutsägelsepoäng | 99,97 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd farmakologisk kunskap är streptozocin ett nitrosourealiknande alkyleringsmedel som selektivt tas upp i GLUT2-uttryckande celler (framför allt pankreatiska betaceller och neuroendokrina tumörceller) via GLUT2-transportören, vilket leder till DNA-alkylering och celldöd. Denna mekanism är välbevisad vid behandling av neuroendokrina tumörer med hög GLUT2-expression.

Recidiverande-remitterande multipel skleros (RRMS) är däremot en autoimmun sjukdom där det adaptiva immunsystemet angriper myelinskidan kring centralnervystemets nervceller. STZ:s GLUT2-selektiva DNA-alkyleringsmekanism har ingen känd biologisk koppling till MS-patologi, och det finns heller inga immunmodulerande egenskaper dokumenterade för STZ.

Den höga TxGNN-poängen beror med stor sannolikhet på **grafnärhet i kunskapsgrafen**: fingolimod (FTY720) är ett godkänt förstalinjemedel vid RRMS och förekommer dessutom frekvent i experimentell litteratur om STZ-inducerade diabetesmodeller (djurstudier på neuroendokrina komplikationer). Modellen har sannolikt tolkat denna samförekomst som en biologisk koppling – en känd begränsning hos grafbaserade prediktionsmodeller.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|-----------|--------------|
| [28162947](https://pubmed.ncbi.nlm.nih.gov/28162947/) | 2017 | Djurstudie | The Journal of Sexual Medicine | FTY720 (fingolimod) förbättrade delvis erektil dysfunktion hos råttor med STZ-inducerad typ 1-diabetes via hämning av endoteldysfunktion och corporal fibros. Studien använder STZ som ett verktyg för att skapa en diabetesmodell – inte som behandling av MS. Relevansen för MS-indikationen bedöms som låg. |

---

## Marknadsinformation Sverige

Streptozocin är för närvarande **inte registrerat i Sverige**. Inga godkännanden finns i Läkemedelsverkets register.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|-------------------|-------------|----------------|-------------------|
| — | — | — | Inga svenska godkännanden registrerade |

---

## Cytotoxicitet

Streptozocin uppfyller kriterierna för antineoplastiskt läkemedel: det är ett nitrosourealiknande DNA-alkyleringsmedel vars ursprungliga indikation är malign neuroendokrin tumör.

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Konventionell cytotoxisk – DNA-alkyleringsmedel (nitrosourealiknande strukturell klass) |
| Myelosuppressionsrisk | Låg till måttlig – STZ är relativt icke-myelosuppressivt jämfört med klassiska nitrosourea-analoger (BCNU, CCNU), vilket framgår av kliniska studier från 1978–1979 |
| Emetogenicitetsklassificering | Hög – kraftig illamående och kräkningar är de vanligaste akuta biverkningarna |
| Övervakningspunkter | Njurfunktion (nefrotoxicitet är dosbegränsande biverkning), leverfunktion (ALAT, ASAT, bilirubin), blodstatus (trombocytopeni möjlig), P-glukos (risk för hypoglykemi/hyperglykemi vid beta-cellsdestruktion) |
| Hanteringsskydd | Ja – cytotoxisk hantering krävs i enlighet med gällande föreskrifter för cytostatikahantering (Arbetsmiljöverkets riktlinjer) |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> Notera: Varningstext, kontraindikationer och läkemedelsinteraktioner saknas i detta evidenspaket (Data Gap DG001). Produktresumén (t.ex. Zanosar® smPC) bör konsulteras innan klinisk bedömning.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots en TxGNN-förutsägelsepoäng på 99,97 % är evidensen för STZ vid RRMS på lägsta möjliga nivå (L5). Repurposing-rationalen saknar biologisk plausibilitet – STZ:s GLUT2-selektiva alkyleringsmekanism har ingen känd koppling till MS:s autoimmuna patofysiologi. Den enda tillgängliga publikationen avser fingolimod i en diabetesmodell och stöder inte STZ som MS-behandling. Den höga modellpoängen bedöms vara ett artefaktuellt resultat av grafnärhet, inte en äkta farmakologisk signal.

**För att gå vidare krävs:**
- Identifiering av en biologiskt plausibel verkningsmekanism för STZ vid autoimmun sjukdom eller demyelinisering
- Prekliniska studier i MS-djurmodeller (t.ex. EAE-modellen) som visar effekt
- Fullständig säkerhetsprofil: MOA-data från DrugBank (DG002), varningstext och kontraindikationer från produktresumé (DG001)
- Uteslutande av att förutsägelsen enbart beror på grafnätverkets nodgranneffekt via fingolimod/FTY720
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

