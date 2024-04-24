exp = input("Expression: ").strip()
x, y, z = exp.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float((x + z)))
elif y == "-":
    print(float((x - z)))
elif y == "*":
    print(float((x * z)))
else:
    print(float((x / z)))





