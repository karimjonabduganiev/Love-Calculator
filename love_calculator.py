print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name = name1 + name2
name_lover = name.lower()

t = name_lover.count("t")
r = name_lover.count("r")
u = name_lover.count("u")
e = name_lover.count("e")

true = t + r + u + e

l = name_lover.count("l")
o = name_lover.count("o")
v = name_lover.count("v")
e = name_lover.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together life coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

