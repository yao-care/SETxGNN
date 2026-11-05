---
layout: default
title: Integritetspolicy
nav_order: 95
permalink: /privacy-policy/
description: "Integritetspolicy för SETxGNN: en statisk webbplats utan konton och formulär; den använder analyskakor från Google Analytics 4 för användningsstatistik."
---

# Integritetspolicy

<div class="key-takeaway">
Detta är en statisk webbplats — ingen registrering och inga formulär. Den använder analyskakor från Google Analytics 4 för att ta fram användningsstatistik.
</div>

---

## Vad vi samlar in

<p class="key-answer" data-question="Samlar SETxGNN in personuppgifter?">
<strong>Endast användningsstatistik, via Google Analytics 4.</strong> Denna webbplats driftas på GitHub Pages som en helt statisk
webbplats. Det finns inget kontosystem och inga formulär, och vi samlar inte in namn, e-postadresser eller
patientjournaler. Webbplatsen använder analyskakor från Google Analytics 4 för att ta fram användningsstatistik (visade
sidor, hänvisande webbplats, scrolldjup och tid på sidan). Kakorna sätts när en sida laddas; sökord, formulärinnehåll
och frågeparametrar i webbadressen skickas inte.
</p>

---

## Tredjepartstjänster

Webbplatsen använder följande tredjepartsresurser, vilka kan logga åtkomst enligt sina egna
policyer:

| Tjänst | Syfte | Integritetspolicy |
|---------|---------|----------------|
| GitHub Pages | Webbhotell | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Besöksstatistik (visade sidor, hänvisande sida); använder analyskakor. Sökord, formulärinnehåll och URL-parametrar skickas inte. | [Googles integritetspolicy](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Skriptbibliotek: d3-diagram på alla sidor; Fuse.js för namnmatchning och SMART on FHIR-klienten på SMART-sidorna | [jsDelivrs integritetspolicy](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Sökning efter kliniska prövningar på SMART-sidorna: bara när du ber om det skickas läkemedlets och indikationens namn till ClinicalTrials.gov-API:et | [NLM:s webbpolicyer](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART-appen: RxNorm-koderna för läkemedlen som läses från din elektroniska patientjournal skickas till NLM:s RxNav-API för att slå upp substansnamnet (inga patientidentifierare) | [NLM:s webbpolicyer](https://www.nlm.nih.gov/web_policies.html) |

När du aktivt startar SMART on FHIR-appen hämtar den läkemedelsdata från ditt
journalsystem. Patientens identitet och journaldata <strong>skickas inte till denna webbplats servrar</strong> (det är en
statisk webbplats utan backend) och lagras inte av webbplatsen. För att matcha läkemedelsnamn skickar appen
läkemedlens RxNorm-koder till RxNav-tjänsten hos amerikanska National Library of Medicine; koderna innehåller inga
uppgifter som identifierar patienten. När du ber om kliniska studier skickas läkemedlets namn och indikationen till
ClinicalTrials.gov.

---

## Registrerades rättigheter

Denna webbplats har inga konton och lagrar inga personuppgifter på egna servrar (den har inga).
Användningsstatistiken samlas in av Google Analytics 4; du kan blockera eller radera dess kakor i webbläsarens
inställningar.
Vid frågor om denna policy, kontakta service@yao.care.

---

## Ändringar av denna policy

Eventuella ändringar publiceras direkt på denna sida.

---

## Om utvecklaren

Denna plattform utvecklas och drivs av **藥提醒科技有限公司** (yao.care). Se sidan
<a href="{{ '/about/' | relative_url }}">Om</a> för fullständig bakgrund om företaget och metoden.

---

<div class="disclaimer">
<strong>Ansvarsfriskrivning</strong><br>
Denna rapport är endast avsedd som referens för akademisk forskning och <strong>utgör inte medicinsk rådgivning</strong>. Följ alltid din läkares anvisningar; justera aldrig din medicinering på egen hand. Varje beslut om läkemedelsrepositionering kräver fullständig klinisk validering och regulatorisk granskning.
<br><br>
<small>Granskad av: 藥提醒科技有限公司 (yao.care)</small>
</div>
