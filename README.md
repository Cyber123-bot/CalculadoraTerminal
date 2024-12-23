# Proyecto de Calculadora

Este proyecto es una calculadora simple en Python que realiza varias operaciones matemáticas como suma, resta, multiplicación, división, raíz cuadrada, potencia, MCM (mínimo común múltiple), MCD (máximo común divisor), porcentaje, raíz cúbica, factorización prima y resto de la división.

## Características
- **Suma**: Suma dos números.
- **Resta**: Resta un número de otro.
- **Multiplicación**: Multiplica dos números.
- **División**: Divide un número por otro (con manejo de errores para división por cero).
- **Resto de la División**: Calcula el resto de la división (operación de módulo).
- **Raíz Cuadrada**: Calcula la raíz cuadrada de un número.
- **Raíz Cúbica**: Calcula la raíz cúbica de un número.
- **Potencia**: Calcula la potencia de un número (x^y).
- **MCM (Mínimo Común Múltiple)**: Encuentra el mínimo común múltiple de dos números.
- **MCD (Máximo Común Divisor)**: Encuentra el máximo común divisor de dos números.
- **Porcentaje**: Calcula el porcentaje de un número relativo a otro.
- **Factorización Prima**: Descompone un número en sus factores primos.

## Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Cyber123-bot/CalculadoraTerminal.git
   ```

2. Ejecutar el programa:
   ```bash
   python calculadora.py
   ```

## Dependencias
- Python 3.x
- os (normalmente preinstalada con Python)
- unittest (para correr pruebas unitarias)
- io (para manejar la entrada/salida de cadenas, incluyendo StringIO)
- sys (para interactuar con el sistema y manejar la entrada/salida estándar)
- módulo style (debe estar en el mismo directorio que `calculadora.py`)

## Estructura del Código

- `Calculator`: Clase principal que maneja la funcionalidad de la calculadora.
  - `__init__`: Inicializa la calculadora con textos y preguntas opcionales.
  - `factorizacion`: Calcula e imprime la factorización prima de un número.
  - `porcentaje`: Calcula e imprime el porcentaje de un número relativo a otro.
  - `suma`: Suma una lista de números e imprime el resultado.
  - `resta`: Resta una lista de números secuencialmente e imprime el resultado.
  - `division`: Divide el primer número por los números subsecuentes e imprime el resultado.
  - `multiplicacion`: Multiplica una lista de números e imprime el resultado.
  - `raiz_cuadrada`: Calcula e imprime la raíz cuadrada de un número usando el método de Newton.
  - `raiz_cubica`: Calcula e imprime la raíz cúbica de un número.
  - `potencia`: Eleva una base a un exponente e imprime el resultado.
  - `mcm`: Calcula e imprime el mínimo común múltiple de dos números.
  - `mcd`: Calcula e imprime el máximo común divisor de dos números usando el algoritmo de Euclides.
  - `resto_division`: Calcula e imprime el resto de la división de dos números.
  - `iniciar_programa`: Inicia el programa de la calculadora, muestra un menú de operaciones y solicita la entrada del usuario.