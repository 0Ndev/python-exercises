class Patient:
    def __init__(self, name = 'x', alter = 0, nr = 0):
        self._patientID = nr
        self._patientAge = alter
        self._patientName = name
        
    def display(self):
        print('Nummer: ', self._patientID, ' Name: ',self._patientName, ' Alter: ', self._patientAge)
        
    def read(self, patientID):
        self._patientID = patientID
        self._patientName = input('Name: ')
        self._patientAge = input('Alter: ')
        
    
class Station:
    def __init__(self, stationsname):
        self.__stationsName = stationsname
        self.__PatientenListe = []
        self.__anzPatienten = 0
        
    def getName(self):
        return self.__stationsName
    
    def addPatient(self, patient = None):
        if patient == None:
            patient = Patient()
            patient.read(self.__anzPatienten +1)
        self.__PatientenListe.append(patient)
        self.__anzPatienten += 1
        
    def searchPatient(self, patientID):
        for x in self.__PatientenListe:
            if x._patientID == patientID:
                return True
        return False
    
    def deletePatient(self, patientID):
        for x in self.__PatientenListe:
            if x._patientID == patientID:
                self.__PatientenListe.remove(x)
                return True
        return False
    
    def displayAll(self):
        for x in self.__PatientenListe:
            x.display()
    

class Krankenhaus:
    def __init__(self, name):
        self.__name = name
        self.__stationsListe = []
        self.__anzStationen = len(self.__stationsListe)
        
    def fuegStationHinzu(self, station):
        self.__stationsListe.append(station)
        self.__anzStationen = len(self.__stationsListe)
    
    def sucheStation(self, stationsName):
        for i in self.__stationsListe:
            if i.getName() == stationsName:
                return True
        return False
    
    def loescheStation(self, stationsName):
        for i in self.__stationsListe:
            if i.getName() == stationsName:
                self.__stationsListe.remove(i)
                self.__anzStationen = len(self.__stationsListe)
                return True
        return False
    
    def zeigeAlle(self):
        for i in self.__stationsListe:
            print(i.getName())

# main
class MainClass:
    def run():
        p1 = Patient('SickMan', 31, 1)
        p1.display()

        p2 = Patient()
        p2.read(2)

## class Station
        S = Station('Kardiologie')
        S.getName()
        S.addPatient(p1)
        S.addPatient()
        S.displayAll()
        S.searchPatient(2)
        S.deletePatient(1)
        S.displayAll()

## class Krankenhaus
        K = Krankenhaus('Charite')
        K.fuegStationHinzu(S)
        K.fuegStationHinzu(Station('Onkologie'))
        K.zeigeAlle()
        K.sucheStation('Kardiologie')
        K.loescheStation('Onkologie')
        K.zeigeAlle()
