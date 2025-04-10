from flask import Flask, render_template, request
from clicker import MuffinClicker
clicker_game = MuffinClicker()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clicker', methods=['POST', 'GET'])
def clicker():
    return render_template('clicker.html', game=clicker_game)

@app.route('/bake', methods=['POST', 'GET'])
def bake():
    clicker_game.bake()
    return render_template('clicker.html', game=clicker_game)

@app.route('/upgrade', methods=['POST', "GET"])
def upgrade():
    clicker_game.upgrade()
    return render_template('clicker.html', game=clicker_game)

@app.route('/bakery', methods=['POST', 'GET'])
def bakery():
    clicker_game.multiplier()
    return render_template('clicker.html', game=clicker_game)

if __name__ == '__main__':
    app.run()