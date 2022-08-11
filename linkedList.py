class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_first(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_last(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)


    def print(self):
        if self.head==None:
            print("Empty")
            return
        itr=self.head
        storage=''
        while itr:
            storage+=str(itr.data)+'-->'
            itr=itr.next
        print(storage)


ll=LinkedList()
ll.insert_first(30)
ll.insert_last(20)
ll.insert_last(10)
ll.print()