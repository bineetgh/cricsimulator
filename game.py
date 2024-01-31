import math
import random
from data import score_options, weights, players, countries, bowling_options
   
class Tournament:
    
    def __init__(self, name):
        self.name = name
        self.teams = {}
        for country in countries:
            self.teams[country] = Team(country)
        self.fixtures= self.setFixtures()
        self.players = self.setPlayers()
        self.player_stats = self.setPlayerStats()
        
    def setFixtures(self):
        fixtures = {}
        seq = 1
        
        for t1 in self.teams:
            for t2 in self.teams:
                key1 = t1 + " vs " + t2
                key2 = t2 + " vs " + t1
                if key1 not in fixtures and key2 not in fixtures and t1 != t2:
                    fixtures[key1] = Match("T20I", t1, t2, seq) 
                    seq = seq + 1
        return fixtures
    
    def setPlayers(self):
        all_players = {}
        
        for team in self.teams:
            for player in players[team]:
                all_players[player] = Player(player)

        return all_players
    
    def setPlayerStats(self):
        all_player_stats = {}
        
        for team in self.teams:
            for player in players[team]:
                all_player_stats[player] = Stats(player)

        return all_player_stats
    
    def getTeam(self, team):
        return self.teams[team]
        
                    

class Team:
      
    def __init__(self, name):
        self.name = name
        self.players = []
        self.scores = {}
        self.stats = TeamStats(name)

        for player in players[name]:
            self.players.append(Player(player))
   
        
    def play_match(self, match):
        #self.matches.append(match)
        self.scores[match.key] = Score(self, match)
        
        
    def __str__(self):
        return self.name
    
                      
        
class Player:
    
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.did_not_bat = True
        self.out = False
        
        self.balls_bowled = 0
        self.wickets = 0
        self.overs_bowled = 0
        self.runs_conceded = 0
        
        
    def addToScore(self, runs, balls):
        self.runs = self.runs + runs
        self.balls = self.balls + balls
        
    def ballBowled(self, runs, balls):
        self.runs_conceded += runs
        self.balls_bowled += balls
        
    def addWicket(self):
        self.wickets +=1
        
    def overBowled(self):
        self.overs_bowled += 1
        
    def getOvers(self):
        if self.balls_bowled > 0:
            return str(math.floor(self.balls_bowled/6)) + "." + str(self.balls_bowled % 6)
        return "0"
              
    def batted(self):
        self.did_not_bat = False
            
    def got_out(self):
        self.did_not_bat = False
        self.out = True
        
               
        
