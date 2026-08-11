# Michael Coleman
# August 5th

from players import players
from analytics import analyze_player

player_results = []

for player in players:
    rating, grade = analyze_player(player)
    player_results.append({
        "player": player["name"],
        "team": player["team"],
        "rating": rating,
        "grade": grade
    })
ranked_players = sorted(
    player_results,
    key=lambda x: x["rating"],
    reverse=True
)