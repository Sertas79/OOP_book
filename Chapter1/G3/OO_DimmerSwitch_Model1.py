from DimmerSwitch import *

# создаем первый DimmerSwitch, включаем его и поднимаем уровень
# яркости дважды
o_dimmer1 = DimmerSwitch('Dimmer1')
o_dimmer1.turn_on()
o_dimmer1.raise_level()
o_dimmer1.raise_level()

# создаем второй DimmerSwitch, включаем его и поднимаем уровень
# яркость в 3 раза
o_dimmer2 = DimmerSwitch('Dimmer2')
o_dimmer2.turn_on()
o_dimmer2.raise_level()
o_dimmer2.raise_level()
o_dimmer2.raise_level()

# создаем третий DimmerSwitch, используя настройки по умолчанию
o_dimmer3 = DimmerSwitch('Dimmer3')

# просим каждый переключатель вывести свои показатели
o_dimmer1.show()
o_dimmer2.show()
o_dimmer3.show()

