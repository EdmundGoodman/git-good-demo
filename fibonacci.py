import sys

a = 0
b = 1

print("Garden tiger moth")

output = f"{a}, {b}"

try:
    terms = int(sys.argv[1])
except:
    print("That isn't a number! Defaulting to 10 terms")
    terms = 10

for i in range(3, terms + 1):
    a, b = b, a + b
    output += f", {b}"

print(f"The first fibonacci numbers are: {output}")

