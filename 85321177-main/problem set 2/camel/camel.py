
def main():
    word = input("camelCase: ")
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(word)):
        for j in range(len(upper)):
            if word[i] == upper[j]:
                letter = word[i].lower()
                word = word[:i] + letter + word[i+1:]
                word = insert_dash(word,i)
    print("snake_case:", word)

def insert_dash(string,index):
    return string[:index] + "_" + string[index:]


main()
