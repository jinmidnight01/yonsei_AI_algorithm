# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 6

def matrix(n, i, j):
    if n == 0 or i == j:
        return 0
    
    if (i <= 2 ** (n-1) and j > 2 ** (n-1)) or (i > 2 ** (n-1) and j <= 2 ** (n-1)):
        return n
    
    new_i = i % (2 ** (n-1))
    new_j = j % (2 ** (n-1))
    if new_i == 0:
        new_i = 2 ** (n-1)
    if new_j == 0:
        new_j = 2 ** (n-1)
        
    return matrix(n-1, new_i, new_j)

command_list = []
for i in range(int(input())):
    command = input().split()
    command_list.append(command)

for command in command_list:
    print(matrix(int(command[0]), int(command[1]), int(command[2])))