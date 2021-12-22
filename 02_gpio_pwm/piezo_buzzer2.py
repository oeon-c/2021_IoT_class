import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [262,294, 330, 349, 392, 440, 494, 523] #도, 레, 미, 파, 솔, 라, 시, 도

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()