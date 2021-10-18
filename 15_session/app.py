# CircleTable - Christopher Liu, Yusuf Elsharawy, Naomi Naranjo
# SoftDev
# K15 -- Sessions Greetings
# 2021-10-18

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

# Secret key for session
app.secret_key = "SUPER_SECRET_OOOH_AHAHAH"


@app.route("/", methods=["GET"])
def index():
    """Displays a login page if the user is not logged in and a welcome page
    if the user is logged in."""

    if "username" in session:
        # User is logged in
        return render_template("response.html", username=session["username"])

    return render_template("login.html")


@app.route("/auth", methods=["GET", "POST"])
def auth():
    """Authenticates a log in request and either logs in or returns an error
    page."""

    # XXX HARDCODED USERNAME AND PASSWORD
    correct_username = "circletable"
    correct_password = "123456"

    # Check if username and password are correct
    username = request.form.get("username", default="")
    password = request.form.get("password", default="")


    if username == correct_username and password == correct_password:
        # Authentication success
        session["username"] = username
        return redirect(url_for("index"))
    else:
        # Authentication failure
        return render_template("error.html")


@app.route("/logout")
def logout():
    """Logs out the user and returns to the log in page."""
    if "username" in session:
        del session["username"]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    app.run()
