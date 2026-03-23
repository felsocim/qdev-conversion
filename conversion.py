conversions = [
  ("km", "mi"),
  ("mi", "km"),
  ("kg", "lbs"),
  ("lbs", "kg"),
  ("°C", "°F"),
  ("°F", "°C")
]

def kilometres_en_miles(x):
  return x * 0.6214

print("Bienvenue dans votre convertisseur d'unités !")

print("\nListe des fonctions de conversion :\n")

i = 0
for depuis, vers in conversions:
  print(f"({i}) {depuis} en {vers}")
  i += 1

choix = int(input(f"\nVotre choix (0-{i - 1}) ? "))

x = float(input("Valeur à convertir ? "))

resultat = None

if choix == 0:
  resultat = kilometres_en_miles(x)

print(f"\n{x} {conversions[choix][0]} = {resultat} {conversions[choix][1]}")
