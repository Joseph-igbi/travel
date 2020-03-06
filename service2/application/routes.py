

from flask import redirect, url_for, request, Response
from application import app
import random 
import requests

@app.route('/')
@app.route('/random_1', methods=['GET','POST'])
def random_1():
    name = request.data.decode("utf-8")

    name = name.replace(' ','')


    length = len(name)
    re = length %5

    if re == 0:
        char = 'A'
    
    elif re ==1:
        char = 'B'

    elif re == 2:
    	char = 'C'
    
    elif re == 3:
    	char = 'D'
    
    else:
    	char = 'E'
	
    if char =='A':
    	index = random.sample(range(0,20),13)
    if char =='B':
    	index = random.sample(range(20,40),13)
    if char =='C':
        index = random.sample(range(40,60),18)
    if char =='D':
        index = random.sample(range(60,80),18)
    if char =='E':
    	index = random.sample(range(80,100),18)

    return str(index)


