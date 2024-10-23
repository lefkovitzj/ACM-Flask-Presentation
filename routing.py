from flask import Flask

app = Flask(__name__)

@app.route("/static")
def static_demo():
    return "This is a static URL located at \"/static\""

@app.route("/dynamic/<url_end>")
def dynamic_demo(url_end):
    return f"This is a dynamic URL located at \"/dynamic/{url_end}\""

app.run()
