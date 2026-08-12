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

def offense_grade(offensive_rating):
    if offensive_rating >= 117.8:
        return "Elite Offense"
    elif offensive_rating >= 115.7:
        return "Very Good Offense"
    elif offensive_rating >= 114.1:
        return "Average Offense"
    elif offensive_rating >= 112.2:
        return "Below Average Offense"
    else:
        return "Poor Offense"


def defense_grade(defensive_rating):
    if defensive_rating <= 112.2:
        return "Elite Defense"
    elif defensive_rating <= 113.5:
        return "Very Good Defense"
    elif defensive_rating <= 115.3:
        return "Average Defense"
    elif defensive_rating <= 118.0:
        return "Below Average Defense"
    else:
        return "Poor Defense"


def ast_to_grade(ast_to_ratio):
    if ast_to_ratio >= 2.03:
        return "Elite Passing Team"
    elif ast_to_ratio >= 1.86:
        return "Very Good Passing Team"
    elif ast_to_ratio >= 1.79:
        return "Average Passing Team"
    elif ast_to_ratio >= 1.70:
        return "Below Average Passing Team"
    else:
        return "Poor Passing Team"


def rebound_grade(rebound_pct):
    if rebound_pct >= 51.8:
        return "Elite Rebounding Team"
    elif rebound_pct >= 49.9:
        return "Very Good Rebounding Team"
    elif rebound_pct >= 49.2:
        return "Average Rebounding Team"
    elif rebound_pct >= 48.9:
        return "Below Average Rebounding Team"
    else:
        return "Poor Rebounding Team"


def turnover_grade(turnover_pct):
    if turnover_pct <= 13.6:
        return "Elite Ball Control Team"
    elif turnover_pct <= 14.0:
        return "Very Good Ball Control Team"
    elif turnover_pct <= 14.7:
        return "Average Ball Control Team"
    elif turnover_pct <= 15.2:
        return "Below Average Ball Control Team"
    else:
        return "Poor Ball Control Team"