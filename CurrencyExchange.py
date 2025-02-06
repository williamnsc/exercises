import time

def exchange_money(budget,exchange_rate):
    return budget/exchange_rate

def get_change(budget,exchanged_value):
    return budget-exchanged_value

def get_number_of_bills(exchanged_value,denomination):
    return exchanged_value//denomination

def get_leftover_of_bills(amount,denomination):
    return amount%denomination

def exchangable_value(budget,exchange_rate,spread,denomination):
    fee = exchange_rate*(1+ spread/100)
    conversion = budget/fee
    result = conversion // denomination * denomination
    return int(result)

try:
    budget = float(input("Qual o valor total que deseja seja convertido? "))
    exchange_rate = float(input("Qual a taxa da moeda que deseja converter? "))
    exchanged_value = exchange_money(budget,exchange_rate)
    print(f"Você irá receber {exchanged_value:.2f} da nova moeda")
    denomination = int(input("Qual o valor da cédula desejada ? "))
    number_of_bills = get_number_of_bills(exchanged_value,denomination)
    time.sleep(1.5)
    print(f"Você receberá {int(number_of_bills)} cedúlas")
    amount = exchanged_value
    change_value = get_leftover_of_bills(amount,denomination)
    time.sleep(1)
    if change_value !=0:
        print(f"Devido a divisão do valor total pelo valor das cédulas não ter sido exata, houve um troco de {change_value:.2f} ")
    else:
        print("Valor exato, não haverá troco")
    spread = int(input("Qual o valor da taxa de reajuste da moeda ? "))
    final_value=exchangable_value(budget,exchange_rate,spread,denomination)
    print(f"Você receberá o valor máximo de {(final_value)} em cédulas de {denomination} , após o reajuste calculado. ")

except ValueError:
    print("Por favor, insira um número válido.")

input("\nPressione Enter para sair...")