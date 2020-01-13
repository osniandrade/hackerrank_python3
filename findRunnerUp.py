# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

list = []

for num in arr:
    list.append(num)

list.sort(reverse=True)

i = 0

while list[i+1] >= list[i]:
    i += 1

print(list[i+1])
