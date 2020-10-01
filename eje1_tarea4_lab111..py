n=int(input("n"))
i=0
while(i<n):
    x=float(input("costo del pasaje sin tarjeta:"))
    y=float(input("costo del pasaje con tarjeta:"))
    a=float(input("costo de la tarjeta:"))
    b=float(input("carga inicial de la tarjeta:"))
    if(x>y):
        cds=0
        d=0
        q=b%(y*2)
        m=b//(y*2)
        ds=x*2
        dc=y*2
        cc=a-b
        while(cds<cc):
            cc=cc+dc
            cds=cds+ds
            d=d+1
        if(d>5):
            p=d%5
            z=d//5
            print(z,"SEMANAS",p,"DIAS")
        else:
            print(d,"dias")
    else:
        print("NO SE RECUPERA")
    i=i+1

