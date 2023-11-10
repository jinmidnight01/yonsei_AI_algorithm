# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 10

a = [0,2,4,3,1,5,9,5,8,6]
n = len(a) - 1

# part1
for i in range(n // 2, 0, -1):
  pi = i
  while 2 * pi <= n:
    ci = 2 * pi
    if 2 * pi + 1 <= n:
      if a[2 * pi] < a[2 * pi + 1]:
        ci = 2 * pi + 1
    if a[pi] >= a[ci]:
      break
    tmp = a[pi]
    a[pi] = a[ci]
    a[ci] = tmp
    pi = ci

# part2
for m in range(n,1,-1):
  tmp = a[1]
  a[1] = a[m]
  a[m] = tmp
  pi = 1
  while 2 * pi <= m - 1:
    ci = 2 * pi
    if 2 * pi + 1 <= m - 1:
      if a[2 * pi] < a[2 * pi + 1]:
        ci = 2 * pi + 1
    if a[pi] >= a[ci]:
      break
    tmp = a[pi]
    a[pi] = a[ci]
    a[ci] = tmp
    pi = ci