countries = ["India", "Australia", "England", "New Zealand", "West Indies", "Pakistan", "Afganistan", "South Africa"]
clubs = []

#all_players = {}

#all_players['India'] = [("R Sharma", ["Bat", "Ct"]), ("YB Jaiswal", ["Bat"]), ("V Kohli", ["Bat"]), ("S Iyer", ["Bat"]), ("KL Rahul", ["Bat", "WC"]), ("H Pandya", ["Bat", "Bowl"]), ("A Patel", ["Bat", "Bowl"]),("R Jadeja", ["Bat", "Bowl"]), ("J Bumrah", ["Bowl"]), ("M Shami", ["Bowl"]), ("K Yadav", ["Bowl"])] 
#all_players['Australia'] = ["D Warner", "T Head", "S Smith", " G Maxwell", "A Carey", "M Marsh", "M Stoinis", "C Green", "A Zampa", "P Cummins", "J Hazelwood"] 
#all_players['England'] = ["J Buttler", "J Roy", "J Bairstow", "D Malan", "B Stokes", "E Morgan", "M Ali", "S Curran", "C Woaks", "M Wood", "T Curran"] 
#all_players['New Zealand'] = ["D Conway", "T Lathem", "K Williamson", "D Mitchell", "R Ravindra", "G Phillips", "M Santner", "M Henry", "N Wagner", "T Boult", "T Southee"] 
#all_players['West Indies'] = ["S Hope", "R Chase", "K Carty", "M Forde", "R Shepherd", "K Hodge", "A Athanaze", "A Joseph", "K Ottely", "S Joseph", "O Thomas"] 
#all_players['Pakistan'] = ["F Zaman", "A Shafique", "B Azam", "M Rizwan", "S Shakeel", "S Khan", "H Rauf", "H Ali", "SS Afridi", "O Mir", "A Salman"]  
#all_players['Afganistan'] = ["I Zardan", "R Gurbaz", "H Shahidi", "R Hassan", "M Nabi", "R Khan", "F Farooqi", "A Rahman", "M Rahman", "NU Haq", "N Ahmed"]  
#all_players['South Africa'] = ["R Hendricks", "A Markram", "D Elgar", "H Klassan", "D Miller", "M Jansen", "G Coetzee", "K Maharaj", "T Shamsi", "K Rabada", "L Ngidi"] 


players = {}
players['India'] =        ["R Sharma",    "YB Jaiswal",  "V Kohli",      "S Iyer",        "KL Rahul",   "Ishan K",    "H Pandya",  "R Jadeja",  "A Patel",   "J Bumrah",  "M Shami",  "K Yadav",    "M Siraj",     "Mukesh K",   "S Thakur"] 
players['Australia'] =    ["D Warner",    "T Head",      "S Smith",      "G Maxwell",     "A Carey",    "M Marsh",    "S Marsh",   "T Paine", "M Stoinis", "C Green",   "A Zampa",  "P Cummins",  "J Hazelwood", "N Lyon" ,    "M Stack" ] 
players['England'] =      ["J Buttler",   "J Roy",       "J Bairstow",   "D Malan",       "B Stokes",   "E Morgan",   "J Root",    "O Pope",    "M Ali",     "S Curran",  "C Woaks",  "M Wood",     "T Curran",    "J Anderson", "J Archer"] 
players['New Zealand'] =  ["D Conway",    "T Lathem",    "K Williamson", "D Mitchell",    "R Ravindra", "G Phillips", "M Santner", "M Henry",   "M Patel",   "N Wagner",  "T Boult",  "T Southee",  "Cory A",      "J Patel",    "S James"] 
players['West Indies'] =  ["S Hope",      "R Chase",     "K Carty",      "S Chandrapaul", "M Forde",    "R Shepherd", "A Athanaze","K Hogde",  "Sunil N",   "A Joseph",   "K Ottely",  "S Joseph",   "O Thomas",    "K Pollard",  "M Holder"] 
players['Pakistan'] =     ["F Zaman",     "A Shafique",  "B Azam",       "M Rizwan",      "K Akmal",    "Shadab K",   "Shahid A",  "S Shakeel","S Khan",     "H Rauf",    "H Ali",    "SS Afridi",  "O Mir",       "A Salman",   "U Gul"] 
players['Afganistan'] =   ["I Zardan",    "R Gurbaz",    "H Shahidi",    "R Hassan",      "M Nabi",     "R Khan",     "F Farooqi", "A Rahman",  "M Rahman",  "NU Haq",    "N Ahmed",  "Rashid K",   "Mujeeb R",    "Naveen U",   "K Baksh"]  
players['South Africa'] = ["R Hendricks", "A Markram",   "K Bavuma",     "Henry K",       "D Elgar",    "H Klassan",  "D Miller",  "M Jansen",  "G Coetzee", "K Maharaj", "T Shamsi", "K Rabada",  "L Ngidi",      "K Phulkwayo","Aaron F"] 
players['Team X'] =       ["Aviral M",    "Aarav Singh", "Vedant K",     "B Mishra",      "A Mishra",   "R Singh",    "Omi M",    "S Samson",  "M Stacky",  "KL Yadav",  "AB Sharma", "Nimit K",  "Siddhant M",   "Ridant S",   "S Jaiswal"] 

