---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

Jag använder **txgnn-pipeline**-skickligheten för att hantera TxGNN-relaterat arbete. Nu genererar jag rapporten baserat på Evidence Pack-data.

---

# Ritonavir: Från HIV-1-infektion till SIV-infektion (icke-mänskliga primater)

## Sammanfattning

Ritonavir är en proteashämmare som ursprungligen godkändes för behandling av HIV-1-infektion hos människor, där det verkar genom att hämma virusets aspartatproteas och blockera mognaden av nya infektiösa viruspartiklar. TxGNN-modellen förutsäger att det kan vara effektivt mot **simian immunodeficiency virus (SIV)-infektion hos icke-mänskliga primater**, med ett förutsägelsepoäng på **99,9%**. Evidensbasen består av **12 vetenskapliga publikationer** – inga registrerade kliniska prövningar finns för denna specifika indikation – och rör uteslutande pre-kliniska djurmodeller, vilket begränsar tillämpbarheten till veterinärmedicinska och experimentella forskningskontexter, inte human klinisk återanvändning.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | HIV-1-infektion (proteashämmare) |
| Förutsagd ny indikation | Simian immunodeficiency virus (SIV)-infektion |
| TxGNN-förutsägelsepoäng | 99,9% |
| Evidensnivå | L3 – Djurexperimentella studier och in vitro-data |
| Marknadsstatus i Sverige | Inte registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Ritonavir hämmar HIV-1:s aspartatproteas – ett enzym som är nödvändigt för att klyva Gag-Pol-polyproteinet till funktionella strukturproteiner och enzymer. Utan denna klyv bildas omogna, icke-infektiösa viruspartiklar och replikationscykeln bryts. Denna verkningsmekanism är välkarakteriserad och utgör grunden för ritonavirs etablerade roll i HIV-behandling, dels som aktiv proteashämmare och dels som farmakokinetisk förstärkare (CYP3A4-hämning) för andra proteashämmare.

SIV:s proteas delar hög tredimensionell strukturell homologi med HIV-1-proteaset. Det konserverade aktiva sätets aminosyratriplett (Asp25-Thr26-Gly27) är identisk mellan de båda virusarna. Direkta laboratorieexperiment (PMID 12709355; PMID 15040537) har mätt SIV:s känslighet för ritonavir via biokemiska metoder och bekräftat hämning av SIVmac239 med ett IC₅₀ på cirka 13 nM – en effektivitet jämförbar med, om än något lägre än, den mot HIV-1 (~25 nM i samma assay).

Mekanismen stöds vidare av flera in vivo-studier med rhesus- och cynomolgus-makaker (PMID 16973590; PMID 25033210; PMID 12951220; PMID 22737073), där ritonavir-innehållande kombinationsbehandling effektivt supprimerade SIV-virusnivåerna i blodet och förbättrade immunologiska parametrar. Det är dock av central vikt att understryka att **SIV är en sjukdom hos icke-mänskliga primater** – denna förutsägelse är relevant inom veterinärmedicin och experimentella primata HIV-modeller, men utgör inte ett klassiskt humanmedicinskt återanvändningsscenario.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|-----------|--------------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro (komparativ enzymassay) | Antimicrobial Agents and Chemotherapy | SIVmac239 hämmades av ritonavir med IC₅₀ ~13 nM; direkt biokemisk jämförelse mot HIV-1 bekräftar korsreaktivitet |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro (komparativ) | Antiviral Therapy | 16 godkända antiretroviraler testades mot HIV-2, SIV mac251/B670 och SHIV; SIV-stammer visade variabel men påvisbar känslighet för proteashämmare |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | In vivo (cynomolgus-makak) | Journal of Virology | Fyra SIVmac251-infekterade makaker behandlades med fyra-läkemedels-HAART under 7 dagar; snabb viral nedgång observerades med dynamik liknande HIV-1 hos människa |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | In vivo (rhesus-makak) | PLoS Pathogens | Högintensiv ART (innehållande ritonavir) i SIVmac251-infekterade makaker inducerade långvarig viral suppression och begränsade storleken på virusreservoaren |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | In vivo (kinesisk rhesus-makak) | PLoS ONE | SIV-infekterade makaker fick intensiv cART kombinerat med HDAC-hämmaren SAHA; ritonavir-baserad regim supprimerade virusnivåerna och utvärderades som HIV-reservoarmodell |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | In vivo (SHIV-makak) | Journal of Virological Methods | Oral Lopinavir/Ritonavir-baserad HAART i SHIV 89.6P-infekterade makaker supprimerade virusmängden och förbättrade CD8-subsetprofilen |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | In vivo (SHIV-modell) | Microbes and Infection | Konstruerade en ny SHIV med HIV-1-proteas i SIVmac-genomet; komplett viral hämning med proteashämmare bekräftar targetbarhet av primata virusproteaser |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | In vivo (NHP + human) | mBio | Lentivirusinfektion kvarstår i hjärnan trots effektiv ART i NHP-modeller och HIV-patienter; belyser gränserna för proteashämmarbaserad behandling mot virusreservoarer |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro | Antiviral Chemistry & Chemotherapy | Fluorokinolonderivat K-12 testades mot HIV-1 (inkl. ritonavir-resistenta stammar), HIV-2 och SIV; ritonavir användes som referenskontroll |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Grundforskning (biokemisk) | Journal of Virology | HIV-1 Vif-protein genomgår intraviriont proteolytisk bearbetning av viralt proteas; bidrar till förståelse av HIV/SIV-proteasets substratspecificitet och funktion |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Förutsägelsen har en välgrundad mekanistisk bas – SIV-proteasets strukturella homologi med HIV-1-proteaset är experimentellt verifierad, och ritonavir demonstrerar påvisbar hämmande aktivitet mot SIV i både in vitro- och in vivo-modeller. Eftersom SIV är en sjukdom exklusivt hos icke-mänskliga primater saknas ett direkt humanmedicinskt återanvändningsscenario; tillämpningen rör istället veterinärmedicinska eller pre-kliniska forskningskontexter, där bedömningsprocessen skiljer sig fundamentalt från human klinisk prövning.

**För att gå vidare krävs:**
- Klargörande av tillämpningskontext: veterinärmedicin (behandling av SIV-infekterade primater i fångenskap) eller experimentell djurmodell för HIV-kurationsresearch
- Inhämtning av fullständig MOA-dokumentation från DrugBank (DataGap DG002)
- Inhämtning av säkerhets- och kontraindikationsdata från produktresumén (DataGap DG001)
- Om human tillämpning avses (t.ex. HIV-1-behandling i Sverige): komplettera med EMA/FASS-godkännandeunderlag, eftersom läkemedlet saknar registrering i Sverige per tillgängliga data
- Uteslutning av övriga förutsägda indikationer (felin AIDS-liknande syndrom; neurodevelopmental disorder) som båda bedömts som Avvakta (L4 respektive L5) med svag eller obefintlig mekanistisk grund
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

