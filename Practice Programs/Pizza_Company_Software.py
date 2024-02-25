name = {}
phone = ''
chosen_pizza_list = []
chosen_toppings_list = []

def pizza_list(pizza_available, toppings_available):

    print("We have the following pizzas :\n")
    for i in pizza_available:
        print(i.title())
    print()
    print("You can add following toppings to your pizza :\n")
    for i in toppings_available:
        print(i.title())
    print()

def final_pizza(chosen_pizza, chosen_toppings):

    print("\nYou have chosen\n")
    for i in chosen_pizza:
        print(i)
    print()
    if chosen_toppings:
        print("You would like to add folling toppings to your pizza :\n")
        for i in chosen_toppings:
            print(i)
    else:
        print("You didn't choose any extra toppings for your pizza")

if name:
    print()

else:
    fname_input = input("Please enter your First name : ")
    name['f_name'] = fname_input
    lname_input = input("Please enter your Last name : ")
    name['l_name'] = lname_input

if phone:
    print()

else:
    phone_input = input("Please enter your Phone number : ")
    phone = phone_input

pizza_input = ''
topping_input = ''

while name:

    while phone:

        # chosen_pizza_list = []

        print("\nHello " + name['f_name'].title() + " " + name['l_name'].title() + ", welcome to Agrawal Pizza Palace")

        pizza_list(['paneer pasanda', 'king onion', 'sweet home', 'all in one'], ['paneer', 'tomato', 'onion', 'green paper', 'olives'])

        print("Which pizza would you like to order?(Type no after finalizing pizza list)\n")

        while pizza_input != 'no':
            pizza_input = input("")
            if pizza_input != 'no':
                chosen_pizza_list.append(pizza_input)

        print("\nWhich toppings would you like to add?(type no to skip this step)\n")

        while topping_input != 'no':
            topping_input = input('')
            if topping_input != 'no':
                chosen_toppings_list.append(topping_input) 

        final_pizza(chosen_pizza_list, chosen_toppings_list)
        print("\nThank You for choosing Agrawal Pizza Palace!")
        break
    break
print()