# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 4

class Node:
    def __init__(self, master, member_list):
        self.master = master
        self.member_list = member_list
        self.next = None

class Linkedlist:
    def __init__(self, member_list):
        self.head = Node(None, member_list)
        self.member_dict = {}
        self.size = 0
    
    def build(self, member):
        current = self.head
        if member in self.member_dict:
            current = self.member_dict[member]
        
        new_node = Node(member, [member])
        if current.next is not None:
            new_node.next = current.next
        current.next = new_node
        
        current.member_list.remove(member)
        self.member_dict[member] = new_node
        self.size = self.size + 1
        
    def move(self, member):
        current = self.head
        if member in self.member_dict:
            current = self.member_dict[member]

        if current.next is not None:
            current.member_list.remove(member)
            current.next.member_list.append(member)
            self.member_dict[member] = current.next            


first_line = input().split(' ')

member_list = [k for k in range(int(first_line[0]))]
command_list = []
for i in range(int(first_line[1])):
    # command = input().split(' ')
    command = [i, 'build']
    # if i >=0 and i < 10000:
    #     command = [i, 'build']
    # elif i >= 10000 and i < 20000:
    #     command = [i, 'move']
    # else:
    #     command = [i-20000, 'build']
    command_list.append(command)

import time
start = time.time()

linkedlist = Linkedlist(member_list)
for i in range(len(command_list)):
    member = int(command_list[i][0])
    action = command_list[i][1]

    if action == 'build':
        linkedlist.build(member)
    elif action == 'move':
        linkedlist.move(member)

print(linkedlist.size)
current = linkedlist.head.next
while current is not None:
    print(current.master)
    current = current.next

print("time :", time.time() - start)

