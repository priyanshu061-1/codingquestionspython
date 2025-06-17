class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class singly_linked_list:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):

        if not self.is_empty():
            n=Node(data)
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            
            temp.next=n
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None

        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

