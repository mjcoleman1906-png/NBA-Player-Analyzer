# Michael Coleman
# August 8th

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
        field_goal_pct * 0.2 + 
        three_point_pct * 0.3 +
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