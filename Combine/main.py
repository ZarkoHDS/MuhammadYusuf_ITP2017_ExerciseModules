import Combine.Jumbled as Jumble
import Combine.Bank as Bank

print("1. Jumble")
print("2. Bank")

while True:
    choice = int(input("Choose the program : "))

    if choice == 1:
        Jumble.jumble()
        break
    elif choice == 2:
        Bank.bank()
        break
