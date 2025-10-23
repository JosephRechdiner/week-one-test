from game_logic import game 

if __name__ == "__main__":
    game_dict = game.init_game()
    for _ in range(26):
        game.play_round(game_dict["player1"], game_dict["player2"])

    if len(game_dict["player1"]["won_pile"]) > len(game_dict["player2"]["won_pile"]):
        print(f"{game_dict["player1"]["name"]} won the game! ")
    elif len(game_dict["player2"]["won_pile"]) > len(game_dict["player1"]["won_pile"]):
        print(f"{game_dict["player2"]["name"]} won the game! ")
    else:
        print("TIE, nobody won the game! ")






