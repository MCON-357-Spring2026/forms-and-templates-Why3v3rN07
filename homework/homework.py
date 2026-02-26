from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# In-memory storage
students = {}


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None
    name = ''
    grade = ''

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        if not name or name.strip() == "":
            error = "Name is required."
        elif not grade or grade.strip() == "":
            error = "Grade is required."
        elif not grade.isnumeric() or int(grade) not in range(0, 101):
            error = "Grade must be an integer between 0 and 100."
        else:
            if name in students: flash("Student "+name+" already existed, updated grade.")
            else: flash("Student "+name+" added.")
            students[name] = int(grade)
            return render_template("students.html", students=students)

    return render_template("add.html", error=error, name=name, grade=grade)

# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)

@app.route("/students/sort")
def display_students_sorted():
    sorted_students = {}
    for name in sorted(students, key=lambda x: students[x], reverse=True):
        sorted_students[name] = students[name]
    return render_template("students.html", students=sorted_students)

@app.route("/delete/<string:name>")
def delete_student(name):
    students.pop(name)
    return render_template("students.html", students=students)

# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    if len(students) > 0:
        stats = {
            "total": len(students),
            "average": sum(students.values()) / len(students),
             "highest": max(students.values()),
            "lowest": min(students.values())
        }
    else: stats = None

    return render_template("summary.html", stats=stats)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
