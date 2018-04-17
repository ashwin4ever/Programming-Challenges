#Linked List implementation in Python

class Node:

      def __init__(self , data):

            self.data = data
            self.next = None

class LinkedList:

      def __init__(self):

            self.head = None


      #add data at the head
      def push(self , val):

            #create new node and add data
            new_node = Node(val)

            #make head point to new node
            new_node.next = self.head

            #make new node as head
            self.head = new_node

      #add node to the end
      def append(self , val):

            #create a new node and add data
            new_node = Node(val)

            #check if head in none
            if self.head is None:
                  self.head = new_node
                  return

            prev = self.head

            while prev.next:
                  prev = prev.next

            prev.next = new_node
            new_node.next = None


      def printList(self):

            temp = self.head

            while temp:
                  print(temp.data , ' -> ' , end ='')
                  temp = temp.next

            print(None)
            
l = LinkedList()
l.push(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.printList()
