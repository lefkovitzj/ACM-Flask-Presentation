from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dynamic/<url_end>")
def dynamic_demo(url_end):
    return render_template("template.html", url_end_data=url_end)

app.run()