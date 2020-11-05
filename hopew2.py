l=0
h=0
z=0
s=0
m=0
n=0
t=0
while t <12:
    
    x=int(input("dati temperatura: "))
    
    if(x<0):
        z=x+s
        n=n+1
        s=z
    elif(x>=0):
        h=x+l
        m=m+1
        l=h 