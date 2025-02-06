import time
import sys

def typewriter(text, delay):
    """
    Exibe o texto no terminal simulando uma animação de digitação.
    Args:
        text (str): O texto a ser exibido.
        delay (float): O atraso entre cada caractere (em segundos).
    """
    for char in text:
        sys.stdout.write(char) # Escreve um caractere no terminal sem pular para a próxima linha
        sys.stdout.flush()  # Garante que o caractere seja exibido imediatamente
        time.sleep(delay)
    print()  # Adiciona uma nova linha ao final

# Exemplo de uso
typewriter("Olá, seja bem-vindo ao sistema!", delay=0.05)
typewriter("Isso é uma simulação de digitação.", delay=0.09)