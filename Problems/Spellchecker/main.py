dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word = input()

count = 0
answer = "Incorrect"

while count < len(dictionary):
    if dictionary[count] == word:
        answer = "Correct"
        count = len(dictionary)
    count += 1

print(answer)