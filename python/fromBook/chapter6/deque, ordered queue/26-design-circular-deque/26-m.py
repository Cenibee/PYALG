class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.q = [-1] * k
        self.head = 0 # 마지막으로 헤드가 들어간곳
        self.tail = 0 # 다음 테일이 들어가야할 곳
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.head = (self.head - 1) % self.size
        self.q[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.q[self.head] = -1
        self.head = (self.head + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.tail = (self.tail - 1) % self.size
        self.q[self.tail] = -1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.q[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.q[self.tail - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head == self.tail and self.q[self.head] == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.head == self.tail and self.q[self.head] != -1


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()