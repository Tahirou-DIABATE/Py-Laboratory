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
  entrerUn = int(input())
  entrerDeux = int(input())
  listeUn = [int(input()) for _ in range(3)]

  entrerSix = int(input())
  consoAvantSi = []

  for i, item in enumerate(listeUn):
    if i == 0:
      consoAvantSi.append((entrerDeux*listeUn[0])/100)
    else:
      consoAvantSi.append((entrerDeux*listeUn[1])/100 - (listeUn[i-1]))
  
  for i in range(3):
    if consoAvantSi[i] < listeUn[i]:
      print("KO")
      break
  else:
    print("OK")
  pass

if __name__ == "__main__":
  main()