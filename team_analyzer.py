# Michael Coleman
# August 5th

from analytics import analyze_player

def team_average(team_players, stat):

    total = 0

    for player in team_players:
        total += player[stat]

    average = total / len(team_players)

    return average


def team_leader(team_players, stat):

    leader = max(
        team_players,
        key=lambda player: player[stat]
    )

    return leader



def best_rated_player(team_players):

    best_player = None
    best_rating = -1

    for player in team_players:
        rating, grade = analyze_player(player)

        if rating > best_rating:
            best_rating = rating
            best_player = player

    return best_player, best_rating