from models.database import db
from flask import Flask, render_template, request

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit', methods=['POST'])
def confirmar():
    if request.method == 'POST':
        nome= request.form['nome']
        contato= request.form['contato']
        email= request.form['email']
        msg= request.form['msg']
        #print(nome, contato, email, msg)
        if nome == '' or email == '' or contato == '' and msg == '':
            return render_template('contact.html', message='Há campos a ser preenchidos.')
        return render_template('index.html')


if __name__ == '__main__':               
    app.run(debug=True)    
