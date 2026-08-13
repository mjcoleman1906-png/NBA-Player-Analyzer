#Michael Coleman
#AUG 5th


from players import players, nba_teams, nba_team_search

from team_stats import team_stats, team_stats_search

from comparison import compare_stat, compare_team_stat

from analytics import analyze_player, player_rating, player_grade, offense_grade, defense_grade, ast_to_grade, rebound_grade, turnover_grade

from search import find_player

from rankings import ranked_players

from team_analyzer import team_average, team_leader, best_rated_player

team_name = input("\nEnter a team to analyze: ").strip().lower()

if team_name in nba_team_search:
    team_players = nba_team_search[team_name]
    official_team_name = team_stats_search[team_name]
    stats = team_stats[official_team_name]

    leader = team_leader(team_players, "points")
    leading_passer = team_leader(team_players, "assists")
    leading_rebounder = team_leader(team_players, "rebounds")
    leading_turnover = team_leader(team_players, "turnovers")
    leading_three = team_leader(team_players, "three_pct")
    leading_steals = team_leader(team_players, "steals")
    leading_blocks = team_leader(team_players, "blocks")
    best_player, best_rating = best_rated_player(team_players)



    print("\n" + "=" * 50)
    print(f"{team_name.title()} TEAM REPORT")
    print("=" * 50)

    print(f" Offense Grade: {offense_grade(stats['offensive_rating'])}")
    print(f" Defense Grade: {defense_grade(stats['defensive_rating'])}")
    print()
    print(f" Assists to Turnover Ratio: {stats['ast_to_ratio']:.2f}")
    print(f" Assists to Turnover Ratio Grade: {ast_to_grade(stats['ast_to_ratio'])}")
    print()
    print(f" Rebound Percentage: {stats['rebound_pct']:.2f}%")
    print(f" Rebounding Grade: {rebound_grade(stats['rebound_pct'])}")
    print()
    print(f" Turnover Percentage: {stats['turnover_pct']:.2f}%")
    print(f" Turnover Grade: {turnover_grade(stats['turnover_pct'])}")
    print()
    print()

    print(f"Scoring leader: {leader['name']}")
    print(f"Points: {leader['points']}")
    print()
    print(f"Leading passer: {leading_passer['name']}")
    print(f"Assists: {leading_passer['assists']}")
    print()
    print(f"Leading rebounder: {leading_rebounder['name']}")
    print(f"Rebounds: {leading_rebounder['rebounds']}")
    print()
    print(f"Leading turnover: {leading_turnover['name']}")
    print(f"Turnovers: {leading_turnover['turnovers']}")
    print()
    print(f"Leading three-point shooter: {leading_three['name']}")
    print(f"Three-point percentage: {leading_three['three_pct']}%")
    print()
    print(f"Leading steals: {leading_steals['name']}")
    print(f"Steals: {leading_steals['steals']}")
    print()
    print(f"Leading blocks: {leading_blocks['name']}")
    print(f"Blocks: {leading_blocks['blocks']}")
    print()
    print(f"Best rated player: {best_player['name']}")
    print(f"Rating: {best_rating:.2f}")

else:
    print("Team not found.")

player1_name = input("Enter first player: ").strip()
player2_name = input("Enter second player: ").strip()

player1 = find_player(players, player1_name)
player2 = find_player(players, player2_name)
if player1 is not None and player2 is not None:

    comparison_stats = [
        "points",
        "assists",
        "rebounds",
        "fg_pct",
        "three_pct",
        "steals",
        "blocks"
    ]

    player1_wins = 0
    player2_wins = 0

    for stat in comparison_stats:

        winner = compare_stat(player1, player2, stat)

        print()
        print(stat.upper())

        print(f"{player1['name']}: {player1[stat]}")
        print(f"{player2['name']}: {player2[stat]}")

        if winner == player1:
            print(f"Advantage: {player1['name']}")
            player1_wins += 1

        elif winner == player2:
            print(f"Advantage: {player2['name']}")
            player2_wins += 1

        else:
            print("Advantage: Tie")


    print()
    print("=" * 50)
    print("Player Comparison Summary")
    print("=" * 50)

    print(f"{player1['name']}: {player1_wins} categories")
    print(f"{player2['name']}: {player2_wins} categories")

    if player1_wins > player2_wins:
        print(f"Overall Winner: {player1['name']}")

    elif player2_wins > player1_wins:
        print(f"Overall Winner: {player2['name']}")

    else:
        print("Overall Result: Tie")


