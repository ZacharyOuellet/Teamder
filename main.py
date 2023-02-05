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

def note(listOfPeople):
	score=0;
	for i in (len(listOfPeople)-1):
        j=i+1;
		if i.goal==j.goal:
			score+=5;
		else:
			score-=5;	
		for i in range( 0, len(#### nombre de languages 6? ####)):
			if i in #liste des langages
				score +=2;	
			
		if len( self.languageprog[other.languageprog.index(2)] ):# certainement changer les noms
			score-=4;
			
		if ()
	






if __name__ == '__main__':
    profiles = readCSV("data.csv")
    for profile in profiles:
        print(profile)
    print("----------------------------")
    org = Organisation()
    for i, profile in enumerate(profiles[::4]):
        org.teams.append(Team([*profiles[i*4:i*4+4]]))
    org.nameTeams()
    org.createJson()

