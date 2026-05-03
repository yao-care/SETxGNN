---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

Använder **txgnn-pipeline**-skillet som bekräftelse av arbetsflöde — genererar nu utvärderingsrapporten för SeTxGNN (Sverige) baserat på Evidence Pack v4 för Daptomycin.

---

# Daptomycin: Från grampositiva bakterieinfektioner till artros

## Sammanfattning

Daptomycin är ett cykliskt lipopeptidantibiotikum som internationellt godkänts för behandling av allvarliga grampositiva bakterieinfektioner — däribland hud- och mjukdelsinfektioner, bakteremi och högersidig endokardit. TxGNN-modellen placerar **artros (osteoarthritis)** som den högst rankade nya indikationen med ett förutsägelsepoäng på 99,86 %, men sökningen finner **0 kliniska prövningar** och ingen litteratur som direkt studerar daptomycin som artrosbehandling — förutsägelsen bedöms vara ett topologiskt artefakt i kunskapsgrafen snarare än ett genuint behandlingssignal. Den vetenskapligt mer intressanta förutsägelsen i detta Evidence Pack är **reumatoid artrit (rank 2)**, där djurmodellstudier från 2025 påvisat anti-inflammatorisk effekt via NF-κB-hämning.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Grampositiva bakterieinfektioner (hud- och mjukdelsinfektioner, bakteremi, högersidig endokardit) |
| Förutsagd ny indikation | Artros (osteoarthritis) |
| TxGNN-förutsägelsepoäng | 99,86 % |
| Evidensnivå | L5 — Enbart modellförutsägelse, inga relevanta kliniska studier |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta Evidence Pack. Baserat på känd farmakologisk information är daptomycin ett cykliskt lipopeptid-antibiotikum (Cubicin®) som verkar genom att binda kalciumberoende till den bakteriella cellmembranen, vilket leder till membrandepolarisering och bakteriedöd. Det är primärt aktivt mot grampositiva patogener som *Staphylococcus aureus* (inklusive MRSA), streptokocker och enterokocker.

Kopplingen till **artros** saknar känd biologisk plausibilitet. Artrosens kärna patologi — degenerativ brosk­nedbrytning, subkondral benremodellering och synovial låggradig inflammation — involverar mekanismer (brosk­cell­apoptos, matrixmetalloproteinaser, IL-1β/TNF-α-driven synovit) som daptomycin inte har dokumenterade effekter på. Den litteratur som hittats handlar uteslutande om daptomycin som antibiotikum vid *osteoartikulära infektioner* — alltså bakteriella ledinfektioner, inte den degenerativa sjukdomen artros. Det höga TxGNN-poänget förklaras sannolikt av att kunskapsgrafen sammanlänkar "osteoartikulär infektion"-noder med "artros"-noder via delade anatomiska termer.

