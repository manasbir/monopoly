import random

locations = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap"]
average_monopoly_game = 30

def roll_dice():
    x_die = random.randrange(6)
    y_die = random.randrange(6)
    return x_die + y_die


def move_players(players):
    new_locations = players
    player = 0
    while player < len(players):
        new_locations[player] += roll_dice()
        
        if new_locations[player] > 42:
            new_locations[player] -= 42

        player += 1
    return new_locations


def game(): 
    players = [0,0,0,0]
    for i in range(average_monopoly_game):
        players = move_players(players)
        print(players)


game()