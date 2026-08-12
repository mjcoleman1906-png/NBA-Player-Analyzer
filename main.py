#Michael Coleman
#AUG 5th


from players import players, nba_teams, nba_team_search

from team_stats import team_stats, team_stats_search



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
    