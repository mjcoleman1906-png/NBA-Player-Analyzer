#Michael Coleman
#AUG 5th

def player_rating(
    points,
    assists,
    rebounds,
    turnovers,
    field_goal_pct,
    three_point_pct,
    steals_per_game,
    blocks_per_game,
    free_throw_percentage
):
    rating = (
        points * 0.5 +
        assists * 0.4 +
        rebounds * 0.2 -
        turnovers * 0.3 +
        field_goal_pct * 0.3 + 
        three_point_pct * 0.2 +
        steals_per_game * 0.2 +
        blocks_per_game * 0.2 +
        free_throw_percentage * 0.1
    )
    return rating

def player_grade(rating):
    if rating >= 48:
            return "A+ -- MVP Level Production"
    elif rating >= 45:
            return "A -- All-NBA Level Production"
    elif rating >= 40:
            return "A- -- All-Star Level Production"
    elif rating >= 36:
            return "B+ -- Very Good Starter"
    elif rating >= 32:
            return "B -- Good Starter"
    elif rating >= 25:
            return "C -- Average Starter"
    elif rating >= 20:
            return "D -- Below Average Production"
    else:
            return "F -- Very Low Production"

def analyze_player(player):
    rating = player_rating(
        player["points"],
        player["assists"],
        player["rebounds"],
        player["turnovers"],
        player["fg_pct"],
        player["three_pct"],
        player["steals"],
        player["blocks"],
        player["ft_pct"]
    )

    grade = player_grade(rating)

    return rating, grade

def find_player(players, search_name):
    for player in players:
        if player["name"].lower() == search_name.lower():
            return player

    return None

