from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():

    reponse = request.args.get("game")

    if reponse == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    madlibs = ["madlib1.html", "madlib2.html"]
    exclamations = request.args.getlist("exclamation")

    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")



    return render_template(choice(madlibs), 
                            exclamations=exclamations,
                            noun=noun,
                            adjective=adjective,
                            verb=verb)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
