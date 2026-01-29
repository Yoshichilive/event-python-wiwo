def heronVerfahren():
  #Wir fragen den Nutzer nach der Ausgangszahl z
  z = int(input("Von welcher Zahl möchtest du die Quadratwurzel erfahren? "))
  #Falls die Zahl z negativ ist, nehmen wir die Zahl positiv (-2 wird zu 2)
  if z < 0:
    z = abs(z)
    print("Du hast eine negative Zahl eingegeben!")
    print("Wir werden mit dem positiven Äquivalent rechnen, also:", z)
  return z
  
def wurzel():
  #Wir legen die Werte für unsere Variblen fest
  #Wir geben z den Wert von heronVerfahren, das ist unser Code von oben
  z = heronVerfahren()
  az = z
  altz = z
  neuz = 0
  #Hiermit wird die Rechnung solange durchgeführt, bis der Unterscheid zwischen der alten Zahl, altz, und der neuen Zahl, neuz, klein genug ist
  while altz - neuz > 0.0000000001:
    #Wir geben altz den Wert von z, bevor er sich ändert
    altz = z
    #Das hier ist die Formel des Heron Verfahrens
    z = (z+(az/z))/2
    #Wir geben neuz den Wer von z, nach der Änderung
    neuz = z
  print("Deine Wurzel beträgt annähernd:",z)

#Hiermit führen wir unseren Code aus
wurzel()
