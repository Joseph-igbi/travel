

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
    	index = random.sample(range(0,20),18)
    	tw= random.sample(range(20,40),2)
    	fr= random.sample(range(40,60),2)
    	sx= random.sample(range(60,80),2)
    	eg= random.sample(range(80,100),2)
    	for i in [tw,fr,sx,eg]:
            for a in i:
            	index.append(a)
    if char =='B':
    	index = random.sample(range(20,40),18)
    	zr= random.sample(range(0,20),2)
    	fr= random.sample(range(40,60),2)
    	sx= random.sample(range(60,80),2)
    	eg= random.sample(range(80,100),2)
    	for i in [zr,fr,sx,eg]:
            for a in i:
            	index.append(a)
    if char =='C':
        index = random.sample(range(40,60),18)
        zr= random.sample(range(0,20),2)
        tw= random.sample(range(20,40),2)
        sx= random.sample(range(60,80),2)
        eg= random.sample(range(80,100),2)
        for i in [zr,tw,sx,eg]:
            for a in i:
                index.append(a)
    if char =='D':
        index = random.sample(range(60,80),18)
        zr= random.sample(range(0,20),2)
        tw= random.sample(range(20,40),2)
        fr= random.sample(range(40,60),2)
        eg= random.sample(range(80,100),2)
        for i in [zr,tw,fr,eg]:
            for a in i:
            	index.append(a)
    if char =='E':
    	index = random.sample(range(80,100),18)
    	zr= random.sample(range(0,20),2)
    	tw= random.sample(range(20,40),2)
    	fr= random.sample(range(40,60),2)
    	sx= random.sample(range(60,80),2)
    	for i in [zr,tw,fr,sx]:
            for a in i:
                index.append(a)
    print('length of list for {}: '.format(char), len(index))
    print(index)

    


    return str(index)


