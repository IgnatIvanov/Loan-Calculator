in_word = input()

answer = ""
answer += str.lower(in_word[0])

for i in range(1, len(in_word), 1):
    if str.isupper(in_word[i]):
        answer += "_"
    answer += str.lower(in_word[i])
print(answer)