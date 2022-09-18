def main():
    num = get_int()
    perc = round(num[0]/num[1] * 100)
    if perc <= 1:
        print('E')
    elif perc >= 99:
        print('F')
    else:
        print(str(perc)+'%')


def get_int():
    while True:
        try:
            x = input('Whats x ')
            x = x.split('/')
            x[0] = int(x[0])
            x[1] = int(x[1])
            if x[1] == 0 or x[0] > x[1]:
                pass
            else:
                return x
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()