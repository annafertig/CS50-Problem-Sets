def main():
    sentence = input()
    print(convert(sentence))
def convert(x):
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x
main()