from textblob import TextBlob
from flask import Flask, render_template, request

def get_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0:
        return "positive."
    elif score == 0:
        return "neutral."
    else:
        return "negative." # -0.3

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("text")
        sentiment = get_sentiment(content)
        return sentiment
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
