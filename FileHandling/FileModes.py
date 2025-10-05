# w	(Write) -> Creates a new file or overwrites existing file.
file = open("Modestest.txt", "w")
content = "I am new here"
file.write(content)
file.close()

# r (Read (default)) -> Opens file for reading. Error if file doesn’t exist.
file = open("Modestest.txt", "r")
content = file.read()
print(content)
file.close()

# r -> (Read & Write) File must exist; pointer at beginning.
file = open("Modestest.txt", "r+")
wcontent = "I am newly added here"
file.write(wcontent)
file.close()

file = open("Modestest.txt", "r+")
content = file.read()
print(content)
file.close()

# w+ -> (Write & Read) Creates file or overwrites existing file.
file = open("Modestest.txt", "w+")
wcontent = "I am also newly added here"
file.write(wcontent)
file.close()

file = open("Modestest.txt", "w+")
content = file.read()
print(content)
file.close()

# a+ -> (Append & Read) Creates file if not exist; pointer at end.
file = open("Modestest.txt", "a+")
wcontent = "I am also newly appened here"
file.write(wcontent)
rcontent = file.read()
print(rcontent)
file.close()


