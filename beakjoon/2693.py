a = int(input())
for i in range(a):
    n = list(map(int, input().split()))
    n.sort()
    print(n[2])