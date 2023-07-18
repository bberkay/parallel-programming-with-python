"""
    Asynchronous
    ------------
    Asynchronous programming, introduced in Python 3.5 with the asyncio module, is a way to
    write concurrent code that can efficiently handle I/O-bound tasks without blocking the
    program's execution. It leverages coroutines and the await keyword to pause and resume
    tasks cooperatively.

    - All descriptions and comments created by ChatGPT and GitHub Copilot
"""
import time
import os
from datetime import datetime

import asyncio

async def main() -> None:
    await asyncio.sleep(1)
    print('hello')

if __name__ == "__main__":
    star_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    print(f"Finished in {end_time - star_time} seconds")

"""
    Output:
    -------
"""