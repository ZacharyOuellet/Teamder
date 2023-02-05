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
                    if not ((member1.fr == member2.fr==True) or (member1.en==member2.en==True)):
                        score+=10;
                    else:
                        score-=10;
                    if member1.goal==member2.goal:
                        score+=5;
                    else:
                        score-=5;
                    for i in ["Python","Java","C++","C#","JavaScript","Ruby","Go","Rust","HTML & CSS","Swift","Kotlin"]:
                        if (i in member1.progLang) and (i in member2.progLang):
                            score +=2;
                    if member1.allNighter==member2.allNighter:
                        score+=2
                    else:
                        score-=2
                    if member1.level==member2.level:
                        score+=1
                    else:
                        score-=1
        subjects=[self.algo, self.backend, self.frontend, self.dataScience, self.ml, self.cybersecurity]
        for i in subjects:
            for j in subjects:
                if i!=j:
                    if (i and j ) in self.members:
                        score+=5
                    else:
                        score-=5
        return score