class Match:
    
    target = 0
    
    def __str__(self):
        return 'Match ' + str(self.seq) + ': '+ self.team1.name + ' vs ' + self.team2.name
    
    def __init__(self, format, team1, team2, seq):
        self.key = str(team1+team2)
        self.seq = seq
        self.format = format
        self.toss(team1, team2)       
        self.target = 0
        self.winner = {}
        self.loser = {}
        self.result = "Match Yet To Be played"
        
    def toss(self, team1, team2):
        toss = random.choice(["H", "T"])
        if toss == "H":
            self.toss = team1
        else:
            self.toss = team2
        
        self.decision = random.choice(["Bat First", "Field First"])
        
        if (self.toss == team1 and self.decision == "Bat First") or (self.toss == team2 and self.decision == "Field First"):
            self.team1 = Team(team1)
            self.team2 = Team(team2)
        else:
            self.team1 = Team(team2)
            self.team2 = Team(team1)
        
    def simulate(self, tournament):
               
        self.simulate_innings(self.team1, self.team2)
        self.simulate_innings(self.team2, self.team1)    
        self.setResult(tournament)
    
    def updateStats(self, tournament):
        for player in self.team1.players:
            player_stats = tournament.player_stats[player.name]
            player_stats.matches_played += 1
            player_stats.total_runs += player.runs
            player_stats.balls_played += player.balls
            if player.out:
                player_stats.dismissed += 1
            if not player.did_not_bat:
                player_stats.innings += 1
            player_stats.wickets += player.wickets
            player_stats.balls_bowled += player.balls_bowled
            player_stats.runs_conceded += player.runs_conceded
            
        for player in self.team2.players:
            player_stats = tournament.player_stats[player.name]
            player_stats.matches_played += 1
            player_stats.total_runs += player.runs
            player_stats.balls_played += player.balls
            if player.out:
                player_stats.dismissed += 1
            if not player.did_not_bat:
                player_stats.innings += 1
            player_stats.wickets += player.wickets
            player_stats.balls_bowled += player.balls_bowled
            player_stats.runs_conceded += player.runs_conceded
        
    def setResult(self, tournament):
            
        #Result
        diff = self.team1.scores[self.key].runs - self.team2.scores[self.key].runs
        by_wickets = 10 - self.team2.scores[self.key].wickets
        if diff >0:
            self.result = self.team1.name + " Won by " + str(diff) + " Runs."
            tournament.teams[self.team1.name].stats.add_points("W")
            tournament.teams[self.team2.name].stats.add_points("L")
            self.winner = self.team1
            self.loser=self.team2
        elif diff <0:
            self.result = self.team2.name + " Won by " + str(by_wickets) + " Wickets."
            tournament.teams[self.team1.name].stats.add_points("L")
            tournament.teams[self.team2.name].stats.add_points("W")
            self.winner = self.team2
            self.loser = self.team1
        else:
            self.result = "Match Tied."
            tournament.teams[self.team1.name].stats.add_points("NR")
            tournament.teams[self.team2.name].stats.add_points("NR")
            
        # NRR 
        tournament.teams[self.team1.name].stats.runs += diff
        if self.team1.scores[self.key].wickets == 10:
            tournament.teams[self.team1.name].stats.balls += 120
        else:
            tournament.teams[self.team1.name].stats.balls += self.team1.scores[self.key].balls
            
        tournament.teams[self.team2.name].stats.runs -= diff
        if self.team2.scores[self.key].wickets == 10:
            tournament.teams[self.team2.name].stats.balls += 120
        else:
            tournament.teams[self.team2.name].stats.balls += self.team2.scores[self.key].balls
    
    def strike_change(self):
        temp = self.player_on_strike
        self.player_on_strike.batted()
        self.player_on_strike = self.player_on_non_strike
        self.player_on_non_strike = temp
    
    def simulate_innings(self, team1:Team, team2:Team):

        runs = 0
        wickets = 0
        balls = 0
        extras = 0
        scorecard = ""
        results = ""
       
        team1.play_match(self)
        
        self.player_on_strike = team1.players[0]
        self.player_on_strike.batted()
        self.player_on_non_strike = team1.players[1]
        self.bowler = random.choices(team2.players, bowling_options[team2.name])[0]
        
        over_counter = 0

            
        while wickets < 10 and balls < 120 :

            if self.target != 0 and runs >= self.target:
                break
            
            choice = random.choices(score_options, weights)
            result = choice[0]
            results = results + result + " "
            
            # Runs
            if(result == "0"):
                balls = balls + 1
                self.player_on_strike.addToScore(0, 1)
                self.bowler.ballBowled(0,1)
            if(result == "1"):
                balls = balls + 1
                runs = runs + 1
                self.player_on_strike.addToScore(1, 1)
                self.strike_change()
                self.bowler.ballBowled(1,1)
            if(result == "2"):
                runs = runs + 2
                balls = balls + 1
                self.player_on_strike.addToScore(2, 1)
                self.bowler.ballBowled(2,1)
            if(result == "3"):
                runs = runs + 3
                balls = balls + 1
                self.player_on_strike.addToScore(3, 1)
                self.strike_change()
                self.bowler.ballBowled(3,1)
            if(result == "4"):
                runs = runs + 4
                balls = balls + 1
                self.player_on_strike.addToScore(4, 1)
                self.bowler.ballBowled(4,1)
            if(result == "6"):
                runs = runs + 6
                balls = balls + 1
                self.player_on_strike.addToScore(6, 1)
                self.bowler.ballBowled(6,1)

            # Wicket   
            if(result == "W"):
                balls = balls + 1
                wickets = wickets + 1
                self.player_on_strike.addToScore(0, 1)
                self.player_on_strike.got_out()
                self.bowler.ballBowled(0,1)
                self.bowler.addWicket()
                if wickets != 10:
                    self.player_on_strike = team1.players[wickets+1]

            if(result == "1Ro"):
                balls = balls + 1
                wickets = wickets + 1
                runs = runs + 1
                self.player_on_strike.addToScore(1, 1)
                self.player_on_strike.got_out()
                self.bowler.ballBowled(0,1)
                if wickets != 10:
                    self.player_on_strike = team1.players[wickets+1]
                self.strike_change()
                
            if(result == "2Ro"):
                balls = balls + 1
                wickets = wickets + 1
                runs = runs + 2
                self.player_on_strike.addToScore(2, 1)
                self.player_on_strike.got_out()
                self.bowler.ballBowled(0,1)
                if wickets != 10:
                    self.player_on_strike = team1.players[wickets+1]

            # No Balls
            if(result == "Nb"):
                runs = runs + 1
                extras = extras + 1
                self.player_on_strike.addToScore(0, 1)
                self.bowler.ballBowled(1,0)
            if(result == "1Nb"):
                runs = runs + 2
                extras = extras + 1
                self.player_on_strike.addToScore(1, 1)
                self.bowler.ballBowled(2,0)
                self.strike_change()
            if(result == "2Nb"):
                runs = runs + 3
                extras = extras + 1
                self.player_on_strike.addToScore(2, 1)
                self.bowler.ballBowled(3,0)
            if(result == "3Nb"):
                runs = runs + 4
                extras = extras + 1
                self.player_on_strike.addToScore(3, 1)
                self.bowler.ballBowled(4,0)
                self.strike_change()
            if(result == "4Nb"):
                runs = runs + 5
                extras = extras + 1
                self.player_on_strike.addToScore(4, 1)
                self.bowler.ballBowled(5,0)
            if(result == "6Nb"):
                runs = runs + 7
                extras = extras + 1
                self.player_on_strike.addToScore(6, 1)
                self.bowler.ballBowled(7,0)
                      
            
            # Wides
            if(result == "Wd"):
                runs = runs + 1
                extras = extras + 1
                self.bowler.ballBowled(1,0)
            if(result == "1Wd"):
                runs = runs + 2
                extras = extras + 1
                self.strike_change()
                self.bowler.ballBowled(2,0)
            if(result == "2Wd"):
                runs = runs + 3
                extras = extras + 1
                self.bowler.ballBowled(3,0)
            if(result == "3Wd"):
                runs = runs + 4
                extras = extras + 1
                self.strike_change()
                self.bowler.ballBowled(4,0)
            if(result == "4Wd"):
                runs = runs + 5
                extras = extras + 1
                self.bowler.ballBowled(5,0)

            # Byes    
            if(result == "1B"):
                runs = runs + 1
                balls = balls + 1
                extras = extras + 1 
                self.player_on_strike.addToScore(0, 1)  
                self.strike_change()
                self.bowler.ballBowled(0,1)  
            if(result == "2B"):
                runs = runs + 2
                balls = balls + 1
                extras = extras + 2
                self.player_on_strike.addToScore(0, 1) 
                self.bowler.ballBowled(0,1)  
            if(result == "3B"):
                runs = runs + 3
                balls = balls + 1
                extras = extras + 3
                self.player_on_strike.addToScore(0, 1) 
                self.bowler.ballBowled(0,1)  
                self.strike_change()
            if(result == "4B"):
                runs = runs + 4
                balls = balls + 1
                extras = extras + 4
                self.player_on_strike.addToScore(0, 1) 
                self.bowler.ballBowled(0,1)  

            # Leg Byes
            if(result == "1Lb"):
                runs = runs + 1
                balls = balls + 1
                extras = extras + 1
                self.player_on_strike.addToScore(0, 1) 
                self.bowler.ballBowled(0,1)  
                self.strike_change()
            if(result == "2Lb"):
                runs = runs + 2
                balls = balls + 1
                extras = extras + 2   
                self.player_on_strike.addToScore(0, 1) 
                self.bowler.ballBowled(0,1)  
            if(result == "3Lb"):
                runs = runs + 3
                balls = balls + 1
                extras = extras + 3
                self.player_on_strike.addToScore(0, 1)
                self.bowler.ballBowled(0,1)  
                self.strike_change()
            if(result == "4Lb"):
                runs = runs + 4
                balls = balls + 1
                extras = extras + 4
                self.player_on_strike.addToScore(0, 1) 
                self.bowler.ballBowled(0,1) 



            if wickets == 10: 
                break
            
            if result not in ["Nb","1Nb","2Nb","3Nb","4Nb","6Nb","Wd","1Wd"]:
                over_counter += 1
                if over_counter % 6 == 0:
                    self.bowler.overs_bowled += 1
                    self.strike_change()
                    ##New Blower
                    bowler = random.choices(team2.players, bowling_options[team2.name])[0]
                    while bowler == self.bowler or bowler.balls_bowled >= 30:
                        bowler = random.choices(team2.players, bowling_options[team2.name])[0]
                    self.bowler = bowler
            
                
        if self.target == 0:
            self.target = runs + 1
                
        team1.scores[self.key].runs = runs
        team1.scores[self.key].wickets = wickets
        team1.scores[self.key].balls = balls
        team1.scores[self.key].extras = extras                  
        team1.scores[self.key].setScorecard(results)
        
            
            

            
    
    
