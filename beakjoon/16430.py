import math

a, b = map(int, input().split())
p = b-a
q = b
if math.gcd(p, q) != 1:
    s = math.gcd(p, q)
    p //= s
    q //= s
print(p, q)