"""     The concours Boilerplate      """

def takeSecond(elem):
    return elem[1]

def fonctionDeux( a ):
  return a

def main(): # main
  séquenceDeLettre = input()
  liste = []
  ok = True
  while ok:
    liste.append(input())
    if liste[-1] == '':
      liste.remove('')
      ok = False
  
  newListe = []
  for mot in liste:
    score = 0
    for lettre in mot:
      if lettre in séquenceDeLettre:
        indexLettre = séquenceDeLettre.index(lettre)
        score += int(séquenceDeLettre[indexLettre+2])
    newListe.append((mot, score))

  newListe = sorted(newListe, key=takeSecond)

  for i in reversed(newListe):
    print(i[0])
  pass

if __name__ == "__main__":
  main()
