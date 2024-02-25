questions = [
    ["Who is the greatest coder of all time?", "Prathmesh", "Steve", "jones", "none", "1"],

    ["Who is the greatest robotics engineer of all time?", "Rebal", "Prathmesh", "Kimonel", "none", '2'],

    ["Who will win the game", "india", "america", "canada", "russia", '1'],

    ["Name the most intelligent person on earth", "Prathmesh", "Steve", "Andrew", "Jones", '1']
]

price = [1000, 2000, 4000, 6000]

i = 0

while True:
    for question in questions:
        print(f"\n{question[0]}       For price amount of Rs.{price[i]}\n")
        # for i in range(1, len(question)-1):
        print(f"a. {question[1].title()}            b. {question[2].title()}")
        print(f"c. {question[3].title()}            d. {question[4].title()}")
        print("\nPress q to exit")
        ans = input("\nWrite your answer: ")
        
        if ans == question[5]:
            print("\nYou are right!")
            if i == len(price)-1:
                print("\nYou are taking Rs.6000 at home")
                ans = input("Press q to exit: ")
            i += 1
        
        elif ans == "q":
            print(f"\nYou are taking Rs.{price[i-1]} at home")
            print("")
            break
        
        else:
            print("\nYou are wrong!")
            
            if i < 3:
                print("\nYou are taking Rs.1000 at home")
            
            else:
                print(f"\nYou are getting the amount of: Rs.{price[i-1]}")
            
            print("")
            break

        # print("") 

print("")