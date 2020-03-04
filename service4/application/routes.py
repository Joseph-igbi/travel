from application.models import City
from application import app, db
from flask import render_template, redirect, url_for, request, Response
import requests

@app.route('/', methods=['GET','POST'])
@app.route('/dbchoose', methods=['GET','POST'])
def dbchoose():
    
    name = request.data.decode("utf-8")
    name=str(name)
    
    num = requests.post('http://service3:5000/random_2', name).text
    num_response=int(num)

    index = requests.post('http://service2:5000/random_1', name).text
    lst = index.strip('[]').split(',')
              
    rand = int(lst[int(num_response)])

    dbcity = City.query.filter_by(id=rand).first()
    city = str(dbcity.city_name)
    
    
    
    
    return str(city)