Däremot visar **rank 2-förutsägelsen (reumatoid artrit, RA)** ett mer intressant vetenskapligt spår: En djurmodellstudie från 2025 (PMID 39571268) demonstrerade att daptomycin dämpar kollagenin­ducerad artrit hos möss genom att hämma NF-κB-signalvägen och minska pro-inflammatoriska cytokiner (TNF-α, IL-1β, IL-6). Ytterligare strukturoptimering av det cykliska lipopeptid-skelettet för anti-RA-effekter undersöks aktivt (PMID 40923559). Dessa fynd är preliminära och utgör ännu inte grund för klinisk tillämpning.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Nedanstående publikationer hittades vid sökning på daptomycin + artros. **Observera:** Samtliga handlar om daptomycin som antibiotikum vid *bakteriella* led- och beninfektioner (osteoartikulära infektioner) — ingen studie undersöker daptomycin som behandling av degenerativ artros.

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Retrospektiv jämförande studie | J Antimicrob Chemother | Utfall med daptomycin vs standardbehandling vid osteoartikulära infektioner associerade med *S. aureus*-bakteremi |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Retrospektiv fallserie | J Antimicrob Chemother | Klinisk erfarenhet av daptomycin vid periprotetiska ledinfektioner i höft och knä; säkerhet och effekt utvärderades |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro-studie | J Antibiotics | In vitro-känslighet hos *S. aureus* och *S. epidermidis* isolerade från periprotetiska ledinfektioner, inklusive mot daptomycin |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Enkätstudie/register | Int J Antimicrob Agents | Enkät bland infektionsläkare (n=556) om antibiotikaval vid periprotetiska ledinfektioner; daptomycin ingick som alternativ |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Retrospektiv fallserie | Int Orthop | Säkerhet och effekt av högdos daptomycin + rifampicin vid grampositiva osteoartikulära infektioner |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Register/observationsstudie | Medicina Clinica | EU-CORE-registret: demografiska data och behandlingsutfall för daptomycin i spanska sjukhus, inkl. osteoartikulära infektioner |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Mikrobiologisk observationsstudie | Surg Infect | Mikrobiologisk profil av stafylokocker vid osteoartikulära infektioner under tio år; antibiotikaresistensmönster inkl. daptomycin |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Retrospektiv kohortstudie | Int J Antimicrob Agents | Effekt och säkerhet av högdos daptomycin (>6 mg/kg) vid komplicerade ben- och ledinfektioner samt implantatassocierade infektioner |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Fallrapport | Case Rep Orthop | Patient med artrosdiagnos remitterad för knäprotes visade sig ha septisk artrit (*C. striatum*); daptomycin användes i behandlingen |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Fallrapport | ASM Case Reports | Septisk artrit i nativled orsakad av *Corynebacterium propinquum*; patienter med befintlig ledsjukdom har ökad risk för hematogen seeding |

---

## Marknadsinformation Sverige

Daptomycin är **inte registrerat** hos Läkemedelsverket och saknar godkännande för den svenska marknaden. Inga produktgodkännanden finns att redovisa.

> Vid behov av daptomycin i Sverige hanteras detta via licensförfarande hos Läkemedelsverket.

---

## Säkerhetsaspekter

> Se produktresumén (SmPC) för fullständig säkerhetsinformation. Notera särskilt den välkända risken för **myopati och rabdomyolys** vid daptomycinanvändning — ett faktum som är särskilt relevant i samband med förutsägelsen om reumatoid artrit (rank 2), där kronisk administrering i en ny indikation skulle kräva noggrann säkerhetsgenomgång. En fallrapport (PMID 36693494) dokumenterar daptomycin-inducerad rabdomyolys som sekundärt utlöste akut giktattack via hyperurikemi.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Förutsägelsen för artros (rank 1) saknar biologisk plausibilitet och kliniskt stöd — litteraturen rör uteslutande daptomycins roll som antibiotikum vid bakteriella ledinfektioner, inte behandling av degenerativ artros. Förutsägelsepoänget förklaras av topologisk proximitet i kunskapsgrafen snarare än ett reellt behandlingssignal.

**Det mer lovande spåret är reumatoid artrit (rank 2, evidensnivå L4):**
Djurmodelldata från 2025 visar ett mekanistiskt samband via NF-κB/cytokin-hämning, men humandata saknas helt.

**För att gå vidare med reumatoid artrit som kandidat krävs:**
- Verifiering av anti-inflammatorisk effekt i ytterligare pre-kliniska modeller (t.ex. adjuvant artrit, humaniserade musmodeller)
- Farmakokinetisk analys: Daptomycin ges intravenöst och är inte oralt biotillgängligt — en fundamental barriär för kronisk RA-behandling
- Säkerhetsprofil vid upprepad/kronisk administrering med fokus på myotoxicitet och njurpåverkan
- Strukturoptimering av det cykliska lipopeptidskelettet för att separera anti-inflammatorisk effekt från antibiotisk/toxisk aktivitet (se PMID 40923559)
- Fullständig MOA-data från DrugBank API samt säkerhetsdata från Läkemedelsverkets produktresumé
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

