---
layout: default
title: Rifampicin
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Rifampicin
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

Använder `txgnn-pipeline`-skillet för att vägleda rapportgenerering för TxGNN-läkemedelsåteranvändning. Nu genererar jag rapporten baserat på Evidence Pack JSON.

---

# RIFAMPICIN: Från tuberkulos till konjunktivit

## Sammanfattning

Rifampicin är ett bredspektrumantibiotikum som primärt används för behandling av tuberkulos och andra allvarliga bakteriella infektioner. TxGNN-modellen förutsäger att det kan vara effektivt mot **konjunktivit** (ögoninflammation), baserat på läkemedlets bevisade aktivitet mot ett brett spektrum av konjunktivitpatogener, inklusive *Chlamydia trachomatis*, *Staphylococcus aureus* och *Neisseria meningitidis*. Förutsägelsen stöds av **0 registrerade kliniska prövningar** och **20 publikationer**, varav en randomiserad kontrollerad studie om lokal rifampicinbehandling av trakomatöst konjunktivit från 1975.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Tuberkulos och allvarliga bakteriella infektioner (ej godkänd i Sverige) |
| Förutsagd ny indikation | Konjunktivit |
| TxGNN-förutsägelsepoäng | 99,95% |
| Evidensnivå | L3 – Observationsstudier och enstaka äldre klinisk prövning |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta Evidence Pack. Baserat på känd information är Rifampicin ett rifamycinantibiotikum som hämmar den bakteriella DNA-beroende RNA-polymerasen (β-subenheten), vilket blockerar transkriptionen och leder till snabb bakteriedöd. Denna mekanism är brett applicerbar mot grampositiva och gramnegativa bakterier, mykobakterier och obligata intracellulära patogener som *Chlamydia trachomatis*.

Sambandet mellan den ursprungliga indikationen (tuberkulos) och den förutsagda nya indikationen (konjunktivit) är mekanistiskt välmotiverat. Konjunktivit orsakas av många bakterier som är känsliga för rifampicin: *Chlamydia trachomatis* (trakomatöst konjunktivit och inklusionskonjunktivit), *Staphylococcus aureus*, *Neisseria meningitidis* (primärt meningokockal konjunktivit) och *Corynebacterium macginleyi*. Litteraturen från 1970-talet visar att lokal rifampicinbehandling prövades kliniskt i oftalmologin med lovande resultat, men utan moderna uppföljningsstudier.

Lokal ögonapplikation — t.ex. 1% rifampicinsalva eller ögondroppar — utgör en farmakologiskt fördelaktig väg eftersom den ger terapeutiska koncentrationer i konjunktiva och kornea med minimal systemisk absorption. Detta minskar väsentligt riskerna för de systemiska biverkningar och läkemedelsinteraktioner (t.ex. CYP3A4-induktion) som är förknippade med oral rifampicinbehandling. Topikala formuleringar skulle kunna ta tillvara läkemedlets potens mot konjunktivitpatogener utan de bekymmer som begränsar systemisk användning.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|-----|-----------|--------------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | RCT | *American Journal of Ophthalmology* | Kontrollerad studie av trakomatöst konjunktivit i Tunisien: 1% rifampicinssalva (76 patienter) jämfördes med 1% tetracyklin och 5% borsyra under 10 veckor — visade klinisk effekt mot aktiv trachomasjukdom |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Narrativ översikt | *Annals of Ophthalmology* | Tidig genomgång av rifampicins användning i oftalmologisk praktik |
| [4250391](https://pubmed.ncbi.nlm.nih.gov/4250391/) | 1970 | Övrig | *Archives d'ophtalmologie* | Tidig klinisk erfarenhet av rifampicin som ögonpreparat |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | Övrig | *Nature* | Anti-trakomatös aktivitet hos rifampicin och rifamycinderivat — visade in vitro-potens mot *Chlamydia trachomatis* |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | Tvärsnittsstudie | *Advanced Biomedical Research* | Kartläggning av bakteriell etiologi och antibiotikaresistens vid konjunktivit i Iran — identifierade konjunktivitpatogener med känd rifampicinkänslighet |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | Fallrapport | *Clinical Microbiology and Infection* | Primär meningokockal konjunktivit hos 6-åring: initialt lokalt behandlad, framgångsrikt avslutad med systemisk rifampicin efter konfirmerad diagnos |
| [7806886](https://pubmed.ncbi.nlm.nih.gov/7806886/) | 1994 | Fallserie | *Journal of Infection* | Tre fall av primär meningokockal konjunktivit med systemisk sepsis — rekommendation om kombinerad lokal och parenteral terapi med kemorofylax för nära kontakter |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | Observationsstudie | *Anales de Pediatría* | Vanligaste konjunktivitpatogener hos barn och deras antibiotikakänslighet — empirisk antibiotikabehandling utan föregående kultur diskuteras |
| [21191558](https://pubmed.ncbi.nlm.nih.gov/21191558/) | 2010 | Susceptibilitetsstudie | *Revista Española de Quimioterapia* | Antibiotikaresistensmönster hos *Corynebacterium macginleyi* vid konjunktivit — en patogen med dokumenterad rifampicinkänslighet |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Fallserie | *Current Opinion in Ophthalmology* | Okulära manifestationer av kattskrapsfeber (*Bartonella henselae*) inkl. Parinauds okulöglandulära syndrom — rifampicin ingår i rekommenderad behandling |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensbasen är begränsad (L3) och vilar på en enda RCT från 1975 med specifikt fokus på trakomatöst konjunktivit, kompletterad av fallrapporter och susceptibilitetsstudier utan moderna kontrollerade effektstudier. Rifampicin är dessutom inte godkänt eller marknadsförd i Sverige, och ingen oftalmisk formulering finns tillgänglig på marknaden.

**För att gå vidare krävs:**
- Verifiering av säkerhetsprofil, varningar och kontraindikationer via fullständig produktresumé (SmPC)
- Identifiering eller utveckling av en godkänd oftalmisk formulering (t.ex. 1% ögonsalva/droppar)
- Moderna, väldesignade kliniska prövningar för bakteriell konjunktivit med dokumentation av effekt mot nutidens resistensmönster
- Jämförelse med befintliga förstahandsbehandlingar godkända i Sverige (t.ex. kloramfenikol, fusidinsyra, tobramycin)
- Utredning av resistensutvecklingsrisk vid lokal rifampicinanvändning, med tanke på läkemedlets centrala roll i tuberkulosbehandling
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

