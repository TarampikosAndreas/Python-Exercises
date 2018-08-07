import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

    if 'Silver' in medal:
        if team in teams:
            teams[team][1] = teams[team][1] + 1
        else:
            teams[team] = [0,0,0]
            teams[team][1] = 1

    if 'Gold' in medal:
        if team in teams:
            teams[team][2] = teams[team][2] + 1
        else:
            teams[team] = [0,0,0]
            teams[team][2] = 1
            
for team in teams:
    print (team , "has " , teams[team][0] , 'Gold medals ' , teams[team][1] , "Silver medals " , "and " , teams[team][2] , "Bronze medals")
        

legend = [data[6]]
plt.xlabel("Runs/Delivery")
plt.ylabel("Frequency")
plt.legend(legend)
plt.xticks(range(0, 7))
plt.yticks(range(1, 20))
plt.title('Champions Trophy 2017 Final\n Runs scored in 3 overs')
plt.show()    