player_selection_weights = [0.2, 0.05, 0.05, 0.05, 0.1, 0.08, 0.02, 0.05, 0.03, 0.1, 0.07, 0.05, 0.05, 0.07, 0.03]

bowling_options = {}
bowling_options["India"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Australia"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["England"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["New Zealand"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["West Indies"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Pakistan"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Afganistan"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["South Africa"] = [0, 0.8, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Team X"] = [1, 0.8, 0, 1, 0, 0, 0.8, 0.7, 1, 1, 1]

bowlers = {}
bowlers['India'] = ["H Pandya", "A Patel", "R Jadeja", "J Bumrah", "M Shami", "K Yadav"]
bowlers['Australia'] = ["T Head", " G Maxwell", "M Marsh", "M Stoinis", "A Zampa", "P Cummins", "J Hazelwood"] 
bowlers['England'] = ["B Stokes", "J Roy", "M Ali", "S Curran", "C Woaks", "M Wood", "T Curran"] 
bowlers['New Zealand'] = ["R Ravindra", "G Phillips", "M Santner", "M Henry", "N Wagner", "T Boult", "T Southee"] 
bowlers['West Indies']  = ["K Hodge", "A Athanaze", "A Joseph", "K Ottely", "S Joseph", "O Thomas"] 
bowlers['Pakistan']  = ["S Khan", "H Rauf", "H Ali", "SS Afridi", "O Mir", "A Salman"]  
bowlers['Afganistan']  = ["M Nabi", "R Khan", "F Farooqi", "A Rahman", "M Rahman", "NU Haq", "N Ahmed"]  
bowlers['South Africa']  = ["A Markram", "M Jansen", "G Coetzee", "K Maharaj", "T Shamsi", "K Rabada", "L Ngidi"] 
bowlers['Team X']  = ["B Mishra", "Aviral M", "T John", "Aarav Singh", "Siddhant M",   "Ridant S",   "S Jaiswal"] 

keepers = {}
keepers['India'] = ["KL Rahul", "I Kishan"]
keepers['Australia'] = ["A Carey", "T Paine"]
keepers['England'] = ["J Buttler", "J Roy", "J Bairstow"]
keepers['New Zealand'] = ["T Lathem", "D Conway"]
keepers['West Indies']  = ["S Hope", "K Carty"]
keepers['Pakistan']  =  ["M Rizwan", "K Akmal"]
keepers['Afganistan']  =  ["I Zadran", "R Hassan"]
keepers['South Africa']  = ["H Klassan", "D Miller"]
keepers['Team X']  = ["Nimit K", "Omi M", "A Mishra"]

score_weights = {}
score_options =                     ["W",  "0",   "1",  "2",  "3",  "4",  "6", "1Ro",  "2Ro", "Nb",  "1Nb", "2Nb", "3Nb", "4Nb", "6Nb", "Wd", "1Wd", "1Lb", "2Lb", "1B", "2B"]
score_weights["Batting Paradise"] = [0.04,  0.30, 0.20, 0.03, 0.01, 0.20, 0.20, 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0.005, 0.005,  0.07, 0.01,  0.03,  0.01,  0.01, 0.01]
score_weights["Batting Friendly"] = [0.05,  0.35, 0.25, 0.03, 0.01, 0.15, 0.15, 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0.005, 0.005,  0.06, 0.01,  0.04,  0.01,  0.01, 0.01]
score_weights["Balanced"] =         [0.06,  0.40, 0.30, 0.02, 0.01, 0.10, 0.10, 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0.005, 0.005,  0.05, 0.01,  0.05,  0.01,  0.01, 0.01]
score_weights["Bowling Friendly"] = [0.07,  0.45, 0.35, 0.02, 0.01, 0.08, 0.08, 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0.005, 0.005,  0.06, 0.01,  0.06,  0.01,  0.01, 0.01]
score_weights["Bowling Paradise"] = [0.08,  0.50, 0.40, 0.02, 0.01, 0.05, 0.05, 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0.005, 0.005,  0.07, 0.01,  0.07,  0.01,  0.01, 0.01]


pitch_conditions = ["Batting Paradise", "Batting Friendly", "Bowling Friendly", "Balanced", "Bowling Paradise"]
pitch_conditions_weights = [0.05, 0.20, 0.30, 0.40, 0.05]


dismissal_types = ["c", "st", "", "lbw"]

fielding_positions = ["Mid-Off","Mid-On","Long-On","Long-Off","Square-Leg","Deep-Point","First-Slip","Second-Slip","Third-Slip","Cover-Point","Leg-Gully","Third-Man"]