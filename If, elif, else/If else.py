balance = int(input("Enter your balance: "))

if balance > 200:
    print("You are good to go!")
elif (balance < 150) and (balance > 100):
    print("You need to be aware while purchasing something")
else:
    print("You do not have enough")