import RPi.GPIO as GPIO
import time

LED_PIN = 4
LED_PIN1 = 23
LED_PIN2 = 5
SWITCH_PIN = 26
SWITCH_PIN1 = 13
SWITCH_PIN2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
# 내부 풀다운저항 (안 눌렀을 때: 0, 눌렀을 때: 1)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
        val = GPIO.input(SWITCH_PIN1)
        print(val)
        GPIO.output(LED_PIN1, val)
        val = GPIO.input(SWITCH_PIN2)
        print(val)
        GPIO.output(LED_PIN2, val)
        #time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')