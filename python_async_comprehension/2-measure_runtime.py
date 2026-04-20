#!/usr/bin/env python3
"""Measure the total runtime of async_comprehension executed 4 times."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Return total execution time for 4 parallel async_comprehension calls."""
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.time() - start
