"""Scrieţi un program care citeşte de la tastatură elementele mulţimilor A şi B şi afişează pe ecran:
a) intersecţia mulţimilor A şi B;
b) reuniunea mulţimilor A şi B;
c) diferenţa mulţimilor A şi B;
Mulţimile A şi B sunt formate din literele mari ale alfabetului latin."""
A=set()
i=1
while i!=0:
    x=input("Dati o litera:")
    y=x.upper()
    A.add(y)
    i=int(input("dati 0 in caz ca nu mai aveti nevoie de elemente in multime:"))
B=set()
i=1
while i!=0:
    x=input("Dati o litera:")
    y=x.upper()
    B.add(y)
    i=int(input("dati 0 in caz ca nu mai aveti nevoie de elemente in multime:"))
print(A)
print(B)
print("a)Intersectia multimilor A si B este",A.intersection(B))
print("b)Reuniunea multimilor A si B este",A.union(B))
print("c)Diferenta multimilor A si B este",A.difference(B),"\n","Iar diferenta multimilor B si A este",B.difference(A))
