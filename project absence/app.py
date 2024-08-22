from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')





from flask import render_template, request, redirect, url_for

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        

        return redirect(url_for('student'))

    return render_template('signin.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        
        return redirect(url_for('signedup'))
    return render_template('signup.html')


@app.route('/aboutus')
def aboutus():
    return '<h2>Add later</h2>'

@app.route('/contactus')
def contactus():
    return '<h2>Add later</h2>'

@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/scanned')
def scanned():
    return render_template('scanned.html')

@app.route('/historystudent')
def historystudent():
    return render_template('historystudent.html')

@app.route('/historyteacher')
def historyteacher():
    return render_template('historyteacher.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/activate')
def activate():
    return render_template('activate.html')



@app.route('/kill')
def kill():
    return render_template('kill.html')

@app.route('/signedup')
def signedup():
    return render_template('signedup.html')

    

if __name__ == '__main__':
    app.run(debug=True)

