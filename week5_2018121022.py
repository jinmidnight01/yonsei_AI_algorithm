# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 5

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enq(self, item):
        node = Node(item)
        if self.size == 0:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.size += 1
        return 0

    def deq(self):
        if self.size == 0:
            return -1
        else:
            item = self.front.item
            self.front = self.front.next
            self.size -= 1
            return item

input_num = int(input())
command_list = []

for i in range(input_num):
    command = input().split()
    command_list.append(command)

queue = LinkedQueue()
for i in range(input_num):
    if command_list[i][0] == 'enq':
        print(queue.enq(command_list[i][1]))
    else:
        print(queue.deq())