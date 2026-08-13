# Michael Coleman
# August 8th

from analytics import player_rating, player_grade

def compare_stat(player1, player2, stat):

    if stat not in player1 or stat not in player2:
        raise ValueError(f"Stat '{stat}' not found in one of the players.")

    value1 = player1[stat]
    value2 = player2[stat]

    if value1 > value2:
        return player1

    elif value2 > value1:
        return player2

    else:
        return None

def compare_team_stat(team1, team2, stat, lower_is_better=False):

    if stat not in team1 or stat not in team2:
        raise ValueError(f"Stat '{stat}' not found in one of the teams.")

    value1 = team1[stat]
    value2 = team2[stat]

    if lower_is_better:
        if value1 < value2:
            return team1

        elif value2 < value1:
            return team2

        else:
            return None

    else:
        if value1 > value2:
            return team1

        elif value2 > value1:
            return team2

        else:
            return None