from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://matthewacutler:NU2bI6PoEeKs@ep-shiny-mouse-158204.us-east-2.aws.neon.tech/sarah-profile'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(200), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    account_number = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.Text)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/update_notes', methods=['POST'])
def update_notes():
    user_id = request.form.get('user_id')
    notes = request.form.get('notes')
    user = User.query.get(user_id)
    user.notes = notes
    db.session.commit()
    return redirect('/')
