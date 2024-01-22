word = input()
result = 1
for i in range(0, len(word)//2):
    if word[i]!=word[len(word)-i-1]:
        result = 0
print(result)
# a = input()
# re_a = a[::-1]
# if re_a == a:
#     print(1)
# else:
#     print(0)