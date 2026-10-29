# SETxGNN - Sverige: Lakemedelsrepositionering

> 本專案由 **藥提醒科技有限公司**（[yao.care](https://www.yao.care)）開發與維運。
> SETxGNN 站台：<https://setxgnn.yao.care/>｜產品總覽：<https://www.yao.care/medical/txgnn/>

[![Website](https://img.shields.io/badge/Website-setxgnn.yao.care-blue)](https://setxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Forutsaegelser foer lakemedelsrepositionering av MPA-godkaenda lakemedel (Sweden) med TxGNN-modellen.

## Ansvarsfriskrivning

- Resultaten av detta projekt aer endast foer forskningsaendamaal och utgoer inte medicinsk raadgivning.
- Kandidater foer lakemedelsrepositionering kraever klinisk validering foere tillaempning.

## Projektoeversikt

### Rapportstatistik

| Element | Antal |
|------|------|
| **Lakemedelsrapporter** | 450 |
| **Totala forutsaegelser** | 3,672,147 |
| **Unika lakemedel** | 152 |
| **Unika indikationer** | 16,564 |
| **DDI-data** | 302,516 |
| **DFI-data** | 857 |
| **DHI-data** | 35 |
| **DDSI-data** | 8,359 |
| **FHIR-resurser** | 108 MK / 556 CUD |

### Foerdelning av evidensnivaaer

| Evidensnivaa | Antal rapporter | Beskrivning |
|---------|-------|------|
| **L1** | 0 | Flera Fas 3 RCT:er |
| **L2** | 0 | Enskild RCT eller flera Fas 2 |
| **L3** | 0 | Observationsstudier |
| **L4** | 0 | Prekliniska / mekanistiska studier |
| **L5** | 108 | Endast beraekningsbaserad forutsaegelse |

### Per kaella

| Kaella | Forutsaegelser |
|------|------|
| DL | 3,671,591 |
| KG + DL | 485 |
| KG | 71 |

### Per tillit

| Tillit | Forutsaegelser |
|------|------|
| very_high | 386 |
| high | 174,589 |
| medium | 363,223 |
| low | 3,133,949 |

---

## Forutsaegelsemetoder

| Metod | Hastighet | Noggrannhet | Krav |
|------|------|--------|----------|
| Kunskapsgraf | Snabb (sekunder) | Laegre | Inga speciella krav |
| Djupinlaerning | Laangsam (timmar) | Hoegre | Conda + PyTorch + DGL |

### Kunskapsgraf-metod

```bash
uv run python scripts/run_kg_prediction.py
```

| Maetvaerde | Vaerde |
|------|------|
| MPA Totalt antal lakemedel | 14,492 |
| Kartlagda till DrugBank | 2,175 (15.0%) |
| Repositioneringskandidater | 556 |

### Djupinlaerning-metod

```bash
conda activate txgnn
PYTHONPATH=src python -m setxgnn.predict.txgnn_model
```

| Maetvaerde | Vaerde |
|------|------|
| Totala DL-forutsaegelser | 298,386 |
| Unika lakemedel | 152 |
| Unika indikationer | 16,564 |

### Poaengtolkning

TxGNN-poaengen representerar modellens tillit till ett lakemedels-sjukdomspar, med ett intervall fraan 0 till 1.

| Troeskelvaerde | Betydelse |
|-----|------|
| >= 0.9 | Mycket hoeg tillit |
| >= 0.7 | Hoeg tillit |
| >= 0.5 | Maattlig tillit |

#### Poaengfoerdelning

| Troeskelvaerde | Betydelse |
|-----|------|
| ≥ 0.9999 | Extremt hoegt foertroende, modellens mest saekra foeruts aegelser |
| ≥ 0.99 | Mycket hoegt foertroende, vaert att prioritera foer validering |
| ≥ 0.9 | Hoegt foertroende |
| ≥ 0.5 | Maattligt foertroende (sigmoid-beslutsgraens) |

#### Definitioner av evidensnivaaer

| Nivaa | Definition | Klinisk betydelse |
|-----|------|---------|
| L1 | Fas 3 RCT eller systematisk oeeversikt | Kan stoedja klinisk anvaendning |
| L2 | Fas 2 RCT | Kan oevervagas foer anvaendning |
| L3 | Fas 1 eller observationsstudie | Kraever ytterligare utvaerdering |
| L4 | Fallrapport eller preklinisk forskning | AEnnu inte rekommenderat |
| L5 | Endast beraekningsbaserad foeruts aegelse, ingen klinisk evidens | Kraever ytterligare forskning |

#### Viktiga paaminnelser

1. **Hoega poaeng garanterar inte klinisk effektivitet: TxGNN-poaeng aer kunskapsgrafikbaserade foeruts aegelser som kraever klinisk validering.**
2. **Laaga poaeng betyder inte ineffektivt: modellen kanske inte har laert sig vissa samband.**
3. **Rekommenderas att anvaenda med valideringspipeline: anvaend detta projekts verktyg foer att granska kliniska studier, litteratur och andra bevis.**

### Valideringspipeline

```mermaid
flowchart TD
    A["TxGNN-forutsaegelseresultat"] --> B
    subgraph B["Step 1: DrugBundle Collector"]
        B1["Lakemedelsnivaa: MPA, DDI, DrugBank"]
        B2["Indikationsnivaa: ClinicalTrials, PubMed, ICTRP"]
    end
    B --> |"drug_bundle.json"| C
    subgraph C["Step 2: Evidence Pack Generator"]
        C1["Programmatisk dataoeverfoering (100%)"]
        C2["+ LLM Analys (L1-L5)"]
    end
    C --> |"drug_evidence_pack.json/md"| D
    subgraph D["Step 3: Notes Writer"]
        D1["drug_pharmacist_notes.md"]
        D2["drug_sponsor_notes.md"]
    end
```

---

## Snabbstart

### Steg 1: Ladda ner data

| Fil | Nedladdning |
|------|------|
| MPA Data | [Läkemedelsverket - Läkemedelsregister](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) |

### Steg 2: Installera beroenden

```bash
uv sync
```

### Steg 3: Behandla lakemedelsdata

```bash
uv run python scripts/process_fda_data.py
```

### Steg 4: Foebereda vokabulaerdata

```bash
uv run python scripts/prepare_external_data.py
```

### Steg 5: Koer kunskapsgraf-forutsaegelse

```bash
uv run python scripts/run_kg_prediction.py
```

### Steg 6: Konfigurera djupinlaerningsmiljoe

```bash
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb
```

### Steg 7: Koer djupinlaerning-forutsaegelse

```bash
conda activate txgnn
PYTHONPATH=src python -m setxgnn.predict.txgnn_model
```

---

## Resurser

### TxGNN Kaerna

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine, 2024
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org)

### Datakaellor

| Kategori | Data | Kaella | Anmaerkning |
|------|------|------|------|
| **Lakemedelsdata** | MPA | [Läkemedelsverket - Läkemedelsregister](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) | Sweden |
| **Kunskapsgraf** | TxGNN KG | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 diseases, 7,957 drugs |
| **Lakemedelsdatabas** | DrugBank | [DrugBank](https://go.drugbank.com/) | Kartlaeggning av lakemedelsingredienser |
| **Lakemedelsinteraktioner** | DDInter 2.0 | [DDInter](https://ddinter2.scbdd.com/) | DDI-par |
| **Lakemedelsinteraktioner** | Guide to PHARMACOLOGY | [IUPHAR/BPS](https://www.guidetopharmacology.org/) | Godkaenda lakemedelsinteraktioner |
| **Kliniska studier** | ClinicalTrials.gov | [CT.gov API v2](https://clinicaltrials.gov/data-api/api) | Register foer kliniska studier |
| **Kliniska studier** | WHO ICTRP | [ICTRP API](https://apps.who.int/trialsearch/api/v1/search) | Internationell plattform foer kliniska studier |
| **Litteratur** | PubMed | [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) | Medicinsk litteratursoekning |
| **Namnkartlaeggning** | RxNorm | [RxNav API](https://rxnav.nlm.nih.gov/REST) | Standardisering av lakemedelsnamn |
| **Namnkartlaeggning** | PubChem | [PUG-REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Kemiska aemnes-synonymer |
| **Namnkartlaeggning** | ChEMBL | [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data) | Bioaktivitetsdatabas |
| **Standarder** | FHIR R4 | [HL7 FHIR](http://hl7.org/fhir/) | MedicationKnowledge, ClinicalUseDefinition |
| **Standarder** | SMART on FHIR | [SMART Health IT](https://smarthealthit.org/) | EHR-integration, OAuth 2.0 + PKCE |

### Modellnedladdningar

| Fil | Nedladdning | Anmaerkning |
|------|------|------|
| Fortranad modell | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | model_ckpt.zip |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | Noddata |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | Kunskapsgrafdata |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | Kantdata (DL) |

## Projektintroduktion

### Katalogstruktur

```
SETxGNN/
├── README.md
├── CLAUDE.md
├── pyproject.toml
│
├── config/
│   └── fields.yaml
│
├── data/
│   ├── kg.csv
│   ├── node.csv
│   ├── edges.csv
│   ├── raw/
│   ├── external/
│   ├── processed/
│   │   ├── drug_mapping.csv
│   │   ├── repurposing_candidates.csv
│   │   ├── txgnn_dl_predictions.csv.gz
│   │   └── integration_stats.json
│   ├── bundles/
│   └── collected/
│
├── src/setxgnn/
│   ├── data/
│   │   └── loader.py
│   ├── mapping/
│   │   ├── normalizer.py
│   │   ├── drugbank_mapper.py
│   │   └── disease_mapper.py
│   ├── predict/
│   │   ├── repurposing.py
│   │   └── txgnn_model.py
│   ├── collectors/
│   └── paths.py
│
├── scripts/
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   └── integrate_predictions.py
│
├── docs/
│   ├── _drugs/
│   ├── fhir/
│   │   ├── MedicationKnowledge/
│   │   └── ClinicalUseDefinition/
│   └── smart/
│
├── model_ckpt/
└── tests/
```

**Foerklaring**: 🔵 Projektutveckling | 🟢 Lokal data | 🟡 TxGNN-data | 🟠 Valideringspipeline

### Dataflode

```mermaid
flowchart TD
    FDA["MPA Data"] --> proc["process_fda_data.py"]
    TxGNN["TxGNN Data"] --> prep["prepare_external_data.py"]

    proc --> json["se_fda_drugs.json"]
    prep --> ext["data/external/"]

    json --> norm["normalizer.py"]
    ext --> norm

    norm --> drug_map["drug_mapping.csv"]
    drug_map --> ind_map["indication_mapping.csv"]

    ind_map --> KG["Kunskapsgraf"]
    ind_map --> DL["Djupinlaerning"]

    KG --> kg_out["repurposing_candidates.csv"]
    DL --> dl_out["txgnn_dl_predictions.csv"]
```

---

## Citering

Om du anvaender detta dataset eller denna programvara, vaenligen citera:

```bibtex
@software{setxgnn2026,
  author       = {Yao.Care},
  title        = {SETxGNN: Drug Repurposing Validation Reports for Sweden MPA Drugs},
  year         = 2026,
  publisher    = {GitHub},
  url          = {https://github.com/yao-care/SETxGNN}
}
```

Citera aeven den ursprungliga TxGNN-artikeln:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

<!-- txgnn-ops:start -->
## 維運：資料還原與許可證更新

### 完整還原

git 只放程式碼與網站頁面；許可證原始資料、證據包、藥師報告原稿、預測結果放在本 repo 的 Release。

```bash
git clone https://github.com/yao-care/setxgnn.git && cd setxgnn
uv sync                                  # Python 相依套件
bash scripts/restore_data.sh             # 取最新的 data-* Release，還原 data/（含校驗）
bash scripts/restore_data.sh --with-kg   # 另加共用知識圖譜與預測模型（只有重跑預測才需要）
```

需要 [GitHub CLI](https://cli.github.com/)（`gh auth login`）與 [uv](https://docs.astral.sh/uv/)。

### 改頁工具鏈

事實層、checker、許可證狀態計算等放在 `tools/txgnn/.claude/`，是母 repo `yao-care/txgnn` 的 `.claude/` 複本（版本見 `tools/txgnn/VERSION`）。
規則要改請改母 repo，再用 `python3 .claude/sync_site_tools.py SETxGNN` 同步過來，不要直接改這裡的複本。
在本 repo 單獨使用時，先組工作目錄：

```bash
WS=$(bash scripts/txgnn_ws.sh)
cd "$WS"
python3 .claude/dump_license_facts_20261021.py SETxGNN       # 依證據包算市場狀態（checker 要用）
python3 .claude/checker_trend.py --no-append SETxGNN           # 全部藥物頁 checker，必須「非 0 0」
```

### 許可證排程更新（GitHub Actions）

`.github/workflows/license-refresh.yml` 每週一 UTC 03:17 自動執行，也可以在 Actions 頁手動觸發（可選只試跑）：

1. 從 Release 還原 `data/`（`scripts/restore_data.sh`）
2. 從主管機關下載最新許可證資料（`scripts/license_adapter.py`），檢查筆數與格式
3. 更新證據包的許可證狀態 → 重算市場狀態 → 同步許可證表 → 事實層改頁 → checker 全量必須 0 → 衍生檔 → gate
4. 全部通過才推上 `main` 並觸發部署；更新後的 `data/` 另存成新的 `data-YYYYMMDD` Release

以下情況一律不推、自動開 issue（label `license-refresh`）：下載失敗或格式改變、狀態變動超過兩成、
改到的藥物頁超過 min(200, 5%)、checker／gate／h1 沒過、有人工查核紀錄的頁會被改到。全程不使用 AI。
<!-- txgnn-ops:end -->
