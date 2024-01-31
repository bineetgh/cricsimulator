# app.py

from flask import Flask, render_template, request, session
from flask_assets import Bundle, Environment
from flask_session import Session

from todo import todos
from game import *
from data import *
import random


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
js = Bundle("src/*.js", output="dist/main.js") # new

assets.register("css", css)
assets.register("js", js) # new
css.build()
js.build() # new


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search_todo():
    search_term = request.form.get("search")

    if not len(search_term):
        return render_template("todo.html", todos=[])

    res_todos = []
    for todo in todos:
        if search_term in todo["title"]:
            res_todos.append(todo)

    return render_template("todo.html", todos=res_todos)

@app.route("/simulate", methods=["GET"])
def simulate():
    session.clear()
    return render_template("simulation.html")

@app.route("/tournament", methods=["GET"])
def tournament():
    game = Game()
    game.setTournament("ICC")
    session.clear()
    session['tournament'] = game.tournament
    return render_template("tournament.html", tournament=game.tournament)

@app.route("/simulate-all", methods=["GET"])
def simulate_all():
    game = Game()
    game.setTournament("ICC")
    game.simulate()
    session['tournament'] = game.tournament
    return render_template("tournament-simulated.html", tournament=game.tournament)
    
    
@app.route("/scorecard", methods=["GET"])
def scorecard():
    t1 = request.args.get('t1')
    t2 = request.args.get('t2')
    seq = request.args.get('seq')
    info = {}

    if not t1:        
        pick1 = random.choice(countries)
        countries.remove(pick1)
        t1 = pick1

    if not t2:
        pick2 = random.choice(countries)
        countries.append(pick1)
        t2 = pick2

    if 'tournament' in session:
        tournament = session['tournament']
    else:
        tournament = Tournament("ICC WT20")
        
    match = Match("T20I", t1, t2, seq) 
    
    match.simulate(tournament)
    session['tournament'] = tournament

    info['result'] = match.result     
    info['team1'] = match.team1
    info['team2'] = match.team2 
     
    return render_template("scorecard.html", info=info, tournament=tournament)
    


if __name__ == "__main__":
    app.run(debug=True)
