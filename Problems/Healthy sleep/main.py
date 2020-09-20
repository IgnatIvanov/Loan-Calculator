A = int(input())
B = int(input())
H = int(input())

answer = "Normal"

if H < A:
    answer = "Deficiency"
else:
    if B < H:
        answer = "Excess"

print(answer)