#Michael Coleman
#AUG 5th


from players import players

from analytics import analyze_player

from search import find_player

from rankings import ranked_players


search_name = input("\nEnter the player you want to search for: ").strip()

found_player = find_player(players, search_name)

if found_player is not None:
    rating, grade = analyze_player(found_player)

    print("\n" + "=" * 50)
    print("PLAYER REPORT")
    print("=" * 50)

    print(f"Name: {found_player['name']}")
    print(f"Team: {found_player['team']}")
    print(f"Points: {found_player['points']}")
    print(f"Assists: {found_player['assists']}")
    print(f"Rebounds: {found_player['rebounds']}")
    print(f"Turnovers: {found_player['turnovers']}")
    print(f"FG%: {found_player['fg_pct']}%")
    print(f"3PT%: {found_player['three_pct']}%")
    print(f"FT%: {found_player['ft_pct']}%")
    print(f"Steals: {found_player['steals']}")
    print(f"Blocks: {found_player['blocks']}")
    print(f"Rating: {rating:.2f}")
    print(f"Grade: {grade}")

else:
    print("Player not found.")

print("=" * 85)
print("Player Ratings and Grades:")
print("=" * 85)

print(
    f"{'Rank':<6}"
    f"{'Player':<22}"
    f"{'Team':<22}"
    f"{'Rating':<10}"
    f"{'Grade':<30}"
)

for i, player in enumerate(ranked_players, start=1):
    print(
        f"{i:<6}"
        f"{player['player']:<22}"
        f"{player['team']:<22}"
        f"{player['rating']:<10.2f}"
        f"{player['grade']:<30}"
    )
    