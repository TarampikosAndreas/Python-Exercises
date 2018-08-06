import json

file = open('recipes.json','r')
data = json.loads(file.read())

splitted_data=[]


for recipes in data:
    for x in recipes['ingredients']:
        if "" "eggs" in x:
            if "" "egg" in x:
                print (recipes['id'])
