q=(input("what subject do you need help with? "))

while True:
    if q == "exit":
        print("Goodbye! Thanks for chatting with me.")
        break
    elif q == "math":
        a=input("what specific topic in math do you need help with? ")
        if a == "algebra":
            print("For a linear equation in the form , the slope is quickly found using ")
            print("m = (y2 - y1) / (x2 - x1)")
        elif a == "geometry":
            print("The area of a triangle can be calculated using the formula: A = 1/2 * base * height")
        elif a == "calculus":
            print("The derivative of a function f(x) can be found using the limit definition: f'(x) = lim(h->0) [f(x+h) - f(x)] / h")
        elif a == "multiplication":
            print("To multiply two numbers, you can use the multiplication operator (*). For example, 3 * 4 = 12.")
        elif a == "division":
            print("To divide two numbers, you can use the division operator (/). For example, 10 / 2 = 5.")
        elif a == "fractions":
            print("To add or subtract fractions, you need to find a common denominator. For example, to add 1/2 and 1/3, you can find the common denominator of 6 and rewrite the fractions as 3/6 and 2/6, then add them to get 5/6.")
        elif a == "percentages":
            print("To calculate a percentage, you can use the formula: percentage = (part / whole) * 100. For example, if you want to find what percentage 25 is of 200, you can calculate it as (25 / 200) * 100 = 12.5%.")
        elif a == "probability":
            print("Probability is calculated as the number of favorable outcomes divided by the total number of possible outcomes. For example, if you have a standard six-sided die, the probability of rolling a 3 is 1/6, since there is one favorable outcome (rolling a 3) and six possible outcomes (rolling a 1, 2, 3, 4, 5, or 6).")
        elif a == "simplifying algebraic expressions":
            print("Multiply the term outside the parentheses by every term inside. For example, 2(x + 3) becomes 2x + 6.")
        elif a == "solving equations":
            print("To solve an equation, you can use inverse operations to isolate the variable. For example, to solve the equation 2x + 3 = 7, you can subtract 3 from both sides to get 2x = 4, and then divide both sides by 2 to find x = 2.")
        elif a == "graphing":
            print("To graph a linear equation, you can find the slope and y-intercept. For example, for the equation y = 2x + 3, the slope is 2 and the y-intercept is 3. You can plot the y-intercept on the graph and then use the slope to find another point by going up 2 units and right 1 unit from the y-intercept.")
        else:
            print("I'm sorry, I don't have information on that specific topic in math.")
    elif q == "science":
        b=input("what specific topic in science do you need help with? ")
        if b == "physics":
            print("Newton's second law of motion states that the force acting on an object is equal to the mass of that object multiplied by its acceleration: F = m * a.")
        elif b == "chemistry":
            print("The periodic table organizes elements based on their atomic number, electron configuration, and recurring chemical properties.")
        elif b == "biology":
            print("The process of photosynthesis in plants converts light energy into chemical energy, producing glucose and oxygen from carbon dioxide and water.")
        elif b == "astronomy":
            print("The Hubble Space Telescope has provided valuable insights into the universe, allowing scientists to observe distant galaxies, nebulae, and other celestial objects.")
        elif b == "geology":
            print("The rock cycle describes the processes through which rocks are formed, broken down, and transformed over time, including igneous, sedimentary, and metamorphic rocks.")
        elif b == "ecology":
            print("Ecosystems are communities of living organisms interacting with their physical environment, where energy flows and nutrients cycle.")
        elif b == "genetics":
            print("DNA (deoxyribonucleic acid) is the molecule that carries genetic information in living organisms, consisting of two strands that form a double helix.")
        elif b == "evolution":
            print("Natural selection is a key mechanism of evolution, where organisms with traits that are better suited to their environment are more likely to survive and reproduce.")
        elif b == "human anatomy":
            print("The human body is made up of various systems, including the circulatory system, respiratory system, digestive system, and nervous system, each with specific functions.")
        elif b == "environmental science":
            print("Climate change refers to long-term changes in temperature, precipitation, and other atmospheric conditions on Earth, largely driven by human activities such as burning fossil fuels.")
        else:
            print("I'm sorry, I don't have information on that specific topic in science.")
    elif q == "history":
        c=input("what specific topic in history do you need help with? ")
        if c == "world war 1":
            print("World War 1, also known as the Great War, was a global conflict that lasted from 1914 to 1918, involving many of the world's great powers.")
        elif c == "world war 2":
            print("World War 2 was a global conflict that lasted from 1939 to 1945, involving most of the world's nations, including all of the great powers.")
        elif c == "ancient egypt":
            print("Ancient Egypt was a civilization that flourished along the Nile River for over three millennia, known for its pyramids, pharaohs, and hieroglyphic writing.")
        elif c == "roman empire":
            print("The Roman Empire was a powerful civilization that dominated much of Europe, North Africa, and the Middle East for centuries, known for its engineering, law, and military prowess.")
        elif c == "greek mythology":
            print("Greek mythology is a collection of stories and legends about gods, goddesses, heroes, and creatures that were part of ancient Greek culture and religion.")
        elif c == "american revolution":
            print("The American Revolution was a colonial revolt that took place between 1765 and 1783, resulting in the independence of the United States from British rule.")
        elif c == "french revolution":
            print("The French Revolution was a period of radical social and political change in France from 1789 to 1799, leading to the overthrow of the monarchy and the rise of Napoleon Bonaparte.")
        elif c == "cold war":
            print("The Cold War was a period of geopolitical tension between the United States and the Soviet Union from the late 1940s to the early 1990s, characterized by ideological conflict")
        elif c == "renaissance":
            print("The Renaissance was a cultural movement that spanned the 14th to the 17th century, marked by a revival of interest in classical art, literature, and learning.")
        elif c == "industrial revolution":
            print("The Industrial Revolution was a period of major industrialization that took place during the late 18th and early 19th centuries, leading to significant changes in agriculture, manufacturing, and transportation.")
        else:
            print("I'm sorry, I don't have information on that specific topic in history.")
    elif q == "english":
        d=input("what specific topic in english do you need help with? ")
        if d == "grammar":
            print("Grammar is the set of rules that govern how words are used to form sentences in a language.")
        elif d == "literature":
            print("Literature refers to written works, especially those considered to have artistic or intellectual value, such as novels, poetry, and plays.")
        elif d == "writing":
            print("Writing is the process of creating text to communicate ideas, thoughts, or information to an audience.")
        elif d == "vocabulary":
            print("Vocabulary is the set of words that a person knows and uses in a language.")
        elif d == "spelling":
            print("Spelling is the correct arrangement of letters to form words in a language.")
        elif d == "punctuation":
            print("Punctuation refers to the symbols used in writing to separate sentences and clarify meaning, such as periods, commas, and question marks.")
        elif d == "literary devices":
            print("Literary devices are techniques used by writers to create special effects in their writing, such as metaphors, similes, and personification.")
        elif d == "poetry":
            print("Poetry is a form of literary expression that uses rhythm, imagery, and other stylistic elements to evoke emotions and convey meaning.")
        elif d == "novels":
            print("A novel is a long narrative work of fiction that typically explores characters and themes in depth.")
        elif d == "plays":
            print("A play is a form of literature intended for performance on stage, consisting of dialogue and action performed by actors.")
        else:
            print("I'm sorry, I don't have information on that specific topic in English.")
    else:
        print("I'm sorry, I don't have information on that subject. Please choose from math, science, english, or history.")