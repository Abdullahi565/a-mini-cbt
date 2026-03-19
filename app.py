from flask import Flask, render_template, request, redirect, url_for
from models import Question, CBT

app = Flask(__name__)

cbt = CBT()

# Add questions
cbt.add_question(Question(
    "What is 2 + 2?",
    ["2", "3", "4", "5"],
    "4"
))

cbt.add_question(Question(
    "Python is a?",
    ["Snake", "Programming Language", "Car", "Game"],
    "Programming Language"
))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answer = request.form.get("answer")
        cbt.answer_question(answer)

    question = cbt.get_current_question()

    if question:
        return render_template("quiz.html", question=question)
    else:
        return redirect(url_for("result"))


@app.route("/result")
def result():
    result = cbt.get_result()
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)