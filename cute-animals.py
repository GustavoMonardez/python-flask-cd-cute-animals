from flask import Flask, render_template, redirect
import os
from random import sample


app = Flask(__name__)

@app.route("/")
def index():
    images = os.listdir(os.path.join(app.static_folder, "images"))
    return render_template('index.html', images=images, num=10)

@app.route("/<x>")
def display_images(x):
    images = os.listdir(os.path.join(app.static_folder, "images"))
    return render_template('index.html', images=images, num=int(x))

@app.route("/danger")
def danger():
    print("user accessed danger page")
    return redirect("/")

@app.route("/random/<x>")
def display_random_images(x):
    images = os.listdir(os.path.join(app.static_folder, "images"))
    # shuffle(images)
    newwords = sample(images, int(x))
    print(images)
    return render_template('index.html', images=newwords, num=int(x))

if __name__ == "__main__":
    app.run(debug=True)