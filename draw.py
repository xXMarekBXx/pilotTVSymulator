class Draw():
    def __init__(self):
        pass

    def drawVolumeLevel(self, volumeLvl):
        volumeLvl = int(volumeLvl)
        match (volumeLvl):
            case 1:
                print('_____________')
                print('|          1 ')
                print('-------------')
            case 2:
                print('_____________')
                print('||          2')
                print('-------------')
            case 3:
                print('_____________')
                print('|||         3')
                print('-------------')
            case 4:
                print('_____________')
                print('||||        4')
                print('-------------')
            case 5:
                print('_____________')
                print('|||||       5')
                print('-------------')
            case 6:
                print('_____________')
                print('||||||      6')
                print('-------------')
            case 7:
                print('_____________')
                print('|||||||     7')
                print('-------------')
            case 8:
                print('_____________')
                print('||||||||    8')
                print('-------------')
            case 9:
                print('_____________')
                print('||||||||||  9')
                print('-------------')
            case 10:
                print('_____________')
                print('|||||||||| 10')
                print('-------------')

    def drawTvChannel(self, number):
        number = int(number)
        match (number):
            case 1:
                print('______________')
                print('|       | 2 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 2:
                print('______________')
                print('|       | 4 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 3:
                print('______________')
                print('|       | 6 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 4:
                print('______________')
                print('|       | 8 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 5:
                print('______________')
                print('|       | 11 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 6:
                print('______________')
                print('|       | 24 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 7:
                print('______________')
                print('|       | 32 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 8:
                print('______________')
                print('|       | 45 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 9:
                print('______________')
                print('|       | 67 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')
            case 10:
                print('______________')
                print('|       | 87 || ')
                print('|            |')
                print('--------------')
                print('|     LG     |')
                print('--------------')

draw = Draw()