c = 0

while c == 0:
    a = int(input("Pune un numar: "))  # numar
    operatie = input("Pune semnul operatiei (+, -, x,:) ")  # operatie
    b = int(input("Pune al doilea numar: "))  # alt numar

    if operatie == "+":
        print(a, "+", b, "=", a + b)
    elif operatie == "-":
        print(a, "-", b, "=", a - b)
    
    elif operatie==":": 
       d = a % b
       print(a,":",b,"=",a/b,"sau cu rest este",a//b,"si a ramas",d)
    
    elif operatie == "x":
        print(a, "x", b, "=", a * b)
    else:
        print("Operatie invalida")
    

    s = 1
    while s == 1:
        d = input("Vrei sa iesi? Da/Nu: ")
        if d.lower() == "da":
            c = 1
            s = 0
        elif d.lower() == "nu":
            s = 0
        else:
            print("Raspuns invalid. Te rog sa introduci 'Da' sau 'Nu'.")
