#GitHub - 20SnowBall
import time
while True:
    print('Enter 1 number')
    number1=input()                              #Entering 1 number into a variable
    print('Enter 2 number')
    number2=input()                              #Entering 2 number into a variable
    if number1>number2:                          #Condition
        print('Number', number1, 'is greater')
    elif number1<number2:
        print('Number', number2, 'is greater')
    else:
        print('The numbers are equal')
    time.sleep(1)                                #Wait 1 second
    print('----------')
