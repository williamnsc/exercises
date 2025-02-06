import time

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_timing):
    return EXPECTED_BAKE_TIME-elapsed_bake_timing

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

try:
    number_of_layers = int(input("Digite o número de camadas da sua lasanha: "))
    elapsed_bake_time = int(input("Digite o tempo de cozimento já transcorrido (em minutos): "))
    elapsed_time = elapsed_time_in_minutes(number_of_layers,elapsed_bake_time)
    print(f"Tempo de cozimento total já passado: {elapsed_time} minutos")

except ValueError:
    print("Por favor, insira um número inteiro válido.")

input("\nPressione Enter para sair...")