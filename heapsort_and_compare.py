"""
Assignment 4 - Heaps
Part 1: Heapsort implementation + empirical comparison vs Quicksort and Merge Sort
Author: <Your Name>
"""

from __future__ import annotations
import random
import time
from typing import List, Callable, Dict, Tuple


# -----------------------------
# Heapsort (Max-Heap) - In-place
# -----------------------------
def heapify(arr: List[int], n: int, i: int) -> None:
    """Sift-down at index i in a max-heap within arr[0:n]."""
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            return

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def build_max_heap(arr: List[int]) -> None:
    """Convert arr into a max-heap in-place."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapsort(arr: List[int]) -> List[int]:
    """In-place heapsort. Returns arr for convenience."""
    n = len(arr)
    build_max_heap(arr)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # move max to the end
        heapify(arr, end, 0)  # restore heap in arr[0:end]
    return arr


# -----------------------------
# Merge Sort (returns new list)
# -----------------------------
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(a: List[int], b: List[int]) -> List[int]:
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


# -----------------------------------------
# Quicksort (simple randomized pivot version)
# -----------------------------------------
def quick_sort(arr: List[int]) -> List[int]:
    """Returns a new sorted list (not in-place) using randomized pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randrange(len(arr))]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


# -----------------------------
# Data generation
# -----------------------------
def make_data(n: int, kind: str) -> List[int]:
    if kind == "random":
        return [random.randint(0, n) for _ in range(n)]
    if kind == "sorted":
        return list(range(n))
    if kind == "reverse":
        return list(range(n, 0, -1))
    raise ValueError("kind must be one of: random, sorted, reverse")


# -----------------------------
# Benchmarking
# -----------------------------
def time_fn(fn: Callable[[List[int]], List[int]], data: List[int], repeats: int = 3) -> float:
    """Return best time over repeats."""
    best = float("inf")
    for _ in range(repeats):
        arr = data[:]  # copy so each algorithm gets same input
        t0 = time.perf_counter()
        out = fn(arr)
        # Validate correctness quickly
        if out != sorted(data):
            raise AssertionError(f"{fn.__name__} produced incorrect output")
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return best


def run_benchmarks(
    sizes: List[int] = [1_000, 2_000, 5_000, 10_000, 20_000],
    distributions: List[str] = ["random", "sorted", "reverse"],
    repeats: int = 3,
) -> Dict[Tuple[int, str], Dict[str, float]]:
    algos: Dict[str, Callable[[List[int]], List[int]]] = {
        "heapsort": lambda a: heapsort(a),   # in-place
        "mergesort": lambda a: merge_sort(a),
        "quicksort": lambda a: quick_sort(a),
    }

    results: Dict[Tuple[int, str], Dict[str, float]] = {}
    for n in sizes:
        for dist in distributions:
            data = make_data(n, dist)
            row: Dict[str, float] = {}
            for name, fn in algos.items():
                row[name] = time_fn(fn, data, repeats=repeats)
            results[(n, dist)] = row
    return results


def print_results(results):
    print("\n" + "=" * 80)
    print(f"{'Size':<8}{'Type':<10}{'HeapSort(s)':<15}{'MergeSort(s)':<15}{'QuickSort(s)':<15}")
    print("=" * 80)

    for (n, dist), row in sorted(results.items()):
        print(f"{n:<8}{dist:<10}{row['heapsort']:<15.6f}{row['mergesort']:<15.6f}{row['quicksort']:<15.6f}")

    print("=" * 80)



if __name__ == "__main__":
    random.seed(42)
    res = run_benchmarks()
    print_results(res)
