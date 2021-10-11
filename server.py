from random import randint
from flask import Flask

app = Flask(__name__)

random_num = randint(0, 9)


@app.route("/")
def show_random_img():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200/>"


@app.route("/<int:guessed_number>")
def show_result(guessed_number):
    if guessed_number < random_num:
        return "<h1 style='color:red'>Too Low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guessed_number > random_num:
        return "<h1 style='color: purple'>Too High, try again</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
