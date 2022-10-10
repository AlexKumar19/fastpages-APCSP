import random
import math
from flask import Flask, request
app = Flask(__name__)

quotes = ["The sky is the limit - Kalani", "The celling is the roof - Micheal Jordan", "You miss 100%\ of the shots you don't take -Wayne Gretsky", "hehe - Navan", "JSON! - Mort"]
def randomgen():
    number = int(random.random()*len(quotes))
    return number

@app.route('/get', methods=['GET']) 
def get():
    return {"connection": "succesful", "quote" : quotes[randomgen()]}