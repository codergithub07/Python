# a = 10
# for i in range(0,a): # In range function, end value is excluded
    # print("Hello World", i)




# Using for loop with list
unverified_users = ['kim', 'koi', 'kit', 'sam']
verified_users = []
while True:
    if len(unverified_users) > 0:
        new_user = unverified_users.pop()
        verified_users.append(new_user)
    else:
        break
for i in verified_users:
    print(i)