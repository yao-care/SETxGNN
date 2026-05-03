---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

Läser in `txgnn-pipeline`-skillet. Det ger kontext om TxGNN-arbetsflödet, men inga specifika riktlinjer för rapportskrivning – det täcks av systemprompten. Jag fortsätter direkt med rapporten baserat på det tillhandahållna Evidence Pack-datat.

---

# Ketoprofen: Från inflammatorisk smärtbehandling till acromesomelic dysplasia (Hunter-Thompson-typ)

## Sammanfattning

Ketoprofen är ett välkänt icke-steroidt antiinflammatoriskt läkemedel (NSAID) med beprövad effekt vid smärta och inflammatoriska tillstånd, men det är för närvarande **inte marknadsförd i Sverige** och saknar lokala godkännanden. TxGNN-modellen förutsäger att det kan vara effektivt mot **acromesomelic dysplasia av Hunter-Thompson-typ**, en sällsynt genetisk skelettmissbildning orsakad av *GDF5*-mutation. Evidensstödet för denna specifika förutsägelse är mycket begränsat – **0 kliniska prövningar** och **0 publikationer** stöder riktningen, och den mekanistiska kopplingen bedöms som svag.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige; ketoprofen är internationellt etablerat som NSAID för smärta, feber och inflammation |
| Förutsagd ny indikation | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN-förutsägelsepoäng | 99,98% |
| Evidensnivå | L5 – Endast modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Ketoprofen är ett NSAID som klassiskt verkar som COX-1/COX-2-hämmare och reducerar syntesen av prostaglandiner, vilket dämpar smärta, feber och inflammation. Läkemedlet är i Europa etablerat för inflammatorisk ledvärk och muskuloskeletala smärttillstånd, men saknar specifika godkännanden i Sverige.

Acromesomelic dysplasia av Hunter-Thompson-typ orsakas av mutationer i *GDF5*-genen och leder till underutveckling av de distala delarna av extremiteterna. Sjukdomen är en rent genetisk strukturell skelettdefekt som uppstår under fosterstadiet och inte är medierad av prostaglandiner. Det finns ingen känd biologisk koppling mellan COX-hämning och korrigering av *GDF5*-relaterade skelettmissbildningar.

TxGNN-modellens höga poäng för denna indikation speglar troligen statistiska mönster i kunskapsgrafen snarare än en reell terapeutisk mekanism. Det bör noteras att bland de 10 förutsagda indikationerna är **spondyloartropi (rang 8)** det enda kandidatmålet med faktisk litteraturevidens (L4) och rekommendationen "Research Question". NSAID-klassen är förstahandsbehandling för spondyloartropi enligt ASAS/EULAR-riktlinjer, vilket gör den biologiska kopplingen avsevärt starkare för den indikationen.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

> **Notering:** För den lägre rankade indikationen *spondyloartropi (rang 8)* finns en relevant publikation: PMID [20470931](https://pubmed.ncbi.nlm.nih.gov/20470931/) (2010, Review/Case Series, *Annales de dermatologie et de venereologie*) om reaktiv artrit, som sannolikt behandlar NSAID som behandlingsalternativ. Denna indikation bedöms som L4 och "Research Question".

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivå L5 innebär att förutsägelsen uteslutande baseras på TxGNN-modellens beräkning utan stöd av kliniska prövningar eller litteratur. Den mekanistiska kopplingen till acromesomelic dysplasia är dessutom saknas helt – sjukdomen är en irreversibel genetisk skelettdefekt som inte kan påverkas av COX-hämning.

**För att gå vidare krävs:**
- Insamling av fullständig MOA-data och säkerhetsinformation från DrugBank (DG002) och produktresumé (DG001)
- Utforskning av **spondyloartropi (rang 8)** som det mest lovande kandidatmålet, givet befintlig litteraturevidens och stöd i internationella riktlinjer
- Kartläggning av ketoprofens befintliga europeiska marknadsföringstillstånd utanför Sverige för att fastställa godkända indikationer och säkerhetsprofil
- Sökning av fas 2/3-prövningar för ketoprofen vid spondyloartropi eller relaterade inflammatoriska ledsjukdomar
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

