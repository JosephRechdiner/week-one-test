from game_logic import game 

def find_winner_if_tie(p1: dict, p2: dict):
    if find_heart_count(p1) > find_heart_count(p2):
        print(f"{game_dict["player1"]["name"]} won the game! ")
    elif find_heart_count(p2) > find_heart_count(p1):
        print(f"{game_dict["player2"]["name"]} won the game! ")


def find_heart_count(player: dict):
    hearts_count = 0 
    for card in player["hand"]:
        if card["rand"] == "H":
            hearts_count += 1
    return hearts_count

if __name__ == "__main__":
    game_dict = game.init_game()
    while len(game_dict["player1"]["hand"]) > 0 and len(game_dict["player2"]["hand"]) > 0:
        game.play_round(game_dict["player1"], game_dict["player2"])

    if len(game_dict["player1"]["won_pile"]) > len(game_dict["player2"]["won_pile"]):
        print(f"{game_dict["player1"]["name"]} won the game! ")
    elif len(game_dict["player2"]["won_pile"]) > len(game_dict["player1"]["won_pile"]):
        print(f"{game_dict["player2"]["name"]} won the game! ")
    else:
        # BONUS
        # find_winner_if_tie(game_dict["player1"], game_dict["player2"])
        print("TIE, nobody won the game! ")













