def fibonacci(nbr):
  a, b = 0, 1
  while a < nbr:
    print(a, end=' ')
    a, b = b, a+b

def main():
  fibonacci(17)
  pass


if __name__ == "__main__":
    main()
