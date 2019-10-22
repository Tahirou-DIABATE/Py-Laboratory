#
#   Vous devez déterminer le mot de passe du casier.
#
def motDePasse():
  entierUn = int(input())
  entierDeux = int(input())
  entierTrois = int(input())

  for i in range(entierUn, entierDeux+1):
    if i%entierTrois is 0:
      print(i)
      break
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
#   La fonction principale "main"
#
def main():
  liste = [6, 4, 2, 7, 3, 5, 1, 7, 9, 1]

  print(liste)
  for item in enumerate(liste):
    if item[0] in [2, 6]:
      liste[item[0]]= 0

  fibonacci(sum(liste))
  pass

if __name__ == "__main__":
  main()