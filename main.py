import random
result = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

choices = ( "rock", "paper", "scissors" )

user_input = input("rock, paper, OR scissors: ")
cpu_input = random.choices(choices)

print("\nYOUR CHOICE: " + user_input)
print("\nYOUR OPPONENT'S CHOICE: " + cpu_input[0])

if (user_input == cpu_input[0]):
    print("RESULT: It's a Tie!")

