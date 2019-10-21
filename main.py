def main():
  entierUn = int(input())
  liste = []

  for _ in range(entierUn):
    liste.append(int(input()))

  startIndex = 0
  step = 0
  for index, value in enumerate(liste):
    if value < -0:
      step += 1
    else:
      startIndex = index + 1

  pass


if __name__ == "__main__":
  main()
