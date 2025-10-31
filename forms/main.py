from flask import Flask, render_template, request

app = Flask(__name__,template_folder="template")

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method=="POST":
        form_data = request.form.to_dict()
        print(form_data)
        return f"<h1>Form Submitted Successful</h1>"
    return render_template("index.html")

app.run(debug=True)