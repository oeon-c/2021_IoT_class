import RPi.GPIO as GPIO
import time

SWITCH_PIN = 5

GPIO.setmode(GPIO.BCM)

#GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) # 내부풀업저항 설정

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 내부풀다운저항 설정

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
