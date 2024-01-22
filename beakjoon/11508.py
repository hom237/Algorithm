n = int(input())
items = []
cost = []
for i in range(n):
    items.append(int(input()))
items.sort()
while len(items) > 2:
    cost.append(items.pop(len(items) - 1))
    cost.append(items.pop(len(items) - 1))
    items.pop(len(items) - 1)
print(sum(cost)+sum(items))