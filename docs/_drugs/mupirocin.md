---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 2
---

# Mupirocin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
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

Använder **txgnn-pipeline** för att skapa läkemedelsåteranvändningsrapporten för Mupirocin.

---

# Mupirocin: Från bakteriell hudinfektion till pleural empyem

## Sammanfattning

Mupirocin är ett topikalt antibiotikum som primärt används för behandling av bakteriella hudinfektioner – framför allt impetigo och nasal MRSA-dekolonisering. TxGNN-modellen förutsäger att det kan vara effektivt mot **pleural empyem** (var i lungsäcken), med ett prediktionspoäng på 99,5 %. Det saknas dock helt kliniska prövningar och vetenskapliga publikationer som stöder denna riktning – evidensen är uteslutande baserad på modellförutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Bakteriell hudinfektion (impetigo), MRSA-dekolonisering – ej registrerad i Sverige |
| Förutsagd ny indikation | Pleural empyem |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L5 – Endast modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd farmakologisk information verkar Mupirocin genom att hämma **isoleucyl-tRNA-syntetas (IleRS)** – ett enzym som är nödvändigt för bakteriell proteinsyntesis. Denna mekanism ger stark antibakteriell aktivitet mot *Staphylococcus aureus* (inklusive MRSA) och *Streptococcus pyogenes*.

Pleural empyem orsakas ofta av just de patogener som Mupirocin är aktivt mot: *S. aureus* (inklusive MRSA) och streptokocker. Det finns alltså en mekanistisk koppling i att samma bakteriestammar förekommer vid både de ursprungliga hudindikationerna och den förutsagda nya indikationen – vilket sannolikt förklarar det höga TxGNN-poänget via gemensam patogenöverläppning i kunskapsgrafen.

Den avgörande praktiska barriären är dock **läkemedelsformen**. Mupirocin finns enbart som topikalt preparat (kräm/salva) med en systemisk biotillgänglighet på under 1 %. Preparatet kan inte nå pleuralutrymmet i terapeutiska koncentrationer via befintlig beredningsform. Klinisk behandling av pleural empyem kräver systemiska antibiotika (t.ex. vankomycin vid MRSA) kombinerat med pleuraldränage. Det finns inga studier på intrapleural instillation av Mupirocin, och det höga prediktionspoänget bedöms återspegla patogenöverläppning snarare än ett realistiskt behandlingsalternativ.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Trots ett högt TxGNN-prediktionspoäng (99,5 %) är evidensnivån L5 – utan ett enda kliniskt prövning eller stödjande publikation. Den fundamentala barriären är att Mupirocin enbart finns som topikalt preparat med extremt låg systemisk biotillgänglighet, vilket gör det farmakologiskt olämpligt för behandling av djupgående infektioner som pleural empyem i nuvarande beredningsform.

**För att gå vidare krävs:**
- Preklinisk dokumentation av en systemisk eller intrapleural formulering av Mupirocin
- Farmakokinetikdata som visar tillräckliga läkemedelskoncentrationer i pleuravätskan
- Säkerhetsprofil för icke-topikala beredningsformer
- Jämförande effektstudie mot etablerad standardbehandling (systemiskt vankomycin + pleuraldränage)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

