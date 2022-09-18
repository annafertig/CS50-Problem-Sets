def main():
    x = input("What time is it? ")
    if 7.0 <= convert(x) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(x) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(x) <= 19.0:
        print("dinner time")

def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return float(hours + minutes)

main()