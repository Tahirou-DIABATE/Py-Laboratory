def min_list(liste):
  return [j for j, x in enumerate(liste) if x == min(liste)][-1]

def main():  # main
  plageCours = int(input())
  nbrCoursSéchable = int(input())
  liste = [int(input()) for _ in range(plageCours)]

  pas = nbrCoursSéchable + 1
  cursor = 0
  while True:
    if cursor >= len(liste):
      return print(sum(liste))
    min_index = min_list(liste[cursor:cursor+pas])
    id_item = min_index + cursor
    liste[id_item] = 0
    cursor += id_item + 1

if __name__ == "__main__":
  main()