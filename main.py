#
#   The concours Boilerplate
#
def fonctionUne( a ):
  return a

def fonctionDeux( a ):
  return a

def fonctionTrois( a ):
  return a

def main(): # main
  entierUn = int(input())
  liste = []
  result = []

  for i in range(entierUn):
    liste.append(input())
    if liste[i] is reversed(liste[i]):
      result.append(input())
  result = ' '.join(liste)
  print(result)
  pass

if __name__ == "__main__":
  main()