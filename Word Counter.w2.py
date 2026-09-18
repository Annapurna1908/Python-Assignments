# Word Counter from Text File

filename = "sample.txt"

with open(filename, "r") as file:
    text = file.read()

words = text.split()
lines = text.splitlines()
characters = len(text)

print("===== WORD COUNTER =====")
print("Number of words:", len(words))
print("Number of lines:", len(lines))
print("Number of characters:", characters)