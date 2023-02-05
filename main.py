import math

from organisation import Organisation
from profile import Profile
from team import Team
import csv
import random


def readCSV(filename):
    profiles = []
    with open(filename, encoding="UTF-8") as f:
        reader = csv.reader(f)
        reader.__next__()
        for line in reader:
            profiles.append(Profile(*line[1:]))
    return profiles

class Combinaison:
    def __init__(self, profiles:list[Profile]):
        self.profiles = profiles
    def __iter__(self):
        self.i = 1000000
        return self
    def __next__(self):
        if self.i > 0:
            print(self.i)
            self.i -= 1
            random.shuffle(self.profiles)
            return Organisation(self.profiles)
        raise StopIteration

def optimizeTeams(profiles:list[Profile]):
    maxorg = -math.inf
    bestOrg = None
    for org in iter(Combinaison(profiles)):
        score = org.computeScore()
        print(score, maxorg)
        if score >= maxorg:
            maxorg = score
            bestOrg = org
    return bestOrg



if __name__ == '__main__':
    profiles = readCSV("data.csv")
    bestOrg = optimizeTeams(profiles)
    bestOrg.nameTeams()
    for team in bestOrg.teams:
        print(f"{team.name}  : score : {team.computeScore()}")
    bestOrg.createJson()

