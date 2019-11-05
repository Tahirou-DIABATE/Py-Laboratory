def min_list(liste):
  return [j for j, x in enumerate(liste) if x == min(liste)]

def max_coursSechable(liste, pas, cursor):
  min_indexes = {}
  while True:
    if cursor >= len(liste):
      return sum(liste)
    min_index_liste = min_list(liste[cursor:cursor+pas])
    min_indexes[(cursor, cursor+pas)] = [x+cursor for x in min_index_liste]
    for i in min_index_liste:
      cursor += i + cursor + 1
      max_coursSechable(liste, pas, cursor)

def main():  # main
  plageCours = int(input())
  nbrCoursSéchable = int(input())
  liste = [int(input()) for _ in range(plageCours)]

  pas = nbrCoursSéchable + 1
  cursor = 0
  maxi = 0
  maxi = max(max_coursSechable(liste, pas, cursor), maxi)
  print(maxi)

if __name__ == "__main__":
  main()
