from machine import Timer,Pin

led = Pin(2,Pin.OUT)

timer = Timer(0)

timer.init(period=1000,mode=Timer.PERIODIC,callback = lambda t: led.value(not led.value()))
