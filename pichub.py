import click
from flask import Flask, render_template
import imgur

app = Flask(__name__, template_folder="frontend", static_folder='frontend/static')

@app.route("/")
def render_home():
    imgur.get_images(imgur.username)
    return render_template("/home/index-gallery-main.html")

@app.route("/login")
def login_page():
    return render_template("/login-page/index-login.html")

if __name__ == '__main__':
    app.run(debug=True)
