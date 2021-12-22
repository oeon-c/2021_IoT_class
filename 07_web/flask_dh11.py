from flask import Flask, render_template
import Adafruit_DHT
import json  #클라이언트랑 서버랑 통신할 때... 어... 난 파이썬을 잘 모르는디 뭐 dictionary랑 비슷하대... key value?왔다갔다

sensor = Adafruit_DHT.DHT11
DHT_PIN = 17

app = Flask(__name__)   

@app.route("/")
def home():
    return render_template("dht11.html")

@app.route("/moniter")
def monitoring():
    h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
    print (h, t)
    if h is not None and t is not None: #둘 다 값이 있으면, data라는 이름의 (json)객체
        data = {'humidity':h, 'temperature': t}
        return json.dumps(data) #문자열로 바꿔서 return 해주는 함수 dumps
    else:
        return 'Read error' 

if __name__ == "__main__": #파이썬에서 main 파일은 컴퓨터에서 직접 실행/다른 데서 날 부르기?
    app.run(host = '0.0.0.0') #또는 로컬