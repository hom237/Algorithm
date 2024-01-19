n = int(input())
for k in range(n):
    coin = input()
    pattern = ["TTT","TTH","THT","THH","HTT","HTH","HHT","HHH"]
    result = [0 for i in range(len(pattern))]
    for i in range(0, len(coin)-2):
        for j in range(len(pattern)):
            if pattern[j] == coin[i:i+3]:
                result[j] += 1
    print(*result)