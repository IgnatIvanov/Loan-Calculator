jack_age = int(input())
alex_age = int(input())
lana_age = int(input())

if jack_age > alex_age:
    if alex_age > lana_age:
        print(lana_age)
    else:
        print(alex_age)
else:
    if jack_age > lana_age:
        print(lana_age)
    else:
        print(jack_age)
