def verifica(primeiraPalavra):   
   if(primeiraPalavra[::-1] == segundaPalavra):
      print("Sim,uma é a inversa da outra!")
   else:
      print("Não são inversas uma da outra!")
primeiraPalavra = input("Insira a primeira palavra:")
segundaPalavra = input("Insira a segunda palavra:")

