def main():
  liste = [6, 4, 2, 7, 3, 5, 1, 7, 9, 1]

  print(liste)
  for item in enumerate(liste):
    if item[0] in [2, 6]:
      liste[item[0]]= 0

  print(sum(liste))
  pass

if __name__ == "__main__":
  main()