def verificar():

    idade = []
    sono=[]
    peso=[]

idade = int(input("Informe sua idade:"))
peso = int(input("informe seu peso:"))
sono = int(input("Informe quantas horas de sono você teve nas ultimas 24 horas:"))
napto = ""
apto = 0

if idade > 16 and idade < 69:
  apto = apto + 1
else :
  napto = "idade" + napto

if peso > 50:
  apto = apto + 1
else :
  napto = "peso " + napto

if sono > 6:
  apto = apto + 1
else :
  napto = "sono" + napto

if apto == 3:
  print("Apto para Doação")
else :
  print("Você não esta apto para doação")


#FIQUEI UM TEMPÃO NESSA MT DIFICIL
#NÃO CONSEGUI FAZER A 6.2 NEM NA OUTRA E CONSEQUENTEMENTE NEM NESSA.FOI MAL