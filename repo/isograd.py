# https://www.programiz.com/python-programming/methods/built-in/

"######################"  # Meilleur Dev de France 2015
""" Poker """  # 01

def interpretePoker(evt):
  return int(evt.split(' ')[0]), int(evt.split(' ')[1])

def poker():  # main
  sommeJoueur = int(input())
  nbrTour = int(input())
  liste = [int(input()) for _ in range(nbrTour)]

  for i in liste:
    X, Y = interprete(i)
    sommeJoueur += -X+Y 
  print(sommeJoueur)
  pass


""" Nuage de tags """  # 02

from collections import Counter
"""
  import operator
  dics = {'a':1000, 'b':3000, 'c': 100}
  for i in range(5):
    key, value = max(dics.items(), key=operator.itemgetter(1))
    print("{} {}".format(key, value))
    del dics[key]
  pass
  Max of a dics
"""
def nuageDeTags(): # main
  nbrTag = int(input())
  tags = [input() for _ in range(nbrTag)]
  c = Counter(tags)
  for keyword, nb_occ in c.most_common(5):
    print(keyword, nb_occ)
  pass


""" Salesforce - Qualité de la base """  # 03

import re
"""
  import re
  pattern = '^\+[0-9]{1,3}-[0-9]{9,11}'
  test_string = '+123-258476985'
  result = re.match(pattern, test_string)
  if result:
    print("Search successful.")
  else:
    print("Search unsuccessful.")
"""

def interpreteSales(record):
  return record.split(';')[0], record.split(';')[1], record.split(';')[2], record.split(';')[3], record.split(';')[4]

def sakesForce(): # main
  N = int(input())
  maZone = input().split(';')
  data = [input() for _ in range(N)]
  X, Y, Z = 0, 0, 0

  dics = {}
  pattern = '^\+[0-9]{1,3}-[0-9]{9,11}'

  for i in data:
    nom, prenom, societe, tel, pays = interprete(i)
    if nom+prenom+societe not in dics.keys():
      dics[nom+prenom+societe] = 0
      result = re.match(pattern, tel)
      if result:
        if len(tel.split('-')[1]) > 11:
          Y += 1
      else:
        Y += 1
      if pays not in maZone:
        Z += 1
    else:
      X += 1

  print("{} {} {}".format(X, Y, Z))  
  pass


""" Trending topics """  # 03

from collections import Counter

def trendingTopic(): # main
  nbrHashtags = int(input())
  flux = [input() for _ in range(nbrHashtags)]

  hashtags = []
  c = {}
  for hashtag in flux:
    hashtags.append(hashtag)
    if len(hashtags) == 60:
      c = Counter(hashtags)
    if len(hashtags) > 60:
      c[hashtag] += 1
      c[hashtags[-(60 + 1)]] -= 1
    if len(hashtags) >= 60:
      for hashtag in c:
        if c[hashtag] >= 40:
          return print(hashtag)
  return  print("Pas de trending topic")


"######################" # Meilleur Dev de France Octobre 2019 (Session 18:00)
""" Grand prix de Monaco """  # 01

def grandPrixMonaco():  # main
  p = int(input())-1
  N = int(input())
  pos = [i for i in range(20)]
  pos2 = [i for i in range(20)]
  ko = [False]*20
  for _ in range(N):
    a, c = input().split()
    a = int(a)-1
    if c == 'D':
      po = pos[a]
      b = pos2[po-1]
      pos[a] -= 1
      pos[b] += 1
      pos2[po] = b
      pos2[po-1] = a
    else:
      po = pos[a]
      for i in range(po+1, 20):
        b = pos2[i]
        pos[b] -= 1
        pos2[i-1] = b
      pos[a] = 19
      pos2[19] = a
      ko[a] = True

  if ko[p]:
    print("KO")
  else:
    print(pos[p]+1)
  pass


"######################" # Meilleur Dev de France Octobre 2019 (Session 15:20)
""" Station service """ # 01

def carburantNecessaire(conso, distance):
  return (conso*distance)/100

def stationService():  # main
  entierUn = int(input())
  entierDeux = int(input())
  liste = [int(input()) for x in range(3)]
  entierSix = int(input())

  for index, item in enumerate(liste):
    if index == 0:
      if carburantNecessaire(entierDeux, item) > entierUn:
        print('KO')
        break
    else:
      if carburantNecessaire(entierDeux, item-liste[index-1]) > entierUn:
        print('KO')
        break
  else:
    if carburantNecessaire(entierDeux, entierSix-liste[2]) > entierUn:
      print('KO')
    else:
      print('OK')
  pass

""" Classe tes amis!  #BFF """ # 01

def getRelationshipIds(chaine):
  return int(chaine.split(' ')[0]), int(chaine.split(' ')[1])

def classeTesAmis(): # main
  ligneUne = input()
  _, M = getRelationshipIds(ligneUne)

  lignes = [input() for _ in range(M)]

  rel = {}
  cnt = {}

  for ligne in lignes:
    a, b = getRelationshipIds(ligne)

    if a not in rel:
      rel[a] = set()
    if b not in rel:
      rel[b] = set()

    rel[a].add(b)
    rel[b].add(a)

  if 1 not in rel:
    print(-1)
  else:
    for fr in rel[1]:
      cnt[fr] = 0
      for fr2 in rel[fr]:
        if fr2 in rel[1]:
          cnt[fr] = cnt[fr]+1

  mx = 0
  mx_id = -1

  for fr in cnt.keys():
    if cnt[fr] > mx:
      mx = cnt[fr]
      mx_id = fr
    elif cnt[fr] == mx:
      if mx == 0:
        continue
      mx_id = max(mx_id, fr)

  print(mx_id)
  pass



"######################" # Meilleur Dev de France Octobre 2019 (Session 14:00)
""" Saute brique """  # 01

def sauteBrique(): # main
  entierUn = int(input())
  liste = [input() for _ in range(entierUn)]
  maxi = 0
  s = 0
  for i in liste:
    if i == "X":
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


""" Charlotte et la chocolatinerie """  # 02


def sumEntier(nbr):
  return sum(map(int, [x for x in str(nbr)]))


def charlotteChocolatine():  # main
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
      maxi = max(maxi, (int(i.split(' ')[1]) - int(i.split(' ')[0])))
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

def interprete(evt):
  return int(evt.split(' ')[0]), evt.split(' ')[1]

def fonctionDeux(a):
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