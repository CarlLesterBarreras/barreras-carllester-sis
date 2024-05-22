from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/student-list')
def studentlist():
    return render_template('student.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/grades')
def grades():
    return render_template('grades.html')


if __name__ == '__main__':
    app.run()