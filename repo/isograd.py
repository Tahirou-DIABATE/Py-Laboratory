# https://www.programiz.com/python-programming/methods/built-in/

"######################" # Meilleur Dev de France Octobre 2019 (Session 15:20)
""" Station service """ # 01

def carburantNecessaire(conso, distance):
  return (conso*distance)/100

def stationService():  # main
  entierUn = int(input())
  entierDeux = int(input())
  listeUne = [int(input()) for x in range(3)]
  entierSix = int(input())

  for index, item in enumerate(listeUne):
    if index == 0:
      if carburantNecessaire(entierDeux, item) > entierUn:
        print('KO')
        break
    else:
      if carburantNecessaire(entierDeux, item-listeUne[index-1]) > entierUn:
        print('KO')
        break
  else:
    if carburantNecessaire(entierDeux, entierSix-listeUne[2]) > entierUn:
      print('KO')
    else:
      print('OK')
  pass


""" Charlotte et la chocolatinerie """ # 02

def sumEntier(nbr):
  return sum(map(int, [x for x in str(nbr)]))

def charlotteChocolatine(): # main
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





"######################" # Meilleur Dev de France Octobre 2019 (Session 14:00)
""" Saute brique """  # 01

def sauteBrique(): # main
  entierUn = int(input())
  liste = [input() for _ in range(entierUn)]
  maxi = 0
  s = 0
  for i in range(entierUn):
    if liste[i] == "X":
      s = 0
    else:
      s+=1
    maxi = max(maxi, s)
  print(maxi-1)
  pass



"######################" # Meilleur Dev de France Octobre 2019 (Session 12:40)
""" Paintball """  # 01

def paintball(): # main
  entierUn =  int(input())
  liste = [input() for _ in range(entierUn)]

  for i in liste:
    if i == ''.join(list(reversed(i))):
      print(i, end=' ')
  pass



"######################" # Concours Crédit Agricole 2019
""" Salle de sport """  # 01

def salleDeSport(): # main
  entierUn = int(input())
  entierDeux = int(input())
  entierTrois = int(input())

  for i in range(entierUn, entierDeux+1):
    if i%entierTrois == 0:
      print(i)
      break
  pass




"######################" # Concours Orange Septembre 2019
""" Empreinte de fichier """  # 01

def empreinteDeFichier():
  laChaine = input()

  while ('000' in laChaine) or ('111' in laChaine):
    laChaine = laChaine.replace('000', '00')
    laChaine = laChaine.replace('111', '1')
  
  while '10' in laChaine:
    laChaine = laChaine.replace('10', '1')

  print(laChaine)
  pass




"######################" # Le concours blanc du Meilleur Dec de France 2019
""" Années bissextiles """  # 01

def annéeBissextile(): # main
  entierUn = int(input())
  liste = [int(input()) for _ in range(entierUn)]

  for item in liste:
    if item%400 == 0:
      print('BISSEXTILE')
    else:
      if ((item%4) == 0) and ((item%100) != 0):
        print('BISSEXTILE')
      else:
        print('NON BISSEXTILE')
  pass




"######################" # Concours entrainement La Poste 2019
""" Trading """  # 01

def trading(): # main
  entierUn = int(input())
  entierDeux = int(input())
  liste = [input() for _ in range(entierDeux)]

  maxi = 0

  for i in liste:
    if entierUn > int(i.split(' ')[0]):
      if (int(i.split(' ')[1]) - int(i.split(' ')[0])) > maxi:
        maxi = (int(i.split(' ')[1]) - int(i.split(' ')[0]))
  print(maxi)
  pass




"######################" # Battle Dev Hello Work - Mars 2019
""" Marathon """  # 01

def marathon(): # main
  position = int(input())
  liste = [input() for _ in range(42)]

  for i in liste:
    position = position + (int(i.split(' ')[0]) - int(i.split(' ')[1]))
  
  if position <= 100:
    print(1000)
  else:
    if position <= 10000:
      print(100)
    else:
      print('KO')
  pass




"######################" # Battle Dev Hello Work - Novembre 2018
""" Vente aux enchères """  # 01

def venteAuxEnchère(): # main
  nbrEncheres = int(input())
  prixReserve = int(input())
  liste = [input() for _ in range(nbrEncheres)]

  gagant = 0
  maxEnchere = 0
  for index, item in enumerate(liste):
    if int(item.split(' ')[0]) > prixReserve:
      if int(item.split(' ')[0]) > maxEnchere:
        maxEnchere = int(item.split(' ')[0])
        gagant = index
  if maxEnchere <= prixReserve:
    print('KO')
  else:
    print(liste[gagant].split(' ')[1])
  pass




"######################" # Meilleur Dev de France Octobre 2018 (Session 17:00)
""" Casino """  # 01

def casino(): # main
  nbrTour = int(input())
  nbrJeton = int(input())
  liste = [input() for _ in range(nbrTour)]
  recharge = nbrJeton
  cpt = 0
  
  for i in liste:
    M = i.split(' ')[0]
    Q = i.split(' ')[1]
    R = i.split(' ')[2]
    
    if Q in 'PI':
      if ((Q == 'P') and (int(R) % 2 != 0)) or ((Q == 'P') and (int(R) == 0)):
        nbrJeton -= int(M)
      elif (Q == 'I') and (int(R) % 2 != 1):
        nbrJeton -= int(M)
      else:
        nbrJeton += int(M)
    else:
      if int(Q) != int(R):
        nbrJeton -= int(M)
      else:
        nbrJeton += int(M)*35
    if nbrJeton <= 0:
      cpt += 1
      nbrJeton = recharge

  print(cpt)
  pass




"######################" # The concours boilerplate
""" The concours Boilerplate """  # 01

def fonctionUne( a ):
  return a

def fonctionDeux( a ):
  return a

def main(): # main
  entierUn = int(input())
  #entierDeux = int(input())
  #entierTrois = int(input())
  liste = [int(input()) for _ in range(entierUn)]

  print(liste)
  pass

if __name__ == "__main__":
  main()