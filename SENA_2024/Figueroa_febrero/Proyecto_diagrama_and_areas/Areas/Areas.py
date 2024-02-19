class calculadora: 

    class operaciones: 
        def area(self): 
            pass 

        def perimetro(self): 
            pass
    class triangulo(operaciones): 
        def area(self,b,a):
            suma = b * a /2 
            return f"El area del triangulo es: {suma}"
        
        def perimetro(self,l1,l2,l3):
            suma = l1 + l2 +l3
            return f"El perimetro es: {suma}"
        
    class cuadrado(operaciones): 
        def area(self,a):
            suma = a  ** 2
            return  f"El area del Cuadradp es: {suma}"
        
        def perimetro(self,a):
            suma = a * 4
            return f"El perimetro del Cuadrado es: {suma}"

    class rectangulo(operaciones):
        def area(self,b,a):
            suma = b * a 
            return f"El area del rectangulo es: {suma}"
        
        def perimetro(self,b,a):
            suma = (2* b ) + (2 * a)
            return f"El perimetrop del rectangulo es: {suma}"
        
    class rombo(operaciones): 
        def area(self,dn,dm):
            suma = dm * dn /2
            return f"El area del rombo es: {suma}"
        
        def perimetro(self,l):
            suma =  l *4 
            return f"El perimetro del rombo es: {suma}"
        
    class romboide(operaciones): 
        def area(self,b,a):
            suma = b * a 
            return f"El area del rombiode es: {suma}"
        
        def perimetro(self,b,a):
            suma = (2*b) + (2*a)
            return f"El perimetro del rombiode es: {suma}"


    class trapecio(operaciones): 
        def area(self,bm,bn,a):
            suma = a*(bm + bn ) /2
            return f"El area del trapecio es: {suma}"
        
        def perimetro(self,bm,bn,a):
            suma = bm + bn + a 
            return f"El perimetro del trapecio es: {suma}"

# triangulo_obj = triangulo()
# cuadrado_obj = cuadrado()
# rectangulo_obj = rectangulo()
# rombo_obj = rombo()
# romboide_obj = romboide()
# trapecio_obj = trapecio()
        
class menu():
    def __init__(self):
        while True: 
            print("!Bienvenido al menú de aras y perimetros.¡")
            menu = input(" 1. Triángulo, 2. Cuadrado, 3. Rectángulo, 4. Rombo, 5.  Romboide, 6. Trapecio, 7. salir\n")
            if bool(menu) == False: print("Losiento pero el dato no pude estar vacio..")

            else: 
                opc = input("1. Areas, 2. Perimetros\n")
                if bool(opc) == False : print("Lo siento pero el dato no pude estar vacio..")
                calculator = calculadora()

            if menu == "1":
                programa = calculator.triangulo()
                if opc == "1": print(programa.area(float(input("ingresa la base \n")),
                                                   float(input("ingresa la altura\n"))))
                    
                if opc == "2": print(programa.perimetro(float(input("ingresa el primer lado \n")),
                                                        float(input("ingresa el segundo lado \n")),
                                                        float(input("ingresa el tercer lado \n"))))
                    
            if menu == "2":
                programa = calculator.cuadrado()
                if opc == "1": print(programa.area(float(input("Ingresa el lado\n"))))
                if opc == "2": print(programa.perimetro(float(input("Ingresa el lado\n"))))

            if menu == "3": 
                programa = calculator.rectangulo()
                if opc == "1": print(programa.area(float(input("Ingresa la base\n")),
                                                   float(input("Ingresa la altura\n"))))
                    
                if opc == "2": print(programa.perimetro(float(input("Ingresa la base\n")),
                                                        float(input("Ingresa la altura\n"))))
                    
            if menu == "4": 
                programa = calculator.rombo()
                if opc == "1": print(programa.area(float(input("Ingresa la diagonal mayor\n")),
                                                   float(input("Ingresa la diagonal menor\n"))))
                    
                if opc == "2": print(programa.perimetro(float(input("Ingresa el lado\n"))))

            if menu == "5": 
                programa = calculator.romboide()
                if opc == "1": print(programa.area(float(input("Ingresa la base\n")),
                                                   float(input("Ingresa la altura\n"))))
                    
                if opc == "2": print(programa.perimetro(float(input("Ingresa la base\n")),
                                                        float(input("Ingresa la altura\n")))) 
                    
            if menu == "6": 
                programa = calculator.trapecio()
                if opc == "1": print(programa.area(float(input("Ingresa la base mayor\n")),
                                                  float(input("Ingresa la base menor\n")),
                                                  float(input("Ingresa la altura\n"))))
                    
                if opc == "2": print(programa.perimetro(float(input("Ingresa el lado 1\n")),
                                                        float(input("Ingresa el lado 2\n")),
                                                        float(input("Ingresa el lado 3\n"))))

            if menu == "7": 
                break

menu()