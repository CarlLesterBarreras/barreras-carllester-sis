from flask import Flask, render_template, request, redirect
from users import Users
from students import Students

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form['username']
    password = request.form['password']

    result = Users.check_user(username, password)

    if result:
        return redirect('/student-list')
    else:
         return render_template('login.html')

@app.route('/student-list')
def student_list():

    students = Students.get_all()

    return render_template('student.html', students=students)

@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/grades')
def grades():
    return render_template('grades.html')


if __name__ == '__main__':
    app.run()