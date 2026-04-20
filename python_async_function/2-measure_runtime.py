#!/usr/bin/env python3
"""Module that measures the execution time of wait_n."""

import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average execution time of wait_n(n, max_delay)."""
    start_time: float = time.time()

    import asyncio
    asyncio.run(wait_n(n, max_delay))

    end_time: float = time.time()

    return (end_time - start_time) / n
