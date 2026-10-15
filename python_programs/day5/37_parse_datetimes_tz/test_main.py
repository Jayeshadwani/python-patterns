import pandas as pd
import pytest

from main import load_events


@pytest.fixture
def raw():
    return pd.DataFrame(
        {
            "ts": [
                "2026-11-01T06:30:00Z",  # 01:30 EST (-05:00), second 01:30
                "2026-11-01T05:30:00Z",  # 01:30 EDT (-04:00), first 01:30
                "garbage",
                "2026-10-31T12:00:00Z",  # 08:00 EDT
                None,
            ],
            "site": ["B", "A", "X", "C", "Y"],
            "value": [3.0, 2.0, 99.0, 1.0, 98.0],
        }
    )


def test_index_type_name_and_tz(raw):
    out = load_events(raw)
    assert isinstance(out.index, pd.DatetimeIndex)
    assert out.index.name == "ts"
    assert str(out.index.tz) == "America/New_York"


def test_bad_rows_dropped_and_columns(raw):
    out = load_events(raw)
    assert len(out) == 3
    assert list(out.columns) == ["site", "value"]
    assert "X" not in out["site"].values and "Y" not in out["site"].values


def test_sorted_and_unique(raw):
    out = load_events(raw)
    assert out.index.is_monotonic_increasing
    assert out.index.is_unique


def test_instants_are_correct(raw):
    out = load_events(raw)
    expected = pd.DatetimeIndex(
        ["2026-10-31 12:00", "2026-11-01 05:30", "2026-11-01 06:30"], tz="UTC"
    )
    assert (out.index.tz_convert("UTC") == expected).all()


def test_dst_offsets(raw):
    out = load_events(raw)
    hours = [i.utcoffset().total_seconds() / 3600 for i in out.index]
    assert hours == [-4, -4, -5]


def test_rows_stay_aligned(raw):
    out = load_events(raw)
    assert list(out["site"]) == ["C", "A", "B"]
    assert list(out["value"]) == [1.0, 2.0, 3.0]


def test_input_not_mutated(raw):
    before = raw.copy()
    load_events(raw)
    pd.testing.assert_frame_equal(raw, before)
