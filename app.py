from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ice_breaker2 import break_ice_with

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = break_ice_with(name)

    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url,
        }
    )

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)