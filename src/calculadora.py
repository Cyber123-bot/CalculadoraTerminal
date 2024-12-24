# Importar las bibliotecas necesarias
import estilos
import os

class Calculadora:
    """
    Esta clase es una calculadora que realiza operaciones aritméticas básicas y muestra los resultados.
    """
    def __init__(self, texto="", pregunta="¿Qué operación deseas realizar?: ", salida="Resultado: "):
        '''
        Inicializa la calculadora con texto y pregunta opcionales.
        '''
        self.__texto = texto
        self.__pregunta = f"{pregunta}"
        self.__salida = f"{salida}"

    def factorizacion(self, n):
        '''
        Esta función calcula la factorización prima de un número y muestra el resultado.
        '''
        # Si el número es menor o igual a 1, lanza un error
        if n <= 1:
            print(f"Error: La factorización no está definida para números <= 1.")
            return

        # Calcula los factores primos del número y muestra el resultado
        try:
            # Encuentra los factores primos del número
            i = 2
            factores = []

            while i * i <= n:

                if n % i:
                    i += 1

                else:
                    n //= i
                    factores.append(i)
    
            if n > 1:
                factores.append(n)

        # Maneja entradas no válidas
        except ValueError:
            print("Error: Entrada no válida.")
            return

        # Muestra los factores primos unidos por ' x ' para mayor legibilidad
        print(f"{self.__texto}{' x '.join(map(str, factores))}")

    def porcentaje(self, n1, n2):
        '''
        Esta función calcula el porcentaje de n1 con respecto a n2 y muestra el resultado.
        '''
        try:
            resultado = (n1 / n2) * 100  # Calcula el porcentaje
            print(self.__texto, resultado)  # Muestra el resultado con el texto opcional

        # Maneja errores de división por cero
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
            return
        
        # Maneja entradas no válidas
        except ValueError:
            print("Error: Entrada no válida.")
            return
    
    def sumar(self, args):
        '''
        Esta función suma todos los argumentos proporcionados y muestra el resultado.
        '''
        try:
            total = 0
            for arg in args:
                if not isinstance(arg, (int, float)):  # Verifica si el argumento es un número
                    raise ValueError(f"Entrada no válida: {arg} no es un número")
                
                total += arg
            
            print(f"{self.__texto}{total}")  # Muestra el resultado con el texto opcional
        
        # Maneja entradas no válidas
        except ValueError:
            print(f"Error: Entrada no válida.")
            return

    def restar(self, argumentos):
        '''
        Esta función resta todos los argumentos proporcionados del primero y muestra el resultado.
        '''
        try:
            total = None
            for arg in argumentos:
                if total is None:
                    total = arg  # Inicializa el total con el primer argumento
                    continue
                total -= arg  # Resta cada argumento posterior al total
            print(self.__texto, total)  # Muestra el resultado con el texto opcional

        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return

    def dividir(self, argumentos):
        '''
        Esta función divide el primer argumento por los argumentos posteriores y muestra el resultado.
        '''
        try:
            total = None
            for arg in argumentos:
                if total is None:
                    total = arg  # Inicializa el total con el primer argumento
                else:
                    total /= arg  # Divide el total por cada argumento posterior

            print(self.__texto, total)  # Muestra el resultado con el texto opcional

        # Maneja errores de división por cero
        except ZeroDivisionError:
            print(self.__texto, "Error: No se puede dividir por cero.")
            return

        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return

    def multiplicar(self, argumentos):
        '''
        Esta función multiplica todos los argumentos proporcionados y muestra el resultado.
        '''
        try:
            total = None
            for arg in argumentos:
                if total is None:
                    total = arg  # Inicializa el total con el primer argumento
                else:
                    total *= arg  # Multiplica el total por cada argumento posterior

            print(self.__texto, total)  # Muestra el resultado con el texto opcional

        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return

    def raizCuadrada(self, arg):
        '''
        Esta función calcula la raíz cuadrada del argumento proporcionado y muestra el resultado.
        '''
        try:
            if arg < 0:
                print(self.__texto, "Error: Entrada negativa")  # Maneja la entrada negativa
                return

            suposicion = arg / 2.0
            tolerancia = 0.000001
            while abs(suposicion * suposicion - arg) > tolerancia:
                suposicion = (suposicion + arg / suposicion) / 2.0  # Mejora la suposición usando el método de Newton

            print(self.__texto, suposicion)  # Muestra la raíz cuadrada del argumento con el texto opcional

        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return

    def raizCubica(self, arg):
        '''
        Esta función calcula la raíz cúbica del argumento proporcionado y muestra el resultado.
        '''
        try:
            if arg < 0:
                es_negativo = True
                arg = -arg  # Trabaja con el valor absoluto para el cálculo
            else:
                es_negativo = False

            suposicion = arg / 3.0
            tolerancia = 0.000001
            while abs(suposicion * suposicion * suposicion - arg) > tolerancia:
                suposicion = (2 * suposicion + arg / (suposicion * suposicion)) / 3.0
    
            if es_negativo:
                suposicion = -suposicion  # Ajusta el resultado a negativo si el número original era negativo
    
            print(self.__texto, suposicion)  # Muestra la raíz cúbica del argumento con el texto opcional
        
        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return


    def potencia(self, base, exp):
        '''
        Esta función eleva la base a la potencia de exp y muestra el resultado.
        '''
        try:
            print(self.__texto, base ** exp)  # Muestra el resultado de base elevado a la potencia de exp con el texto opcional
        
        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return
        
    def mcm(self, n1, n2):
        '''
        Esta función calcula el mínimo común múltiplo de dos números y muestra el resultado.
        '''
        try:
            resultado = 0
            m1 = [n1 * i for i in range(1, 51)]  # Genera múltiplos de n1
            m2 = [n2 * i for i in range(1, 51)]  # Genera múltiplos de n2

            for num in m1:
                if num in m2:
                    resultado = num  # Encuentra el primer múltiplo común
                    break

            print(self.__texto, resultado)  # Muestra el mínimo común múltiplo con el texto opcional

        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return

    def mcd(self, n1, n2):
        '''
        Esta función calcula el máximo común divisor (MCD) de dos números usando el algoritmo de Euclides 
        y muestra el resultado.
        '''
        try:
            # Aplica el algoritmo de Euclides
            while n2 != 0:
                n1, n2 = n2, n1 % n2  # Intercambia n1 con n2 y asigna a n2 el residuo de n1 dividido por n2
    
            print(self.__texto, n1)  # Muestra el máximo común divisor con el texto opcional

        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return
       
    def restoDivision(self, n1, n2):
        '''
        Esta función calcula el resto de la división de dos números y muestra el resultado.
        '''
        try:
            resultado = n1 % n2
            print(self.__texto, resultado)  # Muestra el resultado con el texto opcional
        
        # Maneja errores de división por cero
        except ZeroDivisionError:
            print(self.__texto, "Error: No se puede dividir por cero.")
            return
        
        # Maneja entradas no válidas
        except ValueError:
            print(self.__texto, "Error: Entrada no válida.")
            return
        
    def iniciarPrograma(self):
        '''
        Esta función inicia el programa de la calculadora y solicita al usuario elegir una operación.
        '''
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla del terminal

        # Muestra el mensaje de bienvenida
        print(estilos.color.azul + "\t¡Bienvenido al programa de la calculadora!" + estilos.color.RESET)

        print(estilos.color.cian + "\n1. Sumar")
        print("2. Restar")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Raíz cuadrada")
        print("6. Potencia")
        print("7. Mínimo común múltiplo")
        print("8. Máximo común divisor")
        print("9. Resto de la división")
        print("10. Factorización prima")
        print("11. Raíz cúbica")
        print("12. Porcentaje de un número" + estilos.color.RESET)

        try:
            # Obtiene la entrada del usuario para la operación deseada
            respuesta = int(input(estilos.color.purpura + f"\n{self.__pregunta}" + estilos.color.RESET))

        # Maneja los errores de entrada no válida
        except ValueError:
            print(estilos.color.rojo + "\nEntrada no válida. Por favor, ingresa un número válido entre 1 y 8." + estilos.color.RESET)
            return
        
        # Maneja la interrupción del teclado
        except KeyboardInterrupt:
            print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
            return

        # Crea un nuevo objeto calculadora con el texto de salida especificado
        calc = Calculadora(estilos.color.naranga + f"\n{self.__salida}" + estilos.color.RESET)  
        
        # Sumar
        if respuesta == 1:
            numeros = [] # Lista para almacenar los números a sumar

            try:
                num_count = int(input(estilos.color.purpura + "\n¿Cuántos números deseas sumar? " + estilos.color.RESET))

                # Obtiene los números a sumar
                for i in range(num_count):
                    numeros.append(float(input(estilos.color.purpura + f"\nIntroduce el número {i + 1}: " + estilos.color.RESET)))
            
                calc.sumar(numeros) # Suma los números y muestra el resultado

            # Maneja la interrupción del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return
        
        # Restar
        elif respuesta == 2:
            numeros = [] # Lista para almacenar los números a restar
            try:
                num_count = int(input(estilos.color.purpura + "\n¿Cuántos números deseas restar? " + estilos.color.RESET))
                
                # Obtiene los números a restar
                for i in range(num_count):
                    numeros.append(float(input(estilos.color.purpura + f"\nIntroduce el número {i + 1}: " + estilos.color.RESET)))

                calc.restar(numeros) # Resta los números y muestra el resultado

            # Maneja la interrupción del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Dividir
        elif respuesta == 3:
            numeradores = [] # Lista para almacenar los valores a dividir
            try:
                num_count = int(input(estilos.color.purpura + "\n¿Cuántos números deseas dividir? " + estilos.color.RESET))
                
                # Obtiene los valores a dividir
                for i in range(num_count):
                    numeradores.append(float(input(estilos.color.purpura + f"\nIntroduce el número {i + 1}: " + estilos.color.RESET)))

                calc.dividir(numeradores) # Divide los números y muestra el resultado
            
            # Maneja la interrupción del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Multiplicar
        elif respuesta == 4:
            numeros = []
            try:
                num_count = int(input(estilos.color.purpura + "\n¿Cuántos números deseas multiplicar? " + estilos.color.RESET))
                
                # Obtiene los valores a multiplicar
                for i in range(num_count):
                    numeros.append(float(input(estilos.color.purpura + f"\nIntroduce el número {i + 1}: " + estilos.color.RESET)))

                calc.multiplicar(numeros) # Multiplica los números y muestra el resultado

            # Maneja las interrupciones del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return
            
            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Raiz cuadrada
        elif respuesta == 5:
            try:
                n = float(input(estilos.color.purpura + "\nIntroduce un número para calcular su raíz cuadrada: " + estilos.color.RESET))
                calc.raizCuadrada(n) # Calcula la raiz cuadrada del número y muestra el resultado


            # Maneja las interrupciones del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return
            
            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Potencia
        elif respuesta == 6:
            try:
                n = float(input(estilos.color.purpura + "\nIntroduce la base: " + estilos.color.RESET))
                exp = float(input(estilos.color.purpura + "\nIntroduce el exponente: " + estilos.color.RESET))
                calc.potencia(n, exp) # Calcula la potencia y muestra el resultado
            
            # Maneja las interrupciones del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Mínimo común múltiplo
        elif respuesta == 7:
            try:
                n1 = int(input(estilos.color.purpura + "\nIntroduce el primer número: " + estilos.color.RESET))
                n2 = int(input(estilos.color.purpura + "\nIntroduce el segundo número: " + estilos.color.RESET))
                calc.mcm(n1, n2) # Calcula el mcm y muestra el resultado

            # Maneja interrupciones del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return
        
        # Máximo común divisor
        elif respuesta == 8:
            try:
                n1 = int(input(estilos.color.purpura + "\nIntroduce el primer número: " + estilos.color.RESET))
                n2 = int(input(estilos.color.purpura + "\nIntroduce el segundo número: " + estilos.color.RESET))
                calc.mcd(n1, n2) # Calcula el mcd y muestra el resultado

            # Maneja interrupciones de teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Resto de la división
        elif respuesta == 9:
            try:
                n1 = float(input(estilos.color.purpura + "\nIntroduce el primer número: " + estilos.color.RESET))
                n2 = float(input(estilos.color.purpura + "\nIntroduce el segundo número: " + estilos.color.RESET))
                calc.restoDivision(n1, n2) # Divide los números y muestra el resto

            # Maneja interrupciones de teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return
            
            # Maneja entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Factorización
        elif respuesta == 10:
            try:
                n = int(input(estilos.color.purpura + "\nIntroduce un número para su factorización: " + estilos.color.RESET))
                calc.factorizacion(n) # Factoriza el número y muestra el resultado

            # Maneja las interrupciones de teclado            
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Raiz cúbica
        elif respuesta == 11:
            try:
                n = float(input(estilos.color.purpura + "\nIntroduce un número para calcular su raíz cúbica: " + estilos.color.RESET))
                calc.raizCubica(n) # Calcula la raiz cúbica del número y muestra el resultado
            
            # Maneja las interrupciones del teclado
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return
            
            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

        # Porcentanje
        elif respuesta == 12:
            try:
                n1 = float(input(estilos.color.purpura + "\nIntroduce el valor que representa el primer número: " + estilos.color.RESET))
                n2 = float(input(estilos.color.purpura + "\nIntroduce el segundo número para el porcentaje: " + estilos.color.RESET))
                calc.porcentaje(n1, n2) # Calcula el porcentaje y muestra el resultado

            # Maneja las entradas no válidas
            except KeyboardInterrupt:
                print(estilos.color.amarillo + "\nSaliendo del programa..." + estilos.color.RESET)
                return

            # Maneja las entradas no válidas
            except ValueError:
                print(estilos.color.rojo + "\nEntrada no válida." + estilos.color.RESET)
                return

if __name__ == "__main__":
    calc = Calculadora()
    calc.iniciarPrograma()
