import time

def value_of_card(card):
    if card in 'KQJ':
        return 10
    if card == 'A':
        return 1
    if card in ['2','3','4','5','6','7','8','9','10']:
        return int(card)

def higher_card(card1,card2):
    value1 = value_of_card(card1)
    value2 = value_of_card(card2)
    if value1>value2:
        return card1
    if value2>value1:
        return card2
    if value1==value2:
        return card1,card2
    
def value_of_ace(card1,card2):
    if card1 == 'A' or card2 == 'A':
        return 1
    value1 = value_of_card(card1)
    value2 = value_of_card(card2)
    if (value1+value2) <= 10:
        return 11
    else:
        return 1
    
def is_blackjack(card1,card2):
    if value_of_card(card1) == 10 and card2 =='A':
        return True
    if value_of_card(card2) == 10 and card1 =='A':
        return True
    else:
        return False

def can_split_pairs(card1,card2):
    return value_of_card(card1) == value_of_card(card2)

def can_double_down(card1,card2):
    return 9<= value_of_card(card1)+value_of_card(card2)<=11 


try:
    card1 = input('Digita qual sua 1ª carta: ').upper()
    card2 = input('Digite qual sua 2ª carta: ').upper()
    comparasion = higher_card(card1,card2)
    time.sleep(2)
    print(f'Após comparação, a carta de maior valor é: {comparasion}')
    aceValue = value_of_ace(card1,card2)
    print(f'O valor do A na sua mão será de: {aceValue}! Devido as cartas previamente selecionadas ')
    time.sleep(2)
    if is_blackjack(card1,card2):
        print('Sua mão já é considerada 21')
    else:
        print('Sua mão não é considerada 21')
    time.sleep(3)
    canSplit = can_split_pairs(card1,card2)
    if canSplit == True:
        print('Devido as duas cartas em sua mão terem o mesmo valor, é permitido trata-lás como mãos separadas')
    else:
        print('Devido as duas cartas em sua mão não terem o mesmo valor, não será permitido trata-lás como mãos separadas')
    time.sleep(3)
    canDouble = can_double_down(card1,card2)
    if canDouble == True:
        print('Você pode colocar uma aposta adicional')
    else:
        print('Você não pode colocar uma outra aposta')
except ValueError as e:
    print(e)

input('\nPressione Enter para sair...')


"""
Saber valor da carta 
V
card = (input('Digite qual carta você tem na mão: ')).upper()
value = value_of_card(card)
print(f'O valor da sua carta é {value}')

"""
