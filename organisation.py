from profile import Profile
import json


class Organisation():
    def __init__(self):
        self.teams = []

    def createTeams(self, profiles: list[Profile], maxTeamSize):
        pass

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
