# Michael Coleman
# August 5th


def find_player(players, search_name):
    for player in players:
        if player["name"].lower() == search_name.lower():
            return player

    return None

