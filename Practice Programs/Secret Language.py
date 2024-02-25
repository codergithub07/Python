# If the word has atleast 3 characters, the first and the last character will be interchanged and three new random charactors will added at the starting & in the end of the word.

# If the word has only two characters, they both will interchange their places

# First take input message from the user
# Then check for the length of the characters in each word
# Change accordingly
# Reprint the message in secret language


msg = input("Write your message (in paragraph) to convert it into the secret code language:\n\n")

lst = msg.split()

new_lst = []

two_letter_word = ""

if msg != 'decode':

    for i in lst:
        if len(i) >= 3:
            # print("" + i[1] + i[0])
            s1 = 'kor'
            s2 = 'tif'
            new_str = s1 + i[1:] + i[0] + s2
            new_lst.append(new_str)

        
        elif len(i) == 2:
            new_str = i[::-1]
            new_lst.append(new_str)
        
        else:
            new_str = 'yo' + i + 'ru'
            new_lst.append(new_str)

    print(" ".join(new_lst))
        
else:
    msg = input("Write your secret language paragraph to decode into normal language:\n\n")
    lst = msg.split()
    for i in lst:
        if len(i) >=9:
            
            
            new_str = i[len(i)-4] + i[3:len(i)-4]
            new_lst.append(new_str)

        
        elif len(i) == 2:
            new_str = i[::-1]
            new_lst.append(new_str)
        
        else:
            new_str = i[2]
            new_lst.append(new_str)
        
    print(" ".join(new_lst))