import math

l =9


def d(n):
    return(d0+2*l*n)

d0= float(input("Entrez le diamètre de l'axe en mm:"))
n=int(input("Entre nombre de tours n:"))

print("\nCalcul de la longueur L pour chaque tours:")
L=0
for i in range (n):
    L=L+math.pi*d(i)
    print("Tour:",i+1,"-Diamètre[mm]:",round(d(i+1),1),"-Loungueur enroulée [mm]:",round(L))


print("\nCalcul de la longueur L par formule:")
c0=math.pi*d(0)
cn=math.pi*d(n-1)
L=(c0*cn)*(n+0)/2
print("Longueur [mm] pour",n, "tours:",L)