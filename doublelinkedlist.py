class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublelinkedlist:
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
            node.prev=temp
    def printfarward(self):
        if self.root==None:
            return 
        else:
            temp=self.root
            while temp.next!=None:
                print(temp.data)
                temp=temp.next
            print(temp.data)
    def backward(self):
        if self.root is None:
            return 
        else:
            temp=self.root
            while temp.next!=None:
                temp=temp.next

object=Doublelinkedlist()
n=int(input('enter number of nodes:'))
for i in range(n):
    val=int(input('enter the value:'))
    object.addelements(val)
print('print the elements in forward direction')
object.printfarward()
print('print the elements in backward direction')
object.backward()           
            
            
