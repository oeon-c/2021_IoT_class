import Adafruit_DHT
from lcd import drivers
import time
import datetime

sensor = Adafruit_DHT.DHT11
display = drivers.Lcd()
DHT_PIN = 17

try:
    while True: 
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        h,t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            display.lcd_display_string(str(t) + "*C, " + str(h) + "%", 2) #파이썬에서는 문자열끼리만 더할 수 있고, LCD 디스플레이에는 문자열만 출력될 수 있어서 숫자인 온도, 습도를 문자열로 바꿔주고 출력한 것임
        else:
            display.lcd_display_string('Read Error',2)


finally:
    print('cleaning up')
    display.lcd_clear()

