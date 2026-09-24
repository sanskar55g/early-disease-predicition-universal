"""
Tier 1: chronic disease risk datasets (structured tabular records).

Every dataset here is pulled live from the UCI Machine Learning Repository via
its official API. Nothing is generated locally. Each disease gets its own file
under data/tier1/raw/<disease>.parquet plus a provenance entry.

Run:  python backend/scripts/download_tier1.py            # all
      python backend/scripts/download_tier1.py heart ckd   # subset
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.data_guard import record_provenance, tier_dir  # noqa: E402
from app.tiers.tier1_registry import TIER1_DISEASES  # noqa: E402

OUT = tier_dir(1, "raw")


def fetch(key: str) -> None:
    spec = TIER1_DISEASES[key]
    ds = fetch_ucirepo(id=spec["uci_id"])
    X: pd.DataFrame = ds.data.features.copy()
    y: pd.Series = ds.data.targets[spec["target_col"]]
    df = X.copy()
    # UCI metadata occasionally yields duplicate column names (e.g. Parkinsons
    # MDVP:Jitter(%) and MDVP:Jitter(Abs) both arrive as "MDVP:Jitter"). Suffix them.
    seen: dict[str, int] = {}
    cols = []
    for c in df.columns:
        seen[c] = seen.get(c, 0) + 1
        cols.append(c if seen[c] == 1 else f"{c}_{seen[c]}")
    df.columns = cols
    df["__target__"] = spec["to_binary"](y)
    df = df.dropna(subset=["__target__"])
    out = OUT / f"{key}.parquet"
    df.to_parquet(out, index=False)
    record_provenance(
        out,
        source=f"UCI ML Repository #{spec['uci_id']}: {ds.metadata.name}",
        url=f"https://archive.ics.uci.edu/dataset/{spec['uci_id']}",
        rows=len(df),
        note=f"target={spec['target_col']} binarised as: {spec['target_note']}",
    )
    pos = int(df["__target__"].sum())
    print(f"  {key:<14} {ds.metadata.name:<50} rows={len(df):>7}  positives={pos:>6} ({pos/len(df):.1%})")


if __name__ == "__main__":
    keys = sys.argv[1:] or list(TIER1_DISEASES)
    print(f"Tier 1: fetching {len(keys)} real datasets from UCI into {OUT}")
    for k in keys:
        fetch(k)
    print("done. provenance written to", OUT / "provenance.json")
