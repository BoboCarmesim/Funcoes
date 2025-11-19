import math

def linha():
    print(50*"-")

linha()
print("                SISTEMA DE ALUNOS")
linha()


def titulo(msg):
    print(50*"-")
    print(msg)
    print(50*"-")

titulo("Sistema de alunos")
#texto=input("Digite uma mensagem: ")
#titulo(texto)

def soma(a,b):
    print(f"A = {a} e B = {b}")
    s = a+b
    print(f"A soma de A + B = {s}")
soma(4,5)

linha()
#resultA=int(input("Digite o valor A:"))
#resultB=int(input("Digite o valor B:"))
#soma(resultA,resultB)
#linha()

def contador (* num):
    print(num)
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
linha()

def contador(* num):
    for valor in num:
        print(f"{valor}",end="")
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
linha()

linha()
def contador(* num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
linha()

def somador (a,b,c):
    s= a+b+c
    print(f"Recebi 3 numeros e a soma é {s}")

#result1=int(input("Digite o primeiro valor:"))
#result2=int(input("Digite o segundo valor:"))
#result3=int(input("Digite o terceiro valor:"))
#somador(result1,result2,result3)

def dobra (lst):
    pos=0
    while pos < len(lst):
        lst [pos] *=2
        pos +=1

valores=[7,2,5,0,4]
dobra(valores)
print(valores)