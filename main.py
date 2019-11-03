def interprete(evt):
  return int(evt.split(' ')[0]), evt.split(' ')[1]

def fonctionDeux(a):
  return a

def main(): # main
  nbrHashtags = int(input())
  flux = [input() for _ in range(nbrHashtags)]

  dics = {}
  time = 0
  for v in flux:
    time += 1
    if v not in dics.keys():
      dics[v] = 0
    else:
      dics[v] += 1
      if dics[v] == 40 and time < 60:
        print("{}".format(v))
        break
      elif dics[v] == 40 and time > 60:
        dics[v] = 1
  else:
    print("Pas de trending topic")
  pass

if __name__ == "__main__":
  main()
