# Python code to create a file
file = open('write.txt', 'w')
file.write("This is the write command.\n")
file.write("It allows us to write in a particular file")
file.close()

# Python code to illustrate append() mode
file = open('write.txt', 'a')
file.write("\nThis will add this line.\n")
file.close()

# Python code to illustrate with()
with open("write.txt", "r") as file:
    data = file.read()
    print(data)

# Python code to illustrate with() along with write()
with open("write.txt", "w") as f:
    f.write("Hello Aliens!!!")

# Python code to illustrate with()
with open("write.txt", "r") as file:
    data = file.read()
    print(data)

# Python code to illustrate split() function
with open("write.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)