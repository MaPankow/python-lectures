
try:
    datei = open("text.txt", "r")
    print(datei.read())
except Exception as e:
    print('File not found')
else:
    print("Datei erfolgreich gelesen!") # else ist optional, es gibt zusätzlich eine Bestätigung aus, wenn es klappt 
    datei.close()
    print("Datei geschlossen")

finally: 
    print("Das Programm geht weiter und ist nicht abgestürzt!")

    
