#DOCTYPE.python
#EX2.py
from random import randint, random
good= ["good", "great", "amazing", "fantastic", "wonderful",]
#while loop to keep the program running until the user decides to exit
while True:
    Feeling= input("How are you feeling today? (exit to quit) ")
    if Feeling == "exit":
        print("Goodbye! Thanks for chatting with me.")
        break


    if Feeling == "good":
        print(f"so you are feeling {good[randint(0, len(good)-1)]}, thats great to hear!")
    elif Feeling == "sad":
        print("Im sorry to hear that, I hope you feel better soon.")
    elif Feeling == "mad":
        print("Anger is often just the \"smoke\" above a deeper burn of pain or hurt—be gentle with what lies beneath")
    elif Feeling == "tired":
        print("Make sure to get enough rest and take care of yourself.")
    elif Feeling == "anxious":
        print("Try to take deep breaths and focus on the present moment. It can also help to talk to someone you trust about how you're feeling.")
    elif Feeling == "excited":
        print("That's great! Enjoy the moment and make the most of it.")
    elif Feeling == "bored":
        print("Try to find something new and interesting to do, or maybe try a new hobby.")
    elif Feeling == "lonely":
        print("Remember that you are not alone, and there are people who care about you. Consider reaching out to friends or family, or joining a community group or club.")
    elif Feeling == "confused":
        print("Try to take a step back and break down the problem into smaller parts. It can also help to talk to someone else about it or do some research to gain a better understanding.")
    elif Feeling == "happy":
        print("That's wonderful! Keep enjoying the good vibes and spread the positivity.")
    elif Feeling == "stressed":
        print("Try to take a break and do something you enjoy, or try some relaxation techniques like deep breathing or meditation.")
    elif Feeling == "grateful":
        print("That's a great feeling to have! Take a moment to appreciate the good things in your life and share your gratitude with others.")
    elif Feeling == "hopeful":
        print("That's a positive mindset to have! Keep believing in yourself and your goals, and take steps towards making them a reality.")
    elif Feeling == "overwhelmed":
        print("Try to prioritize your tasks and break them down into smaller, manageable steps. It can also help to ask for support from friends, family, or a professional if needed.")
    elif Feeling == "frustrated":
        print("It's okay to feel frustrated sometimes. Try to take a deep breath and approach the situation with a fresh perspective.")
    elif Feeling == "hungry":
        print("Make sure to eat something nutritious and satisfying to fuel your body and mind.")
    else:
        print("Im sorry, I dont understand how you are feeling.")
