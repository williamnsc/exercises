def eat_ghost(power_pellet_active,touching_ghost):
    return power_pellet_active and touching_ghost

def get_boolean(enter):
    while True:
        user_input = input(enter + "(Responda com Sim ou Não): ").strip().lower()
        if user_input in ['sim','s']:
            return True
        elif user_input in ['não','n','nao']:
            return False
        else:
            print ("Favor responder apenas com sim ou não!")

def score(touching_power_pellet,touching_dot):
    return touching_power_pellet or touching_dot

def lose(power_pellet_active,touching_ghost):
    return not power_pellet_active and touching_ghost

def win(eaten_all_dots,power_pellet_active,touching_ghost):
    return eaten_all_dots and not lose(power_pellet_active,touching_ghost)

try:
    power_pellet_active = get_boolean("Pac man está com poder ativo? ")
    touching_ghost = get_boolean("Pac man está tocando algum fantasma? ")
    touching_power_pellet = get_boolean("Pac man está tocando uma esfera de poder? ")
    touching_dot = get_boolean("Pac man está tocando alguma esfera de pontuação? ")
    eaten_all_dots = get_boolean("Pac man já comeu todos os pontos? ")
    if eat_ghost(power_pellet_active,touching_ghost):
        re1="Pac man está comendo"
    else:
        re1="Pac man não está comendo"
    if score(touching_power_pellet,touching_dot):
        re2="Está pontuando!"
    else:
        re2="Não está pontuando"
    print(f'\n{re1} e {re2}')

    if win(eaten_all_dots,power_pellet_active,touching_ghost):
        print("Pac man ganhou!!")
    else:
        print("Pac man perdeu! ")

except Exception as e:
    print("Ocorreu um erro: {e}")

input("\nPressione Enter para sair...")