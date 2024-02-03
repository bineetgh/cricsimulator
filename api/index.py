# app.py

from flask import Flask, render_template, request, session
from flask_assets import Bundle, Environment
from flask_session import Session

from game import *
from data import *
import random
import json

import redis

r = redis.StrictRedis(
  host='redis-13471.c301.ap-south-1-1.ec2.cloud.redislabs.com',
  port=13471,
  password='ADufRBbkEYRnlCpWmc25QPA3qPrBwcDl',
  decode_responses=True)


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


def set_my_team():
    my_team = r.get("my_team")
    
    if not my_team:
        my_team = "Team X"
        r.set("my_team", my_team)
    
    my_players = r.get( "my_players")
    if my_players:
        players[my_team] = json.loads(my_players)
    else:
        my_team = "Team X"
        r.set("my_team", my_team)
        
    return my_team


@app.route("/")
def homepage():
    my_team = set_my_team()
        
    return render_template("index.html", teams=countries, players=players, my_team=my_team)


@app.route("/tournament", methods=["GET"])
def tournament():
    game = Game()
    game.setTournament("ICC")
    session['tournament'] = game.tournament
    return render_template("tournament.html", tournament=game.tournament)

@app.route("/simulate-all", methods=["GET"])
def simulate_all():
    game = Game()
    my_team = set_my_team()        
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
        rounds = request.form.get('rounds')
        my_team = set_my_team()            
        game.setTournament("WT20I Tournament", teams, my_team, rounds)
        game.simulate()
        return render_template("tournament-simulated.html", tournament=game.tournament)  
    else:
        game = Game()
        
        my_team = set_my_team()
            
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
    my_players = []
    for i in range(1, 16):
        player = request.form.get(str(i), "")      
        my_players.append(player)
                 
    players[my_team] = my_players
    
    r.set("my_team", my_team) 
    r.set("my_players", json.dumps(my_players))  
    
    return render_template("index.html", teams=countries, players=players, my_team=my_team) 


if __name__ == "__main__":
    app.run(debug=True)
