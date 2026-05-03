---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

Använder **txgnn-pipeline** för att säkerställa korrekt rapportformat för Sverige-deploymenten.

---

# Brivaracetam: Från fokal epilepsi till visuell epilepsi

## Sammanfattning

Brivaracetam (BRV) är ett antiepileptikum av tredje generationen som är godkänt internationellt (EMA/FDA) för behandling av fokala anfall, men ännu inte registrerat i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **visuell epilepsi** (inklusive ljuskänslig epilepsi), med ett förutsägelsepoäng på **99,5 %**. Stödet baseras på **0 direkta kliniska prövningar** och **19 publikationer** — varav merparten rör BRV:s effekt vid fokal epilepsi i allmänhet snarare än specifikt visuell epilepsi, vilket innebär att kopplingen för närvarande är mekanistiskt motiverad men inte kliniskt verifierad.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Fokal epilepsi — fokala anfall med eller utan sekundär generalisering (godkänt internationellt via EMA/FDA; ej registrerat i Sverige) |
| Förutsagd ny indikation | Visuell epilepsi (visual epilepsy) |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L3 — Observationsstudier / systematisk översikt (indirekt stöd) |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanismdata saknas i den aktuella datakällan. Baserat på den samlade litteraturen är Brivaracetam en selektiv ligand med hög affinitet för **synaptiskt vesikkelprotein 2A (SV2A)** — samma målmolekyl som levetiracetam, men med 15–30 gånger starkare bindningsaffinitet och markant bättre hjärnpenetration tack vare högre lipofili. Bindningen till SV2A hämmar synaptisk vesikkelcirkulering och dämpar därigenom repetitiv neuronal urladdning i epileptiska fokus.

Visuell epilepsi — som inkluderar fotokänslig epilepsi och visuellt utlösta anfallssyndrom — involverar hyperexcitabilitet i den visuella cortex. BRV:s breda SV2A-hämning bör teoretiskt sett kunna höja anfallströsklarna i denna region. Fotosensitivitetsmodellen (photoparoxysmal response, PPR) har sedan länge använts som proof-of-principle i BRV:s tidiga kliniska utveckling: en randomiserad crossover-studie (PMID 32949370) visade att BRV undertrycker PPR signifikant snabbare och mer effektivt än levetiracetam, vilket utgör indirekt mekanistiskt stöd för en effekt vid visuellt utlöst epilepsi.

Det direkta kliniska bevismaterialet för *visuell epilepsi* som primär indikation saknas emellertid helt i form av registrerade kliniska prövningar. Den befintliga litteraturen handlar om BRV:s effekt vid fokal epilepsi generellt, och sambandet till visuell epilepsi bygger på mekanistisk extrapolering snarare än riktad klinisk dokumentation.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | Fas III RCT | *Epilepsia open* | Adjunktiv BRV visade signifikant minskad anfallsfrekvens och god tolerabilitet hos vuxna asiatiska patienter med okontrollerade fokala anfall; dubbelblindat, placebokontrollerat. |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematisk översikt & metaanalys | *Frontiers in neurology* | BRV visade god effekt och säkerhet vid barnepilepsipatienter; stödjer BRV:s tolerabilitetsprofil jämfört med äldre antiepileptika. |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Narrativ översikt | *Advances in therapy* | Genomgång av BRV:s prekliniska profil och kliniska fördelar; bekräftar SV2A-mekanism med 15–30× högre affinitet än levetiracetam och överlägsen blod–hjärnbarriärpenetration. |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Översikt | *Journal of epilepsy research* | Sammanfattar BRV:s farmakologi, klinisk effekt och säkerhet i såväl kliniska prövningar som verklig klinisk praxis; bekräftar godkännande som mono- och tilläggsbehandling. |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Klinisk riktlinje | *BMJ* | Riktlinje för epilepsihandläggning under graviditet och amning; diskuterar BRV:s säkerhetsprofil i förhållande till andra antiepileptika. |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Mekanismöversikt | *Neuropharmacology* | Genomgång av verkningsmekanismer hos nuvarande antiepileptika; BRV:s SV2A-bindning och inverkan på synaptisk transmission beskrivs ingående. |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Klinisk effektöversikt | *Expert review of neurotherapeutics* | BRV:s effekt och säkerhet vid fokal epilepsi; jämförelse med levetiracetam och analys av BRV:s förbättrade CNS-penetration. |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Poolad säkerhetsanalys | *Epilepsy & behavior* | Djupgående säkerhetsanalys av adjunktiv BRV vid fokal epilepsi baserad på poolade kliniska prövningsdata; bekräftar god tolerabilitet. |
| [26664121](https://pubmed.ncbi.nlm.nih.gov/26664121/) | 2015 | Översikt | *Neuropsychiatric disease and treatment* | Tidig profil av BRV inför FDA/EMA-granskning; beskriver SV2A-mekanism och potentiell klinisk roll vid partiella anfall. |
| [38117319](https://pubmed.ncbi.nlm.nih.gov/38117319/) | 2024 | Klinisk översikt | *Intensive care medicine* | Genomgång av status epilepticus-hantering på IVA; nämner BRV bland nyare antiepileptika med gynnsam farmakokinetik. |

---

## Marknadsinformation Sverige

Brivaracetam är för närvarande **inte registrerat i Sverige**. Inga läkemedelsgodkännanden finns tillgängliga hos Läkemedelsverket. Läkemedlet marknadsförs som **Briviact®** i övriga EU-länder efter EMA-godkännande samt i USA efter FDA-godkännande, men saknar marknadsföringstillstånd på den svenska marknaden.

---

## Säkerhetsaspekter

Se produktresumén (SmPC) för Briviact® för fullständig säkerhetsinformation avseende varningar, kontraindikationer och läkemedelsinteraktioner.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots ett högt TxGNN-förutsägelsepoäng (99,5 %) och ett mekanistiskt plausibelt samband via SV2A-hämning i visuell cortex saknas direkta kliniska prövningar för visuell epilepsi som primär indikation. Den befintliga evidensen är indirekt och kan inte ensam motivera en riktad klinisk satsning på denna nischindikation.

**För att gå vidare krävs:**
- Prospektiv observationsstudie eller fallserie hos patienter med ljuskänslig eller visuellt utlöst epilepsi behandlade med BRV
- Direkta kliniska prövningar (Fas II) med visuell epilepsi som primärt utfall
- Registrering av Briviact® i Sverige via Läkemedelsverket
- Fullständig säkerhetsdokumentation (MPA/EMA produktresumé på svenska)

---

> **ℹ️ Notering om övriga förutsagda indikationer:**
> Rapporten fokuserar på den högst rankade TxGNN-förutsägelsen (visuell epilepsi, rang 1). Bland övriga indikationer har **status epilepticus** (rang 2, evidensnivå **L2**) ett betydligt starkare direkt evidensunderlag — inklusive 2 avslutade kliniska prövningar (NCT07163572: IV BRV vs. IV levetiracetam, n=152) och en systematisk översikt (PMID 32278203) — och rekommenderas prioriteras i en separat fördjupad utvärdering med beslut **Fortsätt med försiktighet**.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

