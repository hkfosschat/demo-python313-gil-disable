import concurrent.futures
import contextlib
import time
from typing import Generator

@contextlib.contextmanager
def time_it(what: str) -> Generator[None, None, None]:
    t0 = time.monotonic()
    try:
        yield
    finally:
        print(f"{what}: took {time.monotonic() - t0:.6f} seconds")

def do_thread(n: int, id: int) -> int:
    with time_it(f"thread {id}"):
        x = 0
        for _ in range(n):
            x += 1
        return x

if __name__ == "__main__":
    core = 8
    with time_it("main"):
        with concurrent.futures.ThreadPoolExecutor(core) as pool:
            futures = [pool.submit(do_thread, 10**7, id) for id in range(core)]
            results = [f.result() for f in futures]
            print(results)