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