n = int(input())
line = list(map(int, input().split()))
line.sort()
time = 0
for i in range(1, n+1):
    time+= sum(line[:i])
print(time)