cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("Enter the colour of cat: ")
# ...
interaction = input("Would you like to interact with " + name + ": ")
if interaction == "yes":
    interaction = True
else:
    interaction = False
# start the while loop
while interaction == True:
    # Finish the string below
    option = input("What would you like to do?\n1. Play with your cat\n2. Train your cat\n3. Show stats\n4. Feed cat\n5. Put cat to sleep\noption: ")
    
    if option == '1':
        if cat_attributes['energy'] < 10:
            print(name + " is too tired to play")
        # change the cat's attributes here
        else:
            cat_attributes["intelligence"] = cat_attributes["intelligence"] + 10
            cat_attributes["energy"] = cat_attributes["energy"] - 10
        pass
    elif option == '2':
        if cat_attributes['energy'] < 10:
            print(name + " is too tired to train")
        else:
            cat_attributes["intelligence"] = cat_attributes["intelligence"] + 20
            cat_attributes["energy"] = cat_attributes["energy"] - 20
        pass
    # elif ...
    elif option == "3":
        print(cat_attributes["intelligence"])
        print(cat_attributes["energy"])
        print(cat_attributes["weight"])
    elif option == "4":
        cat_attributes["energy"] = cat_attributes["energy"] + 20
        cat_attributes["weight"] = cat_attributes["weight"] + 10
    elif option == "5":
        cat_attributes["energy"] = cat_attributes["energy"] + 40
        cat_attributes["weight"] = cat_attributes["weight"] + 5
    else:
        pass
    interaction = input("Would you like to interact with " + name + ": ")
    if interaction == "yes":
        interaction = True
    else:
        interaction = False

    