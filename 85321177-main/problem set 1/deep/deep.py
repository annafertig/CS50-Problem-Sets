def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.lower().strip()
    if is_42(answer):
        print("Yes")
    else:
        print("No")

def is_42(x):
    if x == "42" or x == "forty-two" or x == "forty two":
        return True
    else:
        return False

main()