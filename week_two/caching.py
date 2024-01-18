import functools
import time


@functools.lru_cache(maxsize=3)
def expensive_computation(num):
    print(f"Computing {num}...")
    time.sleep(2)  # Simulate an expensive computation
    return num * num


# First time computations, results are cached
print(expensive_computation(1))
print(expensive_computation(2))
print(expensive_computation(3))

# Cached results are used, so these are instant
print(expensive_computation(1))
print(expensive_computation(2))
print(expensive_computation(3))

# New computation, not in cache
print(expensive_computation(4))

# 1 was the least recently used, so it was removed from the cache
# This computation is not instant
print(expensive_computation(1))
