import sys

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

def kilogrammes_en_livres(x):
  return x * 2.2046

def livres_en_kilogrammes(x):
  return x * 0.4536

def miles_en_kilometres(x):
  return x * 1.6093

def celsuis_en_fahrenheit(x):
  return x * (9.0 / 5.0) + 32

def fahrenheit_en_celsius(x):
  return (x - 32) / (9.0 / 5.0)

print("Bienvenue dans votre convertisseur d'unités !")

print("\nListe des fonctions de conversion :\n")

i = 0
for depuis, vers in conversions:
  print(f"({i}) {depuis} en {vers}")
  i += 1

choix = int(input(f"\nVotre choix (0-{i - 1}) ? "))

if choix < 0 or choix >= i:
  print("\nChoix invalide !")
  sys.exit(1)

x = float(input("Valeur à convertir ? "))

resultat = None

if choix == 0: # km en mi
  resultat = kilometres_en_miles(x)
elif choix == 1: # mi en km
  resultat = miles_en_kilometres(x)
elif choix == 2: # kg en lbs
  resultat = kilogrammes_en_livres(x)
elif choix == 3: # lbs en kg
  resultat = livres_en_kilogrammes(x)
elif choix == 4: # °C en °F
  resultat = celsuis_en_fahrenheit(x)
elif choix == 5: # °F en °C
  resultat = fahrenheit_en_celsius(x)

if resultat is not None:
  print(f"\n{x} {conversions[choix][0]} = {resultat:.2f} {conversions[choix][1]}")
