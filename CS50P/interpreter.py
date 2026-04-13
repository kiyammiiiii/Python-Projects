expression = input("Expression:").strip()

x,y,z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z
else:
    print("Invalid Expression")

print(float(answer))


