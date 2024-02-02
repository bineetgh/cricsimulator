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
css = Bundle("src/main.css", output="dist/style.css")
js = Bundle("src/*.js", output="dist/main.js") # new

assets.register("css", css)
assets.register("js", js) # new
css.build()
js.build() # new


@app.route("/")
def homepage():
    print(session)
    if "my_team" in session:
        my_team = session["my_team"]
    else:
        my_team = "Team X"
    
    if "my_team_players" in session:
        players[my_team] = session["my_team_players"]
    else:
        my_team = "Team X"
        
    return render_template("simulation.html", teams=countries, players=players, my_team=my_team)


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
    return render_template("simulation.html", teams=countries)

@app.route("/tournament", methods=["GET"])
def tournament():
    game = Game()
    game.setTournament("ICC")
    session['tournament'] = game.tournament
    return render_template("tournament.html", tournament=game.tournament)

@app.route("/simulate-all", methods=["GET"])
def simulate_all():
    game = Game()
    if "my_team" in session:
        my_team = session["my_team"]
    else:
        my_team = "Team X"
    
    if "my_team_players" in session:
        players[my_team] = session["my_team_players"]
    else:
        my_team = "Team X"
        
    name = "ICC WT20"
    game.setTournament(name, None, my_team)
    game.simulate()
    session['tournament'] = game.tournament
    return render_template("tournament-simulated.html", tournament=game.tournament)
  
  
@app.route("/simulate-a-tournament", methods=["GET", "POST"])
def simulate_a_tournament():
    if request.method == "POST":
        game = Game()
        teams = request.form.getlist('teams')
        if "my_team" in session:
            my_team = session["my_team"]
        else:
            my_team = "Team X"
            
        if "my_team_players" in session:
            players[my_team] = session["my_team_players"]
        else:
            my_team = "Team X"
            
        game.setTournament("WT20I Tournament", teams, my_team)
        game.simulate()
        return render_template("tournament-simulated.html", tournament=game.tournament)  
    else:
        game = Game()
        
        if "my_team" in session:
            my_team = session["my_team"]
        else:
            my_team = "Team X"
            
        if "my_team_players" in session:
            players[my_team] = session["my_team_players"]
        else:
            my_team = "Team X"
        
        
        game.setTournament("WT20I Tournament", countries, my_team)
        game.simulate()
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

    tournament = Tournament("ICC WT20", None, t1)
        
    match = Match("T20I", t1, t2, seq) 
    
    match.simulate(tournament)

    info['result'] = match.result     
    info['team1'] = match.team1
    info['team2'] = match.team2 
     
    return render_template("scorecard.html", info=info, tournament=tournament)
    


@app.route("/save-team-info", methods=["POST", "GET"])
def save_team_info():
    my_team = request.form.get("my_team_name", "")
    my_team_players = []
    for i in range(1, 12):
        print(i)
        player = request.form.get(str(i), "")      
        my_team_players.append(player)
    session['my_team_players'] = my_team_players
    session['my_team'] = my_team
    players[my_team] = my_team_players
    return render_template("simulation.html", teams=countries, players=players, my_team=my_team) 


if __name__ == "__main__":
    app.run(debug=True)
