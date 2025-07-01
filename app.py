from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("Received name:", name)  #  Add this line to see name in terminal

    return render_template("thankyou.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

