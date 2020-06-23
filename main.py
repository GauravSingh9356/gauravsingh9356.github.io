from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)


class Messages(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    date = db.Column(db.String(12), nullable=True)
    mes = db.Column(db.String(120), nullable=False)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        mes = request.form.get('message')
        date = datetime.now()
        entry = Messages(name=name, email=email, mes=mes, date=date)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')


@app.route("/index.html")
def ok():
    return render_template('index.html')


app.run()
