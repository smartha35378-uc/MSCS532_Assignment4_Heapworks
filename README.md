# MSCS532 Assignment 4 - Heapworks

## Overview

This repository contains implementations of heap-based algorithms and data structures for Assignment 4 of the MSCS 532 course. The project focuses on understanding and implementing heaps, heapsort algorithms, and priority queue-based scheduling systems.

## Contents

### Project Structure

```
├── heapsort_and_compare.py        # Part 1: Heapsort implementation & benchmarking
├── priority_queue_scheduler.py    # Part 2: Priority queue scheduler
└── README.md
```

## Part 1: Heapsort and Comparative Analysis

### File: `heapsort_and_compare.py`

Implements an in-place heapsort algorithm and compares its performance against merge sort and quicksort across different data distributions.

#### Key Components

- **Heapsort (Max-Heap)**
  - `heapify()` - Sift-down operation for maintaining heap property
  - `build_max_heap()` - Constructs a max-heap in O(n) time
  - `heapsort()` - Complete in-place sorting algorithm

- **Reference Algorithms**
  - `merge_sort()` - Merge sort implementation for comparison
  - `quick_sort()` - Randomized quicksort implementation

- **Benchmarking Framework**
  - `time_fn()` - Measures algorithm performance with validation
  - `run_benchmarks()` - Runs comprehensive performance tests across multiple data sizes and distributions
  - `print_results()` - Formats and displays benchmark results

#### Data Distributions Tested

- **Random**: Randomly shuffled integers
- **Sorted**: Already sorted sequences (best case for some algorithms)
- **Reverse**: Reverse-sorted sequences (worst case for some algorithms)

#### Usage

```bash
python heapsort_and_compare.py
```

This will run benchmarks on array sizes: 1K, 2K, 5K, 10K, and 20K elements.

---

## Part 2: Priority Queue Scheduler

### File: `priority_queue_scheduler.py`

Implements a task scheduling system using a priority queue (min-heap) structure.

#### Features

- Priority-based task scheduling
- Heap-based priority queue implementation
- Task management and execution simulation

#### Usage

```bash
python priority_queue_scheduler.py
```

---

## Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)

## Learning Objectives

- Understand heap data structure properties and operations
- Implement heapsort and analyze its time complexity (O(n log n))
- Perform empirical analysis comparing sorting algorithms
- Apply heaps to practical problems (priority queue scheduling)
- Analyze trade-offs between theoretical complexity and practical performance

## Time Complexity Analysis

| Algorithm  | Best Case      | Average Case   | Worst Case     | Space        |
|-----------|----------------|----------------|----------------|--------------|
| Heapsort  | O(n log n)     | O(n log n)     | O(n log n)     | O(1)         |
| Merge Sort| O(n log n)     | O(n log n)     | O(n log n)     | O(n)         |
| Quicksort | O(n log n)     | O(n log n)     | O(n²)          | O(log n)     |

## Key Insights

- **Heapsort** guarantees O(n log n) performance with O(1) space complexity
- Performance varies based on input distribution and data size
- Practical considerations (cache locality, constant factors) impact real-world performance
- Priority queues are essential for scheduling and resource management problems

## Notes

- Heapsort is performed **in-place**, while merge sort and quicksort create new arrays
- The benchmark uses `time.perf_counter()` for high-precision timing
- Each algorithm is validated to ensure correctness before timing

---

## Author

Created by GitHub Copilot Chat Assistant as part of MSCS 532 coursework

## License

Educational use

---

*Last Updated: February 16, 2026*