# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 9

def inorderTraversal(arr, index):
  if index < len(arr):
    inorderTraversal(arr, 2 * index + 1)
    print(arr[index])
    inorderTraversal(arr, 2 * index + 2)

n = int(input())
data = []
for i in range(n):
  data.append(input())
inorderTraversal(data, 0)