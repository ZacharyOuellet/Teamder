from profile import Profile


class Team:
    def __init__(self, members: list[Profile]):
        self.members = members
        self.name = "NO NAME"

    def addMember(self, member: Profile):
        self.members.append(member)

    def setName(self, name: str):
        self.name = name

    def __repr__(self):
        result = f"{self.name} :\n"
        for member in self.members:
            result += f"{member.name}     "
        return result

    
    def computeScore(self):
        score=0
        l=[0,0,0,0,0,0]
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
                        score -= 2
                    if member1.level==member2.level:
                        score += 1
                    else:
                        score -= 1
            l[0] += member1.algo
            l[1] += member1.backend
            l[2] += member1.frontend
            l[3] += member1.dataScience
            l[4] += member1.ml
            l[5] += member1.cybersecurity
        mean=(l[0]+l[1]+l[2]+l[3]+l[4]+l[5])/6
        sum=0
        for i in range(6):
            sum+=(l[i]-mean)**2
        standardDeviation=(sum/5)**(1/2)
        if standardDeviation<=0.1:
            standardDeviation = 0.1
        score+=5/standardDeviation
        score-= -78.64626131895065  # moyenne
        return score
