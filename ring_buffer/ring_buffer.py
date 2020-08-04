class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = [None] * capacity
        self.head = 0
        self.tail = 0

    def __str__(self):
        return str(self.container)

    def append(self, item):
        t = (self.tail + 1) % self.capacity
        # print(f"\nappend: {item}\nhead: {self.head}, tail: {self.tail}, capacity: {self.capacity} new tail: {t}")
        self.container[self.tail] = item
        # print(self)
        self.tail = t

    def get(self):
        v = []
        for i in range(self.capacity):
            if self.container[i] is not None:
                v.append(self.container[i])
        # print(f"\nget:\n{v}")
        return v
