from profile import Profile
from team import Team
import json


class Organisation:
    def __init__(self, profiles: list[Profile], maxTeamSize=4):
        self.teams = []
        nEquipe1moins = maxTeamSize - len(profiles) % maxTeamSize
        if nEquipe1moins == maxTeamSize:
            nEquipe1moins = 0
            nEquipeMax = len(profiles) // maxTeamSize
        else:
            nEquipeMax = len(profiles) // maxTeamSize - nEquipe1moins + 1
        for i in range(nEquipeMax):
            self.teams.append(Team(profiles[i * maxTeamSize:i * maxTeamSize + maxTeamSize]))
        for i in range(nEquipe1moins):
            self.teams.append(Team(profiles[nEquipeMax * maxTeamSize + i * (maxTeamSize - 1):
                                            nEquipeMax * maxTeamSize + i * (maxTeamSize - 1) + maxTeamSize - 1]))

    def computeScore(self):
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
            teams.append({"name": team.name, "members": members, "score": team.computeScore()})
        with open("teams.json", "w") as f:
            json.dump(teams, f)

    def sortTeams(self, r = False):
        self.teams.sort(key=lambda x: x.computeScore(), reverse=r)
        orderedProfiles = []
        for team in self.teams:
            print(team.computeScore())
            orderedProfiles.extend(team.members)
        return orderedProfiles

    def __repr__(self):
        result = ""
        for team in self.teams:
            result += str(team) + "\n"
        return result
