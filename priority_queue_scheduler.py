from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Task:
    # Represents a schedulable task
    task_id: str
    priority: int        # higher value = higher priority
    arrival_time: int    # time when task enters system
    deadline: int        # used for tie-breaking
    duration: int = 1    # how long the task runs


class MaxHeapPriorityQueue:
    """
    Max-heap priority queue using an array-based binary heap.
    Also maintains a map: task_id -> index for fast updates.
    """

    def __init__(self) -> None:
        self.heap: List[Task] = []   # stores tasks
        self.pos: Dict[str, int] = {}  # maps task_id to index

    def is_empty(self) -> bool:
        # Check if heap has no elements
        return len(self.heap) == 0

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        # Swap two nodes and update their positions
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i].task_id] = i
        self.pos[self.heap[j].task_id] = j

    def _higher_priority(self, a: Task, b: Task) -> bool:
        """
        Returns True if task 'a' should come before 'b'.
        Tie-breaking rules applied.
        """
        if a.priority != b.priority:
            return a.priority > b.priority
        if a.arrival_time != b.arrival_time:
            return a.arrival_time < b.arrival_time
        if a.deadline != b.deadline:
            return a.deadline < b.deadline
        return a.task_id < b.task_id

    def insert(self, task: Task) -> None:
        # Add a new task into heap
        if task.task_id in self.pos:
            raise ValueError("Task ID already exists")

        self.heap.append(task)
        i = len(self.heap) - 1
        self.pos[task.task_id] = i
        self._sift_up(i)  # restore heap property

    def extract_max(self) -> Task:
        # Remove and return highest-priority task
        if self.is_empty():
            raise IndexError("extract from empty queue")

        root = self.heap[0]
        last = self.heap.pop()
        del self.pos[root.task_id]

        # Move last element to root and fix heap
        if self.heap:
            self.heap[0] = last
            self.pos[last.task_id] = 0
            self._sift_down(0)

        return root

    def increase_key(self, task_id: str, new_priority: int) -> None:
        # Increase priority and move task upward
        if task_id not in self.pos:
            raise KeyError("Task not found")

        i = self.pos[task_id]
        if new_priority < self.heap[i].priority:
            raise ValueError("Priority must increase")

        self.heap[i].priority = new_priority
        self._sift_up(i)

    def decrease_key(self, task_id: str, new_priority: int) -> None:
        # Decrease priority and move task downward
        if task_id not in self.pos:
            raise KeyError("Task not found")

        i = self.pos[task_id]
        if new_priority > self.heap[i].priority:
            raise ValueError("Priority must decrease")

        self.heap[i].priority = new_priority
        self._sift_down(i)

    def _sift_up(self, i: int) -> None:
        # Move element up until heap property satisfied
        while i > 0:
            p = self._parent(i)
            if self._higher_priority(self.heap[i], self.heap[p]):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        # Move element down until heap property satisfied
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
    Non-preemptive scheduler:
    - Add tasks when they arrive
    - Always run highest-priority task
    - Run until its duration completes
    """

    pq = MaxHeapPriorityQueue()
    timeline: List[str] = []

    # Group tasks by arrival time
    tasks_by_time: Dict[int, List[Task]] = {}
    for task in tasks:
        tasks_by_time.setdefault(task.arrival_time, []).append(task)

    current: Optional[Task] = None
    remaining = 0

    # Simulate time step by step
    for t in range(end_time):

        # Insert newly arrived tasks
        for task in tasks_by_time.get(t, []):
            pq.insert(task)

        # If CPU idle, pick next highest priority task
        if current is None and not pq.is_empty():
            current = pq.extract_max()
            remaining = current.duration

        # Run for one time unit
        if current is None:
            timeline.append("IDLE")
        else:
            timeline.append(current.task_id)
            remaining -= 1

            # Task finished
            if remaining == 0:
                current = None

    return timeline


if __name__ == "__main__":
    # Example tasks for demo
    demo_tasks = [
        Task("A", priority=5, arrival_time=0, deadline=10, duration=2),
        Task("B", priority=9, arrival_time=1, deadline=5, duration=1),
        Task("C", priority=5, arrival_time=1, deadline=3, duration=2),
        Task("D", priority=1, arrival_time=2, deadline=9, duration=1),
    ]

    # Run scheduler simulation
    tl = simulate_scheduler(demo_tasks, end_time=8)
    print("Timeline:", tl)
