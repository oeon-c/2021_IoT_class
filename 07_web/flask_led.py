from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
app = Flask(__name__) #__name__은 파일명

#라우팅(함수로 연결해주는 것?)을 위한 뷰 함수

#p 태그는 문단
@app.route("/")
def hello():   
    return '''
    <p>Hello, Flask!!<p>
    <a href = "/led/on">LED ON</a>
    <a href = "/led/off">LED OFF</a>
     '''  #웹페이지에 보여줄 내용

#동적 라우팅(코드를 간결하게 만들 때 사용할 수 있음)
@app.route("/led/<op>") #중요한 건 여기! 
def led_op(op):    #함수명은 상관 없음(겹치지만 않게!)
    if op == "on": #밖의 라우팅 부분과 안의 함수에서는 변수 공유 안됨
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
        <p>LED ON<p>
        <a href = "/">Go Home</a>
        '''  #웹페이지에 보여줄 내용
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
        <p>LED OFF<p>
        <a href = "/">Go Home</a>
         ''' 

#터미널에서 직접 실행
if __name__ == "__main__": #파이썬에서 main 파일은 컴퓨터에서 직접 실행/다른 데서 날 부르기?
    app.run(host = '0.0.0.0') #또는 로컬

#라즈베리파이 말고 노트북에서 실행할거면 라즈베리파이 주소 쓰고 : 쓴 다음에 5000 쓰면 끝