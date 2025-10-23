from utils import deck


def create_player(name="AI") -> dict:
    if not name:
        return {"name": "AI", "hand": [], "won_pile": []}
    
    return {"name": name, "hand": [], "won_pile": []}


def init_game() -> dict:
    player1 = create_player("Yossi")
    player2 = create_player("AI")
    deck = deck.create_deck()
    deck = deck.shuffle(deck)

    player1["hand"] = deck[:26]
    player2["hand"] = deck[26:]
    
    game_dict = {"deck": deck, "player1": player1, "player2": player2}
    return game_dict


def play_round(p1: dict, p2: dict):
    winner = deck.compare_cards(p1["hand"][0], p2["hand"][0])
    if winner == "p1":
        winner_hand = p1["hand"].pop(0)
        losser_hand = p2["hand"].pop(0)
        p1["won_pile"].append(winner_hand)
        p1["won_pile"].append(losser_hand)
    if winner == "p2":
        winner_hand = p1["hand"].pop(0)
        losser_hand = p2["hand"].pop(0)
        p2["won_pile"].append(winner_hand)
        p2["won_pile"].append(losser_hand)

    if winner == "WAR":
        print(winner)
        # BONUS
        # war_round(p1, p2)
    else:
        print(f"{winner} won the game! ")

temp_hands = []
def war_round(p1: dict, p2: dict):
    global temp_hand
    for _ in range(3):
        temp_hands.append(p1["hand"].pop(0))
        temp_hands.append(p2["hand"].pop(0))

    next_round_winner = play_round(p1, p2)
    if next_round_winner == "p1":
        for temp_hand in temp_hands:
            p1["won_pile"].append(temp_hand)

    elif next_round_winner == "p2":
        for temp_hand in temp_hands:
            p2["won_pile"].append(temp_hand)

    temp_hands = []




