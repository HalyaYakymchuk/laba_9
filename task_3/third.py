class Node:
    """node initialising"""
    def __init__(self, data):
        self.data = data
        self.next = None

class FreqNode:
    """frequency node"""
    def __init__(self, freq):
        self.freq = freq
        self.stack_head = None
        self.next = None

class ValueFreqNode:
    """value frequency node"""
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.next = next


class FreqStack:
    """frequency stack"""
    def __init__(self):
        self.freq_levels_head = None
        self.values_head = None

    def get_count_and_increment(self, val):
        """looks for a number and calculates its new frequency"""
        current = self.values_head
        while current:
            if current.val == val:
                current.count += 1
                return current.count
            current = current.next

        new_val_node = ValueFreqNode(val)
        new_val_node.count = 1
        new_val_node.next =  self.values_head
        self.values_head = new_val_node
        return 1

    def decrement_count(self, val):
        """decreases the count"""
        current = self.values_head
        while current:
            if current.val == val:
                current.count -= 1
                return
            current = current.next

    def push(self, val: int) -> None:
        """adding an element"""
        f = self.get_count_and_increment(val)
        curr_f = self.freq_levels_head
        prev_f = None

        while curr_f and curr_f.freq < f:
            prev_f = curr_f
            curr_f = curr_f.next

        if not curr_f or curr_f.freq != f:
            new_f_node = FreqNode(f)
            if prev_f:
                new_f_node.next = prev_f.next
                prev_f.next = new_f_node
            else:
                new_f_node.next = self.freq_levels_head
                self.freq_levels_head = new_f_node
            curr_f = new_f_node

        new_node = Node(val)
        new_node.next = curr_f.stack_head
        curr_f.stack_head = new_node


    def pop(self) -> int:
        """removing an element"""
        curr_f = self.freq_levels_head
        if not curr_f:
            return -1
        prev_f = None

        while curr_f.next:
            prev_f = curr_f
            curr_f = curr_f.next

        val = curr_f.stack_head.data
        curr_f.stack_head = curr_f.stack_head.next
        self.decrement_count(val)

        if curr_f.stack_head is None:
            if prev_f:
                prev_f.next = None
            else:
                self.freq_levels_head = None

        return val




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
