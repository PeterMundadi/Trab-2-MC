import matplotlib.pyplot as plt

def grafico_ABC(A, B, C):
    plt.figure(figsize=(11, 8.5))  # Define o tamanho da figura

    # Plotando os valores de A, B e C
    plt.plot(B, A, color='blue', marker='o', linestyle='-', label='A versus B')  # A versus B
    plt.plot(C, A, color='green', marker='s', linestyle='-', label='A versus C')  # A versus C

    # Adicionando rótulos e título
    plt.xlabel('Valores de B e C', color='red', fontweight='bold')
    plt.ylabel('Valor de A', color='red', fontweight='bold')
    plt.title('Valores de A em relação a B e C', color='blue', fontweight='bold')
    
    # Adicionando legenda
    plt.legend()

    # Adicionando grade
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

# Exemplo de uso
A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10]
C = [3, 6, 9, 12, 15]

grafico_ABC(A, B, C)
