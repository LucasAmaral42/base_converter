from image import *
from calc import *

number       = input("Insira o número a ser convertido: ")
base_inicial = int(input("Insira a base a ser convertida: "))
base_final   = int(input("Insira para qual será convertido: "))

print(run_calc(number, base_inicial, base_final))
