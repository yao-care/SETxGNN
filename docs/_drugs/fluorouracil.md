---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

Bra. Jag har bekräftat att detta är ett TxGNN-projekt (Se = Sverige). Nu genererar jag rapporten baserat på Evidence Pack JSON.

---

# Fluorouracil (5-FU): Från cancerbehandling till botryoid embryonal rabdomyosarkom i vagina

## Sammanfattning

Fluorouracil (5-FU) är ett klassiskt fluoropyrimidin-antimetabolit-cytostatikum med bred klinisk användning inom onkologin – framför allt vid kolorektal-, magsäcks- och pankreascancer – men saknar registrerade godkännanden i Sverige. TxGNN-modellen förutsäger att det kan vara effektivt mot **botryoid embryonal rabdomyosarkom i vagina**, ett extremt sällsynt pediatriskt tumörtillstånd. Förutsägelsen stöds av **0 kliniska prövningar** och **0 publikationer** för denna specifika indikation, vilket innebär att evidensunderlaget är otillräckligt för vidare utredning i nuläget.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige (5-FU används kliniskt vid kolorektal-, magsäcks- och pankreascancer) |
| Förutsagd ny indikation | Botryoid embryonal rabdomyosarkom i vagina |
| TxGNN-förutsägelsepoäng | 99,75% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanismdata (MOA) saknas i detta datapaket. Baserat på känd farmakologi är fluorouracil en antimetabolit ur fluoropyrimidingruppen. Dess primära verkningsmekanism bygger på hämning av enzymet tymidylatsyntetas (TS), vilket blockerar omvandlingen av deoxyuridylat (dUMP) till deoxytymidylat (dTMP) – ett nyckelsteg i DNA-syntesen. Därutöver inkorporeras aktiva metaboliter av 5-FU i cellulär RNA och DNA, vilket stör cellernas funktion. Dessa mekanismer leder till hämning av celldelning i snabbväxande celler, vilket är grunden för 5-FU:s brett etablerade cytotoxiska effekt.

Botryoid embryonal rabdomyosarkom i vagina är en undertyp av rabdomyosarkom (RMS) som utgår från skelettmuskelprogenitorceller och drabbar huvudsakligen barn under fem år. Den internationella standardbehandlingen är VAC-regimen (vinkristin + aktinomycin D + cyklofosfamid), med tillägg av strålbehandling vid behov. Fluorouracil ingår inte i något etablerat behandlingsprotokoll för RMS, vare sig som förstahandsval eller salvage-terapi, och det saknas känd specifik biologisk motivering för att 5-FU:s TS-hämning skulle ha mekanistiska fördelar gentemot just denna tumörtyp jämfört med VAC:s komponenter.

Det höga TxGNN-poänget (99,75%) bör tolkas med stor försiktighet. Alla tio topprankade förutsägelser i detta paket tillhör RMS-klustret eller en besläktad sarkomgrupp, vilket tyder på att poängen speglar spridningseffekter i kunskapsgrafen via delade grannoder snarare än ett äkta biologiskt signal för denna sällsynta undertyp. Det fullständiga avsaknaden av kliniska prövningar och litteratur bekräftar att förutsägelsen inte är handlingskraftig i nuläget.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Cytotoxicitet

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Konventionellt cytotoxiskt läkemedel – antimetabolit (fluoropyrimidin) |
| Myelosuppressionsrisk | Medel – kan orsaka leukopeni, neutropeni och trombocytopeni, framför allt vid bolusadministration; kontinuerlig IV-infusion ger lägre hematologisk toxicitet men högre risk för hand-fotsyndrom (palmar-plantar erytrodysestesi) |
| Emetogenicitetsklassificering | Låg till medel – varierar beroende på doseringsregim; IV bolus har högre emetogen potential än kontinuerlig infusion |
| Övervakningspunkter | Fullständigt blodstatus (CBC) inkl. differentialräkning; lever- och njurfunktionsprover; DPD-enzymstatus (dihydropyrimidindehydrogenas) – patienter med DPD-brist löper kraftigt ökad risk för livshotande toxicitet och bör testas innan behandling |
| Hanteringsskydd | Ja – klassificeras som cytotoxiskt läkemedel och kräver skyddsåtgärder vid beredning, administrering och avfallshantering enligt cytostatikaföreskrifter (AFS 2005:5) |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivån är L5 (enbart TxGNN-modellförutsägelse) utan stöd från kliniska prövningar eller publicerad litteratur för denna indikation. Den biologiska kopplingen är spekulativ och standardbehandlingen (VAC-regimen) för botryoid embryonal RMS i vagina är väletablerad och involverar inte fluorouracil.

**För att gå vidare krävs:**
- Prekliniska in vitro-studier av 5-FU mot botryoid RMS-cellinjer för att etablera biologisk motivering
- Klargörande av varför 5-FU:s TS-hämning skulle erbjuda fördelar utöver etablerad VAC-behandling
- Komplettering av säkerhetsdata: fullständig produktresumé, kontraindikationer och varningsprofil (DPD-brist är särskilt relevant i pediatrisk population)
- Granskning av om 5-FU förekommer i något pediatriskt RMS-salvage-protokoll för att utesluta exkludering av faktisk klinisk användning från litteratursökningen
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

