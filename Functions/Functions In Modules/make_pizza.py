def pizza(size, *toppings):
    print("You chose these toppings for a " + size + " inch pizza")
    for i in toppings:
        print("- ", i)
    print()