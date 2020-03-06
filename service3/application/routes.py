from application import app
import random
from flask import request, jsonify, Response
import requests

@app.route('/', methods =['GET','POST'])
@app.route('/random_2', methods=['GET','POST'])
def random_2():
    
    name = str(request.data.decode("utf-8"))
    name = name.replace(' ','')
    index = random.randint(0,1)
    index -=1
    letter = name[index]
    letter = letter.lower()
    print(letter)

    if letter =='':
        letter_num= random.randint(0,25)
        print('space')
    
    else:
        asci =(ord(letter))
    
    if asci in range(97,123):
        letter_num = asci -97
        print('letters')
    else:
        print('random')
        letter_num = random.randint(0,25)

    if letter_num in range(13,27):
        letter_num = int(letter_num/2)
    
    return str(letter_num)





    
