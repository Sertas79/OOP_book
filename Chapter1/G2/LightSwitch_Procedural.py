# Процедурный выключатель света

def turnOn():
    global switchIsOn
    # включаем свет
    switchIsOn = True

def turnOff():
    global switchIsOn
    switchIsOn = False

# основной код
switchIsOn = False
# код текста
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
