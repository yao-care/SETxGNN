---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

Använder **txgnn-pipeline**-skillet för att kontextualisera rapporten. Nu genererar jag den svenska utvärderingsrapporten baserad på Evidence Pack för SUNITINIB.

---

# Sunitinib: Från njurcellscancer till liposarkom

## Sammanfattning

Sunitinib är en multimålriktad tyrosinkinasinhibitor (TKI) som globalt är godkänd för behandling av avancerad njurcellscancer (RCC), imatinibresistent gastrointestinal stromacellstumör (GIST) samt progressiv pankreatisk neuroendokrin tumör (pNET) – men saknar för närvarande registrering i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara verksamt mot **liposarkom**, med stöd av delade signaleringsvägar via VEGFR och PDGFR som är aktiva i båda tumörtyperna. Förutsägelsen backas av **3 kliniska prövningar** och **9 publikationer** som direkt undersöker sunitinib vid mjukdelssarkom, varav liposarkom är en av de studerade histologierna.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Njurcellscancer (global godkänning; ej registrerat i Sverige) |
| Förutsagd ny indikation | Liposarkom |
| TxGNN-förutsägelsepoäng | 99,87% |
| Evidensnivå | L2 – Minst en avslutad Fas 2-prövning |
| Marknadsstatus i Sverige | Inte upptagit |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Formell verkningsmekanismdata (MOA) saknas i detta evidenspaket. Baserat på tillgänglig information är sunitinib en multimålriktad TKI vars primära verkningsmekanism vid njurcellscancer utgörs av hämning av VEGFR1/2/3 och PDGFR-α/β: VHL-mutation leder till HIF-ackumulering och VEGF/PDGF-överstimulering av tumörangiogenes, och sunitinib bryter direkt denna signalkedja. Effekten vid RCC är kliniskt väl bevisad och utgör grunden för läkemedlets globala godkännande.

Liposarkom är biologiskt beroende av tumörangiogenes via VEGFR/PDGFR-signalering. Dedifferentierat liposarkom uppvisar visserligen vanligtvis CDK4/MDM2-amplifiering som primär drivande förändring, men tumörmikromiljön förblir beroende av VEGFR-aktivering. PDGFR-α/β uttrycks dessutom i liposarkomets stromaceller, vilket ger sunitinibs dubbla hämning av VEGFR och PDGFR ett direkt mekanistiskt stöd vid denna tumörtyp.

Kopplingen mellan den ursprungliga indikationen och liposarkom vilar på det delade beroendet av angiogen VEGFR/PDGFR-signalering. Sunitinibs dokumenterade aktivitet vid GIST – en annan PDGFR-driven tumörtyp – stärker ytterligare analogin till PDGFR-uttryckande mjukdelssarkom, och de genomförda Fas 2-prövningarna vid mjukdelssarkom bekräftar att denna mekanistiska övergång är kliniskt testbar.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|--------------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Fas 2 | Avslutad | 48 | Öppen singelcenterstudie med sunitinib vid metastatiskt/icke-resektabelt mjukdelssarkom (STS), specifikt inkluderande leiomyosarkom, liposarkom, fibrosarkom och malignt fibrohistiocytom. Behandling gavs oralt en gång dagligen dagar 1–28 per 42-dagarscykel tills progression eller toxicitet. |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Fas 2 | Avslutad | 53 | Multicenter Fas 2-studie med kontinuerlig sunitinib-dosering vid non-GIST-sarkom (inkl. liposarkom). Sunitinib kan stoppa tumörtillväxt genom att blockera enzymer för celltillväxt och tumörblodflöde. Ger tvärhistologiska data för sunitinib i mjukdelssarkom. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fas 2 | Avslutad | 131 | SARC024-protokollet studerade regorafenib (ej sunitinib) vid utvalda sarkomsubtyper. Studiens bakgrund bekräftar att sorafenib, sunitinib och pazopanib uppvisar aktivitet vid mjukdelssarkom, vilket motiverar undersökning av ytterligare TKI-hämmare i denna grupp. Ger indirekt stöd för TKI-klassen. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Fas 2-studie | International Journal of Cancer | Singelcenter Fas 2-studie med sunitinib specifikt vid leiomyosarkom, liposarkom och malignt fibrohistiocytom. Undersökte säkerhet och effekt av sunitinib som multimålriktad RTK-inhibitor vid dessa tre vanliga STS-subtyper. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Fallrapport | Anticancer Research | Dokumenterar långvarig klinisk nytta av sunitinib vid kraftigt förbehandlat metastatiskt liposarkom – stödjer aktivitet med sunitinib även i sent behandlingsskede och vid recidiv. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Översikt | Cancers | Genomgång av genetiska, epigenetiska och transkriptomförändringar vid liposarkom med relevans för målriktad behandlingsval; belyser VEGFR/PDGFR-banan som potentiellt terapeutiskt mål i samtliga liposarkomsubtyper. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Översikt | Annals of Oncology | Beskriver histologistyrd behandling av mjukdelssarkom och bekräftar evidens för TKI-aktivitet, med trabectedin vid liposarkom och sunitinib/sorafenib som TKI-alternativ vid flera STS-subtyper. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Översikt | Expert Review of Anticancer Therapy | Sammanfattar nya terapier vid vuxna STS; evidensläget för målriktade alternativ per subtyp, inkl. TKI-aktivitet vid liposarkom och angiosarkom. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Översikt | Magyar Onkologia | Diskuterar histologidriven behandling av mjukdelssarkom med cytotoxika och målriktade läkemedel; bekräftar sunitinibs roll i TKI-arsenalen vid avancerat STS. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Molekylär studie | Oncotarget | Helgenomsekvensering av extraskelettalt myxoidt kondrosarkom; utvärderar prediktiva faktorer för sunitinib-nytta i TKI-känsliga sarkomsubtyper och identifierar potentiella resistensmekanismer. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Studieprotokoll | BMC Cancer | REGOSARC-studieprotokoll för regorafenib vid avancerat STS; bakgrundsdata bekräftar att angiogena signalvägar (inkl. VEGFR/PDGFR) spelar nyckelroll i sarkombiologi och motiverar TKI-strategier. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Klinopatologisk studie | American Journal of Surgical Pathology | Analys av 25 fall av myxoidt inflammatoriskt myofibroblastiskt sarkom; belyser den ökande identifieringen av targetbara molekylära förändringar i sarkomsubtyper, relevant för TKI-stratifiering. |

