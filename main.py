from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from datetime import datetime
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
#db = SQLAlchemy(app)
app.config['MONGO_DBNAME'] = 'message'
app.config['MONGO_URI'] = 'mongodb+srv://iamgs75:%23mongo12345@cluster0-jqf9r.mongodb.net/message?retryWrites=true&w=majority'

mongo = PyMongo(app)

# class Messages(db.Model):
# sno = db.Column(db.Integer, primary_key=True)
#name = db.Column(db.String(80), nullable=False)
# email = db.Column(db.String(20),  nullable=False)
#date = db.Column(db.String(12), nullable=True)
#mes = db.Column(db.String(120), nullable=False)


@app.route("/", methods=['POST'])
def hello():
    #name = request.form.get('name')
    #email = request.form.get('email')
    #mes = request.form.get('message')
    #date = datetime.now()
    #entry = Messages(name=name, email=email, mes=mes, date=date)
    # db.session.add(entry)
    # db.session.commit()
    # print(data)
    users = mongo.db.users
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    date = datetime.now()

    user_id = users.insert({
        'name': name,
        'email': email,
        'subject': subject,
        'date': date
    })
    return redirect(url_for('success'))


@app.route('/hello')
def success():
    return render_template('success.html')


@app.route("/")
def ok():
    return render_template('index.html')


app.run()
