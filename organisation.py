from profile import Profile
import json


class Organisation():
    def __init__(self):
        self.teams = []


    def orgScore(self):
        return sum([team.computeScore() for team in self.teams])

    def nameTeams(self):
        for i, team in enumerate(self.teams):
            team.setName(f"Team {i}")

    def createJson(self):
        teams = []
        for team in self.teams:
            members = []
            for member in team.members:
                members.append(member.name)
            teams.append({"name": team.name, "members": members})
        with open("teams.json", "w") as f:
            json.dump(teams, f)

    def __repr__(self):
        result = ""
        for team in self.teams:
            result += str(team) + "\n"
        return result
