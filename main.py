import json
import random
import copy
f = open("AIC_quotes.json","r")
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
    guess = input().lower()
    if guess == splitQuote[removed_word].lower():
        print("Correct")
    #exit program
    elif guess == "":
        break
    else:
        print(splitQuote[removed_word])
    #character guess
    chrGuess = input("Who said it? ").lower()
    if chrGuess == quote["character"].lower():
        print("Correct")
    else:
        print (quote["character"])
    #guess the act
    actGuess = input("Now guess the act and scene: ").lower()
    if actGuess == quote["act_scene"].lower():
        print("Correct")
    else:
        print (quote["act_scene"])
    #guess the themes
    for theme in quote["themes"]:
        guess = input("Guess a theme ").lower()
        if guess in quote["themes"]:
            print("Correct")
    print(quote["themes"])