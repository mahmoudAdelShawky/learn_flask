from flask import Flask , render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def home():
    return render_template("home.html", pagetitle = "home page", custom_css = "master" )

@skills_app.route("/about")
def about():
    return render_template("about.html" , pagetitle = "aboutPage", custom_css = "main")

if __name__ == "__main__":
    skills_app.run(debug= True )

