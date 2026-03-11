from flask import Flask, render_template, request
from instagrapi import Client

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        target = request.form["target"]

        try:

            cl = Client()
            cl.login(username,password)

            user_id = cl.user_id_from_username(target)

            followers = cl.user_followers(user_id)

            result = f"Followers found: {len(followers)}"

        except Exception as e:

            result = f"Error: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()