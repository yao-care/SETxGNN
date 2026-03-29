#!/usr/bin/env python3
"""處理瑞典 MPA 藥品資料

從 Läkemedelsverket REST API 下載藥品註冊 CSV 並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    API: https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv
    目錄: https://www.dataportal.se/en/datasets/140_5467
    搜尋: https://www.lakemedelsverket.se/sv/sok-lakemedelsfakta

產生檔案:
    data/raw/se_fda_drugs.json
"""

import json
from io import StringIO
from pathlib import Path

import pandas as pd
import requests
import yaml


# Läkemedelsverket REST API — 按 ATC 首字母分批匯出
# 完整匯出無 atcCode 參數會回 500 錯誤，需按 ATC 第一碼逐批下載
LMV_EXPORT_URL = "https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv"
ATC_GROUPS = list("ABCDGHJLMNPRSV")  # 14 個 ATC 主群組


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_mpa_data(output_path: Path) -> Path:
    """從 Läkemedelsverket REST API 分批下載藥品 CSV

    API 端點按 ATC 群組匯出 CSV（分號分隔、UTF-8）。
    逐一下載 A-V 群組後合併為單一 CSV。

    Args:
        output_path: CSV 輸出路徑

    Returns:
        下載的檔案路徑
    """
    print("正在從 Läkemedelsverket REST API 下載藥品 CSV...")
    print(f"API: {LMV_EXPORT_URL}")
    print()

    params_base = {
        "narcClass": 0,
        "open": 0,
        "prescript": 0,
        "prodClass": 0,
        "registrationDateType": 0,
        "sale": 0,
        "status": 0,
        "vetHum": 0,
    }

    all_dfs = []
    header_saved = False

    for atc in ATC_GROUPS:
        params = {**params_base, "atcCode": atc}
        print(f"  ATC 群組 {atc}...", end=" ", flush=True)

        try:
            response = requests.get(
                LMV_EXPORT_URL,
                params=params,
                timeout=120,
                headers={
                    "User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)",
                },
            )
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            if "text/html" in content_type:
                print(f"跳過 (回傳 HTML)")
                continue

            # 解析 CSV（分號分隔）— MPA API 回傳 UTF-16-LE 編碼（瑞典字元 ä, ö, å）
            text = None
            for enc in ("utf-16", "utf-16-le", "utf-16-be", "utf-8-sig", "utf-8", "latin-1", "iso-8859-1", "cp1252"):
                try:
                    text = response.content.decode(enc)
                    # Verify it looks like actual CSV (not mojibake)
                    if "\x00" not in text[:200]:
                        break
                    text = None
                except (UnicodeDecodeError, ValueError):
                    continue
            if text is None:
                text = response.content.decode("utf-8", errors="replace")
            df = pd.read_csv(
                StringIO(text),
                sep=";",
                dtype=str,
                on_bad_lines="skip",
            )

            if len(df) == 0:
                print("0 筆")
                continue

            all_dfs.append(df)
            print(f"{len(df):,} 筆")

        except requests.RequestException as e:
            print(f"失敗: {e}")
            continue

    if not all_dfs:
        raise RuntimeError("所有 ATC 群組下載均失敗")

    combined = pd.concat(all_dfs, ignore_index=True)

    # 去重
    before = len(combined)
    if "MT-nummer" in combined.columns:
        combined = combined.drop_duplicates(subset=["MT-nummer"], keep="first")
    elif "NPL-id" in combined.columns:
        combined = combined.drop_duplicates(subset=["NPL-id"], keep="first")
    after = len(combined)

    print(f"\n下載完成，共 {after:,} 筆（去重前 {before:,}）")

    # 儲存合併的 CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(output_path, index=False, sep=";", encoding="utf-8")

    size_mb = output_path.stat().st_size / 1024 / 1024
    print(f"已儲存: {output_path} ({size_mb:.1f} MB)")

    return output_path


def process_mpa_data(data_path: Path, output_path: Path) -> Path:
    """處理 MPA CSV/XLSX 並轉換為 JSON

    支援 CSV（API 匯出）和 XLSX（舊版直接下載）。

    欄位映射（API CSV -> fields.yaml）:
        Namn -> Läkemedelsnamn
        Verksamt ämne (förenklad) / Verksamt ämne -> Aktiv substans
        Registreringsstatus -> Status
        Godkännandenummer / MT-nummer -> Godkännandenummer
        Godkännandedatum -> Godkännandedatum
        Form -> Beredningsform
        Innehavare -> Innehavare

    Args:
        data_path: CSV 或 XLSX 檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()
    encoding = config.get("encoding", "utf-8")

    print(f"\n讀取資料檔案: {data_path}")

    # 根據副檔名選擇讀取方式
    suffix = data_path.suffix.lower()
    if suffix in (".xlsx", ".xls"):
        df = pd.read_excel(data_path, dtype=str)
    else:
        # CSV: 嘗試不同分隔符
        try:
            df = pd.read_csv(data_path, encoding=encoding, sep=";", dtype=str, on_bad_lines="skip")
            if len(df.columns) <= 1:
                raise ValueError("Only one column - wrong delimiter")
        except (ValueError, Exception):
            try:
                df = pd.read_csv(data_path, encoding=encoding, sep=",", dtype=str, on_bad_lines="skip")
            except Exception:
                df = pd.read_csv(data_path, encoding=encoding, sep="\t", dtype=str, on_bad_lines="skip")

    print(f"原始資料筆數: {len(df)}")
    print(f"欄位: {', '.join(df.columns.tolist())}")

    # 映射 API CSV 欄位名稱到 fields.yaml 期望的名稱
    col_map = {
        "Namn": "Läkemedelsnamn",
        "Verksamt ämne (förenklad)": "Aktiv substans",
        "Registreringsstatus": "Status",
        "MT-nummer": "Godkännandenummer",
        "Form": "Beredningsform",
    }

    # 只映射存在的欄位
    actual_map = {k: v for k, v in col_map.items() if k in df.columns and v not in df.columns}
    if actual_map:
        df = df.rename(columns=actual_map)
        print(f"欄位映射: {actual_map}")

    # 如果有 "Verksamt ämne" 但無 "Aktiv substans"，使用完整版
    if "Aktiv substans" not in df.columns and "Verksamt ämne" in df.columns:
        df = df.rename(columns={"Verksamt ämne": "Aktiv substans"})

    # 清理資料
    df = df.fillna("")

    # 轉換為 JSON
    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理瑞典 MPA (Läkemedelsverket) 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    csv_path = raw_dir / "lmv_medicinal_products.csv"
    xlsx_path = raw_dir / "Lakemedelsprodukter.xlsx"  # 舊路徑相容
    old_csv_path = raw_dir / "mpa_lakemedel.csv"  # 舊路徑相容
    output_path = raw_dir / "se_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找已下載的資料檔（優先新 API CSV，再找舊格式）
    data_path = None
    if csv_path.exists():
        data_path = csv_path
        print(f"使用已存在的 API CSV: {data_path}")
    elif xlsx_path.exists():
        data_path = xlsx_path
        print(f"使用已存在的 XLSX 檔案: {data_path}")
    elif old_csv_path.exists():
        data_path = old_csv_path
        print(f"使用已存在的 CSV 檔案: {data_path}")
    else:
        existing_csv = list(raw_dir.glob("*.csv"))
        if existing_csv:
            data_path = existing_csv[0]
            print(f"使用已存在的 CSV: {data_path}")
        else:
            download_mpa_data(csv_path)
            data_path = csv_path

    # 處理資料
    process_mpa_data(data_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
