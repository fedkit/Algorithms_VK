class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
        i = len(self.data) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.data[p] <= self.data[i]:
                break
            self.data[p], self.data[i] = self.data[i], self.data[p]
            i = p

    def pop(self):
        if not self.data:
            return None

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        res = self.data.pop()

        i = 0
        n = len(self.data)

        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            m = i

            if l < n and self.data[l] < self.data[m]:
                m = l
            if r < n and self.data[r] < self.data[m]:
                m = r

            if m == i:
                break

            self.data[i], self.data[m] = self.data[m], self.data[i]
            i = m

        return res

    def peek(self):
        return self.data[0] if self.data else None

def solve(nums, k):
    heap = MinHeap()

    for i in nums:
        heap.push(i)
        if len(heap.data) > k:
            heap.pop()

    return heap.peek()

print(solve([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
