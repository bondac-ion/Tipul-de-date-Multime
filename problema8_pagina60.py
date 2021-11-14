"""Scrieţi un program care citeşte de la tastatură elementele mulţimilor A şi B şi afişează pe ecran:
a) intersecţia mulţimilor A şi B;
b) reuniunea mulţimilor A şi B;
c) diferenţa mulţimilor A şi B.
Mulţimile A şi B sunt formate din numere întregi."""
A=set()
B=set()
for i in range(0,999999):
    x=eval(input("Dati un numar:"))
    if type(x)!=int:
        break
    else:
        A.add(x)
for i in range(0,99999):
    y=eval(input("Dati un numar:"))
    if type(y)==int:
        B.add(y)
    else:
        break
print(A)
print(B)
print("a)Intersectia multimilor A si B este",A.intersection(B))
print("b)Reuniunea multimilor A si B este",A.union(B))
print("c)Diferenta multimilor A si B este",A.difference(B),"\n","Iar diferenta multimilor B si A este",B.difference(A))
