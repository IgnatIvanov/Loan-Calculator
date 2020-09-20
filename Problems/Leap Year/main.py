# put your python code here

year = int(input())

answer = "Ordinary"

if year % 4 == 0 and year % 100 != 0:
    answer = "Leap"
if year % 400 == 0:
    answer = "Leap"

print(answer)