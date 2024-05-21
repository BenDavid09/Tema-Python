
a = int(input("Pune un numar "))#numar

operatie  = input("Pune semnul operatiei ")#operrratie

b = int(input("Pune al doilea numar "))#alt numar



if(operatie== "+"):
   print(a,"+",b,"=",a+b)
elif (operatie== "-"):
   print(a,"-",b,"=",a-b)
elif (operatie == "x"):
   print(a,"x",b,"=",a*b)

elif(operatie==":"):
   d = a % b
   print(a,":",b,"=",a/b,"sau cu rest este",a//b,"si a ramas",d)
else:
   print("Nu ai pus semnul operatiei data viitoare sa pui semnul operatiei")
