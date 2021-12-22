from _typeshed import OpenTextModeUpdating
import RPi.GPIO as GPIO
import time

#GPIO 7개 핀 번호 설정
#               A  B  C  D  E  F  G 
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8] #리스트 

GPIO.setmode(GPIO.BCM)

for segmemt in SEGMENT_PINS:
    GPIO.setup(segmemt, GPIO.OUT)
    GPIO.output(segmemt, GPIO.LOW)

#Common Cathode (HIGH->ON, LOW->OFF)
data = [1, 1, 1, 1, 1, 1, 0]

try:
    for _ in range(3): # 0~2
        for in in range(7): # 0~6
            GPIO.output(SEGMENT_PINS[i], data[i])

    time.sleep(1)
    
        for in in range(7):
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)
        time.sleep(1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
