name1 = 'james'
name2 = 'kim'
name3 = 'mike'
name4 = 'robert'
name5 = 'steve'


# alien_0 = {'color' : 'green'} # Sets string value green in color key
    # print(alien_0['color'])




# alien_0 = {'color' : 'green', 'points' : '10'}
    # print(alien_0['color'])
    # print(alien_0['points'])




# Adding keys and their value to the dictionary :

    # alien_0 = {'color' : 'green'}
    # print(alien_0)
    # alien_0['X_coordinate'] = 50
    # alien_0['Y_coordinate'] = 50
    # print(alien_0)




# Changing keys and their value in the dictionary :

    # alien_0 = {'colour' : 'green'}
    # print(alien_0['colour'])
    # alien_0['colour'] = 'yellow' # This changes to value of the key in dictionary
    # print(alien_0['colour'])

    




# Using del statement in dictionary :

    # color = 'color'
    # point = 'point'
    # alien = {color : 'green', point : 5}
    # print(alien)
    # del alien[point]
    # print(alien)




# Another way of writing a dictionary :

    # fav_lan = {
        # 'james' : 'python',
        # 'ken' : 'c',
        # 'kit' : 'html',
        # 'Sir' : 'python'
        # }
    # print("Your favourite language is: ", fav_lan['Sir'].title())




# Another way of writing dictionary :

    # x_pos = 'x'
    # y_pos = 'y'
    # speed = 'speed'
    # alien = {x_pos : 50, y_pos : 50} # No need to use ' ' to store integer value
    # alien[speed] = 'm'
    # if alien[speed] == 's':
        # x_incr = 10
    # elif alien[speed] == 'm':
        # x_incr = 20
    # else:
        # x_incr = 30
    # print("Initial position of alien: ( " + str(alien[x_pos]) + "," + str(alien[y_pos]) + ")") # Need to convert int datatype to str because print statement can only concatenate str to str
    # alien[x_pos] = alien[x_pos] + x_incr
    # print("Position of alien after one second: " + "(" + str(alien[x_pos]) + "," + str(alien[y_pos]) + ")")




# Using loop for dictionary :

    # user = {
        # 'james' : 34,
        # 'kim' : 45,
        # 'rom' : 23,
    # }
    # for n, age in user.items(): # Items method is used to get pair of key-value from the dictonary
        # print("Name of User: ", n)
        # print("Age of User: ", age)
        # print("") # Just used to add empty line




# Using key method :

    # user = {
        # 'james' : 34,
        # 'kim' : 45,
        # 'rom' : 23,
    # }
    # for n in user.keys(): # keys method is used to get keys from the dictionary which is also by default
        # print("Name of User: ", n)
        # print("")

    # Another example
        # age = {
            # 'james' : 34,
            # 'kim' : 45,
            # 'rom' : 23,
        # }

        # friends = ['james', 'rame', 'rom']
        # for n in age.keys():
            # print(n)
            # if n in friends:
                # print("Hey " + n + " I see you turned into " + str(age[n]) + " CONGRADULATIONS for that we met at your " + str(age[n] - 5) + "th Birthday")
            # print("")




# To get the key-value pairs in alphabetical order from the dictionary :

    # users = {
        # 'james' : 'python',
        # 'roma' : 'java',
        # 'kit' : 'c'
    # }
    # for u in sorted(users.keys()):
        # print("" + u.title() + " Thank You for taking part in the poll")
        # print("we got your favourite language is " + users[u].title())
        # print("")




# Looping through values :

    # users = {
        # 'james' : 'python',
        # 'rama' : 'c',
        # 'mike' : 'java'
    # }
    # for languages in users.values():
        # print("The mentioned languages are: ", languages.title())




# set function to avoid repeatation of values :

    # fav_lan = {
        # name1 : 'python',
        # name2 : 'c',
        # name3 : 'java',
        # name4 : 'python',
        # name5 : 'java'
    # }
    # print("The mentioned Languages are:")
    # for language in set(fav_lan.values()):
        # print(language)




# Filling dictionary with loops :

    # poll = {}
    # poll_status = True
    # print('WELCOME TO Agrawal Tours & Travels\n')
    # while poll_status:
        # name = input('\nEnter your name : ')
        # response = input('\nEnter the place you want to visit : ')
        # poll[name] = response
        # ask_status = True
        # while ask_status:
            # ask = input('\nDo you want to add more passengers? (yes/no) : ')
            # if ask == 'no':
                # ask_status = False
                # poll_status = False
            # elif ask == 'yes':
                # break
            # else:
                # print('Please respond in yes/no')
                # continue
    # for stored_name, stored_response in poll.items():
        # print('\nCongradulations ' + stored_name.title() + " your flight to " + stored_response.title() + ' is booked')
    # print()




# from collections import OrderedDict   # This OrderedDict class is used to maintain the order of the dictionary

    # fav_language = OrderedDict()

        # fav_language[name1] = 'python'
        # fav_language[name2] = 'C'
        # fav_language[name3] = 'java'

        # for name, language in fav_language.items():
        #     print(name + " like " + language)