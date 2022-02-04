class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
      def __int__(self):
          self.head=None
          self.tail=None

      def __iter__(self):
          node=self.head
          while node:
                  yield node
                  node=node.next
                  if node ==self.tail.next:
                      break

      def createCSLL(self,nodeValue):
          node = Node(nodeValue)
          node.next=node
          self.head=node
          self.tail=node
          return "CSLL has been created"



      def insertCSLL(self,value,location):
          if self.head is None:
              return " The linked list does not exist"
          else:
              newNode=Node(value)
              if location ==0:
                  newNode.next=self.head
                  self.head=newNode
                  self.tail.next=newNode

              elif location ==1:
                   newNode.next=self.tail.next
                   self.tail.next=newNode
                   self.tail=newNode
              else :
                  tempNode=self.head
                  index=0
                  while index < location-1:
                        tempNode=tempNode.next
                        index=index+1
                  nextNode=tempNode.next
                  tempNode.next=newNode
                  newNode.next=nextNode
              return ("Node instrted ")


      def traversal(self):
          if self.head is None:
              print("There is no Linkedlist")
          else:
              tempNode=self.head
              while tempNode:
                  print(tempNode.value)
                  tempNode=tempNode.next
                  if tempNode == self.tail.next:
                      break

      def searchSLL(self,nodeValue):
          if self.head is None:
              print("The list does not exist")
          else:
              tempNode = self.head
              while tempNode :
                   if tempNode.value==nodeValue:
                       return tempNode.value
                   tempNode=tempNode.next
                   if tempNode ==self.tail.next:
                       return "Node does not exist"


circularsll= CircularSinglyLinkedList()
print(circularsll.createCSLL(1))

circularsll.insertCSLL(0,0)
circularsll.insertCSLL(2,1)
circularsll.insertCSLL(3,1)
circularsll.insertCSLL(2,2)

circularsll.traversal()
g=circularsll.searchSLL(4)
print(g)
#print([node.value for node in circularsll])
