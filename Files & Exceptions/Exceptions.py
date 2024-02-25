print('\n\n') # This is just to add blank line before the main output. It's nothing to do with the main code




# Using try-except blocks :-

    # try:
    #     print(5/0)
    # except ZeroDivisionError:
    #     print("Can't divide by zero")




# Working with exceptions :- Running action if no error occured

    # print("Enter any numbers and I'll divide them for you :-")
    # print("press 'q' to quit")
    # while True:
    #     num1 = input("Enter your first number :- ")
    #     if num1 == 'q':
    #         break
    #     num2 = input("Enter your second number :- ")
    #     if num2 == 'q':
    #         break
    #     try:
    #         ans = int(num1)/int(num2)
    #     except ZeroDivisionError:
    #         print("Can't divide by zero")
    #     else:
    #         print(ans)




# File_Not_Found_Error :-

    # file = 'alice.txt'
    # try:
    #     with open(file) as f:
    #         content = f.read()
    # except FileNotFoundError:
    #     print("The file " + file + " is missing")
    # else:
    #     with open(file) as f:
    #         content = f.read()
    #     print(content)




# Counting number of words in the text file :-

    # file = 'test.txt'
    # try:
    #     with open(file) as f:
    #         content = f.readlines()
    # except FileNotFoundError:
    #     print("We can't find the file")
    # else:
    #     string = ''
    #     for line in content:
    #         string += line.rstrip()
    #         string += ' '
    #     print(string.split())
    #     print(len(string.split()))




# Working with more files :- This way of code makes it easier to work with different files without rewriting whole code
    # def count_word(file_name):
    #     try:
    #         with open(file_name) as f:
    #             content = f.readlines()
    #     except FileNotFoundError:
    #         print("We can't find the file")
    #     else:
    #         string = ''
    #         for line in content:
    #             string += line.rstrip()
    #             string += ' '
    #         print(string.split())
    #         print(len(string.split()))

    # file = 'test_write.txt'
    # count_word(file)




# Accessing a list of files

    # def count_word(file_name):
    #     try:
    #         with open(file_name) as f:
    #             content = f.readlines()
    #     except FileNotFoundError:
    #         print("We can't find the file " + file_name)
    #     else:
    #         string = ''
    #         for line in content:
    #             string += line.rstrip()
    #             string += ' '
    #         print(string.split())
    #         print(len(string.split()))

    # files = ['test.txt', 'test_write', 'test_write.txt']
    # for file in files:
    #     count_word(file)
    #     print()




# Failing to access a file silently :-

# def count_word(file_name):
    #     try:
    #         with open(file_name) as f:
    #             content = f.readlines()
    #     except FileNotFoundError:
    #         print("We can't find the file")
    #     else:
    #         string = ''
    #         for line in content:
    #             string += line.rstrip()
    #             string += ' '
    #         print(string.split())
    #         print(len(string.split()))

    # file = 'test_write.txt'
    # count_word(file)




# Accessing a list of files

    # def count_word(file_name):
    #     try:
    #         with open(file_name) as f:
    #             content = f.readlines()
    #     except FileNotFoundError:
    #         pass    # This ignores the error and continues with rest of the code
    #     else:
    #         string = ''
    #         for line in content:
    #             string += line.rstrip()
    #             string += ' '
    #         print(string.split())
    #         print(len(string.split()))

    # files = ['test.txt', 'test_write', 'test_write.txt']
    # for file in files:
    #     count_word(file)
    #     print()




# Using Finally :

    # def file_check(file):
    #     try:
    #         with open(file) as f:
    #             content = f.readlines()
    #     except:
    #         pass
    #     else:
    #         for line in content:
    #             print(line.rstrip())
    #     finally:
    #         print("This part will run in any situation whether the code gets and error or not")

    # file = 'test.txt'
    # file_check(file)


    
    






print('\n\n')   # This is just to add blank line after the main output. It's nothing to do with the main code