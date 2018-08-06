import csv

file = open('athlete_events.csv','r')

file.readline()

counter = 0
teams = {}    

for row in file:
    data = row.split(",")
    team = data[6]
    medal = data[14]
    if 'Gold' in medal:
        if team in teams:
            teams[team][0] = teams[team][0] + 1
        else:
            teams[team] = [0,0,0]
            teams[team][0] = 1
            
for team in teams:
    print (team, teams[team][0])
        
    
