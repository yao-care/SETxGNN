---
layout: default
title: Aztreonam
parent: Endast modellprediktion (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aztreonam: predikterad ny indikation Hyperamylasemi (evidensnivå L5). Ursprunglig indikation: Urinvägsinfektion (enligt kunskapsgrafen"
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

## Aztreonam: Från urinvägsinfektion till hyperamylasemi
{: .text-alpha }

---

### Sammanfattning

Aztreonam är ett antibiotikum av monobaktamtyp som ursprungligen används mot gramnegativa bakterieinfektioner, bland annat urinvägsinfektion, bukhinneinflammation (peritonit) och infektioner orsakade av *Pseudomonas aeruginosa* och *E. coli*. TxGNN-modellen förutsäger att det kan vara effektivt mot **hyperamylasemi** med en mycket hög poäng (99,7 %). Det finns dock **inga kliniska prövningar och ingen publicerad litteratur** som stöder detta, och förutsägelsen saknar rimlig biologisk förklaring.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Urinvägsinfektion (enligt kunskapsgrafen; godkännandetexten för den svenska produkten är tom) |
| Förutsagd ny indikation | Hyperamylasemi |
| TxGNN-förutsägelsepoäng | 99,7 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 1 (avregistrerat) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det sammanställda underlaget. Baserat på känd information är aztreonam ett monobaktamantibiotikum som hämmar bakteriers cellväggssyntes genom att binda till penicillinbindande protein 3 (PBP3) hos gramnegativa bakterier. Effekten vid infektioner som urinvägsinfektion är väl belagd.

Hyperamylasemi är dock ett laboratoriefynd, förhöjt amylas i blodet, och inte en infektionssjukdom. Ett antibakteriellt medel har ingen känd verkan på tillståndet. Mekanistiskt finns därför **ingen trolig koppling** mellan aztreonams verkan och den förutsagda indikationen.

Den höga poängen beror sannolikt på ett grafbaserat artefaktmönster i modellen och inte på verklig biologisk eller klinisk grund. Det är därför säkrast att betrakta förutsägelsen som ett falskt positivt resultat tills motsatsen visats.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 10284 (avregistrerat) | Azactam (Laboratoires Delbert) | Pulver till injektions-/infusionsvätska, lösning | – |

Det enda godkännandet i Sverige är avregistrerat, så det finns för närvarande inget giltigt godkännande för aztreonam.

---

### Säkerhetsaspekter

- **Tillstånd där läkemedlet enligt kunskapsgrafen är kontraindicerat** (härlett från relationer mellan läkemedel och sjukdomar, inte från produkttext): njursjukdom, pyouretär (var i urinledaren), leversjukdom, gallblåsesjukdom, *Clostridium difficile*-kolit, perinatal nekrotiserande enterokolit och bronkial sjukdom.
- **Läkemedelsinteraktioner** (27 interaktioner identifierade). De som bedömts som måttliga:
  - Pikosulfat
  - Dikumarol
  - Warfarin

  Bland övriga interaktioner, där allvarlighetsgraden inte är fastställd, finns vankomycin, amikacin, heparin, takrolimus, amfotericin B, acetylsalicylsyra, metronidazol, flukonazol, aciklovir, morfin, hydrokortison, dexametason, ondansetron, salbutamol samt protonpumpshämmarna omeprazol, pantoprazol och lansoprazol. Särskild uppmärksamhet bör ägnas åt blödningsrisk och förändrad antikoagulationseffekt vid samtidig behandling med warfarin eller dikumarol.

Se produktresumén för fullständiga varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen om hyperamylasemi stöds varken av kliniska prövningar eller litteratur och saknar biologisk rimlighet. Aztreonam är dessutom för närvarande inte marknadsfört med giltigt godkännande i Sverige.

**För att gå vidare krävs:**
- Ett tydligt mekanistiskt eller kliniskt argument för varför ett antibiotikum skulle påverka amylasnivåer. Utan det bör spåret inte prioriteras.
- Kompletterande data om verkningsmekanism och godkänd produktinformation (varningar och kontraindikationer) från Läkemedelsverket.
- En systematisk litteratursökning som kan bekräfta att evidens saknas.
- Bland de tio högst rankade förutsägelserna är **gonokockuretrit** (gonorré) den bäst underbyggda (evidensnivå L3). Den bygger på flera enkeldosstudier från 1980-talet och en öppen enarmad studie från 2020. Det finns även en rapport om uppkomst av aztreonamresistenta stammar. Det är en mer realistisk kandidat för fortsatt utvärdering, men kräver jämförande data.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

