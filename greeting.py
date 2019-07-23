name = input("What your name?")
print("Hello there, " + name.capitalize())
length = str(len(name))
print("your name is " + length + " letters long!".capitalize())
first_let = str(name[0]).upper()
last_let = str(name[-1]).upper()
print("the first letter of your name is " + first_let + " and the last letter is " + last_let)
els = name[1:-1]
print("missing letter are: " + els)
