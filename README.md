# MSCS532 Assignment 4 - Heapworks

## Overview

This repository contains implementations of heap-based algorithms and data structures for Assignment 4 of the MSCS 532 course. The project focuses on understanding and implementing heaps, heapsort algorithms, and priority queue-based scheduling systems.

---

## Project Structure

```
├── heapsort_and_compare.py        # Part 1: Heapsort implementation & benchmarking
├── priority_queue_scheduler.py    # Part 2: Priority queue scheduler simulation
└── README.md
```

---

## How to Run the Code

Follow these steps to execute the programs:

### Step 1: Clone the Repository

```bash
git clone <your-repository-link>
cd <repository-folder>
```

### Step 2: Run Heapsort Benchmark Program

```bash
python heapsort_and_compare.py
```

This will:

* Execute sorting benchmarks
* Compare heapsort, merge sort, and quicksort
* Display performance results for multiple input sizes and distributions

### Step 3: Run Priority Queue Scheduler Simulation

```bash
python priority_queue_scheduler.py
```

This will:

* Simulate task scheduling using a max-heap priority queue
* Print the execution timeline of tasks

---

## Part 1: Heapsort and Comparative Analysis

### File: `heapsort_and_compare.py`

Implements an in-place heapsort algorithm and compares its performance against merge sort and quicksort across different data distributions.

#### Key Components

* **Heapsort (Max-Heap)**

  * `heapify()` – Maintains heap property
  * `build_max_heap()` – Builds max heap in O(n)
  * `heapsort()` – Complete in-place sorting algorithm

* **Reference Algorithms**

  * `merge_sort()` – Merge sort implementation
  * `quick_sort()` – Randomized quicksort implementation

* **Benchmarking Framework**

  * `time_fn()` – Measures execution time
  * `run_benchmarks()` – Runs full comparison tests
  * `print_results()` – Displays results in table format

#### Data Distributions Tested

* Random data
* Sorted data
* Reverse-sorted data

---

## Part 2: Priority Queue Scheduler

### File: `priority_queue_scheduler.py`

Implements a task scheduling system using a max-heap priority queue.

#### Features

* Priority-based task scheduling
* Heap-based priority queue implementation
* Task execution simulation
* Non-preemptive scheduling strategy

---

## Time Complexity Analysis

| Algorithm  | Best Case  | Average Case | Worst Case | Space    |
| ---------- | ---------- | ------------ | ---------- | -------- |
| Heapsort   | O(n log n) | O(n log n)   | O(n log n) | O(1)     |
| Merge Sort | O(n log n) | O(n log n)   | O(n log n) | O(n)     |
| Quicksort  | O(n log n) | O(n log n)   | O(n²)      | O(log n) |

---

## Summary of Findings

Based on experimental benchmarking results:

* Heapsort showed consistent performance across all input types because its time complexity remains O(n log n).
* Merge sort generally performed faster than heapsort due to better cache efficiency, though it requires extra memory.
* Quicksort performed very well on random inputs but showed slower performance on sorted and reverse inputs.
* Performance differences became more noticeable as input size increased.
* Experimental results matched theoretical time complexity expectations.

---

## Learning Objectives

* Understand heap data structure operations
* Implement heapsort algorithm
* Compare sorting algorithm performance
* Apply priority queues to scheduling problems
* Analyze theoretical vs practical performance trade-offs

---

## Requirements

* Python 3.7+
* No external dependencies required

---

## License

Educational use only.
