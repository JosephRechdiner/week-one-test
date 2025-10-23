
from utils import deck


def create_player(name="AI") -> dict:
    if not name:
        return {"name": "AI", "hand": [], "won_pile": []}
    
    return {"name": name, "hand": [], "won_pile": []}


def init_game() -> dict:
    player1 = create_player("Yossi")
    player2 = create_player("AI")
    deck = deck.create_deck()
    deck = deck.shuffle()

    player1["hand"] = deck[:26]
    player2["hand"] = deck[26:]

    game_dict = {"deck": deck, "player1": player1, "player2": player2}
    return game_dict


def play_round(p1: dict, p2: dict):
    if p1["hand"][0]["value"] > p2["hand"][0]["value"]:
        messege = p1["name"] + "won the round"
        winner_hand = p1["hand"].pop(0)
        losser_hand = p2["hand"].pop(0)
        p1["won_pile"].append(winner_hand)
        p1["won_pile"].append(losser_hand)

    elif p2["hand"][0]["value"] > p1["hand"][0]["value"]:
        messege = p2["name"] + "won the round" 
        winner_hand = p2["hand"].pop(0)
        losser_hand = p1["hand"].pop(0)
        p2["won_pile"].append(winner_hand)
        p2["won_pile"].append(losser_hand)

    else:
        messege = "TIE"

    print(messege)

