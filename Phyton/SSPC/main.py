import random

print("Deine Auswahl:")
print("1: Stein")
print("2: Schere")
print("3: Papier")

playerChoice = input()

choices = ["Stein", "Schere", "Papier"]
aiChoice = random.choice(choices)

if playerChoice == aiChoice:
    print("unentschieden")
elif playerChoice == "Stein" and aiChoice == "Schere" or playerChoice == "Schere" and aiChoice == "Papier" or playerChoice == "Papier" and aiChoice == "Stein":
    print("Du hast Gewonnen")
elif playerChoice == "Stein" and aiChoice == "Papier" or playerChoice == "Schere" and aiChoice == "Stein" or playerChoice == "Papier" and aiChoice == "Schere":
    print("Du hast Verloren")

print( playerChoice +  " " + aiChoice)
