import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody1 = [392, 392, 440, 440, 392, 392, 330]
melody2 = [392, 392, 330, 330]
melodyend1 = [294]
melody3 = [392, 330, 294, 330]
melodyend2 = [262]

#  도,  레,  미,  파,  솔,  라,  시,  도
# 262, 294, 330, 349, 392, 440, 494, 523

try:
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    for i in melodyend1:
        pwm.ChangeFrequency(i)
        time.sleep(2.0)
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    for i in melodyend2:
        pwm.ChangeFrequency(i)
        time.sleep(2.0)

finally:
    pwm.stop()
    GPIO.cleanup()