else:
    print("One or both players were not found.")

team1_name = input("Enter first team: ").strip().lower()
team2_name = input("Enter second team: ").strip().lower()


if team1_name in team_stats_search and team2_name in team_stats_search:

    official_team1 = team_stats_search[team1_name]
    official_team2 = team_stats_search[team2_name]

    team1 = team_stats[official_team1]
    team2 = team_stats[official_team2]

    team_comparison_stats = [
    "points_per_game",
    "offensive_rating",
    "fg_pct",
    "three_pct",
    "rebounds_per_game",
    "assists_per_game",
    "steals_per_game",
    "blocks_per_game"
    ]
    lower_stats = [
    "opponent_points_per_game",
    "defensive_rating",
    "turnover_pct"
    ]
    team1_wins = 0
    team2_wins = 0
for stat in team_comparison_stats:

    winner = compare_team_stat(team1, team2, stat)

    for stat in team_comparison_stats:

        winner = compare_team_stat(team1, team2, stat)

    print()
    print(stat.replace("_", " ").title())

    print(f"{official_team1}: {team1[stat]}")
    print(f"{official_team2}: {team2[stat]}")

    if winner == team1:
        print(f"Advantage: {official_team1}")
        team1_wins += 1

    elif winner == team2:
        print(f"Advantage: {official_team2}")
        team2_wins += 1

    else:
        print("Advantage: Tie")


for stat in lower_stats:

    winner = compare_team_stat(
        team1,
        team2,
        stat,
        lower_is_better=True
    )

    print()
    print(stat.replace("_", " ").title())

    print(f"{official_team1}: {team1[stat]}")
    print(f"{official_team2}: {team2[stat]}")

    if winner == team1:
        print(f"Advantage: {official_team1}")
        team1_wins += 1

    elif winner == team2:
        print(f"Advantage: {official_team2}")
        team2_wins += 1

    else:
        print("Advantage: Tie")
print("-" * 40)
print()
print("=" * 50)
print("TEAM COMPARISON SUMMARY")
print("=" * 50)

print(f"{official_team1}: {team1_wins} categories")
print(f"{official_team2}: {team2_wins} categories")

if team1_wins > team2_wins:
        print(f"Statistical Edge: {official_team1}")

elif team2_wins > team1_wins:
        print(f"Statistical Edge: {official_team2}")

else:
        print("Statistical Edge: Tie")




# search_name = input("\nEnter the player you want to search for: ").strip()

# found_player = find_player(players, search_name)

# PLAYER REPORT SECTION (COMMENTED OUT)
# if found_player is not None:
#     rating, grade = analyze_player(found_player)

#     print("\n" + "=" * 50)
#     print("PLAYER REPORT")
#     print("=" * 50)

#     print(f"Name: {found_player['name']}")
#     print(f"Team: {found_player['team']}")
#     print(f"Points: {found_player['points']}")
#     print(f"Assists: {found_player['assists']}")
#     print(f"Rebounds: {found_player['rebounds']}")
#     print(f"Turnovers: {found_player['turnovers']}")
#     print(f"FG%: {found_player['fg_pct']}%")
#     print(f"3PT%: {found_player['three_pct']}%")
#     print(f"FT%: {found_player['ft_pct']}%")
#     print(f"Steals: {found_player['steals']}")
#     print(f"Blocks: {found_player['blocks']}")
#     print(f"Rating: {rating:.2f}")
#     print(f"Grade: {grade}")

# else:
#     print("Player not found.")

# PLAYER RATINGS AND GRADES SECTION (COMMENTED OUT)
# print("=" * 85)
# print("Player Ratings and Grades:")
# print("=" * 85)

# print(
#     f"{'Rank':<6}"
#     f"{'Player':<22}"
#     f"{'Team':<22}"
#     f"{'Rating':<10}"
#     f"{'Grade':<30}"
# )

# for i, player in enumerate(ranked_players, start=1):
#     print(
#         f"{i:<6}"
#         f"{player['player']:<22}"
#         f"{player['team']:<22}"
#         f"{player['rating']:<10.2f}"
#         f"{player['grade']:<30}"
#     )
    