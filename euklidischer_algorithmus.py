#Hier wird die Variable ergebnis erstellt, damit wir sie später verwenden können. Das int() begrenzt die Werte auf Zahlen
ergebnis = int(0)

def Zahl():
    #Hier wird nach den Eingaben des Nutzers gebeten
    za1 = abs(int(input("Was ist deine erste Zahl? ")))
    za2 = abs(int(input("Was ist deine zweite Zahl? ")))
    #Jetzt sagen wir dem Computer, dass die Eingaben global, also nicht nur innerhalb von Zahl() verwendet werden können
    return za1, za2

def ggtBestimmen():
    #Hier wird dem Computer gesagt, dass die vorher vom Nutzer eingegebenen Werte für diese Methode verwendet werden
    za1, za2 = Zahl()
    #Jetzt schauen wir, ob die beiden Zahlen unterschiedlich groß sind. Falls sie das nicht sind, wird nach erneuter Eingabe gefragt, bis zwei verschiedene Werte eigegeben werden
    while za1 == za2:
        print("Bitte gib nicht die gleiche Zahl doppelt ein")
        za1, za2 = Zahl()
    #Wir sparen uns doppeltes Coden, indem wir hier die größere Zahl zuerst stellen für die nächste Methode
    if za1 > za2:
        ggt(za1,za2)
    elif za1 < za2:
        ggt(za2,za1)

#Jetzt wird der größte gemeinsame Teiler berechnet     
def ggt(z1,z2):
    ergebnis = z1
    zwerg = z1
    if z2 == 0:
      print("Dein größter gemeinsamer Teiler ist:", z1)
    elif z2 != 0:
      while zwerg != 0:
          while ergebnis >= z2:
              ergebnis = ergebnis - z2
          zwerg = ergebnis
          ergebnis = z2
          z2 = zwerg
      print("Dein größter gemeinsamer Teiler ist:",ergebnis)

ggtBestimmen()

