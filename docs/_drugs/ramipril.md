---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Ramipril
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

Jag har läst in `txgnn-pipeline`-skillet. Nu genererar jag rapporten baserat på Evidence Pack JSON och den svenska rapportmallen.

---

# RAMIPRIL: Från hypertoni till pulmonell hypertension vid lungsjukdom och/eller hypoxi

## Sammanfattning

RAMIPRIL är en ACE-hämmare (angiotensinkonverteringsenzymhämmare) som globalt används för behandling av hypertoni, hjärtsvikt och kardiovaskulär riskreduktion, men som för närvarande saknar godkännande och marknadsstatus i Sverige. TxGNN-modellen förutsäger att det kan vara effektivt mot **pulmonell hypertension vid lungsjukdom och/eller hypoxi (WHO grupp 3)**, med ett förutsägelsepoäng på 99,93 %. Stödet bygger på **inga registrerade kliniska prövningar** och **20 publikationer** som huvudsakligen behandlar hypoxipatofysiologi generellt – direkta kliniska studier med ramipril för denna specifika indikation saknas helt.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige (globalt: hypertoni, hjärtsvikt, kardiovaskulär riskreduktion) |
| Förutsagd ny indikation | Pulmonell hypertension vid lungsjukdom och/eller hypoxi |
| TxGNN-förutsägelsepoäng | 99,93 % |
| Evidensnivå | L5 – Endast modellförutsägelse, inga direkta kliniska studier |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta dataset. Baserat på känd farmakologisk information är RAMIPRIL en ACE-hämmare som blockerar enzymet angiotensinkonvertas, vilket omvandlar angiotensin I till angiotensin II (Ang II). Ang II är ett potent vasokonstriktivt ämne som också medierar kärlremodellering och fibros via AT1-receptorn. Genom att minska Ang II-nivåerna uppnås systemisk vasodilatation, minskad aldosteronsekretion och sänkt blodtryck.

Kronisk hypoxi – som uppstår vid underliggande lungsjukdomar som KOL eller interstitiell lungfibros – aktiverar renin-angiotensin-aldosteronsystemet (RAAS) och ökar Ang II-produktionen. Detta bidrar till pulmonell vasokonstriktion, hypertrofi av pulmonala arterioler och progressiv kärlremodellering, vilket sammantaget ger pulmonell hypertension av WHO grupp 3-typ. Den teoretiska länken är alltså att ACE-hämning med ramipril skulle kunna dämpa pulmonell vasokonstriktion och hämma fibrotiska processer via Ang II-blockad.

Det saknas dock i dagsläget kliniska studier som direkt undersöker ramipril vid WHO grupp 3 pulmonell hypertension. Dessutom föreligger en etablerad risk för systemisk hypotension vid ACE-hämning, vilket i detta sammanhang kan vara kliniskt problematiskt. Litteraturen som identifierats i detta pack behandlar hypoxibiologi i allmänhet – inte ramipril specifikt i denna indikation – varför förutsägelsen i nuläget bedöms ha låg klinisk verifieringsgrad.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande för RAMIPRIL vid pulmonell hypertension av lungsjukdom och/eller hypoxi.

---

## Litteraturbevis

Nedanstående publikationer identifierades i relation till indikationen. Observera att samtliga berör hypoxipatofysiologi i bred bemärkelse och saknar direkt koppling till ramipril som behandling vid denna specifika diagnos.

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Översikt | Ageing Research Reviews | Genomgår hjärnans akuta sårbarhet för hypoxi vid hög höjd och lungsjukdom samt hypoxins roll i neurodegenerativa sjukdomar. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Översikt | Metabolic Brain Disease | Sammanfattar kliniska bevis och molekylära mekanismer bakom kognitiv svikt vid akut och kronisk hypoxi. |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Laboratoriestudie | Advanced Science | Visar att N4-acetylcytidin via NAT10/SEPT9/HIF-1α-feedbackloop driver glykolyseroende och hypoxitolerans i magsäckscancerceller. |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Översikt | Journal of Cellular Biochemistry | Beskriver cellulärt syresensorsystem och hur hypoxi påverkar metabolism, angiogenes, vaskulär sjukdom och cancer. |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Översikt | Trends in Cancer | Granskar hur deubikuitinaser (DUBs) reglerar HIF-stabilitet och kopplingen till tumörhypoxi. |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Översikt | Respiratory Care Clinics of North America | Genomgår fyra grundläggande mekanismer för hypoxi: lågt omgivningssyre, hypoventilation, V/Q-mismatch och höger-till-vänster-shunt. |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Översikt | Clinical Oncology | Sammanfattar hur tumörhypoxi orsakar strålresistens och diskuterar strategier för terapeutisk modifiering av hypoxi. |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Kommentar | Rev Med Inst Mex Seguro Social | Diskuterar hypobar hypoxi vid höjd och fysiologisk acklimatisering hos höghöjdsbor jämfört med havsnivåbefolkning. |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Kommentar | Journal of Applied Physiology | Introduktionskommentar till temanummer om translationell hypoxiforskning. |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Översikt | Redox Biology | Granskar hypoxins roll i multipel skleros-patologi och symtom, inklusive vaskulär dysfunktion och inflammation. |

---

## Marknadsinformation Sverige

RAMIPRIL är för närvarande **inte registrerat i Sverige**. Inga godkännanden finns registrerade hos relevanta myndigheter. Produktinformation kan sökas via europeiska eller nationella myndighetsdatabaser för länder där läkemedlet är godkänt (exempelvis EMA eller det tyska BfArM, där ramipril är välkänt under varumärket Delix/Tritace).

---

## Säkerhetsaspekter

Säkerhetsdata för RAMIPRIL saknas i detta Evidence Pack.

> Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Förutsägelsen vilar på en teoretiskt rimlig mekanistisk hypotes – RAAS-aktivering vid kronisk hypoxi och möjlig ACE-hämning som motåtgärd – men saknar varje form av direkt klinisk verifiering. Identifierad litteratur behandlar hypoxipatofysiologi generellt, inte ramipril som behandlingsalternativ vid WHO grupp 3 pulmonell hypertension, och inga kliniska prövningar finns registrerade. Därtill är säkerhetsprofilen (risk för systemisk hypotension) ett känt hinder för denna patientkategori.

**För att gå vidare krävs:**
- Genomföra riktad litteratursökning specifikt för *ACE-hämmare + pulmonell hypertension WHO grupp 3* för att fastställa om klassen som helhet har prövats
- Inhämta fullständig säkerhetsinformation: produktresumé, kontraindikationer och varningar (DG001 i data gaps)
- Konfirmera verkningsmekanismen via DrugBank API (DG002 i data gaps)
- Bedöma om systemisk hypotensionsrisk utesluter klinisk tillämpning redan på mekanismnivå (S0-screening)
- Om mekanistisk screening passeras: utforma en explorativ klinisk frågeställning och söka samarbete med lungmedicinsk specialitet
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

