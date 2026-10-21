import pandas as pd

from main import sessionize


def make():
    rows = [
        ("u2", "2026-10-01 09:31"),
        ("u1", "2026-10-01 11:30"),
        ("u1", "2026-10-01 10:00"),
        ("u2", "2026-10-01 09:00"),
        ("u1", "2026-10-01 10:40"),
        ("u1", "2026-10-01 10:10"),
    ]
    df = pd.DataFrame(rows, columns=["user_id", "ts"])
    df["ts"] = pd.to_datetime(df["ts"])
    return df


def test_session_numbers():
    out = sessionize(make())
    assert list(out["user_id"]) == ["u1", "u1", "u1", "u1", "u2", "u2"]
    # u1 gaps: 10, 30 (exactly timeout -> same session), 50 (new). u2: 31 (new)
    assert list(out["session_no"]) == [0, 0, 0, 1, 0, 1]


def test_clean_index_and_int_dtype():
    out = sessionize(make())
    assert list(out.index) == list(range(6))
    assert pd.api.types.is_integer_dtype(out["session_no"])


def test_custom_timeout():
    out = sessionize(make(), timeout="5min")
    assert list(out["session_no"]) == [0, 1, 2, 3, 0, 1]


def test_input_not_mutated():
    df = make()
    before = df.copy()
    sessionize(df)
    pd.testing.assert_frame_equal(df, before)
