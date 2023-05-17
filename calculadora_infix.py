"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ calculadora_infix.py sum 5 2
7

$ calculadora_infix.py mul 10 5
50

$ calculadora_infix.py
operação: sum
n1: 5
n2: 4
9
""" 

__version__ = "0.1.0"

import sys
arguments = sys.argv[1:]

if not arguments:
    operation = input("Operação: ")
    n1 = input("N1: ")
    n2 = input("N2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("Ex: 'sum 7 8'")
    sys.exit(1)
    
operation, *nums = arguments

valid_operation = ("sum", "sub", "mult", "div")
if operation not in valid_operation:
    print("Operação inválida")
    print(valid_operation)
    sys.exit(1)
    
validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
    
n1, n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2
    
    
print(f"O resultado é {result}")