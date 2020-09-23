time_zone = int(input())

if time_zone >= 14:
    print("Wednesday")
elif time_zone < -10:
    print("Monday")
else:
    print("Tuesday")