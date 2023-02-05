from main import readCSV
import math

from organisation import Organisation
from profile import Profile
from team import Team
import csv
import random

def optimize(profiles:list[Profile]):
    org = Organisation(profiles)
    bestOrg = None
    bestScore = -math.inf
    for _ in range(100):
        for _ in range(100):
            if org.computeScore()>bestScore:
                bestOrg = org
                bestScore = org.computeScore()
            orderedProfiles = org.sortTeams()
            lowerHalf = orderedProfiles[:int(len(orderedProfiles)/2)+1]
            random.shuffle(lowerHalf)
            for i,v in enumerate(lowerHalf):
                orderedProfiles[i] = v
            org = Organisation(orderedProfiles)

        orderedProfiles = org.sortTeams(r=True)
        upperHalf = orderedProfiles[:int(len(orderedProfiles) / 2) + 1]
        random.shuffle(upperHalf)
        for i, v in enumerate(upperHalf):
            orderedProfiles[i] = v
        org = Organisation(orderedProfiles)
    return bestOrg

if __name__ == '__main__':
    profiles = readCSV("data.csv")
    bestOrg = optimize(profiles)
    bestOrg.nameTeams()
    for team in bestOrg.teams:
        print(f"{team.name}  : score : {team.computeScore()}")
    print(bestOrg.computeScore())
    bestOrg.createJson()