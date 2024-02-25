# Example 1 :
    # age = int(input("enter your age: "))
    # print(age)




# Example 2 :
age = input("Enter your age: ")
vote = "\nEnter name of the party,"
vote += "\nyou are giving vote to:\t"
if int(age) >= 18:
    print("\nYour Vote is given to: ", input(vote).upper())

else:
    print("\nMinimum age for voting is 18")
print()