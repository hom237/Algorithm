word = input()
result = 1
for i in range(0, len(word)//2):
    if word[i]!=word[len(word)-i-1]:
        result = 0
print(result)