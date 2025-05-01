import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template('index.html')

@app.route("/game1")
def game1():
    return flask.render_template('firstgame.html')

@app.route("/game2")
def game2():
    return flask.render_template('secondgame.html')

@app.route("/game3")
def game3():
    return flask.render_template('thirdgame.html')

@app.route("/game4")
def game4():
    return flask.render_template('fourthgame.html')

@app.route("/game5")
def game5():
    return flask.render_template('fifthgame.html')

app.run('0.0.0.0', 5000)