---

## Cytotoxicitet

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Målriktad terapi – multimålriktad tyrosinkinasinhibitor (TKI); hämmar VEGFR1/2/3, PDGFR-α/β, KIT, FLT3, CSF-1R och RET |
| Myelosuppressionsrisk | Medel – neutropeni (inkl. grad 3–4 hos ~10–15%) och trombocytopeni är kända dosbegränsande toxiciteter; anemi förekommer också |
| Emetogenicitetsklassificering | Låg till medel (oral TKI; lägre emetogen potential jämfört med konventionell cytostatikabehandling; illamående grad 1–2 vanligt) |
| Övervakningspunkter | Fullständigt blodstatus (CBC) inkl. differentialräkning, leverfunktion (ALAT/ASAT/bilirubin), njurfunktion (kreatinin), sköldkörtelfunktion (TSH), blodtryck, EKG (QTc-förlängning), elektrolyter (kalium, magnesium) |
| Hanteringsskydd | Ja – sunitinib klassas som cytotoxiskt läkemedel; hantering kräver skyddshandskar; kapslar ska inte krossas eller öppnas; avfallshantering enligt rutiner för cytotoxiskt avfall |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Fas 2-prövningar med direkt inklusion av liposarkom-patienter är genomförda och avslutade (L2-evidens), en fallrapport dokumenterar långvarig klinisk nytta, och den mekanistiska kopplingen via VEGFR/PDGFR-hämning är biologiskt väl motiverad. Effektstorleken vid liposarkom tycks dock vara begränsad jämfört med njurcellscancer, och ingen Fas 3-studie vid liposarkom existerar.

**För att gå vidare krävs:**
- **Säkerhetsdata**: Ladda ned och analysera aktuell produktresumé (SmPC/EPAR) för sunitinib för att fastställa fullständiga varningar, kontraindikationer och kliniskt relevanta läkemedelsinteraktioner
- **Registreringsstatus i Sverige**: Bekräfta nuläget hos Läkemedelsverket – sunitinib (Sutent®) är godkänt av EMA men saknar nationell registreringsstatus enligt tillgängliga data
- **Subgruppsanalys**: Identifiera och samla efficacydata specifikt för dedifferentierat respektive myxoidt liposarkom från befintliga Fas 2-studier (NCT00400569, NCT00474994) för att uppskatta histologispecifik responsfrekvens
- **Biomarkörsselektion**: Utvärdera VEGFR/PDGFR-expressionsstatus och CDK4/MDM2-amplifieringsstatus som potentiella prediktiva biomarkörer för att identifiera patientundergrupper med högst sannolikhet för behandlingssvar
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

