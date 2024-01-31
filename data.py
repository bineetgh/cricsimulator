countries = ["India", "Australia", "England", "New Zealand", "West Indies", "Pakistan", "Afganistan", "South Africa"]
clubs = []

all_players = {}

all_players['India'] = [("R Sharma", ["Bat", "Capt"]), ("YB Jaiswal", ["Bat"]), ("V Kohli", ["Bat"]), ("S Iyer", ["Bat"]), ("KL Rahul", ["Bat", "WC"]), ("H Pandya", ["Bat", "Bowl"]), ("A Patel", ["Bat", "Bowl"]),("R Jadeja", ["Bat", "Bowl"]), ("J Bumrah", ["Bowl"]), ("M Shami", ["Bowl"]), ("K Yadav", ["Bowl"])] 
all_players['Australia'] = ["D Warner", "T Head", "S Smith", " G Maxwell", "A Carey", "M Marsh", "M Stoinis", "C Green", "A Zampa", "P Cummins", "J Hazelwood"] 
all_players['England'] = ["J Buttler", "J Roy", "J Bairstow", "D Malan", "B Stokes", "E Morgan", "M Ali", "S Curran", "C Woaks", "M Wood", "T Curran"] 
all_players['New Zealand'] = ["D Conway", "T Lathem", "K Williamson", "D Mitchell", "R Ravindra", "G Phillips", "M Santner", "M Henry", "N Wagner", "T Boult", "T Southee"] 
all_players['West Indies'] = ["S Hope", "R Chase", "K Carty", "M Forde", "R Shepherd", "K Hodge", "A Athanaze", "A Joseph", "K Ottely", "S Joseph", "O Thomas"] 
all_players['Pakistan'] = ["F Zaman", "A Shafique", "B Azam", "M Rizwan", "S Shakeel", "S Khan", "H Rauf", "H Ali", "SS Afridi", "O Mir", "A Salman"]  
all_players['Afganistan'] = ["I Zardan", "R Gurbaz", "H Shahidi", "R Hassan", "M Nabi", "R Khan", "F Farooqi", "A Rahman", "M Rahman", "NU Haq", "N Ahmed"]  
all_players['South Africa'] = ["R Hendricks", "A Markram", "T Bavuma", "H Klassan", "D Miller", "M Jansen", "G Coetzee", "K Maharaj", "T Shamsi", "K Rabada", "L Ngidi"] 


players = {}
players['India'] = ["R Sharma", "YB Jaiswal", "V Kohli", "S Iyer", "KL Rahul", "H Pandya", "R Jadeja", "A Patel", "J Bumrah", "M Shami", "K Yadav"] 
players['Australia'] = ["D Warner", "T Head", "S Smith", " G Maxwell", "A Carey", "M Marsh", "M Stoinis", "C Green", "A Zampa", "P Cummins", "J Hazelwood"] 
players['England'] = ["J Buttler", "J Roy", "J Bairstow", "D Malan", "B Stokes", "E Morgan", "M Ali", "S Curran", "C Woaks", "M Wood", "T Curran"] 
players['New Zealand'] = ["D Conway", "T Lathem", "K Williamson", "D Mitchell", "R Ravindra", "G Phillips", "M Santner", "M Henry", "N Wagner", "T Boult", "T Southee"] 
players['West Indies'] = ["S Hope", "R Chase", "K Carty", "M Forde", "R Shepherd", "K Hodge", "A Athanaze", "A Joseph", "K Ottely", "S Joseph", "O Thomas"] 
players['Pakistan'] = ["F Zaman", "A Shafique", "B Azam", "M Rizwan", "S Shakeel", "S Khan", "H Rauf", "H Ali", "SS Afridi", "O Mir", "A Salman"]  
players['Afganistan'] = ["I Zardan", "R Gurbaz", "H Shahidi", "R Hassan", "M Nabi", "R Khan", "F Farooqi", "A Rahman", "M Rahman", "NU Haq", "N Ahmed"]  
players['South Africa'] = ["R Hendricks", "A Markram", "T Bavuma", "H Klassan", "D Miller", "M Jansen", "G Coetzee", "K Maharaj", "T Shamsi", "K Rabada", "L Ngidi"] 

bowling_options = {}
bowling_options["India"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Australia"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["England"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["New Zealand"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["West Indies"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Pakistan"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["Afganistan"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]
bowling_options["South Africa"] = [0, 0, 0, 0, 0, 0.7, 0.8, 0.7, 1, 1, 1]

bowlers = {}
bowlers['India'] = ["H Pandya", "A Patel", "R Jadeja", "J Bumrah", "M Shami", "K Yadav"] 
bowlers['Australia'] = ["T Head", " G Maxwell", "M Marsh", "M Stoinis", "A Zampa", "P Cummins", "J Hazelwood"] 
bowlers['England'] = ["B Stokes", "J Roy", "M Ali", "S Curran", "C Woaks", "M Wood", "T Curran"] 
bowlers['New Zealand'] = ["R Ravindra", "G Phillips", "M Santner", "M Henry", "N Wagner", "T Boult", "T Southee"] 
bowlers['West Indies']  = ["K Hodge", "A Athanaze", "A Joseph", "K Ottely", "S Joseph", "O Thomas"] 
bowlers['Pakistan']  = ["S Khan", "H Rauf", "H Ali", "SS Afridi", "O Mir", "A Salman"]  
bowlers['Afganistan']  = ["M Nabi", "R Khan", "F Farooqi", "A Rahman", "M Rahman", "NU Haq", "N Ahmed"]  
bowlers['South Africa']  = ["A Markram", "M Jansen", "G Coetzee", "K Maharaj", "T Shamsi", "K Rabada", "L Ngidi"] 

keeper = {}
keeper['India'] = "KL Rahul"
keeper['Australia'] = "A Carey"
keeper['England'] = "J Bairstow"
keeper['New Zealand'] = "T Lathem"
keeper['West Indies']  = "S Hope"
keeper['Pakistan']  =  "M Rizwan"
keeper['Afganistan']  =  "I Zadran"
keeper['South Africa']  = "H Klassan"

score_options = ["0","1","2","3","4","6","W","1Ro","2Ro","Nb","1Nb","2Nb","3Nb","4Nb","6Nb","Wd","1Wd","1Lb","2Lb","1B","2B"]
weights = [0.3, 0.3, 0.02, 0.01, 0.1, 0.1, 0.05, 0.005, 0.005, 0.001, 0.001, 0.001, 0.003, 0.002, 0.01, 0.01, 0.05, 0.03, 0.02, 0.01, 0.01]
