from flask import Flask, render_template, redirect, session, url_for, request
import random

app = Flask(__name__)
app.secret_key = "4ac84d6364897ef35b5be192748160b5adef17c849f09c96bbac4ff74ec2b1bf"

questions = [("What floor number are we on right now?", "0"),
                ("What game have we modded as a club?", "minecraft"),
                ("What app do we use for internal communication?", "discord")
            ]

@app.route("/form", methods=["POST", "GET"])
def form_demo():
    if request.method=="POST":
        session["form_data"] = request.form["input"].lower().strip()
        return redirect(url_for("response_demo"))
    else:
        question_data = random.choice(questions)
        session["answer"] = question_data[-1]
        return render_template("post.html", question = question_data[0])

@app.route("/response")
def response_demo():
    if session["form_data"] == session["answer"]:
        return "<h1>Congratulations, you were correct!</h1><br><a href='/form'>Try another one?</a>"
    else:
        return "<h1>Sorry, but that wasn't right!</h1><br><a href='/form'>Try another one?</a>"

app.run(debug=True)



