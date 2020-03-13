
from wtforms.validators import ValidationError 
from flask import render_template, redirect, url_for, request, Response
from application import app, db, bcrypt
from application.forms import NameForm, LoginForm, RegistrationForm, UpdateCommentForm
from application.models import Users, Locations 
from flask_login import login_user, current_user, logout_user, login_required
import requests
import random
import os



# Account functionalities
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
    return render_template('login.html', title='TravelBug', form=form)


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

@app.route("/account_delete", methods=['GET','POST'])
@login_required
def account_delete():
    user =current_user.id
    locations = Locations.query.filter_by(user_id=user).all()
    for location in locations:
        db.session.delete(location)
    account = Users.query.filter_by (id = user).first()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))








# Main service functionalities
@app.route('/search', methods=['GET','POST'])
def search():
    form = NameForm() 
    if form.validate_on_submit():
        name= str(form.name.data)
        response = requests.post('http://service4:5000/dbchoose', name)
        destination= response.text
        lst = destination.strip('[]').split(',')
        city = lst[0]
        country = lst[1]
        country = str(country)
        return redirect(url_for('result', city=city, country=country, name=name))

    return render_template('search.html', title='TravelBug', form=form)

@app.route('/result/<city>/<country>/<name>', methods=['GET', 'POST'])
def result(city,country,name):
    name = str(name)
    city = str(city)
    country= str(country).strip("'")
    api = os.getenv('GOOGLE_API')
    url='https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+tourist+attraction&language=en&key={}'
    r = requests.get(url.format(city,api)).json()
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

    return render_template('result.html', title='TravelBug', api=api, name=name ,country=str(country).strip("'"), city=city, location=location, width=picture['width'], ref=picture['photo_reference'])


@app.route('/add_location/<country>/<activity>/<rating>/<city>/<ref>', methods=['GET', 'POST'])
def add_location(country,activity,rating,city,ref):
    if not current_user.is_authenticated:
        return redirect(url_for('register'))
    country = str(country).strip("'")
    activity = str(activity)
    rating = str(rating)
    city=str(city).strip("'")
    ref = str(ref)

    location = Locations(country=country, city=city, activity= activity, address=rating, user_id = current_user.id, ref=ref)
    db.session.add(location)
    db.session.commit()
    return redirect(url_for('view_location'))

@app.route('/view_location', methods=['GET','POST'])
def view_location():
    api = os.getenv('GOOGLE_API')
    if not current_user.is_authenticated:
        return redirect(url_for('register'))
    user = current_user.id
    loc = Locations.query.filter_by(traveller=current_user).all()
    name = str(current_user.first_name)
    return render_template('locations.html', locations=loc, name=name, api=api)

@app.route('/pic_location/<ref>', methods=['GET','POST'])
def pic_location(ref):
    if not current_user.is_authenticated:
        return redirect(url_for('register'))
    ref = ref
    return render_template('pic_location.html', ref=ref)

@app.route('/update_comment/<location_id>', methods=['GET','POST'])
def update_comment(location_id):
    if not current_user.is_authenticated:
        return redirect(url_for('register'))
    form = UpdateCommentForm()
    if form.validate_on_submit():
        dbcomment = Locations.query.filter_by(id=int(location_id)).first()
        dbcomment.comment = form.comment.data
        db.session.commit()
        return redirect(url_for('view_location'))


    return render_template('update_comments.html', form=form)
    

@app.route('/delete_location/<location_id>', methods=['GET', 'POST'])
def delete_location(location_id):
    if not current_user.is_authenticated:
        return redirect(url_for('register'))
    loc = Locations.query.filter_by(id=int(location_id)).first()
    db.session.delete(loc)
    db.session.commit()
    return redirect(url_for('view_location'))




