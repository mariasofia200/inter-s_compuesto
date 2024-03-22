# input

c = int(input("digite el valor de c: "))

# prossecing 

n = 0
d = 2 * c

while (c<=d):
    n= n+1
    c= c +5*c/100

# output

print("la capital acumulada es" , c)

print("su capital inicial se duplico en: " , n ,"meses")