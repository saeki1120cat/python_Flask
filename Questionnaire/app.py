from flask import render_template, request, redirect, flash, url_for, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base    #雖然沒有import pymysql 但是還是要裝喔!

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root@localhost:3306/ques_data') # mysql+pymysql://帳號:密碼@localhost:3306/資料庫


app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/ques_data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class USER(Base):
    __tablename__ = 'user2' #這邊是要連線的資料庫名稱

    #id = Column(String(10), primary_key=True, autoincrement=True)
    username = Column(String(10), nullable=False)
    email = Column(String(120), primary_key=True, nullable=False)
    gender = Column(String(3), default=None)
    age = Column(String(3), default=None)
    height = Column(Integer, default=None)
    weight = Column(Integer, default=None)
    disliked = Column(String(120), default=False)
    health = Column(String(3), default=None)
    fried = Column(String(3), default=None)
    vegetable = Column(String(3), default=None)
    activity = Column(String(3), default=None)

    def __init__(self, username, email, gender, age, height, weight, disliked, health, fried, vegetable, activity):
        self.username = username
        self.email = email
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.disliked = disliked
        self.health = health
        self.fried = fried
        self.vegetable = vegetable
        self.activity = activity

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Questionnaire.html')

    elif request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            gender = request.form['gender']
            age = request.form['age']
            height = request.form['height']
            weight = request.form['weight']
            disliked = request.form['disliked']
            health = request.form['health']
            fried = request.form['fried']
            vegetable = request.form['vegetable']
            activity = request.form['activity']

            Session = sessionmaker(bind=engine)
            session = Session()
            ed_user = USER(username = username, email = email, gender = gender, age = age, height = height, weight = weight, disliked = disliked, health = health, fried = fried, vegetable = vegetable, activity = activity)
            session.add(ed_user)
            session.commit()
            session.close()
            flash('Item Created.')
            return render_template('End_screen.html')

        except:
            flash('Invalid input.')
            return redirect(url_for('register'))


if __name__ == '__main__':
    app.debug = True
    app.run()