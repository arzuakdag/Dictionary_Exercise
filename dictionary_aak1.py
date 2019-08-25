# Exercise for Section 5
import json #import a library to we can read the json file
from difflib import get_close_matches

data = json.load(open("data.json")) #data is a Python dictionary

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: # so initial cap letters are ok and do not get automatically lowered
        return data[w.title()]
    elif w.upper() in data: # in case for such as usa and USA
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0: #this is an object that gets checked against lenght
        yn = input("Did you mean %s instead? Enter Y or N: " % get_close_matches(w, data.keys())[0]) 
        if yn == "Y": # == this is a comparison operator 
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please check again."
        else:
            return "We did not understand your inquiry." 
    else:
        return "The word does not exist. Check it!"
    
word = input("Enter your word: ") #this passes your word into w up top 

output = (translate(word)) # This section removes quotation marks and signs
if type(output) == list: # Makes sure code doesn't iterate through each "letter"
    for item in output:
        print(item)
else:
    print(output) # Print output without iterating through it
