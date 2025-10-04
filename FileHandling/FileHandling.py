# Syntax
# file_object = open("filename", "mode")

# Reading file Content and closeing it
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()

# File Object Methods

# read(size) -> Reads size characters (or whole file if size not given)
file = open("test.txt", "r")
content = file.read(10)  # It reads first 10 character i.e 0-9
print(content)
file.close()

# readline() -> Reads the next line
# It reads first lines only
file = open("test.txt", "r")
content = file.readline()
print(content)
file.close()

# It reads whole line through looping
file = open("test.txt", "r")
while True:
    content = file.readline()
    print(content, end="")

    if content == "":
        break
file.close()

print()

# It count total number of line that file and print last line only
file = open("test.txt", "r")
count = 0
content2 = ""
while True:
    content1 = file.readline()
    if content1 != "":
        count = count + 1
        content2 = content1
    else:
        print(f"Total number of line is {count}")
        print(f"Last line content: {content2}")
        break
file.close()

# readlines() ->	Reads all lines and returns a list
file = open("test.txt", "r")
content = file.readlines()
print(content)
file.close()

# Print one by one using readlines
file = open("test.txt", "r")
content = file.readlines()
for i in content:
    print(i, end="")
print()
file.close()

# count and print second last line only using readlines
file = open("test.txt", "r")
content = file.readlines()
lines = len(content)
print(f"Total Number of line: {lines}")
print(content[lines - 2])
file.close()

# write(str) -> Writes string to file
file = open("test.txt", "w")
content = "I am new here"
file.write(content)
file.close()

# writelines(list) -> Writes list of strings to file
file = open("test.txt", "w")
content = ["I am one\n", "I am Two\n", "I am Three\n", "I am Four\n", "I am Five\n"]
file.writelines(content)
file.close()

