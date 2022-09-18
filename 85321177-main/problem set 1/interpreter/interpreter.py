def main():
    exp = input("Expression: ")
    x = float(exp[0:exp.find(" ")])
    y = exp[exp.find(" ") + 1:exp.find(" ") + 2]
    z = float(exp[exp.find(" ") + 3:])
    print(math(x,y,z))

def math(x,y,z):
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    elif y == "/":
        return float(x/z)

main()