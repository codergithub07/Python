languages = ['Python', 'C', 'Java', 'Django']

# print(languages,"\n")




# print("\n",languages[0]) # Prints a specific element(Here, first element is being printed) from the list




# print("\n",languages[1])




# print("\n",languages[-1]) # Negative index prints element from the last(starting form -1)




# languages[0] = 'HTML' # Changing the desired element(Here, first) in the list
    # print("\n", languages)




# languages.append('CSS') # Adds element at the last position of the list
    # print("\n",languages)




# languages.insert(0, 'C#') # Inserts element in given position of the list
    # print("\n", languages)




# del languages[0] # Removes element present at the given index(position) permanently after this statement
    # print("\n", languages)




# popped_language = languages.pop() # Removes last element(by default) from the list permanently after this method and stores in the desired variable(if a variable is defined for this)
    # print(languages)
    # print(popped_language)

    # pop_languages = languages.pop(0) # Removes first element from the list and stores in defined variable
    # print(languages)
    # print(pop_languages)




# languages.remove('Python') # This method is used when you don't know the index of an element, but know it's value
    # print(languages)




# for language in languages: # Here for loop is used set every individual value of the languages list in the language variable
    # print(language)




# even_num = list(range(2,21,2)) # list function is used to convert set of integers into list
    # print(even_num)




# num = []
    # for value in range(1,11):
        # square = value**2 # In Python '**' means exponential expression
        # num.append(square)
    # print(num)




# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9] # No need to use inverted comas to store integer in the list
    # print(max(digits))
    # print(min(digits))




# List Comprehension
    # squares = [num**2 for num in range(1,11)] # write the operation to be done before for loop
    # print(squares)




# List Slicing :

    # names = ['ram', 'sham', 'prabhu', 'krishna', 'bro']
        # print(names[0:5])
        # print(names[2:4])
        # print(names[-3:5])
        # print(names[::2])

        # print("The participating candidates are:")
            # for can in names[:3]:
                # print(can)




# dishes = ('pizza', 'paneer masala', 'tandoori roti', 'naan') # Tuple is a type of immutable list whose items can't be changed
    # for item in dishes:
        # print(item)

    # dishes = ('gopal', 'krishna') # You can assign the variable the completely new value set
        # for item in dishes:
            # print(item)




# Checking whether an element is present in the list :

    # menu = ['pizza', 'burger', 'pasta']
    # want = 'paneer'
    # if want in menu:
        # print('Yes you can have',want)
    # else:
        # print("Sorry, we only have:")
        # for i in menu:
            # print(i)




# Checking whether an element is not present in the list :

    # menu = ['pizza', 'burger', 'pasta']
    # want = 'paneer'
    # if want not in menu:
        # print("Sorry, we only have:")
        # for i in menu:
            # print(i)
    # else:
        # print('Yes you can have',want)




# Checking if list is not empty :

    # req_toppings = []
    # if req_toppings: # If no value is asked to check for, it checks whether the list is empty
        # for topping in req_toppings:
            # print("Adding ", topping)
        # print("Finished making your Pizza")
    # else:
        # print("Do you want a plain pizza?")




# Using Multiple Lists :

    # available_cars = ['bmw', 'audi', 'hyundai', 'farrari']
    # requested_cars = ['paurche', 'honda', 'hyundai']
    # for requested_car in requested_cars:
        # if requested_car in available_cars:
            # print("Adding ", requested_car, "in your cart")
        # else:
            # print("Sorry we don't sell ", requested_car)
    # print("Your Cart is ready")




# Updating list with loops :

        # unvarified_users = ['kim', 'jon', 'rom']
        # verified_users = []
        # while unvarified_users: # Loop will continue running untill the list "unverified_users" is empty
            # new_user = unvarified_users.pop()
            # verified_users.append(new_user)
        # for i in verified_users:
            # print("Hello " + i + ', you are our new user')
            # print()
        



# Removing all instances from a list using loops :

        # pets = ['dog', 'cat', 'fish', 'hamster', 'cat', 'dog', 'bird']
        # print("Original list:\n" + str(pets))
        # while 'cat' in pets: # Checks if 'cat' is present in the list
            # pets.remove('cat')
        # print('\nUpdated list after removing all cats:\n' + str(pets))
        # print()




# Using Enumerate : This function gives the index and value of the list, touple, string

fruits = ['apple', 'banana', 'kiwi', 'mango']

# Example 1: Index starting from 0 by default
    # for index, value in enumerate(fruits):
    #     print(f"Index: {index}    Value: {value}")

# Example 2: Setting initial index value

for index, value in enumerate(fruits, start=2):
    print(f"Index : {index}    Value : {value}")