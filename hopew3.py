g=0
s=0
l=0
z=0
x=0
while z==0 or l!=0:
    x=int(input("dati cifra: "))
    z=x%2
    l=x%3
    if(z==0):
        s=x+g
        g=s
print(s) 