# Write a Python program to create a class representing a queue data structure. Include methods
# for enqueueing and dequeuing elements.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)
        
queue = Queue()

print("Enter your choice")
print("1. Enqueue the element")
print("2. Dequeue the element")
print("3. Display the element")
print("4.Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter the data: ")
        queue.enqueue(data)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Enter a Valid choice!")