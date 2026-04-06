#daily routine coach
import random as rand
time=str(input("What time is it currently(round to nearest hr)? \n")).lower()
dict={"learn about something":"1hr","try a diy science expelrement":"1hr","score some points play basketbal/any sport":"1hr","play some video games":"1hr"}
a=list(dict.keys())[rand.randint(0,3)]
b=list(dict.keys())[rand.randint(0,3)]
c=list(dict.keys())[rand.randint(0,3)]
d=list(dict.keys())[rand.randint(0,3)]
e=list(dict.keys())[rand.randint(0,3)]
g=list(dict.keys())[rand.randint(0,3)]
for i in range(1):
    x= ("type exit to quit")
    if x == "exit":
        break
    if time== '8pm':
        print ("go TO BED")
    elif time=='7pm':
        print(a)
    elif time == '6pm':
        print(a+','+b)
    elif time == '5pm':
        print(a+','+b+','+c)
    elif time == '4pm':
        print (a+', '+b+', '+c+', '+d)
    elif time == '3pm':
        print(a+', '+b+', '+c+', '+d+', '+e)
    elif time == '2pm':
        print(a+', '+b+', '+c+', '+d+', '+e+', '+g)
    elif time == '1pm':
        print(a+', '+b+', '+c+', '+d+', '+e+', '+g+', '+a)
    elif time == '12pm'or '12am':
        print(a+', '+b+', '+c+', '+d+ ', '+e+', '+g,', '+a,', '+b)
    else: 
        time == '5am'or '6am'or '7am'or '8am'or'9am'or'10am'or'11am'
        print("Come back later!!")