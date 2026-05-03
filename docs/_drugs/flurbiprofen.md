---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

Använder `txgnn-pipeline`-skillet för att vägleda rapportgenerering. Fokuserar på den indikation med starkast evidens (ankyloserande spondylit, rang 8, L1) snarare än rang 1 som saknar all evidens och bedöms som trolig falsk positiv.

---

# Flurbiprofen: Från reumatiska inflammationstillstånd till ankyloserande spondylit

## Sammanfattning

Flurbiprofen är ett icke-steroidt antiinflammatoriskt läkemedel (NSAID) som verkar via cyklooxygenas-hämning och som historiskt använts för reumatiska inflammatoriska tillstånd såsom reumatoid artrit och artros, men som för närvarande saknar godkännande i Sverige.
TxGNN-modellen förutsäger att det kan vara effektivt mot **ankyloserande spondylit** (Bechterews sjukdom), en kronisk inflammatorisk ryggradssjukdom, med ett förutsägelsepoäng på 99,97 %.
Förutsägelsen stöds av **0 registrerade kliniska prövningar** och **20 publikationer** – varav minst 7 är randomiserade kontrollerade studier som direkt jämför flurbiprofen med etablerade behandlingsalternativ vid ankyloserande spondylit.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Ej registrerat i Sverige – används internationellt som NSAID vid reumatiska sjukdomar (reumatoid artrit, artros) |
| Förutsagd ny indikation | Ankyloserande spondylit (Bechterews sjukdom) |
| TxGNN-förutsägelsepoäng | 99,97 % (global rang 124) |
| Evidensnivå | **L1** – ≥ 2 avslutade RCT identifierade i litteraturen |
| Marknadsstatus i Sverige | Ej på marknaden |
| Antal godkännanden | 0 |
| Rekommenderat beslut | **Gå vidare med försiktighet** |

---

## Varför är denna förutsägelse rimlig?

Flurbiprofen är ett fenylalkansyre-derivat som hämmar enzymerna COX-1 och COX-2, vilket leder till minskad syntes av prostaglandiner – i synnerhet prostaglandin E₂ (PGE₂). PGE₂ spelar en nyckelroll i den inflammatoriska kaskad som driver smärta, stelhet och progressiv benbildning längs ryggraden vid ankyloserande spondylit (AS). Genom att dämpa PGE₂-produktionen kan flurbiprofen lindra både symtom och bidra till att bromsa ankyloseringen. Prekliniska studier har visat att flurbiprofen är minst lika potent som indomethacin och ungefär 200 gånger mer potent än aspirin som antiinflammatoriskt medel.

NSAID-läkemedel är sedan decennier etablerade som förstahandsbehandling vid aktiv ankyloserande spondylit, och COX-hämning utgör den centrala mekanistiska länken. Flurbiprofen delar denna verkningsmekanism med indomethacin och naproxen – båda med stark evidens vid AS. Kopplingen mellan ursprungsindikationen (reumatisk inflammation) och den förutsagda nya indikationen (AS) är därför inte en radikal repurposing, utan snarare en utvidgning inom samma inflammatoriska sjukdomsspektrum och med samma terapeutiska mekanism.

