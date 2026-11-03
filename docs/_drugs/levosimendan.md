---
noindex: true
sitemap: false
layout: default
title: Levosimendan
parent: Endast modellprediktion (L5)
nav_order: 80
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-03
predicted_indications: []
---

# Levosimendan
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **0** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

## LEVOSIMENDAN: Bedömningen ofullständig — inga TxGNN-förutsägelser tillgängliga
{: .text-alpha }

## Sammanfattning

Levosimendan är en inodilatator/kalciumsensibiliserare som används kliniskt vid akut dekompenserad hjärtsvikt på flera europeiska marknader.
Underlaget innehåller för närvarande **inga TxGNN-förutsägelser för läkemedelsrepositionering** för denna substans,
och två blockerande dataluckor — saknade varningar från produktresumén och saknade data om verkningsmekanism — gör att en standardmässig repositioneringsbedömning inte kan slutföras.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Akut dekompenserad hjärtsvikt (känd klinisk användning) |
| Förutsagd ny indikation | Inga förutsägelser tillgängliga i detta underlag |
| TxGNN-förutsägelsepoäng | — |
| Evidensnivå | — (kan inte fastställas) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 10 av 10) |
| Antal godkännanden | 10 (giltiga: 10) |
| Rekommenderat beslut | **Avvakta** |

---

## Varför bedömningen inte kan slutföras

Tre oberoende hinder gör att detta underlag inte kan gå vidare genom det standardmässiga repositioneringsflödet:

**1. Inga TxGNN-förutsägelser (`predicted_indications: []`)**
Modellen har ännu inte genererat kandidatindikationer för DB00922. Utan ett poängsatt sjukdomsmål finns ingen repositioneringshypotes att bedöma, och inga efterföljande avsnitt (evidens från kliniska prövningar, litteraturbevis, mekanistisk rimlighet) kan fyllas i.

**2. Saknade säkerhetsdata från produktresumén (datalucka DG001 — blockerande)**
Varningar och kontraindikationer har inte hämtats. Detta klassas som en *blockerande* lucka: den hindrar det obligatoriska säkerhetsscreeningsteget S1 och innebär att inget säkerhetsavsnitt kan skrivas.

**3. Saknad verkningsmekanism (datalucka DG002 — hög)**
Utan bekräftade verkningsmekanismdata från DrugBank kan det mekanistiska rimlighetsresonemang som bär upp avsnittet ”Varför är denna förutsägelse rimlig?” inte byggas upp.

---

## Säkerhetsaspekter

Alla säkerhetsfält (viktiga varningar, kontraindikationer, läkemedelsinteraktioner) gav inga data i detta underlag. Se den godkända produktresumén för säkerhetsinformation när den har hämtats.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Underlaget för LEVOSIMENDAN är strukturellt ofullständigt: TxGNN-modellen har inte gett någon repositioneringsförutsägelse, och två dataluckor (saknade säkerhetsdata och saknad verkningsmekanism) har flaggats som blockerande respektive hög allvarlighetsgrad. Ingen rekommendation om repositionering kan ges förrän dessa uppgifter finns tillgängliga.

**För att gå vidare krävs:**

- [ ] **Kör om TxGNN-inferensen** för DB00922 och fyll `predicted_indications` med minst en poängsatt sjukdomskandidat
- [ ] **Hämta produktresumén från EMA/FIMEA** — extrahera varningar och kontraindikationer för att åtgärda DG001 *(blockerande)*
- [ ] **Fråga DrugBanks API** efter verkningsmekanismdata för att åtgärda DG002 *(hög)* — möjliggör analys av mekanistisk rimlighet
- [ ] **Kör om sökningen efter läkemedelsinteraktioner** när verkningsmekanismen är bekräftad — den nuvarande sökningen gav `not_found`
- [ ] **Bekräfta den svenska regulatoriska vägen** — om Simdax eller ett generiskt preparat är godkänt någon annanstans i EU, bedöm om ömsesidigt erkännande är tillämpligt

När dessa fyra punkter är åtgärdade, skicka in det uppdaterade underlaget för en fullständig L1–L5-bedömning.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

