import math

x = int(input())

print(round(math.exp(x) / (1 + math.exp(x)), 2))