
from wtforms.validators import ValidationError 
from flask import render_template, redirect, url_for, request, Response
from application import app, db, bcrypt
from application.forms import NameForm, LoginForm, RegistrationForm
from application.models import Users
from flask_login import login_user, current_user, logout_user, login_required

import requests
import random




@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return redirect(url_for('search'))

        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('search'))
    else:
        print(form.errors)
    return render_template('login.html', title='Login', form=form)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(first_name=form.first_name.data,last_name= form.last_name.data,email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('register.html', title='Register', form = form)
@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    user =current_user
    return render_template('account.html', title='Hi %s'%(user.first_name),user=user )






@app.route('/search', methods=['GET','POST'])
def search():
    form = NameForm() 
    if form.validate_on_submit():
        name= str(form.name.data)
        response = requests.post('http://service4:5000/dbchoose', name)
        city = response.text
        return redirect(url_for('result', city=city))
    return render_template('search.html', title='TRAVEL BUG', form=form)








@app.route('/result/<city>', methods=['GET', 'POST'])
def result(city):
    #form = NameForm()
    #city = request.data.decode("utf-8")
    city = str(city)

    #city = form.name.data
    url='https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+tourist+attraction&language=en&key=AIzaSyDHm-RLScd8iBylQ0YGNB44NcmKIU8teDQ'
    r = requests.get(url.format(city)).json()
    num=random.randint(0,len(r['results'])-1)
    location = {
                'name': r['results'][num]['name'],
                'address':r['results'][num]['formatted_address'],
                'rating':r['results'][num]['rating']
                }
    print(location)
        

    picture = {
                'height': r['results'][num]['photos'][0]['height'],
                'html_attributions': r['results'][num]['photos'][0]['html_attributions'],
                'width': r['results'][num]['photos'][0]['width'],
                'photo_reference': r['results'][num]['photos'][0]['photo_reference']
            }
    
    





    return render_template('result.html', title='TRAVEL BUG', location=location, width=picture['width'], ref=picture['photo_reference'])



