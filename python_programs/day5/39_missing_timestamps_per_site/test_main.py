import pandas as pd

from main import missing_timestamps


def make():
    rows = [
        # site A: missing 00:30 (00:15 duplicated)
        ("A", "2026-10-01 00:00"), ("A", "2026-10-01 00:15"), ("A", "2026-10-01 00:15"),
        ("A", "2026-10-01 00:45"), ("A", "2026-10-01 01:00"),
        # site B: missing 00:45, 01:00, 01:15
        ("B", "2026-10-01 00:30"), ("B", "2026-10-01 00:15"), ("B", "2026-10-01 00:00"),
        ("B", "2026-10-01 01:30"),
        # site C: single row
        ("C", "2026-10-01 05:00"),
    ]
    df = pd.DataFrame(rows, columns=["site", "ts"])
    df["ts"] = pd.to_datetime(df["ts"])
    df["value"] = 1.0
    return df


def test_expected_missing():
    out = missing_timestamps(make())
    assert list(out.columns) == ["site", "ts"]
    got = list(zip(out["site"], out["ts"].dt.strftime("%H:%M")))
    assert got == [("A", "00:30"), ("B", "00:45"), ("B", "01:00"), ("B", "01:15")]


def test_clean_index():
    out = missing_timestamps(make())
    assert list(out.index) == [0, 1, 2, 3]


def test_ts_dtype_is_datetime():
    out = missing_timestamps(make())
    assert pd.api.types.is_datetime64_any_dtype(out["ts"])


def test_other_freq():
    df = make()
    df = df[df["site"] == "A"]
    out = missing_timestamps(df, freq="1h")
    assert len(out) == 0
    assert list(out.columns) == ["site", "ts"]


def test_input_not_mutated():
    df = make()
    before = df.copy()
    missing_timestamps(df)
    pd.testing.assert_frame_equal(df, before)
