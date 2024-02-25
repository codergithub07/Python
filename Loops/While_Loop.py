# print()
# a = 0
# while a<= 10:
    # print(a)
    # a += 1




# for a in range(11):
    # while(a<=5):
        # print(a)
        # break
    # while(a>=5):
        # print(a)
        # break




# Example 3 : Program will run untill user want it to stop

    # Way 1 :
        # prompt = "Enter anything and I will convert it to upper case"
        # prompt += "\nEnter quit to exit the program: "
        # message = ""
        # while message != 'quit': #and message != 'will you marry me':
            # print()
            # message = input(prompt)
            # print("\n", message.upper())
            # print()
            # while message == "will you marry me":
                # reply = input("Say Your answer: ")
                # print()
                # if reply == 'yes':
                    # print("CONGRATS! have a beautiful life together.")
                    # message = ""
                # elif reply == 'no':
                    # print("I respect your answer.")
                    # message = ""
                # else:
                    # print("Please answer in yes or no\n")
            # if message == 'quit':
                # print("\nYou chose to exit the program!")
        # print()

    # Way 2 :
        # prompt = "Type anything to change it to upper case"
        # prompt += "\n\nType your word/sentence: "
        # state = True
        # while state:
            # message = input(prompt)
            # print("\n", message.upper())
            # print()
            # if message == 'quit':
                # state = False
                # print("You chose to exit")
        # print()

    # Way 3 : Using Break
        # prompt = 'Which city would you like to go?\n'
        # while True:
            # message = input(prompt)
            # if message == 'quit':
                # break
            # else:
                # print("I would like to go to ", message.title())

# While loop with list :-
    # Updating list :
        # unvarified_users = ['kim', 'jon', 'rom']
        # verified_users = []
        # while unvarified_users: # Loop will continue running untill the list "unverified_users" is empty
            # new_user = unvarified_users.pop()
            # verified_users.append(new_user)
        # for i in verified_users:
            # print("Hello " + i + ', you are our new user')
            # print()
        
    # Removing all instances from a list :
        # pets = ['dog', 'cat', 'fish', 'hamster', 'cat', 'dog', 'bird']
        # print("Original list:\n" + str(pets))
        # while 'cat' in pets: # Checks if 'cat' is present in the list
            # pets.remove('cat')
        # print('\nUpdated list after removing all cats:\n' + str(pets))
        # print()
        