class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, array):
        self.heap = array
        bottom_parent_index = (len(array) - 1) // 2
        for starting_index in reversed(range(bottom_parent_index)):
            self.sift_down(starting_index)
        return self.heap

    def swap(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

    ######### INSERT (log n) ##########

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, starting_index):
        parent_index = (starting_index - 1) // 2
        while (
            self.heap[starting_index] < self.heap[parent_index] and starting_index > 0
        ):
            self.swap(starting_index, parent_index)
            starting_index = parent_index
            parent_index = (starting_index - 1) // 2

    ######## REMOVE (log n) ############

    def pop(self):
        self.swap(0, len(self.heap) - 1)
        popped = self.heap.pop()
        self.sift_down(0)
        return popped

    def sift_down(self, starting_index):
        min_child_index = self.min_child_index(starting_index)
        while (
            self.heap[starting_index] > self.heap[min_child_index]
            and starting_index < len(self.heap) - 1
        ):
            self.swap(starting_index, min_child_index)
            starting_index = min_child_index
            min_child_index = self.min_child_index(starting_index)

    def min_child_index(self, parent_index):
        heap_bound = len(self.heap) - 1

        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        if left_child_index > heap_bound:
            return parent_index
        elif right_child_index > heap_bound:
            return left_child_index
        else:
            return (
                left_child_index
                if self.heap[left_child_index] <= self.heap[right_child_index]
                else right_child_index
            )


class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, array):
        self.heap = array
        bottom_parent_index = (len(array) - 1) // 2
        for starting_index in reversed(range(bottom_parent_index)):
            self.sift_down(starting_index)
        return self.heap

    def swap(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

    ######### INSERT (log n) ##########

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, starting_index):
        parent_index = (starting_index - 1) // 2
        while (
            self.heap[starting_index] > self.heap[parent_index] and starting_index > 0
        ):  # Changed in MaxHeap
            self.swap(starting_index, parent_index)
            starting_index = parent_index
            parent_index = (starting_index - 1) // 2

    ######## REMOVE (log n) ############

    def pop(self):
        self.swap(0, len(self.heap) - 1)
        popped = self.heap.pop()
        self.sift_down(0)
        return popped

    def sift_down(self, starting_index):
        max_child_index = self.max_child_index(starting_index)
        while (
            self.heap[starting_index] < self.heap[max_child_index]
            and starting_index < len(self.heap) - 1
        ):  # Changed in MaxHeap
            self.swap(starting_index, max_child_index)
            starting_index = max_child_index
            max_child_index = self.max_child_index(starting_index)

    def max_child_index(self, parent_index):
        heap_bound = len(self.heap) - 1

        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        if left_child_index > heap_bound:
            return parent_index
        elif right_child_index > heap_bound:
            return left_child_index
        else:
            return (
                left_child_index
                if self.heap[left_child_index] >= self.heap[right_child_index]
                else right_child_index
            )  # Changed in MaxHeap
