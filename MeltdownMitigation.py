def is_criticality_balanced(temperature,neutrons_emitted):
    return temperature<800 and neutrons_emitted>500 and ((temperature*neutrons_emitted)<500000)

def reactor_efficiency(voltage,current,theoretical_max_power):
    generated_power= voltage*current
    percent = (generated_power/theoretical_max_power)*100
    if percent >= 80:
        print("green")
    elif 60 <= percent < 80:
        print("orange")
    elif 30 <= percent < 60:
        print("red")
    else:
        print("black")

def fail_safe(temperature,neutrons_produced_per_second,threshold):
    if (temperature*neutrons_produced_per_second) < (0.9*threshold):
        print("LOW")
    elif (1.1*threshold) >= (temperature*neutrons_produced_per_second) >= (0.9*threshold):
        print("NORMAL")
    else:
        print("DANGER")

temperature = int(input("Qual o valor da temperatura ? (Em KELVIN) "))
neutrons_emitted = int(input("Qual o valor de neutrons emitidos? "))
if is_criticality_balanced (temperature,neutrons_emitted):
    print("Está balanceado")
else:
    print("Não está balanceado")
voltage = int(input("Qual o valor da voltagem ? "))
current = int(input("Qual o valor da corrente ? "))
theoretical_max_power = int(input("Qual o valor da potência máxima teorica ? "))
reactor_efficiency(voltage,current,theoretical_max_power)
threshold = int(input("Qual o valor do limite estabelecido?"))
neutrons_produced_per_second = int(input("Qual o valor de neutrons produzidos por segundo?"))
print("O reator está em: ")
fail_safe(temperature,neutrons_produced_per_second,threshold)

input("\nPressione Enter para sair...")