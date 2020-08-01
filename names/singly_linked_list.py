class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def printAll(self, label = None):
        if label: print(label)
        n = self.head
        while n:
            print(f"\t{n.get_value()}\t{n}")
            n = n.get_next()

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        # print('add_to_tail: start')
        # self.printAll("before values")
        # vH = self.head.get_value() if self.head is not None else None
        # vT = self.tail.get_value() if self.tail is not None else None
        # print(f"head\t{vH}\t{self.head}")
        # print(f"tail\t{vT}\t{self.tail}")
        # print(f" new\t{new_node.get_value()}\t{new_node}")
        # print(f" len\t{self.length}")
        if self.head is None and self.tail is None:
            # print('new')
            self.head = new_node
        elif self.tail is not None:
            # print('not new')
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
        # vH = self.head.get_value() if self.head is not None else None
        # vT = self.tail.get_value() if self.tail is not None else None
        # print(f"head\t{vH}\t{self.head}")
        # print(f"tail\t{vT}\t{self.tail}")
        # print(f" new\t{new_node}\t{new_node.get_value()}")
        # print(f" len\t{self.length}")
        # self.printAll("after values")
        # print('add_to_tail: end\n')

    def remove_head(self):
        if self.head is None:
            return None
        value = self.head.get_value()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        self.length -= 1
        return value

    def remove_tail(self):
        prev_node = None
        cur_node = self.head
        while cur_node.next_node is not None:
            prev_node = cur_node
            cur_node = cur_node.next_node
        if prev_node is not None:
            prev_node.set_next(None)
        value = cur_node.get_value()
        cur_node = None
        self.tail = prev_node
        self.length -= 1
        return value

    def contains(self, value):
        # print('contains: start', value)
        # vH = self.head.get_value() if self.head is not None else None
        # vT = self.tail.get_value() if self.tail is not None else None
        # print('head', self.head, vH)
        # print('tail', self.tail, vT)
        # print(' len', self.length)
        test = False
        cur_node = self.head
        # print('start', cur_node)
        x = 0
        while cur_node is not None:
            v = cur_node.get_value()
            # print(f"    {x}", cur_node, v)
            if v == value:
                test = True
                # print("found!")
            cur_node = cur_node.next_node
            x += 1
        # print('contains: end')
        # print('found?', test)
        return test

    def get_max(self):
        # iterate through all elements
        max = -1
        cur_node = self.head
        while cur_node is not None:
            v = cur_node.get_value()
            if v > max:
                max = v
            cur_node = cur_node.next_node
        return None if max == -1 else max
