import calc

num= int(input("Digite um valor:"))

fat=calc.fatorial(num)
dob=calc.dobro(num)
trip=calc.triplo(num)

print(f"O fatorial do {num} é {fat}")
print(f"O dobro do {num} é {dob}")
print(f"O triplo do {num} é {trip}")