# Write a Python program to create a class representing a linked list data structure. Include
# methods for displaying linked list data, inserting and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
        self.list = []
    
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.temp = self.head
        else:
            self.temp.next = Node(data)
            self.temp = self.temp.next
        self.list.append(data)
        
    def delete(self, data):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.data == data:
                self.head = self.head.next
            else:
                temp = self.head
                while temp.next is not None:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
        self.list.remove(data)
        
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    
    def get_list(self):
        return self.list
    
linked_list = LinkedList()

print("Enter your choice")
print("1. Insert the element")
print("2. Display the element")
print("3. Delete the element")
print("4. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter the data: ")
        linked_list.insert(data)
    elif choice == 2:
        linked_list.display()
    elif choice == 3:
        data = input("Enter the data: ")
        linked_list.delete(data)
    elif choice == 4:
        break
    else:
        print("Enter a Valid choice!")
