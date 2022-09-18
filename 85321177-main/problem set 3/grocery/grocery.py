def main():
    list = []
    while True:
        try:
            item = input().upper()
            list.append(item)
        except EOFError:
            break
    my_dict = frequency(sorted(list))
    for i in my_dict:
        print(my_dict[i],i)

def frequency(my_list):
    dict = {}
    for item in my_list:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    return dict

main()