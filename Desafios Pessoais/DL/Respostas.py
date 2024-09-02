def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def pertence_fibonacci(n):
    if n < 0:
        return False
    fib_sequence = fibonacci(n)
    return n in fib_sequence

numero = 21  # Número a ser verificado
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

##########################################################################

def verifica_a(string):
    count_a = string.lower().count('a')
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

string = "Amazônia é a maior floresta tropical do mundo."
verifica_a(string)

############################################################################

INDICE = 12
SOMA = 0
K = 1
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

############################################################################

#a) 1, 3, 5, 7, 9 (sequência de números ímpares)
#b) 2, 4, 8, 16, 32, 64, 128 (sequência de potências de 2)
#c) 0, 1, 4, 9, 16, 25, 36, 49 (sequência de quadrados perfeitos)
#d) 4, 16, 36, 64, 100 (sequência de quadrados perfeitos de números pares)
#e) 1, 1, 2, 3, 5, 8, 13 (sequência de Fibonacci)
#f) 2, 10, 12, 16, 17, 18, 19, 20 (sequência de números que contêm o dígito 2)

#########################################################################################

#Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
#Desligue o primeiro interruptor e ligue o segundo interruptor.
#Vá até a sala das lâmpadas:
#A lâmpada que está acesa é controlada pelo segundo interruptor.
#A lâmpada que está quente mas apagada é controlada pelo primeiro interruptor.
#A lâmpada que está fria e apagada é controlada pelo terceiro interruptor.