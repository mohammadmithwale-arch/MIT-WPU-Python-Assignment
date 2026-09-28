import re

text = input("Enter: ")

result = re.fullmatch(r"[a-zA-Z0-9]+", text)

print("Input:", repr(text))
print("Result:", result)

if result:
    print("Valid")
else:
    print("Invalid")