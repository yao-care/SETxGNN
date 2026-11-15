/**
 * SETxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author SETxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Allvarlig' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Måttlig' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Lindrig' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarin + Ibuprofen: ökad blödningsrisk',
      detail: 'NSAID hämmar trombocytfunktionen och kan förstärka warfarins antikoagulerande effekt, vilket ökar risken för blödning i mag-tarmkanalen betydligt.',
      recommendation: 'Använd paracetamol i stället, eller lägg till en protonpumpshämmare som magskydd.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarin + Acetylsalicylsyra: ökad blödningsrisk',
      detail: 'Båda påverkar hemostasen; samtidig användning ökar blödningsrisken kraftigt.',
      recommendation: 'Om kombinationen är nödvändig, använd lågdos acetylsalicylsyra och följ PK(INR) noga.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarin + Naproxen: ökad blödningsrisk',
      detail: 'Naproxen tillsammans med warfarin ökar risken för blödning i mag-tarmkanalen och andra blödningar.',
      recommendation: 'Använd paracetamol mot smärta i stället.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformin + jodkontrastmedel: risk för laktacidos',
      detail: 'Kontrastmedel kan ge akut njurskada, vilket leder till ansamling av metformin och laktacidos.',
      recommendation: 'Gör uppehåll med metformin 48 timmar före undersökningen och återuppta först när normal njurfunktion är bekräftad.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Kolkicin + Klaritromycin: risk för toxicitet',
      detail: 'Klaritromycin är en stark CYP3A4-hämmare och ökar blodkoncentrationen av kolkicin kraftigt.',
      recommendation: 'Undvik kombinationen eller minska kolkicindosen betydligt.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Kolkicin + HIV-proteashämmare: risk för allvarlig toxicitet',
      detail: 'HIV-proteashämmare ökar kolkicinkoncentrationen markant och kan orsaka dödlig förgiftning.',
      recommendation: 'Kontraindicerat hos patienter med nedsatt njur- eller leverfunktion.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatin + Amiodaron: risk för myopati',
      detail: 'Amiodaron ökar simvastatinkoncentrationen och därmed risken för rabdomyolys.',
      recommendation: 'Överskrid inte simvastatin 20 mg/dag, eller byt till en annan statin.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'SSRI + Tramadol: risk för serotonergt syndrom',
      detail: 'Båda ökar den serotonerga aktiviteten; samtidig användning kan ge livshotande serotonergt syndrom.',
      recommendation: 'Följ noga upp symtom (hypertermi, myoklonus, förändrat mentalt status) och överväg ett annat analgetikum.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'SSRI + Linezolid: risk för serotonergt syndrom',
      detail: 'Linezolid är en MAO-hämmare; kombination med SSRI är mycket farlig.',
      recommendation: 'Undvik kombinationen. Om linezolid behövs, sätt ut SSRI och låt en lämplig utsättningsperiod passera.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodaron + Moxifloxacin: risk för QT-förlängning',
      detail: 'Båda kan förlänga QT-intervallet; samtidig användning ökar risken för torsade de pointes.',
      recommendation: 'Undvik kombinationen eller följ EKG noga.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoxin + Amiodaron: risk för digoxinförgiftning',
      detail: 'Amiodaron ökar blodkoncentrationen av digoxin med cirka 70%.',
      recommendation: 'Vid insättning av amiodaron: halvera digoxindosen och följ blodkoncentrationen.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Klopidogrel + PPI: minskad trombocythämmande effekt',
      detail: 'Omeprazol hämmar CYP2C19 och minskar omvandlingen av klopidogrel till dess aktiva metabolit.',
      recommendation: 'Överväg pantoprazol eller en H2-blockerare i stället.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Litium + NSAID: risk för litiumförgiftning',
      detail: 'NSAID minskar njurarnas utsöndring av litium och höjer blodkoncentrationen.',
      recommendation: 'Undvik kombinationen eller följ litiumkoncentrationen noga.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Kaliumtillskott + kaliumsparande diuretika: risk för hyperkalemi',
      detail: 'Båda höjer serumkalium; samtidig användning kan ge livshotande hyperkalemi.',
      recommendation: 'Kontrollera serumkalium regelbundet och undvik samtidigt kaliumtillskott.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Metotrexat + Trimetoprim-sulfametoxazol: risk för benmärgshämning',
      detail: 'Båda hämmar folatmetabolismen; samtidig användning ökar risken för benmärgshämning och mukosit.',
      recommendation: 'Undvik kombinationen, eller säkerställ tillräckligt folattillskott och följ blodstatus noga.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Inbyggda interaktionsregler i SETxGNN (15 utvalda regler; inte en fullständig DDInter-sökning)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Inga varningar för interaktioner hittades</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Rekommendation:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Källa: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nRekommendation: ${alert.recommendation}`,
      source: {
        label: 'SETxGNN DDI Checker',
        url: 'https://setxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
