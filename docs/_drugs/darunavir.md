---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 4
---

# Darunavir
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

Using the `txgnn-pipeline` skill to guide report generation for this Swedish TxGNN drug repurposing evaluation.

---

# Darunavir: Från HIV-1-behandling till SIV-infektion (apors immunbristvirus)

## Sammanfattning

Darunavir är en HIV-1-proteashämmare som globalt används i kombinationsbehandling mot HIV-infektion, men som för närvarande inte är registrerat i Sverige. TxGNN-modellen förutsäger att det kan vara verksamt mot **SIV-infektion (simian immunodeficiency virus infection)** – en immunbristsjukdom hos icke-mänskliga primater som är nära besläktad med HIV. Förutsägelsen stöds av **4 vetenskapliga publikationer** från djurmodeller (NHP/SIV-modeller), men inga kliniska prövningar finns registrerade för denna specifika indikation.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | HIV-1-infektion (ej registrerat i Sverige; globalt känd indikation) |
| Förutsagd ny indikation | SIV-infektion (simian immunodeficiency virus infection) |
| TxGNN-förutsägelsepoäng | 99,97 % |
| Evidensnivå | L3 – Djurstudier (icke-mänskliga primater, NHP/SIV-modeller) |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Darunavir binder till det aktiva sätet på HIV-1:s aspartylproteas och blockerar viruspartikelns mognad – en nödvändig process för att producera infektiösa viruspartiklar. Utan fungerande proteas bildas omogenar, icke-infektiösa viruspartiklar och infektionen bromsas effektivt.

HIV och SIV (simian immunodeficiency virus) tillhör samma biologiska familj av lentivirus. De delar hög strukturell likhet i proteasenzymets aktiva säte, med en sekvenshomologi på uppskattningsvis ~60 %. Det innebär att Darunavirs hämningsmekanism är biokemiskt överförbar mellan arterna, och läkemedlet fungerar faktiskt som proteashämmare (PI) i multidrugregimer (cART) som används i NHP-djurmodeller för HIV/AIDS-forskning.

Det bör framhållas att detta snarare representerar en **artmässig tillämpning av en redan känd mekanism** än en klassisk läkemedelsåteranvändning mot en ny indikation. Förutsägelsen bekräftar Darunavirs biologiska relevans i primatmodeller men identifierar ingen ny human sjukdomsindikation.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Djurstudie (NHP/SIV) | AIDS Research and Human Retroviruses | Utvärderade två nya cART-regimer (inkl. PI-komponent) i SIVmac239-infekterade rhesus-makaker; båda regimerna supprimerade virusreplikationen till kliniskt relevanta nivåer |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Djurstudie (NHP/SIV) | PLoS Pathogens | Intensifierad flerdrogbehandling (inkl. NRTI + PI + integrasehämmare) i SIVmac251-infekterade makaker gav långvarig virussuppression och begränsad virusreservoar |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Djurstudie (NHP/SIV) | PLoS ONE | cART kombinerat med HDAC-hämmaren SAHA i SIV-infekterade kinesiska rhesus-makaker; PI ingick i bakgrundsregimen och bidrog till stabil virussuppression |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Djurstudie (NHP/SIV) | AIDS (London, England) | Guldföreningen auranofin kombinerat med ART (inkl. PI) minskade lentiviral reservoar i CD4 T-celler in vivo och inducerade viruskontroll efter ART-avbrott i SIV-modell |

---

## Övriga förutsägda indikationer

TxGNN identifierade ytterligare tre kandidatindikationer. Samtliga bedöms som **Avvakta** av följande skäl:

| Rang | Indikation | Poäng | Evidensnivå | Kommentar |
|------|-----------|-------|-------------|-----------|
| 2 | Kattens förvärvade immunbristsyndrom (FIV) | 99,97 % | L4 | FIV-proteas skiljer sig strukturellt tydligt från HIV-proteas; den enda registrerade prövningen (NCT02770508) rör human HIV-behandling och är felanpassad av datapipelinen |
| 3 | Neurodevelopmentalt störning med ataktisk gång, utebliven tal och minskad kortikal vit substans | 99,97 % | L5 | Ingen känd mekanistisk koppling; inga kliniska prövningar och ingen litteratur |
| 4 | Familjär kombinerad hyperlipidemi (inaktuell term) | 99,19 % | L5 | ⚠️ Omvänd mekanism: HIV-proteashämmare är kända för att *orsaka* lipidrubbningar som biverkning; dessutom är sjukdomsbeteckningen markerad som inaktuell (obsolete) i ontologin |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Darunavirs effekt i NHP/SIV-modeller är mekanistiskt välgrundad och stöds av fyra djurstudier (evidensnivå L3), men inga humana kliniska prövningar finns för SIV-indikationen. Förutsägelsen bekräftar snarast läkemedlets kända verkningsmekanism i en primatkontext än pekar ut en kliniskt exploaterbar ny indikation. Övriga förutsedda indikationer saknar evidens, uppvisar mekanistiska motsägelser eller baseras på inaktuella diagnostermer.

**För att gå vidare krävs:**
- Klargörande av det kliniska syftet: är NHP/SIV-modellerna avsedda som surrogatmodell för human HIV-forskning, eller finns ett fristående veterinärmedicinskt intresse?
- Inhämtning av fullständig säkerhetsinformation (varningstext, kontraindikationer och läkemedelsinteraktioner)
- Mekanistisk valideringsstudie specifikt för FIV-proteashämning om kattmedicinsk tillämpning är av intresse
- Verifiering mot aktuella ontologibeteckningar innan vidare analys av indikation 4 (inaktuell term)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

