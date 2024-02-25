 'test.txt'
try:
    with open(file) as f:
        content = f.readlines()
except FileNotFoundError:
    print("We can't find the file")
else:
    string = ''
    for line in content:
        string += line.rstrip()
        string += ' '
    print(string.split())
    print(len(string.split()))
