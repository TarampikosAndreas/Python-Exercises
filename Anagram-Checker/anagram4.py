def deleteSpaces(s):
    s_new = s.replace(" ","",)
    return s_new

def check(s1,s2):
    if sorted(deleteSpaces(s1).lower()) == sorted(deleteSpaces(s2).lower()):
        print("Anagram")
    else:
        print("Not Anagram")

s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")

check(s1,s2)
