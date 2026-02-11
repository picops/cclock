"""Simple pytest to check all cclock functions work."""

from __future__ import annotations

import sys
from datetime import datetime, timezone

import pytest

import cclock

UTC = timezone.utc


def test_version() -> None:
    assert hasattr(cclock, "__version__")
    assert isinstance(cclock.__version__, str)
    assert cclock.__version__


# --- clock ---


def test_clock_monotonic() -> None:
    t = cclock.clock_monotonic()
    assert isinstance(t, int)
    assert t >= 0


def test_clock_realtime() -> None:
    t = cclock.clock_realtime()
    assert isinstance(t, int)
    assert t >= 0


def test_clock_datetime() -> None:
    dt = cclock.clock_datetime()
    assert isinstance(dt, datetime)
    # Should be a sane recent time (e.g. year in 2020–2040)
    assert 2020 <= dt.year <= 2040


@pytest.mark.skipif(sys.platform == "win32", reason="Linux/macOS-only clocks")
def test_clock_monotonic_raw() -> None:
    t = cclock.clock_monotonic_raw()
    assert isinstance(t, int)
    assert t >= 0


@pytest.mark.skipif(sys.platform == "win32", reason="Linux/macOS-only clocks")
def test_clock_monotonic_coarse() -> None:
    t = cclock.clock_monotonic_coarse()
    assert isinstance(t, int)
    assert t >= 0


@pytest.mark.skipif(sys.platform == "win32", reason="Linux/macOS-only clocks")
def test_clock_realtime_coarse() -> None:
    t = cclock.clock_realtime_coarse()
    assert isinstance(t, int)
    assert t >= 0


# --- conversions (round-trips and units) ---


def test_datetime_ns_roundtrip() -> None:
    dt = datetime(2025, 2, 11, 12, 0, 0, 123456, tzinfo=UTC)
    ns = cclock.datetime_to_ns(dt)
    assert isinstance(ns, int)
    back = cclock.ns_to_datetime(ns)
    assert back == dt


def test_datetime_us_roundtrip() -> None:
    dt = datetime(2025, 2, 11, 12, 0, 0, 123000, tzinfo=UTC)
    us = cclock.datetime_to_us(dt)
    assert isinstance(us, int)
    back = cclock.us_to_datetime(us)
    assert back == dt


def test_datetime_ms_roundtrip() -> None:
    dt = datetime(2025, 2, 11, 12, 0, 0, 123000, tzinfo=UTC)
    ms = cclock.datetime_to_ms(dt)
    assert isinstance(ms, int)
    back = cclock.ms_to_datetime(ms)
    assert back == dt


def test_datetime_s_roundtrip() -> None:
    dt = datetime(2025, 2, 11, 12, 0, 0, tzinfo=UTC)
    s = cclock.datetime_to_s(dt)
    assert isinstance(s, float)
    back = cclock.s_to_datetime(s)
    assert back == dt


def test_change_ts_units_ns_to_us() -> None:
    ns = 1_000_000
    us = cclock.change_ts_units(ns, from_unit="ns", to_unit="us")
    assert us == 1_000


def test_change_ts_units_ns_to_ms() -> None:
    ns = 1_000_000_000
    ms = cclock.change_ts_units(ns, from_unit="ns", to_unit="ms")
    assert ms == 1_000


def test_change_ts_units_identity() -> None:
    ns = 123456789
    assert cclock.change_ts_units(ns, "ns", "ns") == ns


# --- RFC 2822 ---


def test_parse_rfc2822_bytes_to_datetime() -> None:
    # Standard RFC 2822 example
    raw = b"Mon, 11 Feb 2025 12:00:00 +0000"
    dt = cclock.parse_rfc2822_bytes_to_datetime(raw)
    assert isinstance(dt, datetime)
    assert dt.year == 2025
    assert dt.month == 2
    assert dt.day == 11
    assert dt.hour == 12
    assert dt.minute == 0
    assert dt.second == 0


def test_parse_rfc2822_bytes_to_timestamp() -> None:
    raw = b"Mon, 11 Feb 2025 12:00:00 +0000"
    ts = cclock.parse_rfc2822_bytes_to_timestamp(raw)
    assert isinstance(ts, float)
    assert ts > 0


def test_parse_rfc2822_bytes_to_timestamp_with_tz() -> None:
    raw = b"Mon, 11 Feb 2025 12:00:00 +0000"
    ts = cclock.parse_rfc2822_bytes_to_timestamp_with_tz(raw)
    assert isinstance(ts, float)
    assert ts > 0
