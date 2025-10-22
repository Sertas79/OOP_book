# класс TV
class TV:
    def __init__(self, lable):
        self.isOn = False
        self.isMuted = False
        self.lable = lable
        # Некий список каналов по умолчанию
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0 # костанта
        self.VOLUME_MAXIMUM = 100 # константа
        self.volume = self.VOLUME_MAXIMUM  # целочисленная переменная

    def power(self):
        self.isOn = not self.isOn # переключатель

    def volume_up(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # изменение громкости включает звук

        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1


    def volume_down(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # изменение громкости включает звук

        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channel_up(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex >= self.nChannels:
            self.channelIndex = 0

    def channel_down(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isMuted:
            return
        self.isMuted = not self.isMuted

    def set_channel(self, new_channel):
        if new_channel in self.channelList:
            self.channelIndex = self.channelList.index(new_channel)

    def show_info(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('     TV is: On')
            print('     Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('     Volume is', self.volume, '(sound is muted)')
            else:
                print('     Volume is', self.volume)
        else:
            print('     TV is: Off')

