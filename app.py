from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/play/<choice>')
def play(choice):

    choices = ["snake", "water", "gun"]
    computer = random.choice(choices)

    if choice == computer:
        result = "It's a Draw!"

    elif (
        (choice == "snake" and computer == "water") or
        (choice == "water" and computer == "gun") or
        (choice == "gun" and computer == "snake")
    ):
        result = "You Win!"

    else:
        result = "You Lose!"

    return render_template(
        "game.html",
        user=choice,
        computer=computer,
        result=result
    )
if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)


