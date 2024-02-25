# Working with user input

    # Method 1 of writing the code :- Less clean and not recommended

        # import json
        # file = 'username.json'
        # try:
        #     with open(file) as f:
        #         username = json.load(f)
        # except:
        #     username = input("Hello user! what is your username? ")
        #     with open(file, 'w') as f:
        #         name = json.dump(username, f)
        #         print("We will remember you when you return " + username)
        # else:
        #     print("Welcome back! " + username)




    # Method 2 :- More clean
        # import json
        # def get_stored_username():
        #     try:
        #         with open('username.json') as f:
        #             username = json.load(f)
        #     except FileNotFoundError:
        #         return None
        #     else:
        #         return username 
        # def greet_user():
        #     username = get_stored_username()
        #     if username:
        #         print("Welcome Back! " + username)
        #     else:
        #         user = input("Enter your username :- ")
        #         file = 'username.json'
        #         with open(file, 'w') as f:
        #             json.dump(user, f)
        #             print("Your Username is successfully stored!")
        # greet_user()




    # Method 3 :-
import json
def get_stored_username():
    try:
        with open('username.json') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_user_data():
    file = 'username.json'
    user = input("Enter your username :- ")
    with open(file, 'w') as f:
        json.dump(user, f)
    return user

def greet_user():
    user = get_stored_username()
    if user:
        print("Welcome Back! " + user)
    else:
        username = get_new_user_data()
        print("Your username is successfully stored! " + username)
greet_user()