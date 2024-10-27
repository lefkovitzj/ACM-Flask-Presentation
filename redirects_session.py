from flask import Flask, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = "4ac84d6364897ef35b5be192748160b5adef17c849f09c96bbac4ff74ec2b1bf"

questions = [("ACM stands for Association of Computing Majors", False),
                ("Jon is our club president", False),
                ("The club server operating system is Debian", True)
            ]

@app.route("/poll")
def poll_demo():
    question_data = random.choice(questions)
    session["answer"] = question_data[-1]
    return f"<h1>{question_data[0]}</h1><br><a href='/true'>True</a> | <a href='/false'>False</a>"

@app.route("/true")
def true_demo():
    if session["answer"] == True:
        return redirect(url_for("congrats_demo"))
    else:
        return redirect(url_for("sorry_demo"))
@app.route("/false")
def false_demo():
    if session["answer"] == False:
        return redirect("/congrats")
    else:
        return redirect("/sorry")

@app.route("/congrats")
def congrats_demo():
    return "<h1>Congratulations, you were correct!</h1><br><a href='/poll'>Try another one?</a>"

@app.route("/sorry")
def sorry_demo():
    return "<h1>Sorry, but that wasn't right!</h1><br><a href='/poll'>Try another one?</a>"

app.run()



