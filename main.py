def fonctionUne( a ):
  return a

def fonctionDeux( a ):
  return a

def main(): # main
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

if __name__ == "__main__":
  main()
