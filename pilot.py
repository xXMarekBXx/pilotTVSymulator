import draw

draw = draw.Draw()

class Pilot():
    def __init__(self):
        self.turn_on = False
        self.MAX_VOLUME = 10
        self.MIN_VOLUME = 0
        self.currentVolume = 5
        self.numbers_channels = [2,4,6,8,11,24,32,45,67,89]
        self.channelIndex = 0 #index of the element from list numbers_channels
        self.current_channel = self.numbers_channels[self.channelIndex]

    def checkIfTvIsOn(self):
        if self.turn_on == True:
            print('Tv is on')
        else:
            print('Tv is off')

    def turnOnTv(self):
        if self.turn_on == True:
            print('You cant turn on tv. It is currently on.')
        elif self.turn_on == False:
            self.turn_on = True
            self.checkIfTvIsOn()

    def turnOffTv(self):
        if self.turn_on == False:
            print('You cant turn off tv. It is currently off.')
        else:
            self.turn_on = False
            self.checkIfTvIsOn()

    def changeChannelIndexAndChangeCurrenChannel(self, case):
        self.channelIndex = 0
        self.channelIndex = self.channelIndex + case - 1
        self.current_channel = self.numbers_channels[self.channelIndex]
        return self.channelIndex

    def checkVolume(self):
        if self.turn_on == False:
            print('You cant up volume becouse Tv is off. ')
        else:
            print('Current volume:', self.currentVolume)

    def switchChannel(self, number):
        if self.turn_on == True:
            match(number):
                case 1:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 2:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 3:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 4:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 5:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 6:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 7:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 8:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 9:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
                case 10:
                     pilot.changeChannelIndexAndChangeCurrenChannel(number)
                     pilot.checkChannel()
                     draw.drawTvChannel(number)
        else:
            print('You cant switch channel if tv is off')

    def checkChannel(self):
        print('Your are currently on chanel:', self.current_channel)

    def volumeUp(self):
        if self.turn_on == False:
            print('You cant up volume becouse Tv is off. ')
        else:
            if self.currentVolume == self.MAX_VOLUME:
                print('You cant up volume becouse it is max.')
            else:
                self.currentVolume = self.currentVolume + 1
                self.checkVolume()
                draw.drawVolumeLevel(self.currentVolume)
                return self.currentVolume

    def volumeDown(self):
        if self.turn_on == False:
            print('You cant down volume becouse Tv is off. ')
        else:
            if self.currentVolume == self.MIN_VOLUME:
                print('You cant down volume becouse it is min.')
            else:
                self.currentVolume = self.currentVolume - 1
                pilot.checkVolume()
                draw.drawVolumeLevel(self.currentVolume)
                return self.currentVolume
'''
    def channelUp(self):
        self.channelIndex = self.channelIndex + 1
        self.current_channel = self.numbers_channels[self.channelIndex]
        pilot.checkChannel()
        draw.drawTvChannel(self.channelIndex + 1)
        return self.channelIndex

    def channelDown(self):
        self.channelIndex = self.channelIndex - 1
        self.current_channel = self.numbers_channels[self.channelIndex]
        pilot.checkChannel()
        draw.drawTvChannel(self.channelIndex)
        return self.channelIndex
'''

pilot = Pilot()