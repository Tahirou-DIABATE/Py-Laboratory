# https://www.programiz.com/python-programming/examples good link


def sumEntier( nbr ):
  return sum(map(int, [x for x in str(nbr)]))

def laFonctionDeux( a ):
  return a

def laFonctionTrois( a ):
  return a


def main():
  entierUn = int(input())
  #entierDeux = int(input())
  #entierTrois = int(input())

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


if __name__ == "__main__":
  main()
