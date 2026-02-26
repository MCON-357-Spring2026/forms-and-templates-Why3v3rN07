from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        name="student",
        today=datetime.now().strftime("%Y-%m-%d"),
        number=3.1415926
    )


@app.route("/students")
def students():
    student_list = ["Chana", "Miriam", "Leah", "Kaila"]
    return render_template("students.html", students=student_list)


@app.route("/grades")
def grades():
    grade = 75
    return render_template("grades.html", grade=grade)


@app.route("/form", methods=["GET", "POST"])
def form_demo():
    error = None
    username = None

    if request.method == "POST":
        username = request.form.get("username")

        if not username or username.strip() == "":
            error = "Username is required."
            username = None

    return render_template("form.html", error=error, username=username)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
