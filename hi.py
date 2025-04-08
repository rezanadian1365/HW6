class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def intruduce(self):
        return f"my name is {self.name} and {self.age} years old. "


class FootballPlayer(Human):
    def __init__(
        self,
        name,
        age,
        position: str,
        number: int,
        performance_score: float,
        salary: float,
        fee: float,
    ) -> None:
        super().__init__(name, age)
        self.position = position
        self.number = number
        self.performanceperformance_score = performance_score
        self.salarsalary = salary
        self.goal = 0
        self.fee = fee

    def score_goal(self):
        self.goal += 1
        self.performance_score += 1.0
        print("score goal has been updated")


class Coach(Human):
    def __init__(self, name, age, experience: int, salary: float) -> None:
        super().__init__(name, age)
        self.experience = experience
        self.salary = salary


class Team:
    def __init__(self, name: str, coach: Coach, score: int, balance: float) -> None:

        self.name = name
        self.captain = None
        self.players = []
        self.coach = coach
        self.score = score
        self.balance = balance

    def assign_captain(self, cap):
        if cap in self.players:
            self.captain = cap
        else:
            return "This player not in this team"

    def add_player(self, ply):
        if ply not in self.players:
            self.players.append(ply)
        else:
            return "This player alredy in the team"

    def remove_player(self, ply):
        if ply in self.players:
            self.players.remove(ply)
        else:
            return "This player there is not in this team"

    def display_players(self):
        print(f"Team {self.name} Players:")
        for player in self.players:
            print(f"  - {player}")

    def has_enough_players(self):
        if len(self.players) == 11:
            return "Enough"
        else:
            return "Not enough"

    def buy_player(self, ply, feee):
        if ply.fee <= feee:
            return "This player has been butgh"
        else:
            return "Your offer is not enough"


# ===========================
import random


class league:
    def __init__(self, name: str):
        self.name = name
        self.teams = []

    def add_team(self, team):
        # self.team=team
        if team not in self.teams:
            self.teams.append(team)
            print(f"{team.name} added")
        else:
            print("alredy in leage")

    def remove_team(self, team):
        if team in self.teams:
            self.teams.remove(team)
            print(f"{team.name}REMOVED")
        else:
            print(f"{self.team}is not in League")

    def simulate_mach(self, tms):
        team1 = tms[0]
        team2 = tms[0]
        if team1 not in self.teams and team2 not in self.teams:
            print("team1 and team2 not in the league")
            return

        score1 = random.randint(0, 10)
        score2 = random.randint(0, 10)
        print("result={team1.name} {score1}-{score2} {team2.name}")
        if score2 > score1:
            print(f"{team2.name}WINS")
            team2.score += 3
        elif score2 < score1:
            print(f"{team1.name}WINS")
            team1.score += 3
        else:
            print("draw")
            team1.score += 1
            team2.score += 1

    # • display_standings - displays the current standings of the league.
    def display_stadndings(self):
        print(f"league Standing {self.name}")
        sortedT = sorted(self.team, key=lambda t: t.socore, reverse=True)
        for index, team in enumerate(sortedT, start=1):
            print(f"{team.name} {team.score}")

    # select_random_teams - selects two teams randomly from the teams in the league.
    def select_random_teams(self):
        team1 = random.choice(self.teams)
        team2 = random.choice(self.teams)
        return team1, team2

    # display_teams_by_points  - displays the names of the teams in descending order of
    # their points.
    def display_teams_by_points(self):
        print("teams and points")
        sortedT = sorted(self.team, key=lambda t: t.socore, reverse=True)
        for team in sortedT:
            print(f"{team.name}: {team.score}Points")


coach1 = Coach("Reza", 45, 15, 1000)
coach2 = Coach("salim", 45, 15, 2000)
team1 = Team("ps", coach1, 5, 5000)
team2 = Team("ss", coach2, 6, 7000)
player1 = FootballPlayer("saeed", 24, "forward", 9, 7.5, 5.5, 3000)
team1.add_player(player1)
team1.assign_captain(player1)
team1.has_enough_players()
