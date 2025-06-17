from linkedlist import *

class stack:
    def __init__(self):
        self.mylist=singly_linked_list()
        self.itemcount=0

    def isempty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.itemcount +=1

    def pop(self):
        self.mylist.delete_first()
        self.itemcount-=1

    def peek(self):
        if not self.isempty():
            return self.mylist.start.item
    def print_stack(self):
        return self.mylist.print_list()
s=stack()
s.push(20)
s.push(30)
s.pop
print("top element",s.peek())
print("list content")
s.print_stack()

    