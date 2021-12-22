from flask import Flask

app = Flask(__name__) #__name__은 파일명

#라우팅(함수로 연결해주는 것?)을 위한 뷰 함수

#p 태그는 문단
@app.route("/")
def hello():   
    return '''
    <p>Hello, Flask!!<p>
    <a href = "/first">Go first</a>
    <a href = "/second">Go second</a>
     '''  #웹페이지에 보여줄 내용

@app.route("/first") #중요한 건 여기!
def first():    #함수명은 상관 없음
    return '''
    <p>First Page<p>
    <a href = "/">Go Home</a>
     '''  #웹페이지에 보여줄 내용

@app.route("/second")
def second():   
    return '''
    <p>Second Page<p>
    <a href = "/">Go Home</a>
     '''  #웹페이지에 보여줄 내용

#터미널에서 직접 실행
if __name__ == "__main__": #파이썬에서 main 파일은 컴퓨터에서 직접 실행/다른 데서 날 부르기?
    app.run(host = '0.0.0.0') #또는 로컬

#라즈베리파이 말고 노트북에서 실행할거면 라즈베리파이 주소 쓰고 : 쓴 다음에 5000 쓰면 끝