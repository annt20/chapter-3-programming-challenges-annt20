value = int(input("Enter a number from 1 to 12: "))
if value > 12 or value < 1:
    print('You have entered a wrong number!')
elif 1 <= value <= 3:
    print('You have entered the month which is in the first quarter.')
elif 4 <= value <= 6:
    print('You have entered the month which is in the second quarter.')
elif 7 <= value <= 9:
    print('You have entered the month which is in the third quarter.')
elif 10 <= value <= 12:
    print('You have entered the month which is in the fourth quarter.')