lakers_players = [
           {
               "name": "LeBron James",
               "team": "Los Angeles Lakers",
               "points": 23.2,
               "assists": 7.3,
               "rebounds": 6.7,
               "turnovers": 3.8,
               "fg_pct": 45.9,
               "three_pct": 32.7,
               "ft_pct": 74.6,
               "steals": 1.3,
               "blocks": 0.3
           },
           {
               "name": "Austin Reaves",
               "team": "Los Angeles Lakers",
               "points": 20.0,
               "assists": 5.8,
               "rebounds": 4.0,
               "turnovers": 4.5,
               "fg_pct": 40.7,
               "three_pct": 25.7,
               "ft_pct": 86.0,
               "steals": 0.0,
               "blocks": 1.2
           },
           {
               "name": "Rui Hachimura",
               "team": "Los Angeles Lakers",
               "points": 17.5,
               "assists": 1.7,
               "rebounds": 4.0,
               "turnovers": 0.9,
               "fg_pct": 54.9,
               "three_pct": 56.9,
               "ft_pct": 72.7,
               "steals": 0.9,
               "blocks": 0.6
           },
           {
               "name": "Marcus Smart",
               "team": "Los Angeles Lakers",
               "points": 12.9,
               "assists": 5.1,
               "rebounds": 3.5,
               "turnovers": 3.5,
               "fg_pct": 39.4,
               "three_pct": 34.0,
               "ft_pct": 79.1,
               "steals": 2.4,
               "blocks": 1.0
           },
           {
               "name": "Luke Kennard",
               "team": "Los Angeles Lakers",
               "points": 11.5,
               "assists": 2.3,
               "rebounds": 3.5,
               "turnovers": 1.4,
               "fg_pct": 48.8,
               "three_pct": 47.4,
               "ft_pct": 82.6,
               "steals": 0.9,
               "blocks": 0.1
           },
           {
               "name": "Deandre Ayton",
               "team": "Los Angeles Lakers",
               "points": 10.0,
               "assists": 0.9,
               "rebounds": 9.6,
               "turnovers": 1.3,
               "fg_pct": 54.8,
               "three_pct": 0.0,
               "ft_pct": 61.5,
               "steals": 0.2,
               "blocks": 0.8
           },
           {
               "name": "Jaxson Hayes",
               "team": "Los Angeles Lakers",
               "points": 5.7,
               "assists": 0.7,
               "rebounds": 3.2,
               "turnovers": 1.0,
               "fg_pct": 67.9,
               "three_pct": 0.0,
               "ft_pct": 70.4,
               "steals": 0.3,
               "blocks": 0.8
           },
           {
               "name": "Jake LaRavia",
               "team": "Los Angeles Lakers",
               "points": 3.3,
               "assists": 0.8,
               "rebounds": 2.1,
               "turnovers": 1.4,
               "fg_pct": 33.3,
               "three_pct": 28.6,
               "ft_pct": 100.0,
               "steals": 0.5,
               "blocks": 0.8
           },
           {
               "name": "Jarred Vanderbilt",
               "team": "Los Angeles Lakers",
               "points": 2.9,
               "assists": 0.3,
               "rebounds": 3.4,
               "turnovers": 0.1,
               "fg_pct": 40.9,
               "three_pct": 11.1,
               "ft_pct": 33.3,
               "steals": 0.3,
               "blocks": 0.0
           },
           {
               "name": "Nick Smith Jr.",
               "team": "Los Angeles Lakers",
               "points": 2.7,
               "assists": 0.2,
               "rebounds": 0.2,
               "turnovers": 0.2,
               "fg_pct": 42.9,
               "three_pct": 42.9,
               "ft_pct": 50.0,
               "steals": 0.2,
               "blocks": 0.2
           },
           {
               "name": "Dalton Knecht",
               "team": "Los Angeles Lakers",
               "points": 2.0,
               "assists": 0.6,
               "rebounds": 1.2,
               "turnovers": 0.2,
               "fg_pct": 37.5,
               "three_pct": 40.0,
               "ft_pct": 100.0,
               "steals": 0.0,
               "blocks": 0.0
           },
           {
               "name": "Adou Thiero",
               "team": "Los Angeles Lakers",
               "points": 1.5,
               "assists": 0.2,
               "rebounds": 2.0,
               "turnovers": 0.7,
               "fg_pct": 50.0,
               "three_pct": 0.0,
               "ft_pct": 50.0,
               "steals": 0.0,
               "blocks": 0.0
           },
           {
               "name": "Bronny James",
               "team": "Los Angeles Lakers",
               "points": 1.5,
               "assists": 0.9,
               "rebounds": 0.4,
               "turnovers": 0.5,
               "fg_pct": 50.0,
               "three_pct": 33.3,
               "ft_pct": 0.0,
               "steals": 0.1,
               "blocks": 0.0
           },
           {
               "name": "Maxi Kleber",
               "team": "Los Angeles Lakers",
               "points": 0.3,
               "assists": 1.0,
               "rebounds": 0.7,
               "turnovers": 0.7,
               "fg_pct": 0.0,
               "three_pct": 0.0,
               "ft_pct": 50.0,
               "steals": 0.3,
               "blocks": 0.0
           },
]
cavs_players = [
    {
        "name": "Donovan Mitchell",
        "team": "Cleveland Cavaliers",
        "points": 26.0,
        "assists": 3.1,
        "rebounds": 4.8,
        "turnovers": 2.6,
        "fg_pct": 45.1,
        "three_pct": 32.7,
        "ft_pct": 81.5,
        "steals": 1.2,
        "blocks": 0.3
    },
    {
        "name": "James Harden",
        "team": "Cleveland Cavaliers",
        "points": 19.2,
        "assists": 5.5,
        "rebounds": 5.1,
        "turnovers": 4.7,
        "fg_pct": 41.0,
        "three_pct": 29.9,
        "ft_pct": 83.1,
        "steals": 1.7,
        "blocks": 0.7
    },
    {
        "name": "Evan Mobley",
        "team": "Cleveland Cavaliers",
        "points": 17.0,
        "assists": 3.9,
        "rebounds": 8.1,
        "turnovers": 2.3,
        "fg_pct": 53.5,
        "three_pct": 33.8,
        "ft_pct": 62.1,
        "steals": 0.9,
        "blocks": 1.8
    },
    {
        "name": "Jarrett Allen",
        "team": "Cleveland Cavaliers",
        "points": 12.7,
        "assists": 1.1,
        "rebounds": 7.2,
        "turnovers": 0.9,
        "fg_pct": 63.5,
        "three_pct": 0.0,
        "ft_pct": 57.9,
        "steals": 1.0,
        "blocks": 1.7
    },
    {
        "name": "Max Strus",
        "team": "Cleveland Cavaliers",
        "points": 9.6,
        "assists": 2.1,
        "rebounds": 4.8,
        "turnovers": 1.3,
        "fg_pct": 40.6,
        "three_pct": 35.8,
        "ft_pct": 91.7,
        "steals": 0.8,
        "blocks": 0.2
    },
    {
        "name": "Sam Merrill",
        "team": "Cleveland Cavaliers",
        "points": 7.8,
        "assists": 1.1,
        "rebounds": 1.2,
        "turnovers": 0.5,
        "fg_pct": 42.7,
        "three_pct": 37.2,
        "ft_pct": 84.0,
        "steals": 0.5,
        "blocks": 0.0
    },
    {
        "name": "Dennis Schroder",
        "team": "Cleveland Cavaliers",
        "points": 5.5,
        "assists": 2.4,
        "rebounds": 1.5,
        "turnovers": 1.4,
        "fg_pct": 38.1,
        "three_pct": 33.3,
        "ft_pct": 79.2,
        "steals": 0.4,
        "blocks": 0.2
    },
    {
        "name": "Dean Wade",
        "team": "Cleveland Cavaliers",
        "points": 4.4,
        "assists": 0.8,
        "rebounds": 3.9,
        "turnovers": 0.6,
        "fg_pct": 46.2,
        "three_pct": 37.5,
        "ft_pct": 33.3,
        "steals": 0.7,
        "blocks": 0.1
    },
    {
        "name": "Jaylon Tyson",
        "team": "Cleveland Cavaliers",
        "points": 4.1,
        "assists": 1.3,
        "rebounds": 2.8,
        "turnovers": 0.6,
        "fg_pct": 36.2,
        "three_pct": 23.7,
        "ft_pct": 66.7,
        "steals": 0.2,
        "blocks": 0.1
    },
    {
        "name": "Thomas Bryant",
        "team": "Cleveland Cavaliers",
        "points": 1.9,
        "assists": 0.2,
        "rebounds": 1.2,
        "turnovers": 0.2,
        "fg_pct": 28.6,
        "three_pct": 16.7,
        "ft_pct": 100.0,
        "steals": 0.2,
        "blocks": 0.1
    },
    {
        "name": "Keon Ellis",
        "team": "Cleveland Cavaliers",
        "points": 1.6,
        "assists": 0.3,
        "rebounds": 1.2,
        "turnovers": 0.5,
        "fg_pct": 33.3,
        "three_pct": 35.7,
        "ft_pct": 80.0,
        "steals": 0.6,
        "blocks": 0.1
    },
    {
        "name": "Nae'Qwan Tomlin",
        "team": "Cleveland Cavaliers",
        "points": 1.3,
        "assists": 0.3,
        "rebounds": 0.7,
        "turnovers": 0.1,
        "fg_pct": 66.7,
        "three_pct": 0.0,
        "ft_pct": 50.0,
        "steals": 0.1,
        "blocks": 0.0
    },
    {
        "name": "Tyrese Proctor",
        "team": "Cleveland Cavaliers",
        "points": 0.5,
        "assists": 0.5,
        "rebounds": 0.3,
        "turnovers": 0.5,
        "fg_pct": 0.0,
        "three_pct": 0.0,
        "ft_pct": 100.0,
        "steals": 0.0,
        "blocks": 0.0
    },
    {
        "name": "Craig Porter Jr.",
        "team": "Cleveland Cavaliers",
        "points": 0.3,
        "assists": 0.6,
        "rebounds": 0.4,
        "turnovers": 0.6,
        "fg_pct": 33.3,
        "three_pct": 0.0,
        "ft_pct": 0.0,
        "steals": 0.0,
        "blocks": 0.0
    },
    {
        "name": "Larry Nance Jr.",
        "team": "Cleveland Cavaliers",
        "points": 0.0,
        "assists": 0.0,
        "rebounds": 0.0,
        "turnovers": 0.5,
        "fg_pct": 0.0,
        "three_pct": 0.0,
        "ft_pct": 0.0,
        "steals": 0.0,
        "blocks": 0.0
    }
]
pistons_players = [
    {
        "name": "Cade Cunningham",
        "team": "Detroit Pistons",
        "points": 28.1,
        "assists": 7.5,
        "rebounds": 5.1,
        "turnovers": 5.6,
        "fg_pct": 43.2,
        "three_pct": 40.2,
        "ft_pct": 86.1,
        "steals": 1.1,
        "blocks": 0.6
    },
    {
        "name": "Tobias Harris",
        "team": "Detroit Pistons",
        "points": 18.1,
        "assists": 1.6,
        "rebounds": 7.2,
        "turnovers": 1.1,
        "fg_pct": 42.5,
        "three_pct": 29.2,
        "ft_pct": 82.5,
        "steals": 1.5,
        "blocks": 0.8
    },
    {
        "name": "Duncan Robinson",
        "team": "Detroit Pistons",
        "points": 11.8,
        "assists": 2.3,
        "rebounds": 2.4,
        "turnovers": 1.0,
        "fg_pct": 44.7,
        "three_pct": 45.6,
        "ft_pct": 61.1,
        "steals": 1.3,
        "blocks": 0.2
    },
    {
        "name": "Jalen Duren",
        "team": "Detroit Pistons",
        "points": 10.2,
        "assists": 2.1,
        "rebounds": 8.5,
        "turnovers": 2.3,
        "fg_pct": 51.4,
        "three_pct": 0.0,
        "ft_pct": 67.4,
        "steals": 0.6,
        "blocks": 1.2
    },
    {
        "name": "Daniss Jenkins",
        "team": "Detroit Pistons",
        "points": 9.1,
        "assists": 3.0,
        "rebounds": 2.6,
        "turnovers": 0.7,
        "fg_pct": 36.1,
        "three_pct": 27.1,
        "ft_pct": 77.4,
        "steals": 0.4,
        "blocks": 0.4
    },
    {
        "name": "Ausar Thompson",
        "team": "Detroit Pistons",
        "points": 8.2,
        "assists": 3.1,
        "rebounds": 7.9,
        "turnovers": 1.6,
        "fg_pct": 50.5,
        "three_pct": 14.3,
        "ft_pct": 51.6,
        "steals": 2.0,
        "blocks": 1.8
    },
    {
        "name": "Paul Reed",
        "team": "Detroit Pistons",
        "points": 7.4,
        "assists": 0.6,
        "rebounds": 4.0,
        "turnovers": 0.8,
        "fg_pct": 66.7,
        "three_pct": 40.0,
        "ft_pct": 75.0,
        "steals": 0.1,
        "blocks": 0.7
    },
    {
        "name": "Caris LeVert",
        "team": "Detroit Pistons",
        "points": 5.9,
        "assists": 1.2,
        "rebounds": 2.2,
        "turnovers": 0.6,
        "fg_pct": 44.6,
        "three_pct": 37.0,
        "ft_pct": 90.0,
        "steals": 0.6,
        "blocks": 0.5
    },
    {
        "name": "Marcus Sasser",
        "team": "Detroit Pistons",
        "points": 4.5,
        "assists": 0.5,
        "rebounds": 0.8,
        "turnovers": 0.3,
        "fg_pct": 47.8,
        "three_pct": 35.7,
        "ft_pct": 0.0,
        "steals": 0.5,
        "blocks": 0.0
    },
    {
        "name": "Isaiah Stewart",
        "team": "Detroit Pistons",
        "points": 4.0,
        "assists": 0.2,
        "rebounds": 2.4,
        "turnovers": 0.6,
        "fg_pct": 58.8,
        "three_pct": 50.0,
        "ft_pct": 70.6,
        "steals": 0.1,
        "blocks": 1.0
    },
    {
        "name": "Javonte Green",
        "team": "Detroit Pistons",
        "points": 2.7,
        "assists": 0.3,
        "rebounds": 1.8,
        "turnovers": 0.3,
        "fg_pct": 30.0,
        "three_pct": 25.9,
        "ft_pct": 83.3,
        "steals": 0.5,
        "blocks": 0.5
    },
    {
        "name": "Ronald Holland II",
        "team": "Detroit Pistons",
        "points": 1.4,
        "assists": 0.1,
        "rebounds": 1.6,
        "turnovers": 0.3,
        "fg_pct": 30.8,
        "three_pct": 25.0,
        "ft_pct": 60.0,
        "steals": 0.4,
        "blocks": 0.2
    },
    {
        "name": "Tolu Smith",
        "team": "Detroit Pistons",
        "points": 1.3,
        "assists": 0.0,
        "rebounds": 0.7,
        "turnovers": 0.3,
        "fg_pct": 100.0,
        "three_pct": 0.0,
        "ft_pct": 0.0,
        "steals": 0.3,
        "blocks": 0.0
    },
    {
        "name": "Kevin Huerter",
        "team": "Detroit Pistons",
        "points": 1.2,
        "assists": 1.4,
        "rebounds": 1.0,
        "turnovers": 0.4,
        "fg_pct": 28.6,
        "three_pct": 40.0,
        "ft_pct": 0.0,
        "steals": 0.4,
        "blocks": 0.0
    },
    {
        "name": "Chaz Lanier",
        "team": "Detroit Pistons",
        "points": 0.7,
        "assists": 0.3,
        "rebounds": 0.0,
        "turnovers": 0.0,
        "fg_pct": 33.3,
        "three_pct": 0.0,
        "ft_pct": 0.0,
        "steals": 0.0,
        "blocks": 0.0
    }
]

players = (
      lakers_players 
    + cavs_players 
    + pistons_players)

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
    