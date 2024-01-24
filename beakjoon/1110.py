n = input()
target = n[-1]
save = n
cnt = 0
if len(n) == 1:
    n = '0'+n
while n != target:
    s = 0
    for i in save:
        s+=int(i)
    target = save[-1]+str(s)[-1]
    save = target
    cnt += 1
print(cnt)