import os

class operBasicas:
    #Declaración de propiedades
    #Variables "globales"

    num1 = 0
    num2 = 0
    res = 0
    
    #Declaración de constructor
    #self == this
    #todas los metodos que forman parte de la clase deben llevar (self)

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    #Declaración de métodos de clase 

    def suma(self):
        #num1 = 12
        #num2 = 10
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))
    
    def resta(self):

        self.res = self.num1 - self.num2
        print("La resta es: {}".format(self.res))
    
    def multi(self):

        self.res = self.num1 * self.num2
        print("La multiplicacion es: {}".format(self.res))
    
    def divi(self):

        self.res = self.num1 / self.num2
        print("La división es: {}".format(self.res))

def  main():     
        
        op = 0
        while op != 5:
            
            op = int(input("Menu\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Salir "))

            if op == 1:
                numero1 = int(input("Ingrese el num1 "))
                numero2 = int(input("Ingrese el num2 "))
                obj = operBasicas(numero1,numero2)
                obj.suma()
                
            
            elif op == 2:
                numero1 = int(input("Ingrese el num1 "))
                numero2 = int(input("Ingrese el num2 "))
                obj = operBasicas(numero1,numero2)
                obj.resta()
                

            elif op == 3:
                numero1 = int(input("Ingrese el num1 "))
                numero2 = int(input("Ingrese el num2 "))
                obj = operBasicas(numero1,numero2)    
                obj.multi()
                

            elif op == 4:
                numero1 = int(input("Ingrese el num1 "))
                numero2 = int(input("Ingrese el num2 "))
                obj = operBasicas(numero1,numero2)   
                obj.divi()
                
        os.system('cls')
                
                

if __name__ == "__main__":
    main()