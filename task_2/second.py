"""implementing stack using queues"""

# class MyStack:
#     """stack implementation using queues"""

#     def __init__(self):
#         self.first_queue = []
#         self.second_queue = []


#     def push(self, x: int) -> None:
#         """adding new element"""
#         self.first_queue.append(x)


#     def move_elements(self):
#         """additional function for moving elements from one list to another"""
#         if not self.second_queue:
#             while self.first_queue:
#                 self.second_queue.append(self.first_queue.pop())


#     def pop(self) -> int:
#         """removing one element"""
#         self.move_elements()
#         return self.second_queue[0]


#     def top(self) -> int:
#         """returning the top element"""
#         self.move_elements()
#         return self.second_queue[0]


#     def empty(self) -> bool:
#         """defining whether queue is empty or not"""
#         return not self.first_queue and not self.second_queue






class Node:
    """node initialization"""
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    """stack implementing using linked lists"""
    def __init__(self):
        self.head = None

    def push(self, data):
        """adding element"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """deleting element"""
        if self.empty():
            return None
        data_paka = self.head.data
        self.head = self.head.next
        return data_paka

    def top(self):
        """finding peek"""
        return self.head.data if self.head else None

    def empty(self):
        """checking if stack is empty or not"""
        return self.head is None





# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
