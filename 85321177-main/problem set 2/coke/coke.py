
def main():
    amt_due = 50
    while amt_due > 0:
        print("Amount Due:", amt_due)
        ins = int(input("Insert Coin: "))
        if ins == 25 or ins == 10 or ins == 5:
            amt_due = amt_due - ins
    print("Change Owed:", abs(amt_due))

main()