import time
import random
import pandas as pd
 
def make_data(n):
    stations = ["Adyar", "Guindy", "Teynampet", "Velachery"]
    return [
        (stations[i % 4], f"2026-10-{(i % 28) + 1:02d}", float((i * 7) % 300))
        for i in range(n)
    ]
 
def loop_group(data):
    sums, counts = {}, {}
    for s, d, v in data:
        key = (s, d)
        sums[key] = sums.get(key, 0.0) + v
        counts[key] = counts.get(key, 0) + 1
    return {k: sums[k] / counts[k] for k in sums}
 
for n in (1_000, 100_000, 1_000_000):
    data = make_data(n)
    start = time.perf_counter()
    loop_group(data)
    loop_seconds = time.perf_counter() - start
 
    start = time.perf_counter()
    frame = pd.DataFrame(data, columns=["station", "day", "pm25"])
    frame.groupby(["station", "day"])["pm25"].mean()
    pandas_seconds = time.perf_counter() - start
 
    print(n, f"loop={loop_seconds:.4f}s", f"pandas={pandas_seconds:.4f}s")
