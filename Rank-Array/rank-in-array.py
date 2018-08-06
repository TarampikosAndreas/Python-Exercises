a = [10,8,15,12,6,20,1]

ai = []

for i in range(len(a)):
    ai.append(0)
# ai = [0]*len(a)

asort = []

for i in range (len(a)):
    asort.append(a[i])
asort.sort()
# ps = sorted(p)

for i in range(len(asort)):
    pos = a.index(asort[i])
    ai[pos] = i+1

print (ai)    
