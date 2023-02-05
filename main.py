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

french = []
english = []
bilingual = []
for i in (participants polyhx):
	if (i.speaksFrench==True AND i.speaksEnglish==False):
		french.append(i);
	elif (i.speaksEnglish==True AND i.speaksFrench==False):
		english.append(i);
	else:
		bilingual.append(i);

frenchGoal = [];
englishGoal = [];
bilingualGoal = [];

frenchNoGoal = [];
englishNoGoal = [];
bilingualNoGoal = [];

for j in french:
	if j.goal==True:
		frenchGoal.append(j);
	else j.goal==False:
		frenchNoGoal.append(j);

for j in english:
	if j.goal==True:
		englishGoal.append(j);
	else j.goal==False:
		englishNoGoal.append(j);

for j in bilingual:
	if j.goal==True:
		bilingualGoal.append(j);
	else j.goal==False:
		bilingualNoGoal.append(j);
#mettre un mutliple de 4 pour les personnes anglophones 
rest=englishGoal%4;
englishGoal+=bilingualGoal[i for i in rest];
del bilingualGoal[i for i in rest];
rest=englishNoGoal%4;
englishNoGoal+=bilingualNoGoal[i for i in rest];
del bilingualNoGoal[i for i in rest];

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

