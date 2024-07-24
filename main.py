import os
import pilot

pilot = pilot.Pilot() #creating object from pilot.py file

while True:
    os.system('cls')
    print('_______________')
    print('| __      ___ |')
    print('||ON|    |OFF||')
    print('||1|  |2|  |3||')
    print('||4|  |5|  |6||')
    print('||7|  |8|  |9||')
    print('||0|  |+|  |-||')
    print('||UP|   |DOWN||')
    print('| __      ___ |')
    print('|     LG      |')
    print('|_____________|')

    option = input('Wchich option You want to choose? '
                   '1,2,3,4,5,6,7,8,9,0,+,-,ON,OFF, exit-close program: ')
    option = str(option)
    match (option):
        case '1':
            pilot.switchChannel(1)
        case '2':
            pilot.switchChannel(2)
        case '3':
            pilot.switchChannel(3)
        case '4':
            pilot.switchChannel(4)
        case '5':
            pilot.switchChannel(5)
        case '6':
            pilot.switchChannel(6)
        case '7':
            pilot.switchChannel(7)
        case '8':
            pilot.switchChannel(8)
        case '9':
            pilot.switchChannel(9)
        case '10':
            pilot.switchChannel(10)
        case '+':
            pilot.volumeUp()
        case '-':
            pilot.volumeDown()
        case 'ON':
            pilot.turnOnTv()
        case 'OFF':
            pilot.turnOffTv()
        case 'UP':
            print('channel UP')
        case 'DOWN':
            print('channel DOWN')
        case 'exit':
            print('program closed')
            exit()
        case _:
            print('You choose wrong option')