# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 4

# Node: 마을
class Node:
    def __init__(self, master):
        # 마을 주인
        self.master = master
        
        # 다음 마을
        self.next = None

# 마을 목록: build, move 함수를 통해 마을 추가 및 개척자 이동
class Linkedlist:
    def __init__(self, member_num):
        # 총 개척자 수
        self.member_num = member_num
        
        # 출발지: 마을 주인 없기때문에 master는 None
        self.head = Node(None)
        
        # 개척자가 현재 있는 위치
        # 개척자가 출발지에만 있으면 dict안에 추가되지 않음
        # build나 move를 통해 개척자가 다른 마을로 이동하면 dict에 추가
        # ex. {0: Node(0), 1: Node(1), 2: Node(0), 3: Node(1) ... }
        self.member_dict = {}
        
        # 총 마을 수
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