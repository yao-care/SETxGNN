---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

Jag använder `txgnn-pipeline`-skickligheten som guide. Nu genererar jag rapporten baserat på Evidence Pack.

---

# Midazolam: Från preoperativ sedering till insomni

## Sammanfattning

Midazolam är ett kortverkande bensodiazepinläkemedel som primärt används kliniskt för preoperativ sedering, anestesiinduktion och procedursedation. TxGNN-modellen förutsäger med mycket hög konfidenspoäng (99,74 %) att läkemedlet kan vara effektivt mot **insomni**, ett resultat som stöds av direkta historiska RCT-studier och en pågående prövning som explicit utvärderar midazolam vid sömnstörningar. Evidensbasen är mekanistiskt välmotiverad, men läkemedlets ultrakortverkande farmakokinetik och moderna kliniska riktlinjer begränsar dess roll som förstahandsbehandling vid kronisk insomni.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Preoperativ sedering och anestesiinduktion (känd klinisk användning; inga svenska godkännanden registrerade) |
| Förutsagd ny indikation | Insomni |
| TxGNN-förutsägelsepoäng | 99,74 % |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Midazolam tillhör bensodiazepinklassen och verkar som positiv allosterisk modulator av GABA-A-receptorn. Genom att binda till receptorns bensodiazepinbindningsställe – primärt på α1-subenheten – förstärker midazolam kloridinflödet vid GABA-stimulering. Detta leder till hyperpolarisering av nervcellen och en uttalad CNS-dämpning med sedativa, hypnotiska, anxiolytiska och antikonvulsiva egenskaper. Djurmodelldata (PMID 21396773) ger ytterligare mekanistiskt stöd genom att visa att GABAerg signalering i cingulate cortex är direkt kopplad till sömnreglering.

Sambandet mellan den ursprungliga indikationen (sedering) och insomni är direkt mekanistiskt: den hypnotiska effekten av GABA-A-modulering är precis den egenskap som historiskt lagt grunden för bensodiazepiner som sömnmedel. Äldre välkontrollerade studier från 1981–1990 (PMID 6120704, 6138072, 2121802, 2229461) har explicit utvärderat oral midazolam hos patienter med insomni och visat klinisk effekt.

Den viktigaste begränsningen är farmakokinetiken: midazolams eliminationshalveringstid är extremt kort (T½ ≈ 1,5–2,5 timmar). Detta innebär att läkemedlet sannolikt passar bättre vid **insomninssvårigheter** (sleep onset insomnia) än vid **sömnmaintenanceproblem**. Moderna riktlinjer och nyare selektiva sömnmedel (t.ex. orexinantagonister) har i stor utsträckning ersatt bensodiazepiner vid kronisk insomni på grund av beroenderisk och biverkningsprofil.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|--------|-----------|--------------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Rekryterar | 280 | Oral midazolam som premedicinering hos kolorektal cancerpatienter med sömnstörningar/ångest inför kirurgi; utvärderar sömnkvalitet och postoperativ smärta; studieprotokoll citerar explicit att midazolam oral lösning är säkert och effektivt för kortvarig hypnos |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fas 4 | Avslutad | 111 | Randomiserad dubbelblind jämförelse av dexmedetomidin vs. midazolam som sedering vid TURP under spinalanestesi; mäter postoperativ sömnkvalitet; indirekt relevant då sömnkvalitet är primärt utfallsmått |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|-----|-----------|--------------|
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Fas 2 RCT (dosfinnande) | Arzneimittel-Forschung | Oral midazolam 10–30 mg utvärderat hos 75 inlagda patienter med lindrig–måttlig insomni sekundär till muskuloskeletala sjukdomar; optimal dosintervall fastställt; effektivt och vältolererat sömnmedel |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Dubbelblind parallellgruppsstudie, midazolam 15 mg vs. Vesparax hos 30 kvinnliga insomnipatienter; midazolam visade likvärdig hypnotisk effekt med bättre tolerabilitet och frånvaro av hangover-effekt |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | Kontrollerad klinisk prövning | Journal of Clinical Psychopharmacology | Randomiserad multicenterdesign; flurazepam vs. midazolam hos kroniska insomnipatienter med bensodiazepinhistorik under 14 dagars behandling; utvärderade sömn, prestation och plasmanivåer i stor heterogen population |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | Multicenter kontrollerad prövning | Journal of Clinical Psychopharmacology | Sammanfattande analys av multicenterprövningen flurazepam vs. midazolam vid kronisk insomni; bekräftar korttidseffekt för midazolam |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Översikt | Acta Psychiatrica Scandinavica | Klinisk genomgång av bensodiazepinhypnotika inklusive midazolam; diskuterar indikationer, farmakokinetisk variation och kliniskt val av sömnmedel |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT | Journal of Clinical Medicine | Pilotprövning av lemborexant vs. bensodiazepin för insomni hos högriskpatienter med pankreatobiliär sjukdom; belyser att bensodiazepiner kan öka deliriumrisken – relevant för säkerhetsperspektivet |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Översikt | Orvosi Hetilap | Genomgång av insomnipatogenes och cerebral hypoperfusion; diskuterar primär vs. sekundär insomni och hyperarousal-hypotesen |

---

## Marknadsinformation Sverige

Midazolam är för närvarande **inte marknadsförd i Sverige** och saknar registrerade produktgodkännanden. Inga licensposter finns att redovisa.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Midazolams GABA-A-mekanism ger ett välmotiverat och direkt mekanistiskt samband med sömnbehandling, och historiska RCT-studier bekräftar klinisk effekt vid insomni. Däremot begränsar den ultrakortverkande farmakokinetiken (T½ ≈ 1,5–2,5 h) klinisk nytta vid sömnmaintenanceproblem, och moderna behandlingsriktlinjer avråder generellt från bensodiazepiner som förstahandsval vid kronisk insomni på grund av beroenepotential och biverkningsprofil.

**För att gå vidare krävs:**
- Verifiering av fullständig säkerhets- och kontraindikationsprofil via aktuell produktresumé
- Identifiering av specifik målpopulation där midazolams snabba anslagstid utgör en klinisk fördel (t.ex. situationell sleep onset insomnia)
- Jämförande effekt/biverkning-analys mot moderna godkända sömnmedel (zolpidem, eszopiklon, lemborexant, suvorexant)
- Klargörande av administreringsväg och dosformulering lämplig för insomniindikation (oral lösning alternativt sublingval beredning)
- Uppdaterad systematisk översikt av bensodiazepiner specifikt vid kortvarig insomni med modern metodologi
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

