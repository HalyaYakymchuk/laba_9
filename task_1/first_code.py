"""implement queue using stack"""

# class MyQueue:
#     """queue built on stack"""

#     def __init__(self):
#         self.in_stack = []
#         self.out_stack = []

#     def move_elements(self):
#         """additional function for moving elements from one list to another"""
#         if not self.out_stack:
#             while self.in_stack:
#                 self.out_stack.append(self.in_stack.pop())


#     def push(self, x: int) -> None:
#         """adding element"""
#         self.in_stack.append(x)


#     def pop(self) -> int:
#         """deleting element"""
#         self.move_elements()
#         return self.out_stack.pop()


#     def peek(self) -> int:
#         """finding peek"""
#         self.move_elements()
#         return self.out_stack[-1]


#     def empty(self) -> bool:
#         """checking if stack is empty or not"""
#         return not self.out_stack and not self.in_stack


class Node:
    """node initialization"""
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    """queue built on stack"""

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        """adding element"""
        new_node = Node(x)
        if self.empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> int:
        """deleting element"""
        if self.empty():
            return
        data_paka = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return data_paka

    def peek(self) -> int:
        """finding peek"""
        if self.empty():
            return
        return self.head.data


    def empty(self):
        """checking if queue is empty or not"""
        return self.head is None





# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
