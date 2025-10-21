# OO_LightSwitch
class LightSwitch():
    def __init__(self):
        self.switchOn = False

    def turn_on(self):
        self.switchOn = True

    def turn_off(self):
        self.switchOn = False

    def show(self):
        print(self.switchOn)

# Основной код
oLightSwitch = LightSwitch()

oLightSwitch.show()
oLightSwitch.turn_on()
oLightSwitch.turn_off()
oLightSwitch.show()
oLightSwitch.turn_off()
oLightSwitch.show()
oLightSwitch.turn_on()
oLightSwitch.show()

