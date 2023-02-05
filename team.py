from profile import Profile


class Team:
    def __init__(self, members: list[Profile]):
        self.members = members
        self.__name = "NO NAME"

    def addMember(self, member: Profile):
        self.members.append(member)

    def setName(self, name: str):
        self.__name = name

    def __repr__(self):
        result = f"{self.__name} :\n"
        for member in self.members:
            result += f"{member.name}     "
    
    def computeScore(self):    
        score=0
        for member1 in self.members:
            for member2 in self.members:
                if member1!=member2:
                    if not ((member1.speaksFrench == member2.speaksFrench==True) or (member1.speaksEnglish==member2.speaksEnglish==True)):
                        score+=10;
                    else:
                        score-=10;
                    if member1.goal==member2.goal:
                        score+=5;
                    else:
                        score-=5;

                    for i in range( 0, len()):
                        if i in #liste des langages
                            score +=2;
