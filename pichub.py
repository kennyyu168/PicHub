from flask import Flask, render_template
import imgur, os

app = Flask(__name__, template_folder="frontend", static_folder='frontend/static')


@app.route("/")
def login_page():
    return render_template("/login-page/index-login.html")

@app.route("/home")
def render_home():
    imgur.get_images(imgur.username)
    status = failsafe()
    print(status)
    return render_template("/home/index-gallery-main.html", empty=status)

@app.route("/imgur_auth")
def imgur_auth():
    imgur.authorize()

def failsafe():
    if [f for f in os.listdir('./imgur/') if not f.startswith('.')] == []:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
