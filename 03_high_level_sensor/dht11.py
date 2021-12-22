import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 2

try:
    while True:
        h,t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' %(h,t)) #뒤에 humidity에 %두개는 하나는 서식 하나는 %를 출력
        else:
            print('Read Error')

finally:
    print('bye')