a = 0
b = 1

output = f"{a}, {b}"

for i in range(3, 11):
    a, b = b, a + b
    output += f", {b}"

print(output)
