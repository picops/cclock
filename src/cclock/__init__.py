import sys

from .__about__ import __version__
from .clock import clock_datetime, clock_monotonic, clock_realtime
from .conversions import (
    change_ts_units,
    datetime_to_ms,
    datetime_to_ns,
    datetime_to_s,
    datetime_to_us,
    ms_to_datetime,
    ns_to_datetime,
    s_to_datetime,
    us_to_datetime,
)
from .rfc2822 import (
    parse_rfc2822_bytes_to_datetime,
    parse_rfc2822_bytes_to_timestamp,
    parse_rfc2822_bytes_to_timestamp_with_tz,
)

__all__: tuple[str, ...] = (
    # About
    "__version__",
    # Clock
    "clock_datetime",
    "clock_monotonic",
    "clock_realtime",
    # Conversions
    "change_ts_units",
    "datetime_to_ms",
    "datetime_to_ns",
    "datetime_to_s",
    "datetime_to_us",
    "ms_to_datetime",
    "ns_to_datetime",
    "s_to_datetime",
    "us_to_datetime",
    # RFC 2822
    "parse_rfc2822_bytes_to_datetime",
    "parse_rfc2822_bytes_to_timestamp",
    "parse_rfc2822_bytes_to_timestamp_with_tz",
)
if not sys.platform.startswith("win"):
    try:
        from .clock import (
            clock_monotonic_coarse,
            clock_monotonic_raw,
            clock_realtime_coarse,
        )

        __all__ += (
            "clock_monotonic_coarse",
            "clock_monotonic_raw",
            "clock_realtime_coarse",
        )
    except ImportError:
        pass
