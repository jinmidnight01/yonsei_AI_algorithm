# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 7

def sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        sort(left_arr)
        sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

num = int(input())
input_list = []
for i in range(num):
    input_list.append(int(input()))

sorted_list = sort(input_list)
for i in range(num):
    print(sorted_list[i])