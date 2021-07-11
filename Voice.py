import speech_recognition as sr
import flask
from flask import request, jsonify
# Record Audio
app = flask.Flask(__name__)

txt = ""
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition


txt = r.recognize_google(audio)



app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return txt

app.run()