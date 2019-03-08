a=int(input("Ingrese un número: "))
c=0
for i in range(1, a):
    b=a%i
    if b==0:
        c=c+1
        if c==2:
            print("El número no es primo")


    else:
        if c==1:
            print("el número es primo")
            break





