import csv

file = open('athlete_events.csv','r')

file.readline()

GoldCounter = 0
SilverCounter = 0
BronzeCounter = 0

for row in file:
	data = row.split(",")
	if data[6] == 'China':
		if 'Gold' in data[14]:
			GoldCounter += 1
		elif 'Silver' in data[14]:
			SilverCounter += 1
		elif 'Bronze' in data[14]:
			BronzeCounter += 1
	
print ('China has won ',GoldCounter,' medals')
print ('China has won ',SilverCounter,' medals')
print ('China has won ',BronzeCounter,' medals')
