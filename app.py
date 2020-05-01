from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import datetime
from datetime import *


app = Flask(__name__)

app.config  ['SQLALCHEMY_DATABASE_URI']='sqlite:///yt.db'
db = SQLAlchemy(app)

class Tutor_fe(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=10001)
    email=db.Column(db.String(30), unique=True, nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    username=db.Column(db.String(30), nullable=False)
    password=db.Column(db.String(30), nullable=False)
    dob=db.Column(db.DateTime, nullable=False)
    phone=db.Column(db.Integer, nullable=False)
    qualification=db.Column(db.String(12), nullable=False)
    district=db.Column(db.String(12), nullable=False)
    taluk=db.Column(db.String(12), nullable=False)
    village=db.Column(db.String(12), nullable=False)
    tuition=db.Column(db.String(12), nullable=False)
    maths=db.Column(db.Boolean, nullable=True, default=False)
    science=db.Column(db.Boolean, nullable=True, default=False)
    social=db.Column(db.Boolean, nullable=True, default=False)
    computer=db.Column(db.Boolean, nullable=True, default=False)
    physics=db.Column(db.Boolean, nullable=True, default=False)
    chemistry=db.Column(db.Boolean, nullable=True, default=False)
    biology=db.Column(db.Boolean, nullable=True, default=False)
    scmaths=db.Column(db.Boolean, nullable=True, default=False)
    extra=db.Column(db.String(100), nullable=True, default='False')
    image=db.Column(db.LargeBinary, nullable=False, default='False')
    student=db.Column(db.String(30),  default='False')
    earn=db.Column(db.Float,default=0)
    totalearn=db.Column(db.Float,default=0)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    isvarify=db.Column(db.Boolean, nullable=True, default=False)
    ismale=db.Column(db.Boolean, nullable=False)
    isindian=db.Column(db.Boolean, nullable=True, default=True)
    nonindplace=db.Column(db.String(20),  default='False')
class Tutor_m(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=20001)
    email=db.Column(db.String(30), unique=True, nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    username=db.Column(db.String(30), nullable=False)
    password=db.Column(db.String(30), nullable=False)
    dob=db.Column(db.DateTime, nullable=False)
    phone=db.Column(db.Integer, nullable=False)
    qualification=db.Column(db.String(12), nullable=False)
    district=db.Column(db.String(12), nullable=False)
    taluk=db.Column(db.String(12), nullable=False)
    village=db.Column(db.String(12), nullable=False)
    tuition=db.Column(db.String(12), nullable=False)
    maths=db.Column(db.Boolean, nullable=True, default=False)
    science=db.Column(db.Boolean, nullable=True, default=False)
    social=db.Column(db.Boolean, nullable=True, default=False)
    computer=db.Column(db.Boolean, nullable=True, default=False)
    physics=db.Column(db.Boolean, nullable=True, default=False)
    chemistry=db.Column(db.Boolean, nullable=True, default=False)
    biology=db.Column(db.Boolean, nullable=True, default=False)
    scmaths=db.Column(db.Boolean, nullable=True, default=False)
    extra=db.Column(db.String(100), nullable=True, default='False')
    image=db.Column(db.LargeBinary, nullable=False, default='False')
    student=db.Column(db.String(30),  default='False')
    earn=db.Column(db.Float,default=0)
    totalearn=db.Column(db.Float,default=0)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    isvarify=db.Column(db.Boolean, nullable=True, default=False)
    ismale=db.Column(db.Boolean, nullable=False)
    isindian=db.Column(db.Boolean, nullable=True, default=True)
    nonindplace=db.Column(db.String(20),  default='False')
class Customer(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=30001)
    email=db.Column(db.String(100), unique=True, nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    username=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    dob=db.Column(db.DateTime, nullable=False)
    phone=db.Column(db.Integer, nullable=False)
    qualification=db.Column(db.String(12), nullable=False)
    district=db.Column(db.String(12), nullable=False)
    taluk=db.Column(db.String(12), nullable=False)
    village=db.Column(db.String(12), nullable=False)
    tuition=db.Column(db.String(12), nullable=False)
    image=db.Column(db.LargeBinary, nullable=False, default='False')
    tutor=db.Column(db.String(300),  default='False')
    attend=db.Column(db.Integer,nullable=True)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    ismale=db.Column(db.Boolean, nullable=False)


@app.route('/')
def helo():
    return render_template('home.html')



@app.route('/tutor/register',methods=['GET','POST'])
def tutreg():
    if request.method == "POST" :
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        do =request.form.get("dob")
        do = do.split('-')
        print(do)
        # dob=datetime.date(int(do[0]),int(do[1]),int(do[2]))
        dob = date(int(do[0]),int(do[1]),int(do[2]))
        phone = request.form.get("phone")
        qualification = request.form.get("qualification")
        tuition = request.form.get("tuition")
        maths = bool(request.form.get("maths"))
        science = bool(request.form.get("science"))
        social = bool(request.form.get("social"))
        computer = bool(request.form.get("computer"))
        physics = bool(request.form.get("physics"))
        chemistry = bool(request.form.get("chemistry"))
        biology = bool(request.form.get("biology"))
        scmaths = bool(request.form.get("ScMaths"))
        extra = request.form.get("extra")
        username = request.form.get("username")
        name = request.form.get("name")
        ismale=bool(request.form.get("male"))
        image = request.files['image']
        # print(ismale)
        # return(image.read())
        # return(ismale)
        # return(image.filename)
        
        

        pin=request.form.get('pin')
        loc=requests.get('https://api.postalpincode.in/pincode/'+pin)
        locn=loc.json()
        location=locn[0]["PostOffice"][0]["Name"]
        block=locn[0]["PostOffice"][0]["Block"]
        district=locn[0]["PostOffice"][0]["District"]
        # print(location + " " + block + " " + district)
        #  extra=formm['extra']

        if(password1 == password2):
            if(ismale):
                user=Tutor_m(fname=name, username=username, email=email, password=password1, dob=dob, phone=phone, qualification=qualification, district=district, taluk=block, village=location, tuition=tuition, maths=maths, science=science, social=social, computer=computer, physics=physics, chemistry=chemistry, biology=biology, scmaths=scmaths, extra=extra, image=image.read(), ismale=ismale )
                db.session.add(user)
                db.session.commit()
                print('commited')
                return redirect('/')
            else:
                user=Tutor_fe(fname=name, username=username, email=email, password=password1, dob=dob, phone=phone, qualification=qualification, district=district, taluk=block, village=location, tuition=tuition, maths=maths, science=science, social=social, computer=computer, physics=physics, chemistry=chemistry, biology=biology, scmaths=scmaths, extra=extra, image=image.read(), ismale=ismale )
                db.session.add(user)
                db.session.commit()
                print('commited')
                return redirect('/')

            # user=Tutor(fname=name, username=username, email=email, password=password1, dob=dob, phone=phone, qualification=qualification, district=district, taluk=block, village=location, tuition=tuition, maths=maths, science=science, social=social, computer=computer, physics=physics, chemistry=chemistry, biology=biology, scmaths=scmaths, extra=extra, image=image )
            db.session.add(user)
            db.session.commit()
            print('commited')
            return redirect('/')
        else:
            print("password Miss match")
        # print(formm)

    # missing = Tutor.query.filter_by(email='arjun.sk@outlook.com').first()  
    # print(missing)  
    return render_template('tutReg.html',tutor='active')


if __name__ == '__main__':
    app.run(debug=True)