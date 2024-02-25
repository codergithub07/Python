mystr = "Prathmesh is a good boy"

print(mystr[0:23]) # Zero is inclusive(No need to be typed; Default value is zero), but 23 is exclusive

# print(len(mystr)) # shows amount of characters including spaces in string

# print(mystr[0:100]) # Range can be more than actual length

# print(mystr[0:9:2]) # If third data value is 'n', it will print the first character, then delete next (n-1) characters and print next one.
                      # This goes on untill it reaches the last limit value set in after 1st colon.

# If first value is not set, default is zero
# If Second value is not set, default is lenght of string
# If Third value is not set, dafault is 1 (i.e, don't delete any character)

# If first value is Negative, it counts from end of string & Same is for Second value
# NOTE :- First value from left is -1