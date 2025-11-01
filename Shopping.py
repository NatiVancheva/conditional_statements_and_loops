budget = int(input())
command = input()
while command != "End":
    price = int(input())
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")

