# import os

# 1) os.mkdir('dir_1') # Creates a directry in current working directory; One can add extention to make it a type of file NOTE :- It doesn't run if the file is already created

# 2) os.mkdir('D:/dir_2') # Creates a directry in different directory; One can add extention to make it a type of file NOTE :- It doesn't run if the file is already created

# 3) print("", os.getcwd()) # Represents a string showing the path of Current Working Directory

# 4) os.rename('renamed_dir_1', 'dir_1') # Rename an existing directory; One can add extention to make it a type of file

# 5) os.renames('C:/Users/prath/OneDrive/Desktop/r_dir_1', 'dir_1') # Rename and transfer existing directory to new destination with new name; One can add extention to make it a type of file

# 6) print("Directory Before changing : ", os.getcwd())
#    os.chdir('D:/dir_2') # Changes Current Directory to new Directory which is already been made
#    print("Directory After changing : ", os.getcwd())
#    os.mkdir('dir_1') # NOTE :- To modefy files/directory in new one (here it's {D:/dir_2}), the code need to be written below 'os.chdir' function

# 7) print("The Sub directories/Files are:\n\n", os.listdir(os.getcwd()), "\n") # os.listdir(path) is used to show list of all sub-directories and files present is the path NOTE :- If no path is set, current directory is set by default

# 8) dir_lis = os.listdir('dir_1')
#    if len(dir_lis)==0 : # Required to check if the directory which is going to be removed, is empty
#        print("Directory is empty")
#  ***   os.rmdir('dir_1') # It removes ONLY an EMPTY directory from path specified
#        print("Directory is Removed")
#    else:
#        print("directory is not empty")
#        print("The directory contains:", os.listdir('dir_1'))

# 9) cwd = '/'
# ***   print(os.path.isdir(cwd)) # used to check whether the directory of given path exist
#    other = 'k:/'
#    print(os.path.isdir(other))

import os

# 10) print(os.path.getsize('C:/dell')) # Used to get size of a directory