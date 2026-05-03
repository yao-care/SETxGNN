---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

Texten nedan är den fullständiga utvärderingsrapporten baserad på Evidence Pack-JSON:t.

---

# Naproxen: Från smärt- och inflammationsbehandling till brachydactyly-syndactyly syndrome

## Sammanfattning

Naproxen är ett välkänt icke-steroidalt antiinflammatoriskt läkemedel (NSAID) som kliniskt används för behandling av smärta, inflammation och feber. TxGNN-modellen förutsäger att det kan vara effektivt mot **brachydactyly-syndactyly syndrome** – ett sällsynt medfött missbildningssyndrom som påverkar finger- och tåutvecklingen. Det saknas dock helt stödjande evidens: **inga kliniska prövningar** och **inga publikationer** identifierades, vilket placerar förutsägelsen på lägsta evidensnivå (L5).

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej specificerad i tillgängliga regulatoriska data |
| Förutsagd ny indikation | Brachydactyly-syndactyly syndrome |
| TxGNN-förutsägelsepoäng | 99,35 % |
| Evidensnivå | L5 – Enbart modellförutsägelse |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i Evidence Pack. Baserat på känd farmakologisk information är Naproxen ett NSAID som hämmar cyklooxygenas (COX-1 och COX-2), vilket minskar prostaglandinsyntesen och därigenom dämpar smärta och inflammation.

Brachydactyly-syndactyly syndrome är ett sällsynt medfött syndrom som kännetecknas av förkortade fingrar (brachydaktyly) i kombination med sammanvuxna fingrar (syndaktyly). Tillståndet orsakas av mutationer i gener som *HOXD* och *GJA1*, vilka reglerar embryonal extremitetsutveckling. Det handlar alltså om en strukturell embryonal defekt, inte en inflammatorisk sjukdom.

Det saknas kända mekanistiska kopplingar mellan COX-hämning och genetiska utvecklingsdefekter av detta slag. TxGNN:s förutsägelse baseras sannolikt på grafnärhet i kunskapsgrafen – d.v.s. att Naproxen och sjukdomen råkar dela gemensamma grannar i grafen – snarare än en biologiskt förankrad mekanism. Förutsägelsen bedöms som potentiellt falsk positiv.

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
Samtliga fyra förutsagda indikationer (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type och brachyolmia-amelogenesis imperfecta syndrome) klassificeras som L5 – enbart modellförutsägelse utan något som helst kliniskt eller literaturmässigt stöd. Den mekanistiska länken mellan Naproxens COX-hämning och dessa genetiskt betingade skelett- och utvecklingsdefekter bedöms som mycket svag, och förutsägelserna är sannolikt artefakter från kunskapsgrafsstrukturen.

**För att gå vidare krävs:**
- Komplettering av Naproxens säkerhetsprofil via produktresumé och DrugBank (nuvarande data saknas helt)
- Litteratursökning i specialiserade databaser för sällsynta sjukdomar (Orphanet, OMIM, GeneReviews) för att utesluta icke-indexerad evidens
- Mekanistisk analys av om prostaglandinvägen har dokumenterade kopplingar till *HOXD*-, *GJA1*- eller *GDF5*-signalering i embryonal benutveckling
- Expertgranskning av genetiker och/eller specialist på sällsynta skelettsjukdomar innan eventuell vidare utredning motiveras
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

