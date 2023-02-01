

class Incorporated:
    def __init__(self, corpName):
        self.corpName = corpName
        self.corpDept = []

    def addDepWork(self, user):
        self.corpDept.append(user)

    def getIncoListDep(self):
        for i in self.corpDept:
            print(f'{i.depName}  ({self.corpName})')
