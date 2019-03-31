from flask import Flask, render_template, request
import random
from get_data import get_json_obj

app = Flask(__name__)

from word2vec import find_top

# HOME
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# WORD2CODE
@app.route('/word2code', methods=['GET'])
def word2code():
    return render_template("word2code.html")

@app.route('/word2code', methods=['POST'])
def get_nearest():
    json_obj = get_json_obj()
    potential_matches = []
    for language in json_obj["data"]:
        for command in json_obj["data"][language]:
            potential_matches.append(language + " " + command)
    nearest = find_top(request.form["entry"], potential_matches)
    language = nearest[0:nearest.find(" ")]
    command = nearest[nearest.find(" ")+1:]
    print("Language: {}".format(language))
    print("Command: {}".format(command))
    nearest_value = json_obj["data"][language][command]
    return render_template("word2code.html", nearest=nearest_value)

# LANGUAGE RECOGNITION
@app.route('/language_recognition')
def language_recognition():
    return render_template("language_recognition.html")

app.run('0.0.0.0',port=8080,debug=True)
