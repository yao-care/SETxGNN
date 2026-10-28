---
layout: default
title: "Endast kända användningar (inga nya prediktioner)"
nav_order: 24
permalink: /known-uses/
description: "För dessa läkemedel är alla kandidater från TxGNN-modellen redan kända användningar (registrerade i kunskapsgrafen eller i ett godkännande), så det finns i…"
---

# Endast kända användningar (inga nya prediktioner)

För dessa läkemedel är alla kandidater från TxGNN-modellen redan kända användningar (registrerade i kunskapsgrafen eller i ett godkännande), så det finns ingen ny predikterad indikation. Varje sida visar de kända användningarna och lokal marknadsstatus.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} läkemedel**

| Läkemedel | Rapport |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Visa sidan]({{ drug.url | relative_url }}) |
{% endfor %}
