from flask import Flask, render_template, request

app = Flask(__name__,template_folder="template")

@app.route("/")
def jinja():
    name = "Keshav"
    lang = "Python"
    luckynos=[1,8,9,27,16]
    # Query Paramas
    Prediction = request.args.get('prediction')
    Accuracy = request.args.get('accuracy')
    return render_template("index.html", name=name, lang = lang, luck=luckynos, Prediction=Prediction, Accuracy=Accuracy)


app.run(debug=True)