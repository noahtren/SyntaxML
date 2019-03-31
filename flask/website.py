from flask import Flask, render_template, request
import random
from get_data import get_json_obj
from classify import classify

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
@app.route('/language_recognition', methods=['GET'])
def language_recognition():
    return render_template("language_recognition.html")

@app.route('/language_recognition', methods=['POST'])
def run_recognition():
    code = request.form["entry"]
    result = classify(code)
    return render_template("language_recognition.html", determination=result)

app.run('127.0.0.1',port=5000,debug=True)
