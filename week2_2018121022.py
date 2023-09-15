# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 2

def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (array[mid] == target):
            return mid
        elif (array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return -1

a = []
q = []
num = input().split(' ')

for i in range(int(num[0])):
    a.append(int(input()))

for i in range(int(num[1])):
    q.append(int(input()))

for i in range(len(q)):
    print(binary_search(a, q[i]))