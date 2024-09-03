class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ImplemetingQueuebylinkedlist:
    def __init__(self):
        self.root=None
    def addelements(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
        else:
            temp=self.root
            while temp.next!=None:
                temp=temp.next
            temp.next=node
    def  poptheelements(self):
        if self.root==None:
            return
        else:
            temp=self.root
            temp.next=None
    def peek(self):
        if self.root==None:
            return
        else:
            temp=self.root
            return temp.data
    def isempty(self):
        if self.root==None:
            return True
        else:
            return False
obj=ImplemetingQueuebylinkedlist()
n=int(input('enter number of nodes:'))
for 