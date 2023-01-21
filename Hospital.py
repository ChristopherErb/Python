class Employee:
    def __init__(self, nameFirst, nameLast, shift, isRegistered, pay):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.shift = shift
        self.isRegistered = isRegistered
        self.pay = pay

class Patient:
    def __init__(self, ptName, ptSpecies, ptLocation, ptDiagnosis, ptOwners, ptOwnersNumber):
        self.ptName = ptName
        self.ptSpecies = ptSpecies
        self.ptLocation = ptLocation
        self.ptDiagnosis = ptDiagnosis
        self.ptOwners = ptOwners
        self.ptOwnersNumber = ptOwnersNumber


