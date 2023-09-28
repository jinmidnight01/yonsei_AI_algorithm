# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 4

class Node:
    def __init__(self, master):
        self.master = master
        self.next = None

class Linkedlist:
    def __init__(self, member_num):
        self.member_num = member_num
        self.head = Node(None)
        self.member_dict = {}
        self.size = 0
    
    def build(self, member):
        if member >= self.member_num:
            return
        
        current = self.head
        if member in self.member_dict:
            current = self.member_dict[member]
        
        new_node = Node(member)
        if current.next is not None:
            new_node.next = current.next
        current.next = new_node
        
        self.member_dict[member] = new_node
        self.size = self.size + 1
        
    def move(self, member):
        if member >= self.member_num:
            return
        
        current = self.head
        if member in self.member_dict:
            current = self.member_dict[member]

        if current.next is not None:
            self.member_dict[member] = current.next            

first_line = input().split(' ')
member_num = int(first_line[0])
command_num = int(first_line[1])

command_list = []
for i in range(command_num):
    command = input().split(' ')
    command_list.append(command)

linkedlist = Linkedlist(member_num)
for i in range(command_num):
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