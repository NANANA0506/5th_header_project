from flask import Flask, render_template

app = Flask(__name__)

print("Joined Flask Framework Server")

@app.route("/")
def home():
    return render_template("food1.html")




app.run(debug=True)