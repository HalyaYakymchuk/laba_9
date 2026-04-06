"""implementing stack using queues"""

class MyStack:
    """stack implementation using queues"""

    def __init__(self):
        self.first_queue = []
        self.second_queue = []


    def push(self, x: int) -> None:
        """adding new element"""
        self.first_queue.append(x)


    def move_elements(self):
        """additional function for moving elements from one list to another"""
        if not self.second_queue:
            while self.first_queue:
                self.second_queue.append(self.first_queue.pop())


    def pop(self) -> int:
        """removing one element"""
        self.move_elements()
        return self.second_queue[0]


    def top(self) -> int:
        """returning the top element"""
        self.move_elements()
        return self.second_queue[0]


    def empty(self) -> bool:
        """defining whether queue is empty or not"""
        return not self.first_queue and not self.second_queue




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
