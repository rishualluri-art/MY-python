asrxdctfvygbhcdtfvybghnimport random as rand

animals= {'rhino': ["strong", "horned", "gray"],'turtle':['slow', 'shelled', 'green'],'hare':["fast", "white", "furry"],'snake':['scaled','hisses','fangs'],'mouse':['small','squeaky','cheese loving'],'elephant':['big','gray','loud'],'lion':['mane','predator','carnivore'],'parrot':['feathered','repeating','colorful']}
    
choice=list(animals.keys())[rand.randint(0,7)]
print("Guess AWAY")
answerCorrect = False
for i in range(5):
    x=(input("Give me an adjetive, i will tell you if it applies to the animal!  Or guess the animal type exit to quit \n")).lower()
    if x == 'exit':
        print("Goodbye.")
        break
    if x == choice:
        print("Thats Correct!")
    else:
        print("nah")
    if x in list(animals.keys()):
        answerCorrect = True
        break
    if answerCorrect:
        print("CONGRATS U GUESSED THE "+ choice + " CORRECT!!!")
        
    else:
        print("damn bro try again \n\n")
        pass
