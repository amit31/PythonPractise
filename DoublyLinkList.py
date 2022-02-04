class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def createList(self,arr):
        start=self.head
        n=len(arr)
        temp = start
        i=0

        while(i<n):
            newNode=Node(arr[i])
            if i==0:
                start=newNode
                temp=start
            else:
                temp.next=newNode
                newNode.prev=temp
                temp=temp.next
            i=i+1
        self.head=start
        return start

    def printList(self):
        temp=self.head
        linked_list= ""
        while(temp):
            linked_list+=(str(temp.data)+" ")
            temp=temp.next
        print(linked_list)

    def countList(self):
        count=0
        temp=self.head
        while temp:
               temp=temp.next
               count=count+1
        return count







    def insertAtlocation(self,value,index):
        temp=self.head
        count=self.countList()
        if count+1 < index:
             return temp
        newNode= Node(value)
        # First node
        if index==1:
            newNode.next=temp
            temp.prev=newNode
            self.head=newNode
            return self.head
       #last node
        if index==count+1:
            while temp.next is not None:
                  temp=temp.next

            temp.next=newNode
            newNode.prev=temp
            return self.head
        i=1
        while i < index-1:
            temp=temp.next
            i=i+1
        nodeAtTarget=temp.next
        newNode.next=nodeAtTarget
        nodeAtTarget.prev=newNode

        temp.next=newNode
        newNode.prev=temp

        return self.head







arr=[1,2,3,4,5]

dl=LinkedList()
dl.createList(arr)
dl.insertAtlocation(23,6)
dl.printList()

