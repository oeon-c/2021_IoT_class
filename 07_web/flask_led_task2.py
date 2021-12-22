from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 17
LED_PIN2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
app = Flask(__name__) #__name__은 파일명

#라우팅(함수로 연결해주는 것?)을 위한 뷰 함수

#p 태그는 문단
@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<color>/<op>") 
def led_op(color ,op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return "RED LED ON"
        elif op == "off":
            GPIO.output(LED_PIN, GPIO.LOW)
            return "RED LED OFF"
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return "BLUE LED ON"
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return "BLUE LED OFF"
    else:
        return "URL Error"


if __name__ == "__main__": #파이썬에서 main 파일은 컴퓨터에서 직접 실행/다른 데서 날 부르기?
    try:
        app.run(host = '0.0.0.0') #또는 로컬
    finally:
        GPIO.cleanup()
#라즈베리파이 말고 노트북에서 실행할거면 라즈베리파이 주소 쓰고 : 쓴 다음에 5000 쓰면 끝