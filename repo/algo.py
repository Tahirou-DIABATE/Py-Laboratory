# Py-Laboratory
# -*- coding: utf-8 -*-
from copy import deepcopy
from pprint import pprint
from collections import deque

"""
  Linear search.
"""
def linear_search(data, target):
  for index, value in enumerate(data):
    if value == target:
      return print("{} is in position {}".format(target, index))
  else:
    return print("{} is not in the list ".format(target))
  pass


"""
  Iterative binary search.
"""
def iterative_binary_search(data, target):
  low = 0
  high = len(data) - 1

  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:
      return print("{} is in position {}".format(target, data.index(target)))
    elif target < data[mid]:
      high = mid - 1
    else: 
      low = mid + 1
  else: 
    return print("{} is not in the list ".format(target))
  pass


"""
  Recursive binary search.
"""
def recursive_binary_search(data, target, low, high):
  if low > high:
    return print("{} is not in the list ".format(target))
  else:
    mid = (low + high) // 2
    if data[mid] == target:
      return print("{} is in position {}".format(target, data.index(target)))
    elif target < data[mid]:
      recursive_binary_search(data, target, low, mid - 1)
    else:
      recursive_binary_search(data, target, mid + 1, high)
  pass


"""
  Dessine une matrice 10x10 avec une croix.
"""
def matrixAvecCroix(): # main
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
  pass


"""
  Vous devez déterminer si un nombre est premier ou non.
"""
def isPrime(nbr):
  cpt = 0
  for i in range(1, nbr):
    if nbr % i is 0:
      cpt += 1
      if cpt is 2:
        print(nbr, "N'est pas premier")
        break
  else:
    print(nbr, "Est premier")
    print(cpt)
  pass


"""
 Détermine les nombres de la suite de fib inferieur à nbr
"""
def fibonacci(nbr):
  a, b = 0, 1
  while a < nbr:
    print(a, end=' ')
    a, b = b, a+b

""""""""
def takeSecond(elem):
    return elem[1]

def scoreMot(): # main
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
    listDurerCours.pop()

""" Temps d'exécusion d'un programme """

import timeit
exc_time = timeit.timeit(lambda: fibonacci(1000000), number=1)/1
print(exc_time)
