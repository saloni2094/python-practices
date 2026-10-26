year = int(input(input("enter year: ")))

if year % 4 == 0:
    if year % 100 == 0:
        print('leap year')
    else:
        print("leap year")
else:
    print('not a leap year')