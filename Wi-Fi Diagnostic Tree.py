print('Welcome to Wifi Troubleshooting Help')
print('First, reboot the computer and try to connect!')
answer = str(input('Did that fix the problem? (yes or no)'))
if answer == 'yes':
    print('Congratulation! Your troubles have been fixed properly!')
else:
    print('Next, reboot the router and try to connect!')
    answer = str(input('Did that fix the problem? (yes or no)'))
    if answer == 'yes':
        print('Congratulation! Your troubles have been fixed properly!')
    else:
        print('Make sure the cables between the router and modem are plugged in firmly!')
        answer = str(input('Did that fix the problem? (yes or no)'))
        if answer == 'yes':
            print('Congratulation! Your troubles have been fixed properly!')
        else:
            print('Move the router to a new location!')
            answer = str(input('Did that fix the problem? (yes or no)'))
            if answer == 'yes':
                print('Congratulation! Your troubles have been fixed properly!')
            else:
                print('You should buy a new router!')
