from flask import Flask, render_template, flash

app = Flask(__name__,template_folder="template")
app.secret_key = 'your_secret_key'
@app.route("/")
def home():
    flash("Thank you for visiting")
    return render_template("index.html")

@app.route("/about")
def about():
    flash("Thank you for visiting about page")
    return render_template("about.html")

app.run(debug=True)