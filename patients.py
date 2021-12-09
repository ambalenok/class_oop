class patients:
    def __init__(self, surname, name, middlename,year):
        self.setsurname(surname)
        self.name(name)
        self.middlename(middlename)
        self.year(year)

        def setSurname(self, value):self.__surname=value
        def setName(self, value):self.__name=value
        def setMiddlename(self, value):self.__middlename=value
        def setYear(self, value):self.__year=value

        def getSurname(self):return self.__surname
        def getName(self):return self.__name
        def getMiddlename(self):return self.__middlename
        def getYear(self):return self.year
      
      