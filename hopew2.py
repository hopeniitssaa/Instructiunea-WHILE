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
    
    

    
    
    
    t=t+1
a=z/n
b=h/m
print(round(a,2))
print(round(b,2)) 