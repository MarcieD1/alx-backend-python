#!/usr/bin/env python3
from typing import List
import asyncio
from 1-concurrent_coroutines import wait_n
import time

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
