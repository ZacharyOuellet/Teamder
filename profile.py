class Profile:
    studiesLevel = ("Secondaire", "Collégial", "Baccalauréat", "Maîtrise", "Doctorat", "Autre")
    def __init__(self, *args):
        self.name = args[0]
        self.age = int(args[1])
        self.fr = ("Français" in args[2])
        self.en = ("Anglais" in args[2])
        for level, name in enumerate(Profile.studiesLevel):
            if name == args[3]:
                self.level = level+1
                break
        self.progLang = args[4].split(",")
        self.algo, self.backend, self.frontend, self.dataScience, self.ml, self.cybersecurity = [int(x) for x in args[5:11]]
        self.goal = args[11]
        match args[12]:
            case "Oui":
                self.allNighter = True
            case "Non":
                self.allNighter = False
            case _:
                self.allNighter = None




    def __repr__(self):
        return str(self.__dict__)
