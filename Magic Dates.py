day = int(input('Enter a day from 1 to 31: '))
month = int(input('Enter a month from 1 to 12: '))
year = int(input('Enter a year (xx): '))
if year == day * month:
    print('The date you have entered is magic!')
else:
    print('The date you have entered is NOT magic!')

