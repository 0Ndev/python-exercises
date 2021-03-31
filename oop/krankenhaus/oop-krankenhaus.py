# Patient
class Patient:
    def __init__(self, patientAge, patientName):
        patientCounter = 0
        self.patientID = patientCounter + 1
        self.patientAge = patientAge
        self.patientName = patientName

    def read(self):
        # patientName = input("Geben Sie den Namen des Patienten ein : *")
        # patientAge = str(input("Nun das Alter des Patienten : *"))
        # patientId = str(input("Geben Sie die id des Patient ein : *"))
        return "Patient ID: " + str(self.patientID)

    def display(self):
        patientInfo = "Patient: " + str(self.patientName) + " ist " + str(self.patientAge) + " Jahre alt."
        return patientInfo


# Station
class Station:
    def __init__(self, stationsName):
        self.stationsName = stationsName
        self.anzPatienten = 0
        self.patientenListe = []

    def getName(self):
        return "Station: " + self.stationsName

    def addPatient(self, patient):
        # self.patientenListe.append(patient)
        self.patientenListe += [patient]
        self.anzPatienten += 1
        return [print("patient aus liste: ", patient) for patient in self.patientenListe]

    def searchPatient(self, patientId):
        # if patientId == Patient(patientId):
        #     return True
        # else:
        #     return False

        for patient_from_list in self.patientenListe:
            if patient_from_list == patientId:
                return patientId 
            else:
                return "Patient ist nicht gefunden."


    def deletePatient(self, patient):
        for patient_from_list in self.patientenListe:
            if patient_from_list == patient:
                return self.patientenListe.remove(patient)
            else:
                return "nicht gelöscht"


    def displayAll(self):
        patienten_anz = self.anzPatienten
        return "Patienten Anzahl: " + str(self.anzPatienten)
        # return "Patienten Anzahl: " + str(self.anzPatienten) + "\n Patientenliste: " + self.patientenListe



# Krankenhaus
class Krankenhaus:
    def __init__(self, name):
        self.name = name
        self.anzStationen = 0
        self.stationsListe = []

    def fuegStationHinzu(self, station):
        # self.stationsListe.append(station)
        self.stationsListe += [station]
        self.anzStationen += 1
        return self.stationsListe 

    def sucheStation(self, station):
        for station_from_list in self.stationsListe:
            # print("station_from_list:", station_from_list.station)
            if station_from_list == station:
                return "Station: " + str(station) + " ist vorhanden."
            else:
                return "Station " + str(station) + " ist nicht vorhanden."

    def loescheStation(self, station):
        if station in self.stationsListe:
            self.stationsListe.remove(station)
        return self.stationsListe

    def zeigeAlle(self):
        # print("self.stationsListe:", self.stationsListe)
        # return str(self.anzStationen) + " " + self.stationsListe
        return "Stationen Anzahl: " + str(self.anzStationen)


# Instances #########################################
# Patient
patient_1 = Patient("Baumtrud Schneider", 78)
patient_2 = Patient("Ismir Schnuppe", 20)
patient_3 = Patient("Niko Thin", 17)

# Station
station_1 = Station("Unfall") 
station_2 = Station("Geburt")
station_3 = Station("Kettensägen Massaker extrem Chirurgie")
# add patient
station_1.addPatient(patient_1)
station_1.addPatient(patient_3)
station_2.addPatient(patient_2)

# Krankenhaus_1
krankenhaus_1 = Krankenhaus("Martin Luther Krankenhaus")
krankenhaus_1.fuegStationHinzu(station_1)
krankenhaus_1.fuegStationHinzu(station_2)
krankenhaus_1.fuegStationHinzu(station_3)

# testing **************************************
# patient
print("\n* Patient ******************************")
print("patient 1", patient_1.read())
print(patient_1.display())
print("patient 2", patient_2.read())
print("*********************************")

# station
print("\n* Station INFORMATION ***************")
print(station_1.getName())
print(station_1.displayAll())
print("\n* Station SUCHE ********************")
print("Bitte Patienten ID eingeben : ")
print("Der Patient Nr " + str(patient_1.patientID) + " ist im System ", station_1.searchPatient(patient_1.patientID))

print("Geben Sie die ID des zu löschenden Patienten ein: :")
print("\n* Nach loeschen ************")
print("Der Patient Nr " + str(patient_1.patientID) + " wurde gelöscht: " + station_1.deletePatient(patient_1.patientID))
print("*********************************")

# krankenhaus
print("\n* Krankenhau INFO ******************************")
print(krankenhaus_1.zeigeAlle())
print("\n* Krankenhaus Station SEARCH *************")
print(krankenhaus_1.sucheStation("Geburt"))
print("\n* Krankenhaus Station nach loeschen *************”")
# print("Station wurde gelöscht " + krankenhaus_1.loescheStation("Kettensägen Massaker extrem Chirurgie"))
# krankenhaus_1.zeigeAlle()