class Score:
    
    def __init__(self, team:Team, match:Match):
        self.team = team
        if team.name == match.team1.name:
            self.opponent = match.team2
        else:
            self.opponent = match.team1
        self.runs = 0
        self.wickets = 0
        self.balls = 0
        self.extras = 0
        
    def setScorecard(self, results):
        scorecard = "<div class='rounded border-0 bg-gray-100 p-2 my-3'>"
        scorecard = scorecard + "<span class='mb-2 text-lg font-bold tracking-tight text-gray-600 dark:text-white'>"+ str(self.runs)+ "/"+ str(self.wickets) + "</span><br />"
        scorecard = scorecard + "<span class='mb-2 text-md font-bold tracking-tight text-gray-500 dark:text-white'>"+ str(math.floor(self.balls/6))+"."+str(self.balls%6) + " Overs </span><br />"
        scorecard = scorecard + "<span class='mb-2 text-md font-bold tracking-tight text-gray-400 dark:text-white'>Extras: "+ str(self.extras) + "</span></div>"
        
        scorecard = scorecard + "<div class='bg-green-100 p-2 m-3'>"
        for player in self.team.players:
            if not player.did_not_bat:
                scorecard = scorecard + "<p><strong>"+ player.name + "</strong> "+ str(player.runs)
                if not player.out:
                    scorecard = scorecard + "*"
                scorecard = scorecard + "("+ str(player.balls) + ")</p>"
            else:
                scorecard = scorecard + "<p><strong>"+ player.name +"</strong> Did Not Bat</p>"
        scorecard = scorecard + "</div>"
        #scorecard = scorecard + "<hr /><p>Timeline: "+ results + "</p>"
        scorecard = scorecard + "<div>"
        for player in self.opponent.players:
            if player.getOvers() != "0":
                scorecard = scorecard + "<p><strong>"+ player.name + "</strong> " + str(player.getOvers()) + " - " + str(player.runs_conceded) + " - "+ str(player.wickets) + "</p>" 
        scorecard = scorecard + "</div>"   
        
        self.scorecard = scorecard
        
        
    def __str__(self):
        return ""
    
    
