from flask import Flask,render_template

app1=Flask(__name__)



@app1.route('/')
@app1.route('/home')
def form():
    return render_template('form.html')



if __name__=="__main__":
    app1.run()