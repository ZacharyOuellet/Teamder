from profile import Profile
import json


class Organisation():
    def __init__(self):
        self.teams = []

    def createTeams(self, profiles: list[Profile], maxTeamSize):
        french = []
        english = []
        bilingual = []
        for i in (participants polyhx):
            if (i.speaksFrench == True AND i.speaksEnglish == False):
                french.append(i);
            elif (i.speaksEnglish == True AND i.speaksFrench == False):
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
            if j.goal == True:
                frenchGoal.append(j);
            else j.goal == False:
                frenchNoGoal.append(j);

        for j in english:
            if j.goal == True:
                englishGoal.append(j);
            else j.goal == False:
                englishNoGoal.append(j);

        for j in bilingual:
            if j.goal == True:
                bilingualGoal.append(j);
            else j.goal == False:
                bilingualNoGoal.append(j);
        # mettre un mutliple de 4 pour les personnes anglophones
        rest = englishGoal % 4;
        englishGoal += bilingualGoal[i
        for i in rest];
        del bilingualGoal[i
        for i in rest];
        rest = englishNoGoal % 4;
        englishNoGoal += bilingualNoGoal[i
        for i in rest];
        del bilingualNoGoal[i
        for i in rest];

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
