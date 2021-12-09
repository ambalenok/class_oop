from classes import classes 
from patients import patients 

class appeals:
    def __init__(self, classes, patients, date, diagnosis,cost ):
        self.classes(classes) 
        self.patients(patients)
        self.date(date)
        self.diagnosis(diagnosis)
        self.cost(cost)

        def setСlasses(self, value):self.__classes=value
        def setPatients(self, value):self.__patients=value
        def setDate(self, value):self.__date=value
        def setDiagnosis(self, value):self.__diagnosis=value
        def setCost(self, value):self.__cost=value

        def getСlasses(self):return self.__Classes
        def getPatients(self):return self.__Patients
        def getDate(self):return self.__Date
        def getDiagnosis(self):return self.__Diagnosis
        def getCost(self):return self.__Cost