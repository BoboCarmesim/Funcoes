def linha():
    print(50*"-")

def somar (a=0,b=0,c=0,):
    s=a+b+c
    print(f"A soma é de {s}")

somar(4,5,6)

linha()

def teste ():
    print (f"Na função teste n tem valor de {n}")

n=2
print(f"No programa n vale {n}")
teste()

linha()

def teste2 ():
    x=3
    print (f"Na função teste n tem valor de {n}")
    print (f"Na função teste x tem valor de {x}")

n=4
print(f"No programa n vale {n}")
teste2()

linha()

def teste3(b):
    a=2
    b+=3
    print (f"Na função teste n tem valor de {a}")
    print (f"Na função teste x tem valor de {b}")

a=5
teste3(a)

linha()

def somar1(a=0,b=0,c=0):
    s=a+b+c
    return s
r1=somar1(3,4,7)
r2=somar1(3,4)
r3=somar1(3)
print(f"As somas deram, {r1},{r2} e {r3}")

linha()

def fatorial(num=1):
    f=1
    for c in range (num,0,-1):
        f*=c
    return f

n = int(input("Digite um numero:"))
print(f"O fatorial de {n} é de = {fatorial(n)}")

linha()

def parimpar(num=0):
    if num % 2 == 0 :
        return True
    else:
        return False

num=int(input("Digite um numero:"))
if parimpar(num):
    print("É Par")
else:
    print("É impar")