from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return jsonify({"game_id": game_id, "board": game.board})

@app.post("/api/score-word")
def score_word():
    """ Takes in a word and checks to see if the word
    is in the word list and is also on the board """

    word = request.json['word']

    # if word not in games['game_id'].word_list:
    #     return jsonify({word: "not-word"})

    # if not games['game_id'].check_word_on_board(word):
    #     return jsonify({word: "not-on-board"})

    # return jsonify({word: "ok"})

    return

