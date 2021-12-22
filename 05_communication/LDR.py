#얘가 조도센서
import spidev
import time

#SPI 인스턴스 생성
spi = spidev.SpiDev()

#SPI 통신 시작
spi.open(0,0) #bus(데이터가 흐르는 통로를 뜻함): 0, dev:0

#SPI 최대 통신 속도
spi.max_speed_hz = 100000

# analog -> digital 변환
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 : 0000 1000 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

try:
    while True:
        reading = analog_read(0)
        print("Reading=%d" % reading)
        time.sleep(0.5)
finally:
    spi.close() #모든 건 열었으면 닫아줘야 함 위에 open 부분 있음
