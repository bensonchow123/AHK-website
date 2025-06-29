from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/join")
def join():
    return render_template("join.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)