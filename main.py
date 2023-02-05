from organisation import Organisation
from profile import Profile
from team import Team
import csv


def readCSV(filename):
    profiles = []
    with open(filename, encoding="UTF-8") as f:
        reader = csv.reader(f)
        reader.__next__()
        for line in reader:
            profiles.append(Profile(*line[1:]))
    return profiles

class combinaison:
    def __iter__(self):
        pass

def optimizeTeams(orgs:Organisation):
    maxorg = 0


if __name__ == '__main__':
    profiles = readCSV("data.csv")
    for profile in profiles:
        print(profile)
    print("----------------------------")
    org = Organisation()
    for i, profile in enumerate(profiles[::4]):
            org.teams.append(Team([*profiles[i*4:i*4+4]]))
    org.nameTeams()
    for team in org.teams:
        print(f"{team.name}  : score : {team.computeScore()}")
    org.createJson()

