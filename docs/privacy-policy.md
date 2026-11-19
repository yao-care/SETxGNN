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

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Tillämplig lag

För besökare i Sverige gäller [dataskyddsförordningen (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) och [lagen (2018:218) med kompletterande bestämmelser](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218/); för kakor gäller dessutom lagen om elektronisk kommunikation. Tillsynsmyndighet är [Integritetsskyddsmyndigheten (IMY)](https://www.imy.se/). Den personuppgiftsansvarige finns i Taiwan och har inget etableringsställe i EU; behandlingen gäller de användningsuppgifter Google Analytics 4 samlar in via kakor.

## Dina rättigheter och hur du använder dem

- Rätt till tillgång (artikel 15) och rättelse (artikel 16).
- Rätt till radering (artikel 17) och begränsning (artikel 18).
- Rätt att invända (artikel 21), även mot webbanalys.
- Rätt att klaga hos IMY (artikel 77).

Begäranden och frågor: service@yao.care. Eftersom webbplatsen saknar konton kan vi bara hantera uppgifter hos Google Analytics om du ger oss tillräckliga detaljer (t.ex. datum och sidor för besöket); du kan också blockera eller radera analyscookies i webbläsaren.

## Upphovsrätt och datakällor

Webbplatsens texter skyddas av [upphovsrättslagen (1960:729)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1960729-om-upphovsratt-till-litterara-och_sfs-1960-729/). Webbplatsens kod är publicerad under MIT-licensen i [GitHub-förrådet](https://github.com/yao-care/SETxGNN); rapporttexterna är © 藥提醒科技有限公司 (yao.care).

Datakällor på webbplatsen och deras villkor:

- **TxGNN**-prediktionsdata (Harvard Dataverse): CC0 1.0 (allmän egendom); citera Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** och **PubMed**: US National Library of Medicine; se [villkoren för ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions) och [NCBI:s policyer](https://www.ncbi.nlm.nih.gov/home/about/policies/) (vissa PubMed-sammanfattningar omfattas fortfarande av förlagets upphovsrätt).
- **DrugBank**-id:n och -data: enligt [DrugBank](https://go.drugbank.com/):s licensvillkor (icke-kommersiell användning).
- **Lokal datamängd**: [Läkemedelsverket: läkemedelsregistret (CSV-export)](https://www.dataportal.se/en/datasets/140_5467), publicerad av Läkemedelsverket; återanvändning styrs av utgivarens villkor, och webbplatsen ger inga ytterligare rättigheter.

<!-- privacy-law:end -->

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
