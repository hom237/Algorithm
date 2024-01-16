def pac(n):
    if n <= 1:
        return 1
    else:
        return n*pac(n-1)
print(pac(3))

