'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru afbici

  if n<2:
    return False
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True
  
def testIsPrime():
  assert is_prime(3) is True
  assert is_prime(15) is False
'''
Returneaza produsul numerelor din lista lst.

'''
def citire_lista(lst):
  lst=[]
  givenString=input("dati numerele separate printr-o virgula:")
  numbersAsString=givenString.split(",")
  for x in numbersAsString:
    lst.append(int(x))
  return lst

def get_product(lst):
  p=1
  for x in lst:
    p=p*x
  return p

def testGetProduct():
  assert get_product([2,3,1])==6

  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  r=x%y
  while r>0:
    x=y
    y=r
    r=x%y
  return y
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while x!=y:
    if x>y:
      x=x-y
    else:
      y=y-x
    return y
  
  
def main():
  testIsPrime()
  testGetProduct()
  lst=[]
  print("1.determina daca numarul dat este prim")
  print("2.determina produsul numerelor dintr-o lista ")
  print("3.determina cmmdc a doua nr varianta 1")
  print("4.determina cmmdc a doua numere varianta 2")
  print("5.Iesire")
  while True:
    optiune=input("dati optiune:")
    if optiune=="1":
      n=int(input("dati numarul:"))
      print(is_prime(n))
    elif optiune=="2":
      citire_lista(lst)
      print(get_product(lst))
    elif optiune=="3":
      x=int(input("dati primul numar"))
      y=int(input("dati al doilea numar:"))
      print(get_cmmdc_v1(x,y))
    elif optiune=="4":
      x = int(input("dati primul numar"))
      y = int(input("dati al doilea numar:"))
      print(get_cmmdc_v2(x,y))
    elif optiune=="5":
      break
    else:
      print("optiune gresita! reincercati!")

if __name__ == '__main__':
  main()
