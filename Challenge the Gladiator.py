# ARdC exercise: Challenge the Gladiator
import random

# Constants
ATTACK_RANGE = 2
X_ARENA = 5
Y_ARENA = 5


# 1. PLACE THE GLADIATOR IN THE ARENA

def place_gladiator():
    x_glad = random.random() * X_ARENA
    y_glad = random.random() * Y_ARENA
    attack = random.choice([True, False])  # Single random element from a sequence

    return {
        "X": x_glad,
        "Y": y_glad,
        "Attack": attack
    }


# 2. PLACE THE PLAYER IN THE ARENA

def call_input(dimension):
    while True:
        try:
            return float(input("Indicate your %s positioning in the arena: " % dimension))
        except ValueError:
            print("Something went wrong. Choose a number between 0 and 5.")


def place_player():
    print("The arena has a 5 x 5 meters area. You have to chose your position within these dimensions.")
    x_player = call_input("horizontal")
    while x_player < 0 or x_player > X_ARENA:
        x_player = call_input("horizontal")

    y_player = call_input("vertical")
    while y_player < 0 or y_player > Y_ARENA:
        y_player = call_input("vertical")

    return {
        "X": x_player,
        "Y": y_player
    }


# 3. CALCULATE THE DISTANCE BETWEEN THE GLADIATOR AND THE PLAYER

def dist_glad_to_player(x_glad, x_play, y_glad, y_play):
    return ((x_glad - x_play) ** 2 + (y_glad - y_play) ** 2) ** 0.5


# DRIVER CODE

# Statistics
plays_max = 10
plays_count = 0
players_dead = 0
players_survived = 0

while plays_count < plays_max:
    gladiator = place_gladiator()
    # print(gladiator)
    print("The Gladiator is ready!")
    player = place_player()
    # print(player)
    print("The player is ready at position %s x %s!" % (player["X"], player["Y"]))
    distance_to_glad = dist_glad_to_player(gladiator["X"], player["X"], gladiator["Y"], player["Y"])
    input("Fight!")
    if distance_to_glad > ATTACK_RANGE:
        print("The player has survived!")
        players_survived += 1
    elif distance_to_glad <= ATTACK_RANGE and gladiator["Attack"] == True:
        print("The Gladiator has eliminated the opponent!")
        players_dead += 1
    elif distance_to_glad <= ATTACK_RANGE and gladiator["Attack"] == False:
        print("The Gladiator was killed!")
        gladiator_dead = 1
        players_survived += 1
        plays_count += 1
        break
    plays_count += 1
    input("")

print("The battle in the Coliseum has ended!")
print("Victims: %s" % players_dead)
print("Survivors: %s" % players_survived)
print("Attempts to kill the Gladiator: %s" % plays_count)
