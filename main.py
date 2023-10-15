import flask

app = flask.Flask(__name__)

@app.route("/")
def github_redirect():
    return flask.redirect("https://github.com/TotallyNotSethP/teowyor.com/tree/main", code=301)

@app.route("/view/<_>")
def replace_gif(_):
    return flask.send_file("snowy.png", mimetype="image/png")

@app.errorhandler(404)
def error_handler(e):
    return github_redirect()
