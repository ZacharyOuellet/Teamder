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
