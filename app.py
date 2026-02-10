from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")

<<<<<<< HEAD
=======
@app.route("/action")
def action():
    return "🎉 Bouton cliqué ! Flask a réagi."

>>>>>>> b3626e52d9c6f95dbc723a2b02dda63656cd4582
if __name__ == "__main__":
    app.run(debug=True)