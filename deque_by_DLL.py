class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.itemcount = 0

    def is_empty(self):
        return self.itemcount == 0

    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = self.rear = n
        else:
            n.next = self.front
            self.front.prev = n
            self.front = n
        self.itemcount += 1

    def insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = self.rear = n
        else:
            n.prev = self.rear
            self.rear.next = n
            self.rear = n
        self.itemcount += 1

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.itemcount -= 1

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.itemcount -= 1

    def print_items(self):
        temp = self.front
        result = []
        while temp is not None:
            result.append(temp.data)
            temp = temp.next
        print(result)

# Test
q1 = deque()
q1.insert_at_start(20)
q1.insert_last(40)
q1.insert_last(50)
q1.insert_at_start(30)
q1.print_items()  
