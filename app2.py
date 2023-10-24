from flask import Flask,render_template

app2=Flask(__name__)

posts=[
    {
        'Course':"Data Science",
        'topic':"Flask",
        'experience':'fresher',
        'college':'sea College'
    },
     {
        'Course':"Data Analytics",
        'topic':"Flask",
        'experience':'1 year',
        'college':'CRM College'
    }
]

@app2.route('/post')
def home():
    return render_template('post.html',posts=posts)



if __name__=="__main__":
    app2.run(debug=True)