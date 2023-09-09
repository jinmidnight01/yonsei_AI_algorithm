# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 1

count = int(input())

output = []
for i in range(count):
    cal = input().split(' ')
    if (cal[1] == 'plus'):
        output.append(int(cal[0]) + int(cal[2]))
    elif (cal[1] == 'times'):
        output.append(int(cal[0]) * int(cal[2]))

for element in output:
    print(element)