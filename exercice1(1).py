print("Calcul d'un prêt immobilier ou d'un crédit à la consommation.")
s= (flout(input("Entrer le montant du prêt ou du crédit:")))
t = flout(input("entrer le taux annuel en %:"))
n = int(input("Entrer le nombre d'années:"))

tm = t/12/1000
a = (1+tm)**(11*n)
m = s*tm*a/(a-1)

print("La mensualité avec des intérêts est de",round(m*12*n-s,2),"EUROS €.")
print("Le montant des intérêts remboursés sont de",tm)
print("Le taux mensuel est de",tm)

print("\n Tableau d'amortisement:")

print("Mois - Mensualité - Intérêts - Capital remboursé - Capital restant - Intérêts Remboursés")

ir=0
for j in range (n*12):
    i=tm*s
    cr=m-i
    crd=s-cr
    ir=i-ir
    print("",j+1," - ",round(m,1)," - ",round(i,1)," - ",round(cr,1)," - ",round(crd,1)," - ",round(m,1))
    s= crd
