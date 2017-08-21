import json #load json std lib
from difflib import get_close_matches #importing function to perform spellcheck

data=json.load(open("dictionary.json")) #load dictionary

def explain(word):
    '''function that looks up explanation'''
    word=word.upper() #case insensitivity
    if word in data: #test if word is data set
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.7)) > 0:
        '''part that checks against possible misspelling
        and suggest best matching word'''
        yesno= input("Did you mean %s insted? \nEnter y if yes, or n if no " \
        % get_close_matches(word, data.keys())[0])
        yesno=yesno.lower()
        if yesno == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno == "n":
            return "The word is not in dictionary.\nPlease check spelling"
        else:
            return "Wrong input"
    else:
        return "The word is not in dictionary.\nPlease check spelling"

word = input("Enter your word: ") #asking for word to look up

explanation = explain(word)

print(explanation) #returning explanation
