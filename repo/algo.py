# https://www.programiz.com/python-programming/examples
# https://www.programiz.com/python-programming/methods/built-in/

# Py-Laboratory
# -*- coding: utf-8 -*-
"""
  Dessine une matrice 10x10 en croix
"""
# def main():
from copy import deepcopy
from pprint import pprint
from collections import deque
x = 0

for i in range(10):
  cpt = -1
  for j in range(10):
    if i is j:
      x = j
  for j in reversed(range(10)):
    cpt = cpt + 1
    if cpt is x:
      print("|", end='  ')
      continue
    elif i is j:
      print("|", end='  ')
    else:
      print("O", end='  ')
  print()

#   Concours Crédit Agricole 2019
"""
  Vous devez déterminer le mot de passe du casier.  01
"""
def motDePasse(): # main
  entierUn = int(input())
  entierDeux = int(input())
  entierTrois = int(input())

  for i in range(entierUn, entierDeux+1):
    if i%entierTrois == 0:
      print(i)
      break
  pass

"""
  Le nombre de sachets qui ont une chance de contenir le ticket gagnant.  02
"""
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


"""
  Vous devez déterminer le nombre minimun de deplacement pour atteindre le bas de la piste.
"""
MOVES = [(1, 0), (0, 1), (-1, 0)]


def walkable(c):
  return c != 'X'


def is_in_laby(N, M, pos):
  return 0 <= pos[0] < M and 0 <= pos[1] < N


def neighbors(laby, pos):
  x, y = pos
  N, M = len(laby), len(laby[0])
  for delta_x, delta_y in MOVES:
    new = (x + delta_x, y + delta_y)
    if is_in_laby(N, M, new) and walkable(laby[new[1]][new[0]]):
      yield new


def show_moves(laby, moves):
  for pos in moves:
    laby[pos[1]][pos[0]] = '@'

  for y in range(len(laby)):
    laby[y] = ''.join(laby[y])

  print('\n'.join(laby))


def find_shortest_path(N, M, laby, starts):
  queue = deque([(start, 0) for start in starts])
  # orig = deepcopy(laby)

  while queue:
    cur, moves = queue.pop()

    # Reached the end!
    if cur[1] >= N - 1:
      # show_moves(orig, moves)
      return moves

    for next_ in neighbors(laby, cur):
      queue.appendleft((next_, moves + 1))
      laby[next_[1]][next_[0]] = 'X'

  return float('+inf')


def minDeplacement(): # main
  N, M = list(map(int, input().split(' ')))
  laby = [list(input()) for _ in range(N)]

  starts = [(x, 0) for x in range(M) if walkable(laby[0][x])]
  r = find_shortest_path(N, M, laby, starts)
  if r == float('+inf'):
    print(-1)
  else:
    print(r)

"""
  Ecole buissonnière
"""
def minList(list):
  indexes = []
  for i in range(len(list)):
    indexes.append([j for j, x in enumerate(list[i]) if x == min(list[i])])
  return indexes[-1]


def maxCoursSéchable(): # main
  nbrPlageCours = int(input())
  nbrCoursSéchable = int(input())

  listDurerCours = []
  for _ in range(nbrPlageCours):
    listDurerCours.append(int(input()))

  indexesToDel = []
  i, j = 0, nbrCoursSéchable+1

  while True:
    indexesToDel.append(minList(listDurerCours[i:j]))
    if (j - ((nbrPlageCours-1))) <= nbrCoursSéchable:
      break
    else:
      i = j+1
      j = j-(nbrPlageCours-1)

  for i in range(nbrPlageCours):
    listDurerCours.pop


"""     The concours Boilerplate      """


def fonctionUne( a ):
  return a

def fonctionDeux( a ):
  return a

def fonctionTrois( a ):
  return a

def main(): # main
  entierUn = int(input())
  #entierDeux = int(input())
  #entierTrois = int(input())
  liste = []
  result = 0

  for _ in range(entierUn):
    liste.append(int(input()))

  print(result)
  pass

if __name__ == "__main__":
  main()
