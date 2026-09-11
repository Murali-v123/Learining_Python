a = 3
b = "3"
c = 3
print(a == b)
print(a == c)  # check only value
print(a is b)  # checks location of an obj in memory
print(a is c)

d = [1, 2, 3, 4, 5]
e = [1, 2, 3, 4, 5]

print(d == e)
print(d is e)

# snake water gun game

import random as r

option = ["stone", "paper", "scissors"]
r_matrix = [["Draw", "Lose", "Win"], ["Win", "Draw", "Lose"], ["Lose", "Win", "Draw"]]
point = 0
while True:
    player_input = input("Enter your choice: stone,paper,scissors?: ").lower()
    if player_input not in option:
        print("Invalid choice. Exiting the game....")
        break
    else:
        machine_choice = r.choice(option)
        print("Machine Choice :", machine_choice)
        p_index = option.index(player_input)

        m_index = option.index(machine_choice)

        result = r_matrix[p_index][m_index]
        print(f"Result>> {result}")

        if result == "Win":
            point += 1
            print(f"Point: {point}")
        elif result == "Draw":
            print("Point:", point)
        elif result == "Lose":
            if point > 0:
                point -= 1
                print(f"Point: {point}")
            else:
                print(f"Point: {point}")
        new = input("You Still Wants to Play This Game(yes or no): ").lower()
        if new != "yes":
            print("Thanks for playing this game . Exiting the game...")
            break
