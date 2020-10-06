
# Activity 1
strings = input("Enter the strings! ").split()
for i in range(len(strings)):
    string_holder = strings[i]
    if string_holder[-1:] == string_holder[:1]:
        if len(string_holder) >= 2:
            print(string_holder)

# Activity 2
listylist = input("Enter numbers! ").split()
for i in range(len(listylist)):
    listylist[i] = int(listylist[i])
user_value = int(input("Enter the value! "))
for i in range(len(listylist)):
    if listylist[i] < user_value:
        print(listylist[i], " ", end="")

# Activity 3
