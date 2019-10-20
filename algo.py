#
#   Détermine si un nombre est premier ou non
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