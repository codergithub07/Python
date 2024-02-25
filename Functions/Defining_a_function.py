# def greet_user() :
    # """Display a simple greeting.""" # This is a docstring
    # print('Hello World!')
# greet_user()




# Positional Arguments :

    # def greet_user(first_name, last_name):
        # print('Hello ' + first_name.title() + ' ' + last_name.title())
    # greet_user('kim', 'shroff') # These are positional arguments
    # greet_user('tom', 'cruse')




# Keyword Arguments :

    # def pets(pet_type, pet_name) :
        # print("I have a " + pet_type.title())
        # print("His name is " + pet_name.title())
    # pets(pet_name = 'harry', pet_type = 'dog')




# Using default value : The value to default variable can be changed

    # def pets(pet_name, pet_type = 'dog'):
        # print('I have a ' + pet_type.title())
        # print('His name is ' + pet_name.title())
    # pets(pet_name = 'john')
    # pets('kit') # it sets the value 'kit' to first parameter (here, per_name) and uses the default value for second parameter
    # pets(pet_type = 'cat', pet_name = 'koi')




# return statement :

    # Example 1 :

        # def username(name):
            # return name.title()
        # print(username('jarvis'))

    # Example 2 :

        # def username(f_name, m_name = '', l_name = ''):
            # if m_name: # Python enterprets non-empty string as True
                # full_name = f_name + ' ' + m_name + ' ' + l_name
            # else:
                # full_name = f_name + ' ' + l_name
            # return full_name.title()
        # print("My boss's name is " + username('prathmesh'))
        # print("\nHis full name is " + str(username('prathmesh', l_name = 'agrawal', m_name = 'aditya')))
        # print()




# Passing more than one arguments (arbitrary agruments) in function :

    # def pizza(*topping):
        # print("Following toppings are used :")
        # for i in topping:
            # print('- ', i)
        # print()
    # pizza('papperoni')
    # pizza('paneer', 'pasta', 'olives')




# Mixing positional & arbitrary arguments :

    # def pizza(size, *toppings): # Always put arbitrary parameter at the end
        # print("Following toppings are used for " + size + " inch pizza :")
        # for i in toppings:
            # print("- ", i)
        # print()
    # pizza('12', 'paperoni')
    # pizza('16', 'paneer', 'papperoni', 'onion')




# Using Arbitrary number of arguments :

    # def user(first_name, last_name, **extras): # Double astriks are used to make an empty dictionary with arbitrary number of key-value pairs
        # person = {}
        # person['f_name'] = first_name
        # person['l_name'] = last_name
        # for key, value in extras.items():
            # person[key] = value
        # return person
    # user_data = user('James', 'Robin', Location = 'india', profession = 'coder')
    # print(user_data)