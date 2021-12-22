from flask import Flask, render_template

app = Flask(__name__) #__name__은 파일명

#라우팅(함수로 연결해주는 것?)을 위한 뷰 함수

#p 태그는 문단
@app.route("/")
def hello():   
    return render_template(
        "html.html",
        title="Hello") #title의 hello라는 값을 html.html로 전달하겠다

@app.route("/first") #중요한 건 여기!
def first():    #함수명은 상관 없음
    return render_template(
        "first.html",
        title="First Page")  #웹페이지에 보여줄 내용

@app.route("/second")
def second():   
    return render_template(
        "second.html",
        title = "Sencond Page") #웹페이지에 보여줄 내용
#터미널에서 직접 실행
if __name__ == "__main__": #파이썬에서 main 파일은 컴퓨터에서 직접 실행/다른 데서 날 부르기?
    app.run(host = '0.0.0.0') #또는 로컬

#라즈베리파이 말고 노트북에서 실행할거면 라즈베리파이 주소 쓰고 : 쓴 다음에 5000 쓰면 끝