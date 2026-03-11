from flask import Flask, render_template, request
from instagrapi import Client
import json

TARGET_ACCOUNT = "andre.mp2709"

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        try:

            cl = Client()
            cl.login(username,password)

            user_id = cl.user_id_from_username(TARGET_ACCOUNT)

            followers = cl.user_followers(user_id)

            current_followers = [f.username for f in followers.values()]

            with open("followers.json") as f:
                saved = json.load(f)["followers"]

            unfollowed = list(set(saved) - set(current_followers))

            if len(unfollowed) == 0:
                result = "No one unfollowed"
            else:
                result = "Unfollowed:\n" + "\n".join(unfollowed)

        except Exception as e:
            result = str(e)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()

