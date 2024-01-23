a = int(input())
for i in range(a):
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    print(n[2])