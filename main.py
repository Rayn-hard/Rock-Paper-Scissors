import random

choices = ( "rock", "paper", "scissors" )


user_input = input("ENTER YOUR CHOICE [1]rock, [2]paper, OR [3]scissors: ")
cpu_input = random.choices(choices)

print("\nYOUR CHOICE: " + user_input)
print("YOUR OPPONENT'S CHOICE: " + cpu_input[0])

if (user_input == cpu_input[0]):
    print("\nRESULT: It's a Tie!")
elif (user_input == "rock"):
    if (cpu_input == "paper"):
        print("\nRESULT: CPU WON!")
    else:
        print("\nRESULT YOU WON!")
elif (user_input == "paper"):
    if (cpu_input == "scissors"):
        print("\nRESULT: CPU WON!")
    else:
        print("\nRESULT YOU WON!")
elif (user_input == "scissors"):
    if (cpu_input == "rock"):
        print("\nRESULT: CPU WON!")
    else:
        print("\nRESULT YOU WON!")
else:
    print("\nTRY AGAIN!")