def fonctionUne(a):
  return a

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