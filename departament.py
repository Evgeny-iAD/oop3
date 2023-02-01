

class Departament:
    def __init__(self, depName):
        self.depName = depName
        self.posListUser = []
        self.deptListUser = []

    def addUserWork(self, user):
        self.deptListUser.append(user)

    def addPosWork(self, position):
        self.posListUser.append(position)

    def removeUserWork(self, user):
        self.deptListUser.remove(user)

    def getDeptListUser(self):
        for i in self.deptListUser:
            print(f'{i}  ({self.depName})')

    def getDeptListPos(self):
        for i in self.posListUser:
            print(f'{i}  ({self.depName})')
