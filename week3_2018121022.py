# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 3

def computeIndex(sequence, pattern):
    for i in range(len(sequence)-len(pattern)+1):
        for j in range(len(pattern)):
            if sequence[i+j] != pattern[j]:
                break
            if j == len(pattern)-1:
                return i
    return -1

a = []
b = []
num = input().split(' ')

for i in range(int(num[0])):
    a.append(int(input()))

for i in range(int(num[1])):
    b.append(int(input()))

print(computeIndex(a, b))