Under perioden 1974–1986 genomfördes ett flertal dubbelblinda, randomiserade kliniska prövningar med flurbiprofen specifikt vid aktiv ankyloserande spondylit. Studierna jämförde flurbiprofen direkt mot indomethacin, fenylbutazon och naproxen och visade genomgående likvärdig effekt på smärtlindring, ledstelhet och global förbättring. En poolad säkerhetsanalys från nio fas III-studier med totalt 1 677 patienter rapporterade inga kliniskt signifikanta lever- eller njurpåverkningar. TxGNN:s höga förutsägelsepoäng för AS är därmed konsistent med befintlig klinisk evidens.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande i ClinicalTrials.gov eller ICTRP.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|-----|-----------|-------------|
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (jämförande, dubbelblind) | The American Journal of Medicine | 57 patienter, 26 veckor; flurbiprofen 200 mg/dag likvärdig med indomethacin i smärtkontroll vid AS |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (jämförande, dubbelblind) | The American Journal of Medicine | 90 patienter, 26 veckor; flurbiprofen 200 mg/dag likvärdig med fenylbutazon 300 mg vid AS |
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT (dubbelblind crossover) | British Medical Journal | 35 patienter; flurbiprofen 150 mg/dag jämförbart med fenylbutazon 300 mg; väl tolererat |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT (jämförande) | Current Medical Research and Opinion | 26 patienter; flurbiprofen och indomethacin likvärdiga i smärt- och ömhetslindrring vid aktiv AS |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT (jämförande) | Southern Medical Journal | 26 patienter, 6 veckor; flurbiprofen 150–200 mg/dag likvärdig med indomethacin; ingen avhoppare pga otillräcklig effekt |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT (crossover) | The New Zealand Medical Journal | 30 patienter, 4 veckor; flurbiprofen 200 mg vs naproxen 750 mg – likvärdig effekt på smärta och stelhet; fler biverkningar med flurbiprofen |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT (jämförande) | European Journal of Clinical Pharmacology | 27 patienter; flurbiprofen och fenylbutazon likvärdiga i smärtlindring; global förbättring tenderade gynna fenylbutazon utan statistisk signifikans |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Säkerhetskohort (poolad analys) | The American Journal of Medicine | 9 fas III-studier, 1 677 patienter (AS, OA, RA); inga kliniskt signifikanta njur- eller levereffekter av flurbiprofen |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Översiktsartikel | Drugs | Farmakologisk helgenomgång; flurbiprofen 150–300 mg/dag jämförbart med indomethacin vid AS och RA; färre biverkningar än aspirin |
| [3514311](https://pubmed.ncbi.nlm.nih.gov/3514311/) | 1986 | Öppen långtidsstudie | The Journal of International Medical Research | 336 patienter med AS, psoriasisartrit m.fl.; signifikant smärtförbättring från vecka 2 och kvarstående under 12 månader |

---

## Marknadsinformation Sverige

Flurbiprofen är för närvarande **inte registrerat** hos Läkemedelsverket (MPA) i Sverige. Inga godkännanden finns i databasen.

---

## Säkerhetsaspekter

Specifik säkerhetsinformation (varningar, kontraindikationer, läkemedelsinteraktioner) saknas i detta evidence pack. Observera att flurbiprofen tillhör NSAID-klassen och att klassens välkända risker – inklusive gastrointestinal toxicitet, kardiovaskulär risk och njurpåverkan – gäller. En poolad säkerhetsanalys (PMID 3963024) från 9 fas III-studier med 1 677 patienter visade inga kliniskt signifikanta lever- eller njureffekter vid behandlingstider upp till 26 veckor.

> Se produktresumén (SmPC) för fullständig och aktuell säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Gå vidare med försiktighet**

**Motivering:**
Flurbiprofen har **L1-evidens** för behandling av ankyloserande spondylit, grundad på minst sju publicerade RCT från 1974–1986 som alla visar likvärdig effekt jämfört med indomethacin, fenylbutazon och naproxen; den mekanistiska kopplingen via COX-hämning och PGE₂-reduktion är välgrundad och konsistent med nuvarande förståelse av AS-patofysiologi. Läkemedlet saknar dock godkännande i Sverige och fullständig aktuell säkerhetsdokumentation är inte tillgänglig.

**För att gå vidare krävs:**
- Inhämtning och granskning av fullständig produktresumé (SmPC) samt identifiering av eventuella Läkemedelsverket-specifika krav
- Uppdaterad systematisk litteratursökning för perioden 1987–2026 för att identifiera nyare RCT, metaanalyser eller säkerhetsstudier
- Utvärdering av klinisk relevans i relation till nuvarande standardbehandling i Sverige (moderna COX-2-selektiva NSAID, biologiska läkemedel som TNF-hämmare och IL-17-hämmare)
- Konsultation med reumatologisk expertis för att bedöma om det finns ett kliniskt behov som motiverar en formell godkännanseansökan till MPA
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

