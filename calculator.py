import style
import os

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations and prints the results.
    """
    def __init__(self, text="", question="What operation do you want to do?: ", output="Result: "):
        '''
        Initialize the calculator with optional text and question
        '''
        self.__text = text
        self.__question = f"{question}"
        self.__output = f"{output}"

    def add(self, arguments):
        '''
        This function adds all the provided arguments and prints the result
        '''
        total = 0
        for arg in arguments:
            total += arg  # Add each argument to the total
        
        print(self.__text, total)  # Print the result with the optional text

    def subtract(self, arguments):
        '''
        This function subtracts all the provided arguments from the first one and prints the result
        '''
        total = None
        for arg in arguments:
            if total is None:
                total = arg  # Initialize total with the first argument
                continue
            total -= arg  # Subtract each subsequent argument from the total
        print(self.__text, total)  # Print the result with the optional text

    def divide(self, arguments):
        '''
        This function divides the first argument by the subsequent arguments and prints the result
        '''
        total = None
        for arg in arguments:
            if total is None:
                total = arg  # Initialize total with the first argument
            else:
                total /= arg  # Divide total by each subsequent argument

        print(self.__text, total)  # Print the result with the optional text

    def multiply(self, arguments):
        '''
        This function multiplies all the provided arguments and prints the result
        '''
        total = None
        for arg in arguments:
            if total is None:
                total = arg  # Initialize total with the first argument
            else:
                total *= arg  # Multiply total by each subsequent argument

        print(self.__text, total)  # Print the result with the optional text

    def square_root(self, arg):
        '''
        This function calculates the square root of the provided argument and prints the result
        '''
        if arg < 0:
            print(self.__text, "Error: Negative input")  # Handle negative input
            return

        guess = arg / 2.0
        tolerance = 0.000001
        while abs(guess * guess - arg) > tolerance:
            guess = (guess + arg / guess) / 2.0  # Improve the guess using Newton's method

        print(self.__text, guess)  # Print the square root of the argument with the optional text
        
    def power(self, base, exp):
        '''
        This function raises the base to the power of exp and prints the result
        '''
        print(self.__text, base ** exp)  # Print the result of base raised to the power of exp with the optional text
        
    def lcm(self, n1, n2):
        '''
        This function calculates the least common multiple of two numbers and prints the result
        '''
        result = 0
        m1 = [n1 * i for i in range(1, 51)]  # Generate multiples of n1
        m2 = [n2 * i for i in range(1, 51)]  # Generate multiples of n2

        for num in m1:
            if num in m2:
                result = num  # Find the first common multiple
                break

        print(self.__text, result)  # Print the least common multiple with the optional text

    def gcd(self, n1, n2):
        '''
        This function calculates the greatest common divisor of two numbers and prints the result
        '''
        n1_factors = []
        n2_factors = []
        factorize_n1 = [2, 3, 5, 7, 11, n1]  # List of potential factors for n1
        factorize_n2 = [2, 3, 5, 7, 11, n2]  # List of potential factors for n2

        i = 0
        while n1 != 1:
            if n1 % factorize_n1[i] == 0:
                n1_factors.append(factorize_n1[i])  # Add factor to n1_factors
                n1 /= factorize_n1[i] 
            else:
                i += 1
        i = 0
        while n2 != 1:
            if n2 % factorize_n2[i] == 0:
                n2_factors.append(factorize_n2[i])  # Add factor to n2_factors
                n2 /= factorize_n1[i] 
            else:
                i += 1

        final_equation = []
        for num in n1_factors:
            if num in n2_factors and num not in final_equation:
                if n1_factors.count(num) > n2_factors.count(num):
                    for i in range(n2_factors.count(num)):
                        final_equation.append(num)  # Add common factors to final_equation
                else: 
                    for i in range(n1_factors.count(num)):
                        final_equation.append(num)

        total = None
        for arg in final_equation:
            if total is None:
                total = arg  # Initialize total with the first common factor
            else:
                total *= arg  # Multiply total by each subsequent common factor
                
        print(self.__text, total)  # Print the greatest common divisor with the optional text
       
    def start_program(self):
        '''
        This function starts the calculator program and prompts the user to choose an operation
        '''
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(style.color.azul + "\tWelcome to the Calculator Program!" + style.color.RESET)

        print(style.color.cyan + "\n1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Square Root")
        print("6. Power")
        print("7. Least Common Multiple")
        print("8. Greatest Common Divisor" + style.color.RESET)

        try:
            response = int(input(style.color.purpura + f"\n{self.__question}" + style.color.RESET))  # Get user input for the operation

        except ValueError:
            print(style.color.rojo + "\nInvalid input. Please enter a valid number between 1 and 8." + style.color.RESET)
            return
        
        except KeyboardInterrupt:
            print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
            return

        calc = Calculator(style.color.orange + f"\n{self.__output}" + style.color.RESET)  # Create a new calculator object with the specified output text

        if response == 1:
            numers = []
            try:
                num_count = int(input(style.color.purpura + "\nHow many numbers do you want to add? " + style.color.RESET))
            
            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return
            
            print() # Add a new line for better readability

            for i in range(num_count):
                try:
                    print() # Add a new line for better readability
                    num = int(input(style.color.amarillo + f"Number {i+1}: " + style.color.RESET))  # Get user input for the numbers to add
                    
                except KeyboardInterrupt:
                    print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                    return
                
                except ValueError:
                    print(style.color.rojo + "\nInvalid input. Please enter a valid number." + style.color.RESET)
                    return
            
                numers.append(num)

            calc.add(numers)  # Perform addition

        elif response == 2:
            numers = []
            try:
                num_count = int(input(style.color.purpura + "\nHow many numbers do you want to subtract? " + style.color.RESET))
            
            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return
            
            print() # Add a new line for better readability

            for i in range(num_count):
                try:
                    print() # Add a new line for better readability
                    num = int(input(style.color.amarillo + f"Number {i+1}: " + style.color.RESET))  # Get user input for the numbers to subtract
                    numers.append(num)

                except ValueError:
                    print(style.color.rojo + "\nInvalid input. Please enter a valid number." + style.color.RESET)
                    return
                
                except KeyboardInterrupt:
                    print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                    return

            calc.subtract(numers)  # Perform subtraction

        elif response == 3:
            try:
                print() # Add a new line for better readability
                try:
                    n1 = int(input(style.color.amarillo + "Dividend: " + style.color.RESET))
                    n2 = int(input(style.color.amarillo + "Divisor: " + style.color.RESET))
                
                except KeyboardInterrupt:
                    print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                    return
                
                except ZeroDivisionError:
                    print(style.color.rojo + "\nError: Cannot divide by zero." + style.color.RESET)
                    return
                
                print() # Add a new line for better readability
                
            except ValueError:
                print(style.color.rojo + "\nInvalid input. Please enter valid numbers." + style.color.RESET)
                return
            
            calc.divide([n1, n2])  # Perform division

        elif response == 4:
            numers = []
            try:
                num_count = int(input(style.color.purpura + "\nHow many numbers do you want to multiply? " + style.color.RESET))
            
            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return
            
            print() # Add a new line for better readability

            for i in range(num_count):
                try:
                    print() # Add a new line for better readability
                    num = int(input(style.color.amarillo + f"Number {i+1}: " + style.color.RESET))  # Get user input for the numbers to multiply
                    numers.append(num)

                except ValueError:
                    print(style.color.rojo + "\nInvalid input. Please enter a valid number." + style.color.RESET)
                    return
                
                except KeyboardInterrupt:
                    print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                    return

            calc.multiply(numers)  # Perform multiplication

        elif response == 5:
            try:
                print() # Add a new line for better readability
                n1 = int(input(style.color.amarillo + "\nNumber to calculate square root: " + style.color.RESET))
                if n1 < 0:
                    print(style.color.rojo + "\nError: Cannot calculate square root of negative numbers." + style.color.RESET)
                    return
                
            except ValueError:
                print(style.color.rojo + "\nInvalid input. Please enter a valid number." + style.color.RESET)
                return
            
            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return
            
            calc.square_root(n1)  # Calculate square root

        elif response == 6:
            try:
                print() # Add a new line for better readability
                n1 = int(input(style.color.amarillo + "Base: " + style.color.RESET))
                n2 = int(input(style.color.amarillo + "Exponent: " + style.color.RESET))                
                print() # Add a new line for better readability

            except ValueError:
                print(style.color.rojo + "\nInvalid input. Please enter valid numbers." + style.color.RESET)
                return
            
            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return
            
            calc.power(n1, n2)  # Calculate power

        elif response == 7:
            try:
                print() # Add a new line for better readability
                n1 = int(input(style.color.amarillo + "Number 1: " + style.color.RESET))
                n2 = int(input(style.color.amarillo + "Number 2: " + style.color.RESET))
                print() # Add a new line for better readability

            except ValueError:
                print(style.color.rojo + "\nInvalid input. Please enter valid numbers." + style.color.RESET)
                return
            
            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return
            
            calc.lcm(n1, n2)  # Calculate least common multiple

        elif response == 8:
            try:
                n1 = int(input(style.color.amarillo + "Number 1: " + style.color.RESET))
                n2 = int(input(style.color.amarillo + "Number 2: " + style.color.RESET))
                print() # Add a new line for better readability

            except ValueError:
                print(style.color.rojo + "\nInvalid input. Please enter valid numbers." + style.color.RESET)
                return

            except KeyboardInterrupt:
                print(style.color.amarillo + "\nExiting the program..." + style.color.RESET)
                return

            calc.gcd(n1, n2)  # Calculate greatest common divisor

# Code Testing
if __name__ == "__main__":
    calc = Calculator(output="Result: ")  # Create a calculator object with the specified output text
    calc.start_program()  # Start the calculator program