x = input("Hi there what shall I call you? ")
c = f"Hi {x}, nice to meet you, what can I do for you? "
print(c)

while True:
    tt = input("Please ask me a question ")
    
    if tt == "exit":
        print("Goodbye! Thanks for chatting with me.")
        break
    elif tt == "what is your favorite food":
        print("I like pizza")
    elif tt == "what is your favorite color":
        print("I like blue")
    elif tt == "what is your favorite movie":
        print("I like The Mask")
    elif tt == "what is your favorite book":
        print("I like The Hitchhiker's Guide to the Galaxy")
    elif tt == "what is your favorite music":
        print("I like calm music")
    elif tt == "what is your favorite entertainment":
        print("I like video games")
    elif tt == "what is your name":
        print("My name is Tacobell AI")
    elif tt == "what is your age":
        print("I do not have an age, I am a computer program")
    elif tt == "what is your favorite hobby":
        print("I like to help people I also like to learn new things")
    else:
        print