class deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def insert_atstart(self,data):

        self.items.insert(0,data)

    def insert_at_last(self,data):
        self.items.append(data)

    def delete_from_last(self):

        self.items.pop()

    def delete_from_front(self) :
        self.items.pop(0)  

    def get_front(self):
        return self.items[0]
    
    def get_rear(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    
q1=deque()
q1.insert_at_last(1)
q1.insert_atstart(4)
q1.insert_at_last(90)
print(q1.items)