---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

Utmärkt – txgnn-pipeline-skillet är inläst och bekräftar att detta är ett Se (Sverige) TxGNN-projekt. Systemprompten innehåller den fullständiga rapportmallen (v5). Jag genererar nu rapporten direkt.

---

# Digoxin: Från hjärtsvikt och förmaksflimmer till Prinzmetal-angina

## Sammanfattning

Digoxin är ett välkänt kardioglykosid som traditionellt används för behandling av hjärtsvikt och förmaksflimmer. TxGNN-modellen förutsäger att det kan vara verksamt mot **Prinzmetal-angina** (variantangina orsakad av koronarkärlsspasm), men de mekanistiska sambanden pekar i motsatt riktning – Digoxins effekt på vaskulär glatt muskulatur kan snarare **förvärra** koronarkärlsspasmer än lindra dem. Evidensbasen är mycket begränsad, med **inga registrerade kliniska prövningar** och **2 publikationer** som för närvarande berör detta område.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Hjärtsvikt och förmaksflimmer (kardioglykosid) |
| Förutsagd ny indikation | Prinzmetal-angina (variantangina) |
| TxGNN-förutsägelsepoäng | 99,81% |
| Evidensnivå | L4 – Prekliniska/mekanismstudier |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanismdata saknas i detta evidenspaket. Baserat på känd farmakologi är Digoxin ett kardioglykosid vars primära verkningsmekanism är hämning av Na⁺/K⁺-ATPas-pumpen i hjärtmuskeln. Detta höjer den intracellulära kalciumkoncentrationen och förstärker myokardiets kontraktionskraft (positiv inotrop effekt). Läkemedlet har dessutom vagotona egenskaper som bromsar AV-nodal överledning och sänker hjärtfrekvensen, vilket motiverar dess användning vid förmaksflimmer.

Sambandet mellan Digoxins ursprungliga indikation och Prinzmetal-angina är dock mekanistiskt problematiskt. Prinzmetal-angina orsakas av transitoriska koronarkärlsspasmer i epikardiella kärl, och standardbehandlingen utgörs av kalciumkanalblockerare och nitrater – medel som **relaxerar** vaskulär glatt muskulatur. Digoxins hämning av Na⁺/K⁺-ATPas i kärlväggens glatta muskelceller kan paradoxalt nog **inducera** koronarkärlskontraktion genom depolarisering, vilket direkt motverkar det terapeutiska målet.

TxGNN-förutsägelsen baseras sannolikt på sjukdomsnätverkets biologiska kopplingar (t.ex. delade kardiovaskulära noder) snarare än ett faktiskt terapeutiskt samband. Befintlig litteratur stödjer inte behandlingseffekt vid Prinzmetal-angina och signalerar tvärtom en potentiell riskökning. Förutsägelsen bör tolkas som en **varningssignal** snarare än ett återanvändningstips.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Översikt | Acta Physiologica et Pharmacologica Bulgarica | Granskar cirkadiska rytmers påverkan på antihypertensiv behandling; indirekt relevant för dygnsvariation av anginaattacker |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Översikt/Mekanistisk | Chinese Medical Sciences Journal | Omvärdering av mekanism och behandling vid angina decubitus hos 30 patienter; fann ökad myokardial syreförbrukning och hemodynamiska förändringar innan attackdebut |

---

## Marknadsinformation Sverige

Digoxin är för närvarande **inte registrerat i Sverige**. Det finns inga godkännanden att redovisa.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- TxGNN-förutsägelsen för Digoxin vid Prinzmetal-angina är mekanistiskt motsägelsefull: Digoxins hämning av vaskulärt Na⁺/K⁺-ATPas kan förvärra koronarkärlsspasmer snarare än lindra dem, och förutsägelsen bör inte drivas vidare utan grundlig mekanistisk verifiering.

**För att gå vidare krävs:**
- Komplettering av fullständiga säkerhetsdata: kontraindikationer, varningar och DDI-profil (särskilt relevant given Digoxins smala terapeutiska index)
- Verifiering av officiell MOA-data via DrugBank API (DG002)
- Inhämtning av produktresumé/SPC för att bedöma kardiovaskulära kontraindikationer (DG001)
- Preklinisk kartläggning av Digoxins effekt på koronarkärlstonus *in vitro* eller i djurmodell
- Kritisk granskning av om TxGNN-sambandet speglar ett biologiskt nätverksartefakt eller ett reellt omvänt riskförhållande (potentiell kontraindikation snarare än ny indikation)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

