import random

def create_card(rank: str, suite: str) -> dict:
    special_ranks = {"J" : 11, 
                     "Q" : 12,
                     "K" : 13,
                     "A" : 14}
    
    if rank not in special_ranks:
        return {"rank": rank, "suite": suite, "value": int(rank)}
    
    return {"rank": rank, "suite": suite, "value": special_ranks[rank]}
    


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    
    return "WAR"

# print(compare_cards({"value": 14, "suite": "H", "rank": "A"}, {"value": 10, "suite": "H", "rank": "10"}))
# print(compare_cards({"value": 10, "suite": "H", "rank": "10"}, {"value": 14, "suite": "H", "rank": "A"}))
# print(compare_cards({"value": 10, "suite": "H", "rank": "10"}, {"value": 10, "suite": "H", "rank": "10"}))

def create_deck() -> list[dict]:
    special_ranks = {11 : "J", 
                     12: "Q",
                     13: "K",
                     14: "A"}
    cards = []

    for i in range(2, 15):
        for suite in ["H", "D", "C", "S"]:
            if i not in special_ranks:
                cur_card = create_card(str(i), suite)
            else:
                cur_card = create_card(special_ranks[i], suite)
            cards.append(cur_card)

    return cards

# print(len(create_deck()))
# print(create_deck()[0:4])

def shuffle(deck: list[dict]) -> list[dict]:
    for _ in range(1000):
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)

        if index1 == index2:
            continue

        deck[index1], deck[index2] = deck[index2], deck[index1]

    return deck

# d = create_deck()
# d = shuffle(d)
# print(len(d))
# print(d)