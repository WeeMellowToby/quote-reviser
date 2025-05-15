import json
import random
import copy
f = open("poem_quotes.json","r")
quoteJSON = json.loads(f.read())

while True:
    #get quote
    quote = quoteJSON[random.randint(0,len(quoteJSON)-1)]
    #replace a word with _
    splitQuote = quote["quote"].split(" ")
    quoteDisplay = copy.deepcopy(splitQuote)
    removed_word = random.randint(0,len(quoteDisplay)-1)
    quoteDisplay[removed_word] = "_" * len(quoteDisplay[removed_word])
    for i in range(0,len(quoteDisplay)):
        print(quoteDisplay[i],end=" ")
    #guess quote
    guess = input()
    if guess.lower() == splitQuote[removed_word].lower():
        print("Correct")
    #exit program
    elif guess == "":
        break
    else:
        print(splitQuote[removed_word])
    #character guess
    chrGuess = input("Which poem is it? ")
    if chrGuess == quote["poem"]:
        print("Correct")
    else:
        print (quote["poem"])
    #guess the act
    #guess the themes
    for theme in quote["themes"]:
        guess = input("Guess a theme ")
        if guess in quote["themes"]:
            print("Correct")
    print(quote["themes"])