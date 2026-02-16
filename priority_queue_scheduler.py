"""
Assignment 4 - Heaps
Part 2: Priority Queue implemented with a binary heap (array/list) + scheduler simulation
Author: <Your Name>
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Task:
    task_id: str
    priority: int        # higher number = higher priority (max-heap)
    arrival_time: int    # integer time unit
    deadline: int        # integer time unit (optional usage)
    duration: int = 1    # how many time units it takes to run


class MaxHeapPriorityQueue:
    """
    Max-heap priority queue using a Python list as an array-based binary heap.

    Key idea:
    - heap[i] children are heap[2i+1], heap[2i+2]
    - We also keep a 'pos' map: task_id -> index, to support O(log n) key updates.
    """

    def __init__(self) -> None:
        self.heap: List[Task] = []
        self.pos: Dict[str, int] = {}

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i].task_id] = i
        self.pos[self.heap[j].task_id] = j

    def _higher_priority(self, a: Task, b: Task) -> bool:
        """
        Return True if task a should come before task b.
        Tie-breakers: earlier arrival_time, then earlier deadline, then task_id.
        """
        if a.priority != b.priority:
            return a.priority > b.priority
        if a.arrival_time != b.arrival_time:
            return a.arrival_time < b.arrival_time
        if a.deadline != b.deadline:
            return a.deadline < b.deadline
        return a.task_id < b.task_id

    def insert(self, task: Task) -> None:
        """
        Insert task into heap.
        Time: O(log n)
        """
        if task.task_id in self.pos:
            raise ValueError("Task ID already exists in queue")

        self.heap.append(task)
        i = len(self.heap) - 1
        self.pos[task.task_id] = i
        self._sift_up(i)

    def extract_max(self) -> Task:
        """
        Remove and return max-priority task.
        Time: O(log n)
        """
        if self.is_empty():
            raise IndexError("extract_max from empty queue")

        root = self.heap[0]
        last = self.heap.pop()
        del self.pos[root.task_id]

        if self.heap:
            self.heap[0] = last
            self.pos[last.task_id] = 0
            self._sift_down(0)

        return root

    def increase_key(self, task_id: str, new_priority: int) -> None:
        """
        Increase priority of existing task and fix heap.
        Time: O(log n)
        """
        if task_id not in self.pos:
            raise KeyError("Task not found")
        i = self.pos[task_id]
        if new_priority < self.heap[i].priority:
            raise ValueError("new_priority is smaller; use decrease_key")

        self.heap[i].priority = new_priority
        self._sift_up(i)

    def decrease_key(self, task_id: str, new_priority: int) -> None:
        """
        Decrease priority of existing task and fix heap.
        Time: O(log n)
        """
        if task_id not in self.pos:
            raise KeyError("Task not found")
        i = self.pos[task_id]
        if new_priority > self.heap[i].priority:
            raise ValueError("new_priority is larger; use increase_key")

        self.heap[i].priority = new_priority
        self._sift_down(i)

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self._higher_priority(self.heap[i], self.heap[p]):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            best = i

            if left < n and self._higher_priority(self.heap[left], self.heap[best]):
                best = left
            if right < n and self._higher_priority(self.heap[right], self.heap[best]):
                best = right

            if best == i:
                break
            self._swap(i, best)
            i = best


# -----------------------------
# Simple scheduler simulation
# -----------------------------
def simulate_scheduler(tasks: List[Task], end_time: int) -> List[str]:
    """
    Simple non-preemptive scheduler:
    - At each time t: add all tasks whose arrival_time == t
    - If CPU idle and queue not empty: pick extract_max() and run it fully (duration units)
    Returns a timeline list showing what ran at each time unit.
    """
    pq = MaxHeapPriorityQueue()
    timeline: List[str] = []

    tasks_by_time: Dict[int, List[Task]] = {}
    for task in tasks:
        tasks_by_time.setdefault(task.arrival_time, []).append(task)

    current: Optional[Task] = None
    remaining = 0

    for t in range(end_time):
        # arrivals
        for task in tasks_by_time.get(t, []):
            pq.insert(task)

        # if idle, pick next
        if current is None and not pq.is_empty():
            current = pq.extract_max()
            remaining = current.duration

        # run 1 unit
        if current is None:
            timeline.append("IDLE")
        else:
            timeline.append(current.task_id)
            remaining -= 1
            if remaining == 0:
                current = None

    return timeline


if __name__ == "__main__":
    demo_tasks = [
        Task("A", priority=5, arrival_time=0, deadline=10, duration=2),
        Task("B", priority=9, arrival_time=1, deadline=5, duration=1),
        Task("C", priority=5, arrival_time=1, deadline=3, duration=2),
        Task("D", priority=1, arrival_time=2, deadline=9, duration=1),
    ]
    tl = simulate_scheduler(demo_tasks, end_time=8)
    print("Timeline:", tl)
