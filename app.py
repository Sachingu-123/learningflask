from flask import Flask,render_template,request

#create a simple flask appli.

app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return "First Commit"

@app.route('/index',methods=['GET'])
def index():
    return "<h1>Second Commit</h1>"

#variable rule
@app.route('/success/<int:score>')
def success(score):
    return "the person has passed the exam with score "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed the exam with score "+ str(score)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='GET':
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)