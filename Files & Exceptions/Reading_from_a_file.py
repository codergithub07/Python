print('\n\n') # This is just to add blank line before the main output. It's nothing to do with the main code



# Reading a file :-

    # with open('test.txt') as file_object:   # The current working directory is 'C:\Users\prath\OneDrive\Desktop\Programming'
    #     content = file_object.read()
    #     # print(content)
    #     print(content.rstrip()) # this method is used to neglect the blank space after a line




# Reading a file linewise :-

    # file = 'test.txt'
    # with open(file) as f:
    #     for line in f:
    #         print(line.rstrip())




# Storing contents of file in a list :-

    # with open('test.txt') as f:
    #     lists = f.readlines()
    # for line in lists:
    #     print(line.rstrip())




# Arragning a file content in a line :-

    # with open('test.txt') as f:
    #     lines = f.readlines()
    # string = ''
    # for line in lines:
    #     string += line.rstrip()
    #     string += ' '
    # print(string)
    # print(len(string))




# Accessing a file's content till a specific range :-

    # with open('test.txt') as f:
    #     lines = f.readlines()
    # string = ''
    # for line in lines:
    #     string += line.rstrip()
    #     string += ' '
    # print(string[:82])    # NOTE :- This prints the string value till specified length, but the code reads whole file
    # print(len(string))

# USE :- Can be used to eliminate the unwanted blank space after the complition of all lines




# Checking if a string value is present in the file :-
    
    # with open('test2.txt') as f:
    #     pi = f.read()
    # string = ''
    # for line in pi:
    #     string += line.rstrip()
    # print(len(string))
    # if '1472' in string:
    #     print("YES")
    # else:
    #     print('NO')   
    



    







print('\n\n')   # This is just to add blank line after the main output. It's nothing to do with the main code