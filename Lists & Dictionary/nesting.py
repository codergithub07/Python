# Nesting is a process of adding one or more dictinaries to a list (or)
# one or more lists to a dictionary (or)
# one or more dictionaries to a dictionaries

# List of Dictionaries :

    # Example 1
        # alien_0 = {'color' : 'green', 'points' : '10', 'speed' : 'slow'}
        # alien_1 = {'color' : 'purple', 'points' : '20', 'speed' : 'slow'}
        # alien_2 = {'color' : 'red', 'points' : '30', 'speed' : 'slow'}
        # aliens = [alien_0, alien_1, alien_2]
        # for alien in aliens:
            # print(alien)

    # Example 2 : Storing many (here, 30) alien dictionaries in the list
        # aliens = []
        # for i in range(1, 31):
            # new_alien = {'color' : 'green', 'points' : str(i*10), 'speed' : 'slow'}
            # aliens.append(new_alien)
        # for alien in aliens[:5]:
            # print(alien)
        # print(".....")
        # print("The number of aliens in the list is: " + str(len(aliens)))

    # Example 3 : Changing data of some dictionaries from example 2
        # aliens = []
        # for i in range(30):
            # new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
            # aliens.append(new_alien)
        # for alien in aliens[:3]:
            # if alien['color'] == 'green':
                # alien['color'] = 'yellow'
                # alien['points'] = '10'
                # alien['speed'] = 'medium'
        # for alien in aliens[:5]:
            # print(alien)
        # print("Number of aliens stored: ", str(len(aliens)))




# List in dictionary : This method is used when you want to associate more than one values to a single key :

    # Example 1
        # menu = {
            # 'crust' : 'thin',
            # 'toppings' : ['paperoni', 'paneer', 'olives']
        # }
        # print("You chose " + menu['crust'].title() + " crust for your pizza")
        # print("\nYour chosen Crust are:")
        # for topping in menu['toppings']:
            # print(topping.title())

    # Example 2
        # fav_lan = {'jam' : ['python', 'c'], 'kai' : ['java', 'c'], 'sid' : ['ruby', 'go', 'c++']}
        # for name in fav_lan:
            # print("\n" + name.title() + "'s favourite programming language(s) is/are:")
            # for lan in fav_lan[name]:
                # print(lan)
        # print("") # Used to add empty line at the end of the code

    # Example 3
        # fav_lan = {'jam' : ['c', 'python'], 'kim' : ['java', 'html', 'css'], 'tom' : ['python']}
        # for name in fav_lan.keys():
            # if len(fav_lan[name]) >= 2:
                # print(name + "'s favourite languages are:")
                # for languages in fav_lan[name]:
                    # print("\t", languages)
                # print()
            # else:
                # print(name + "'s favourite language is:")
                # for languages in fav_lan[name]:
                    # print("\t", languages)
                # print()




# Dictionary in dictionary
    # users = {
        # 'aeinstein' : {'f_name' : 'Albert', 'l_name' : 'Einstein', 'profession' : 'Theoretical Physicist'},
        # 'developer' : {'f_name' : 'prathmesh', 'l_name' : 'agrawal', 'profession' : 'programmer'}
    # }
    # for username, user_info in users.items():
        # print("Username: ", username)
        # print()
        # print("First name: ", user_info['f_name'].title())
        # print("Last name: ", user_info['l_name'].title())
        # print("Profession: ", user_info['profession'].title())
        # print("\n")