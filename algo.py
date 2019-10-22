# https://www.programiz.com/python-programming/examples good link
# https://www.programiz.com/python-programming/methods/built-in/

#   Concours Crédit Agricole 2019
#   Vous devez déterminer le mot de passe du casier.  01
#
def motDePasse(): # main
  entierUn = int(input())
  entierDeux = int(input())
  entierTrois = int(input())

  for i in range(entierUn, entierDeux+1):
    if i%entierTrois is 0:
      print(i)
      break
  pass

#
#   Le nombre de sachets qui ont une chance de contenir le ticket gagnant.  02
#
def sumEntier( nbr ):
  return sum(map(int, [x for x in str(nbr)]))

def ticketGagnant(): # main
  entierUn = int(input())
  liste = []
  cpt = 0

  for i in range(entierUn):
    liste.append(int(input()))
    if liste[i] is 42:
      cpt += 1
    while len(str(liste[i])) > 2:
      liste[i] = sumEntier(liste[i])
      if liste[i] is 42:
        cpt += 1
        continue
  print(cpt)
  pass










#
#   Vous devez déterminer si un nombre est premier ou non.
#
def isPrime(nbr):
  cpt = 0
  for i in range(1, nbr):
    if nbr%i is 0:
      cpt += 1
      if cpt is 2:
        print(nbr, "N'est pas premier")
        break
  else:
    print(nbr, "Est premier")
    print(cpt)

#
# Détermine les nombres de la suite de fib inferieur à nbr
#
def fibonacci(nbr):
  a, b = 0, 1
  while a < nbr:
    print(a, end=' ')
    a, b = b, a+b

#
# L'objectif est de déterminer l'empreinte d'un fichier à partir de sa représentation binaire.
#
def empreinte():
  laChaine = input()

  while '000' in laChaine:
    laChaine = laChaine.replace('000', '00')

  while '111' in laChaine:
    laChaine = laChaine.replace('111', '1')

  while '10' in laChaine:
    laChaine = laChaine.replace('10', '1')

  print(laChaine)

#
#   The concours Boilerplate
#
def fonctionUne( a ):
  return a

def fonctionDeux( a ):
  return a

def fonctionTrois( a ):
  return a

def main(): # main
  entierUn = int(input())
  entierDeux = int(input())
  entierTrois = int(input())
  liste = []
  result = 0

  for _ in range(entierUn):
    liste.append(int(input()))

  print(result)
  pass

if __name__ == "__main__":
  main()