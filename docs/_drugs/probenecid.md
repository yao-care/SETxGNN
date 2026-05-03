---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 3
---

# Probenecid
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

Analysen är klar. Probenecid är ett känt urikosuriskt läkemedel och den förutsagda indikationen (renal hypourikemi) innehåller en kritisk mekanistisk inkongruens som måste lyftas fram tydligt. Jag genererar nu rapporten.

---

# Probenecid: Från hyperurikemi/gikt till renal hypourikemi

## Sammanfattning

Probenecid är ett urikosuriskt läkemedel som blockerar URAT1-transportören i njurtubuli och därigenom ökar utsöndringen av urinsyra i urinen – primärt använt mot gikt och hyperurikemi. TxGNN-modellen förutsäger med **99,73 %** sannolikhet att det kan vara verksamt mot **renal hypourikemi**, men denna förutsägelse är mekanistiskt motbjudande: renal hypourikemi innebär redan en defekt uratreabsorption, och probenecid skulle förvärra tillståndet snarare än behandla det. Evidensbasen omfattar **0 kliniska prövningar** och **20 publikationer**, varav samtliga använder probenecid som diagnostiskt farmakologiskt verktyg – inte som terapi.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Hyperurikemi och gikt (urikosuriskt läkemedel) |
| Förutsagd ny indikation | Renal hypourikemi (hypouricemia, renal) |
| TxGNN-förutsägelsepoäng | 99,73 % |
| Evidensnivå | L4 – Observationsstudier och mekanismstudier; probenecid förekommer som diagnostisk probe, ej som behandling |
| Marknadsstatus i Sverige | Ej registrerat i Sverige |
| Antal godkännanden | 0 |
| Rekommenderat beslut | ⛔ Avvakta |

---

## Varför är denna förutsägelse rimlig?

Probenecid hämmar de organiska anjontransportörerna URAT1 (SLC22A12) och OAT1/OAT3 i proximala njurtubuli, vilket minskar reabsorptionen av urinsyra och ökar dess utsöndring i urinen. Denna verkningsmekanism är väl etablerad vid behandling av gikt och kronisk hyperurikemi, och läkemedlet har dessutom en klinisk roll som adjuvans vid antibiotikabehandling (ökar serumkoncentrationen av penicillin via OAT-hämning).

**Kritisk mekanistisk inkongruens – varför förutsägelsen sannolikt är felaktig.** Renal hypourikemi är ett ärftligt tillstånd orsakat av förlustmutationer i just de transportörerna (framför allt URAT1/SLC22A12, ibland GLUT9/SLC2A9) som probenecid normalt hämmar. Patienterna har redan en kraftigt ökad renal uratclearance och låga serumnivåer av urinsyra. Att tillföra ytterligare URAT1-blockad med probenecid skulle förstärka uratförlusten och riskera att utlösa eller förvärra de komplikationer som tillståndet redan medför – däribland träningsinducerad akut njursvikt.

Förklaringen till TxGNN-modellens höga poäng är troligen **litterär samförekomst (co-occurrence)**: probenecid används systematiskt i kliniska studier av renal hypourikemi som ett farmakologiskt testverktyg för att kartlägga graden av tubulär reabsorptionsdefekt, och testet kallas ofta "probenecidtest". Modellen har sannolikt tolkat denna frekventa samförekomst i texterna som en terapeutisk association, vilket är en metodologisk felkälla i nätverksbaserade förutsägelsemodeller.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|-----------|--------------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrativ översikt | Clinical Rheumatology | Aktuell genomgång av hypourikemi för reumatologer; etiologi, klassificering (renal vs. icke-renal) och riskstratifiering; probenecid nämns i diagnostiskt sammanhang |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Översikt | Mol Genet Metab | Ärftlig renal hypourikemi (HRH) orsakas primärt av SLC22A12-mutationer (URAT1); probenecid används som diagnostisk probe för att karakterisera reabsorptionsdefekten |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Tvärsnitt/Molekylär | J Am Soc Nephrol | 32 japanska patienter med renal hypourikemi; SLC22A12-mutationsanalys; probenecid- och pyrazinamidtest för subtypsklassificering av tubulär defekt |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Översikt/Fallrapport | Am J Kidney Dis | Isolerad renal hypourikemi med träningsinducerad akut njursvikt hos 29-årig man; probenecid som farmakologiskt diagnostikverktyg; förekomst 0,12–0,20 % i Japan |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Observationsstudie | Arch Intern Med | 7 diabetespatienter med renal hypourikemi; ökad pyrazinamid-suppressibel uratclearance; probenecid-respons analyserad som del av mekanismkarakterisering |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Fallrapport | Nephron | Familjär hypourikemi hos 37-årig kvinna; kraftigt reducerad respons på probenecid och pyrazinamid → bekräftar defekt i proximal reabsorption med hög kapacitet/affinitet |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Fallrapport/Mekanistisk | Nephron | Renal hypourikemi utan respons på varken pyrazinamid eller probenecid – identifierar ny subtyp med kombinerad sekretion- och reabsorptionsdefekt |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Fallrapport | Nephron | Renal hypourikemi med förstärkt tubulär uratsekret och urolithiasis; probenecid ökade uratclearance ytterligare; framgångsrik behandling med K⁺/Na⁺-citrat |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Fallrapport | Am J Kidney Dis | Kolangiokarcinomassocierad hypourikemi; kraftigt ökad uratclearance; pyrazinamid och probenecid gav minimal effekt → stödjer postsekretorisk reabsorptionsdefekt |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Fallserie | Am J Kidney Dis | Familjär renal hypourikemi hos två bröder med träningsinducerad akut njursvikt; genetisk och farmakologisk karakterisering inkl. probenecidtest |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: ⛔ Avvakta**

**Motivering:**
Förutsägelsen för renal hypourikemi (rank 1) är mekanistiskt direkt kontraindikerad – probenecid förstärker exakt den patofysiologiska process (URAT1-blockad → ökad uratförlust) som orsakar sjukdomen, och litteraturen bekräftar att läkemedlets roll i detta sammanhang är uteslutande diagnostisk, inte terapeutisk. TxGNN-modellens höga poäng är ett klassiskt exempel på co-occurrence-artefakt och bör inte tolkas som klinisk evidens.

**För att gå vidare krävs:**

- **Omvärdera fokusindikation**: Rank 2 (Lesch-Nyhans syndrom) har en mekanistiskt logisk koppling – HGPRT-brist leder till hyperurikemi, och probenecid kan i teorin bidra till uratsänkning som adjuvans till allopurinol. Denna indikation bör prioriteras för vidare utredning.
- **Komplettera MOA-data (DG002)**: Hämta fullständig verkningsmekanismbeskrivning från DrugBank API för att möjliggöra mer exakt mekanismanalys.
- **Komplettera säkerhetsdata (DG001)**: Hämta TFDA-jämförbara varningar och kontraindikationer (t.ex. från EMA/Läkemedelsverket) för att möjliggöra säkerhetsinitial bedömning (S1).
- **Utreda möjlig registrering i Sverige**: Probenecid är ej registrerat hos Läkemedelsverket – en marknadsstudie bör genomföras om vidare klinisk utveckling planeras.
- **Publicera en metodologisk notis**: Den identifierade co-occurrence-artefakten för renal hypourikemi är ett värdefullt fynd för validering av TxGNN-modellens begränsningar i sällsynta transportörsjukdomar.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

