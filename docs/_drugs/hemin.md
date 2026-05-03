---
layout: default
title: Hemin
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Hemin
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

Jag använder `txgnn-pipeline`-skillet och producerar nu rapporten baserat på Evidence Pack JSON.

---

# Hemin: Från akut hepatisk porfyri till trombocytopenisk purpura

## Sammanfattning

Hemin (järnprotoporfyrin IX) används etablerat för att behandla akuta attacker vid akut hepatisk porfyri (AHP) genom att hämma ALAS1-enzymet och därigenom minska ackumulationen av neurotoxiska porfyrinprekursorer. TxGNN-modellen förutsäger att hemin kan vara effektivt mot **trombocytopenisk purpura** via induktion av hemoxygenas-1 (HO-1) och antiinflammatorisk immunmodulering. Förutsägelsen saknar för närvarande stöd av kliniska prövningar eller direkt litteratur – evidensnivån är **L5** (enbart modellförutsägelse).

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Akut hepatisk porfyri (ej godkänd i Sverige) |
| Förutsagd ny indikation | Trombocytopenisk purpura |
| TxGNN-förutsägelsepoäng | 99,79 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej godkänd (0 godkännanden) |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Hemin verkar via två sammankopplade mekanismer. Den primära effekten vid porfyri är återkopplingshämning av ALAS1, det hastighetsbegränsande enzymet i hembiosyntesen, vilket minskar ackumulationen av neurotoxiska porfyrinprekursorer ALA och porfobilinogen. Den sekundära mekanismen – och den som är relevant för trombocytopenisk purpura – är induktion av hemoxygenas-1 (HO-1), ett stressinducerbart enzym med potenta antiinflammatoriska och immunmodulerande egenskaper.

Mekanistisk länk till trombocytopenisk purpura: HO-1 katalyserar nedbrytningen av hem till kolmonoxid (CO), biliverdin och fritt järn. CO aktiverar löslig guanylatcyklas och höjer cGMP-nivåerna, vilket hämmar blodplättaktivering och aggregation. Därutöver kan HO-1/biliverdin-axeln teoretiskt dämpa den immunmedierade trombocytförstöringen som är den centrala patofysiologin vid immuntrombocytopenisk purpura (ITP), genom reglering av Th1/Th2-balansen och minskad oxidativ stress.

Det mekanistiska sambandet är logiskt uppbyggt men förblir hittills rent teoretiskt. Ingen klinisk prövning eller preklinisk studie med hemin specifikt vid trombocytopenisk purpura har återfunnits. TxGNN-modellens höga poäng (99,79 %) kan delvis förklaras av grafnätverkets topologi – blodsjukdomsnoder och trombocytopeninoder delar grannskapet med hemin-/porfyrin-noder i kunskapsgrafen, vilket kan ge upphov till ett närhetsbetingat högt poängvärde utan ett verkligt terapeutiskt samband. En ITP-musmodell rekommenderas som obligatoriskt nästa steg för mekanistisk validering.

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
- Förutsägelsen baseras uteslutande på TxGNN-modellens graftraversering (L5, beslutssteg S0) utan stöd av kliniska prövningar, djurstudier eller klinisk litteratur specifikt för trombocytopenisk purpura. Det föreslagna mekanistiska sambandet via HO-1/CO/cGMP-axeln är biologiskt plausibelt men saknar varje form av experimentell bekräftelse.

**För att gå vidare krävs:**
- Preklinisk validering i ITP-musmodell (t.ex. anti-CD41-antikroppsinducerad trombocytopenimodell) med HO-1-induktionsmätning och trombocyträkning som primärt utfall
- Fastställande av dosregim som uppnår tillräcklig HO-1-induktion utan toxisk ackumulering av fritt hem
- Systematisk litteraturöversikt avseende andra HO-1-inducenters effekter vid immunmedierad trombocytopeni som surrogatbevis
- Insamling av hemins fullständiga säkerhetsprofil (varningar, kontraindikationer och interaktionsdata saknas i nuläget)
- Notera: Bland de 10 förutsagda indikationerna har **hemofili (rank 2, L4)** starkare mekanistiskt stöd – en direkt djurstudie (PMID [19890094](https://pubmed.ncbi.nlm.nih.gov/19890094/)) visar att HO-1-induktion reducerar anti-FVIII-immunsvar i FVIII-bristfälliga möss. Hemofili-spåret bör prioriteras parallellt som den translationellt mognare hypotesen.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

