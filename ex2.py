def c(n):
        if n==0:
            return c0
        else:
             return  ((c(n-1)+12*m)*(1+t/100))

print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an.")

c0=int(input("Entrez le placement de départ:"))
m=int(input("Entrez le montant du versement mensuel:"))
t=float(input("Entrez le taux annuel en %:"))
n=int(input("Entrez le nombre d'année:"))

print("Le capital acquis avec intérêts est de", round(c(n),2),"euros au bout de",n,"ans avec des versement mensuels de",m,"euros.")
print("Les intérêts ganés au taux annuel de",t,"% sont de", round(c(n)-n*m*12+c0,2),"euros.")
print("Sans placement avec les intérêts le capital acquis serait de", round(n*m*12+c0,2),"euros.")