import json

file = open('recipes.json','r')
data = json.loads(file.read())

splitted_data=[]
word = 'eggs'

for recipes in data:
    for x in recipes['ingredients']:
        if 'reggiano' in x:
            break

            #print("The recipe with the ID ", recipes['id'], 'has reggiano')
        elif "eggs" in x:
            print("The recipe with the ID ", recipes['id'], 'has many eggs')
            break    
        elif 'egg' in x:
            print("The recipe with the ID ", recipes['id'], 'has only one egg')
            break
        else:
            break           
