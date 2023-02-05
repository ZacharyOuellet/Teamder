from main import readCSV
import itertools

from team import Team

if __name__ == '__main__':
    profiles = readCSV("data.csv")
    scores = [Team(members).computeScore() for members in itertools.combinations(profiles,4)]
    sumOfAllScores =sum(scores)
    for score in scores:
        print(score)
    print("\nMoyenne:")
    print(sumOfAllScores/len(scores))
