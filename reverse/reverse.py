class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def printAll(self):
        n = self
        i = 0
        while n:
            print(f"{i}\t{n.get_value()}\t{n}")
            i += 1
            n = n.get_next()

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        p = prev
        c = node
        n = None

        # print("begin")
        # self.head.printAll()

        while c:
            n = c.get_next()
            c.set_next(p)
            p = c
            c = n
        self.head = p

        # print("end")
        # self.head.printAll()
