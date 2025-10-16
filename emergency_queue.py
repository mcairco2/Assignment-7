class Patient:
    def __init__(self, name, urgency):
        """
        Represents a patient with a name and urgency score.
        Lower urgency value = higher priority.
        """
        self.name = name
        self.urgency = urgency

    def __lt__(self, other):
        """Compare patients based on urgency."""
        return self.urgency < other.urgency

    def __repr__(self):
        """Readable representation for printing."""
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        """Initialize an empty heap."""
        self.data = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def insert(self, patient):
        """
        Add a new patient to the heap.
        """
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        """Reorder heap after insert (bubble up)."""
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.data[index] < self.data[parent_index]:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        """Reorder heap after removal (bubble down)."""
        size = len(self.data)
        while True:
            left_index = self.get_left_child_index(index)
            right_index = self.get_right_child_index(index)
            smallest = index

            if left_index < size and self.data[left_index] < self.data[smallest]:
                smallest = left_index
            if right_index < size and self.data[right_index] < self.data[smallest]:
                smallest = right_index

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def peek(self):
        """Return the most urgent patient (root) without removing."""
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        """Remove and return the most urgent patient (root)."""
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()  # Move last to root
        self.heapify_down(0)
        return root

    def print_heap(self):
        """Print the current queue."""
        if not self.data:
            print("Queue is empty.")
            return
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


# -------------------------------
# TEST YOUR HEAP HERE
# -------------------------------
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Morgan", 2))
    heap.print_heap()

    print("\nNext up:", heap.peek())

    print("\nServing most urgent patient...")
    served = heap.remove_min()
    print("Served:", served)

    heap.print_heap()

    print("\nServing another patient...")
    served = heap.remove_min()
    print("Served:", served)
    heap.print_heap()

    print("\nEdge case: removing all remaining patients...")
    while heap.peek() is not None:
        print("Served:", heap.remove_min())
    heap.print_heap()