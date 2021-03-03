value = int(input("Enter a pocket number from 0 to 36: "))
if value > 36 or value < 0:
    print('ERROR! You have entered the wrong number!')
elif value == 0:
    print('You have entered the pocket number %d which is GREEN!' % value)
elif 1 <= value <= 10:
    if (value % 2) == 0:
        print('You have entered the pocket number %d which is BLACK!' % value)
    else:
        print('You have entered the pocket number %d which is RED!' % value)
elif 11 <= value <= 18:
    if (value % 2) == 0:
        print('You have entered the pocket number %d which is RED!' % value)
    else:
        print('You have entered the pocket number %d which is BLACK!' % value)
elif 19 <= value <= 28:
    if (value % 2) == 0:
        print('You have entered the pocket number %d which is BLACK!' % value)
    else:
        print('You have entered the pocket number %d which is RED!' % value)
elif 29 <= value <= 36:
    if (value % 2) == 0:
        print('You have entered the pocket number %d which is RED!' % value)
    else:
        print('You have entered the pocket number %d which is BLACK!' % value)
