def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    x = 0

    #all plates must start with atleast two letters
    if plate[0:2].isalpha():
        x = x + 1
    else:
        return False

    #max 6 characters and min 2 characters
    if 2 <= len(plate) <= 6:
        x = x + 1
    else:
        return False

    #numbers must come at the end
    index = -1
    for i in range(len(plate)):
        if plate[i].isdigit():
            index = i
            break
    b = plate[index:]
    if index != -1:
        if b[0] == '0':
            return False
        for j in b:
            if not j.isdigit():
                return False

    #no periods, spaces, or punctuations marks allowed
    for i in plate:
        if i.isalpha() or i.isdigit():
            x = x + 1
        else:
            return False

    return True

main()