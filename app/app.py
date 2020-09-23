from flask import Flask, render_template, url_for

app = Flask(__name__)

myself = '''Hi! I am a recent graduate of Coastal Carolina University.
            I am from West Columbia, SC. I am passionate about learning
            and continuing to improve myself. I also enjoy running and wellness.'''

@app.route("/")
def index():
    return render_template("home.html", title="Home", myself=myself)

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/experience")
def experience():
    return render_template("experience.html", title="Experience")

#if __name__ == "__main__":
#    app.run(debug=True)