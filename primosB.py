c1=1
c=0
num=int(input("Introduzaca un número: "))
while c1<num+1:
    if num%c1==0:
        c+=1
    c1+=1
if c>2:
    print("No es primo")
else:
    print("Si es primo")


