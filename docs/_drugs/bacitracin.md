---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

Jag använder `txgnn-pipeline`-skillet för att hantera TxGNN-rapportgenerering, och genererar nu rapporten baserat på Evidence Pack.

---

# Bacitracin: Från ytliga bakteriella infektioner till punktformig epitelial keratokonjunktivit

## Sammanfattning

Bacitracin är ett polypeptidantibiotikum som traditionellt används lokalt mot ytliga bakteriella hud- och sårinfektioner, framför allt orsakade av grampositiva bakterier. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **punktformig epitelial keratokonjunktivit (PEK)**, med ett förutsägelsepoäng på 99,999 %. Förutsägelsen saknar stöd från kliniska prövningar och publicerad litteratur, och den biologiska plausibiliteten bedöms som svag – PEK drivs primärt av virusinfektioner och toxiska reaktioner, inte av bakteriella patogener.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ytliga bakteriella hud- och sårinfektioner (topikalt) |
| Förutsagd ny indikation | Punktformig epitelial keratokonjunktivit |
| TxGNN-förutsägelsepoäng | 99,999 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Det finns för närvarande ingen detaljerad verkningsmekanismdata tillgänglig i evidensdatabasen. Baserat på känd information är Bacitracin ett polypeptidantibiotikum vars verkan bygger på hämning av bakteriell cellväggsyntes – det binder till lipidpyrofosfat-bärarmolekylen och blockerar transporten av peptidoglykana prekursorer genom cellmembranet. Läkemedlet är verksamt primärt mot grampositiva bakterier (t.ex. *Staphylococcus aureus*, betahemolyserande streptokocker) och används uteslutande som lokalt preparat på grund av systemisk nefrotoxicitet vid parenteralt bruk.

Kopplingen till punktformig epitelial keratokonjunktivit är mekanistiskt svag. PEK orsakas vanligtvis av adenovirusinfektion, toxiska reaktioner mot konserveringsmedel i ögondroppar, eller torra ögon – samtliga etiologier som faller utanför Bacitracinets antibakteriella verkningsspektrum. Som ögonsalva kan Bacitracin eventuellt ha ett understödjande värde för att förebygga sekundära bakteriella superinfektioner vid ögonytsjukdomar generellt, men detta utgör en kompletterande roll snarare än en riktad behandling mot PEK.

TxGNN:s extremt höga förutsägelsepoäng (99,999 %) förklaras sannolikt av rumslig grannarskap i kunskapsgrafen – ögonytesjukdomar (keratit, konjunktivit, PEK) klustrar tätt ihop som noder i grafen – snarare än av mekanistisk specificitet mot just PEK. Modellens höga poäng bör tolkas med försiktighet när den biologiska plausibiliteten är svag.

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
Trots ett extremt högt TxGNN-förutsägelsepoäng (99,999 %) saknar indikationen punktformig epitelial keratokonjunktivit all empirisk evidens (evidensnivå L5), och mekanistisk plausibilitet är svag. Bacitracinets antibakteriella verkningsmekanism är inte primärt relevant för PEK:s virala och toxiska etiologi.

> **Notering om bättre evidenserad indikation:** Bland de tio förutsagda indikationerna uppvisar **extern otit** (rang 4, TxGNN-poäng 99,969 %) den starkaste evidensbasen (L3 – historisk klinisk litteratur 1963–2007) med biologisk plausibilitet baserad på Bacitracinets effekt mot *S. aureus*. Nebacetin-kompositionen (bacitracin + neomycin) har sedan 1960-talet använts lokalt vid öroninfektioner. Extern otit förtjänar ett separat utredningsarbete med egna evidens- och säkerhetssektioner.

**För att gå vidare med PEK krävs:**
- Litteraturgenomgång av Bacitracin vid bakteriell ögonytepatologi och potentiella PEK-subgrupper med verifierad bakteriell komponent
- Klarläggande av lämplig okulär formulering och applikationsväg
- Komplettering av MOA-data via DrugBank API (DG002) och säkerhetsdata via produktresumé (DG001) som förutsättning för S1-säkerhetsinitialvärdering
- Inhämtning av TFDA/EMA/MPA regulatoriska data för att bedöma registreringsväg i Sverige
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