class Game:
    
    def setTournament(self, name):
        self.tournament = Tournament(name)
            
    
    def simulate(self):
        for fixture in self.tournament.fixtures:
            match = self.tournament.fixtures[fixture]
            match.simulate(self.tournament)
            match.updateStats(self.tournament)
            
        self.tournament.teams = dict(sorted(self.tournament.teams.items(), key=lambda item: (item[1].stats.points, item[1].stats.getNRR()), reverse=True))
        self.tournament.player_stats = dict(sorted(self.tournament.player_stats.items(), key= lambda item: item[1].total_runs, reverse=True))
            
 
class TeamStats:
    
    def __init__(self, team):
        self.team = team
        # Batting
        self.matches = 0
        self.runs = 0
        self.balls = 0
        self.points = 0
        self.matches_played = 0
        self.matches_won = 0
        self.matches_lost = 0
        self.matches_nr = 0
        
    def getNRR(self):
        return str(round(self.runs*6/self.balls, 2))
    
    def add_points(self, result):
        if result == "W":
            self.points = self.points + 2
            self.matches_won += 1
        if result == "L":
            self.points = self.points + 0
            self.matches_lost += 1
        if result == "NR":
            self.points = self.points + 1
            self.matches_nr += 1
            
        self.matches_played = self.matches_played + 1
           

class Stats:
    
    def __init__(self, player):
        self.player = player
        # Batting
        self.matches_played = 0
        self.innings = 0
        self.total_runs = 0
        self.balls_played = 0
        self.dismissed = 0
        self.fifties = 0
        self.hundreds = 0
        
        #Bowling
        self.fifers = 0
        self.balls_bowled = 0
        self.wickets = 0
        self.overs_bowled = 0
        self.runs_conceded = 0

        
    def getStrikerate(self):
        if self.balls_played > 0:
            return str(round(self.total_runs*100/self.balls_played))
        return "NA"
        
    def getAverage(self):
        if self.dismissed > 0:
            return str(round(self.total_runs/self.dismissed, 2))
        return "NA"
    
    def getOversBowled(self):
        if self.balls_bowled >0:
            return str(math.floor(self.balls_bowled/6)) + "." +str(self.balls_bowled % 6)
        else:
            return "0"
      
    def getBowlingAverage(self):
        if self.balls_bowled >0:
            return str(round(self.runs_conceded*6/self.balls_bowled, 2))
        return "NA"
    
    def getBowlingStrikeRate(self):
        if self.wickets >0:
            return str(round(self.balls_bowled/self.wickets))
        return "NA"

    