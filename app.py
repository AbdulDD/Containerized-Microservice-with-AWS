# Imports
from flask import Flask, request
from utils.sentimental_analyzer import sentiment_analysis
from utils.ner_detector import ner_pipe

# Flask app
app = Flask(__name__)


# front page route
@app.route("/", methods=["GET"])
def Introduce():
    return "Welcode to our simple application"


# sentiment route
@app.route("/sentiment", methods=["POST"])
def sentiment():
    data = request.get_json()
    text = data["text"]
    return sentiment_analysis(text)


# ner route
@app.route("/ner", methods=["POST"])
def ner():
    data = request.get_json()
    text = data["text"]
    # print(text)
    result = ner_pipe(text)
    return result[0]["entity"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
