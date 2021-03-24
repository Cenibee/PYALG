class MyCircularQueue:

    def __init__(self, k: int):
        self.circular_q = [-1] * k
        self.head = 0
        self.tail = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.circular_q[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.circular_q[self.head] = -1
        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        return self.circular_q[self.head]

    def Rear(self) -> int:
        return self.circular_q[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.circular_q[self.head] == -1

    def isFull(self) -> bool:
        return self.tail == self.head and self.circular_q[self.head] != -1

sol = MyCircularQueue(3)
print(sol.enQueue(1))
print(sol.enQueue(2))
print(sol.enQueue(3))
print(sol.enQueue(4))
print(sol.circular_q)
print(sol.Rear())
print(sol.isFull())
print(sol.deQueue())
print(sol.enQueue(4))
print(sol.Rear())
print(sol.circular_q)
