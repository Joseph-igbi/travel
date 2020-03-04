from application import app
import random
from flask import request, jsonify, Response
import requests

@app.route('/', methods =['GET','POST'])
@app.route('/random_2', methods=['GET','POST'])
def random_2():
    
    name = str(request.data.decode("utf-8"))
    length = len(name)
    number = random.randint(0,(length-1))
    letter= name[number]
    letter = letter.lower()
    print(letter)

    if letter =='':
        letter_num= random.randint(1,27)
        print('space')
    
    else:
        asci =(ord(letter))
    
    if asci in range(97,123):
        letter_num = asci -96
        print('letters')
    else:
        print('random')
        letter_num = random.randint(1,27)
    
    return str(letter_num)





    
