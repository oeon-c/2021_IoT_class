import RPi.GPIO as GPIO
import time

LED_PIN = 4
LED_PIN1 = 23
LED_PIN2 = 16                                                                                                                                                                                                                                                                 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

for i in range(3):
    GPIO.output(LED_PIN, GPIO.HIGH) 
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN, GPIO.LOW)  
    print("led off")
    time.sleep(2)
    GPIO.output(LED_PIN1, GPIO.HIGH) 
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN1, GPIO.LOW)  
    print("led off")
    time.sleep(2)
    GPIO.output(LED_PIN2, GPIO.HIGH) 
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN2, GPIO.LOW)  
    print("led off")
    time.sleep(2)

GPIO.cleanup()