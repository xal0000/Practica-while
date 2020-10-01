
n=int(input("n"))
numero=1
i=1
while(i<=n):
    b=0
    a=1
    while(a<=i):
        b=numero+b
        a=a+1
    numero=b
    i=i+1
    print(numero,)

