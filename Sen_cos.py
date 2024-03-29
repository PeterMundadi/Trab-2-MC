# Discplina de Matemática Computacional
# Alunos: Gabriel Bitdinger Medeiros - 118542 e Peter Mundadi - 116338

import math
import matplotlib.pyplot as plt
'''
Sen11_X = X- X^3/3! + X^5/5! - X^7/7! + X^9/9! - X^11/11!

cos12_X = 1 - X^2/2! + X^4/4! - X^6/6! + X^8/8! - X^10/10! + X^12/12!

T11_x =1024x^11-2816x^9+2816x^7-1232x^5+220x^3-11x

T12_x = 2048x^12-6144x^10+6912x^8-3584x^6+840x^4-72x^2+1

M_T11_x= x^11 - 11x^9/4 + 11x^7/4 - 77x^5/64 + 55x^3/256 - 11x/1024 

M_T12_x= x^12 - 3x^10 + 27x^8/8 - 7x^6/4 + 105x^4/256 - 9x^2/256 + 1/2048


S_X = X- X^3/3! + X^5/5! - X^7/7! + X^9/9!  - 11x^9/11!*4 + 11x^7/11!*4 - 77x^5/11!*64 + 55x^3/11!*256 - 11x/11!*1024 

C_X = 1 - X^2/2! + X^4/4! - X^6/6! + X^8/8! - X^10/10! + 3x^10/12! - 27x^8/12!*8 + 7x^6/12!*4 - 105x^4/12!*256 + 9x^2/12!*256 - 1/12!*2048

'''





pi = math.pi

pi_4 = pi/4
pi_6 = pi/6

List_X =[-pi_4,-pi_6,0,pi_6,pi_4]


list_erro_seno = []
list_erro_cosseno = []

#função doFatorial
def fat(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fat(n-1)

#função do expoente
def calc_exp(x, n):  # x^n
    if x == 0:
        return 0
    elif n == 0:
        return 1
    else:
        y = 1
        if n > 0:
            while n > 0:
                y *= x
                n -= 1
        else:
            while n < 0:
                y /= x
                n += 1
        return y

#Função para calcular o seno pelo Chebyshev
def aprox_seno(x):
    x=abs(x)
    
    S_X = x * (1 + calc_exp(x,2) * (-1 / fat(3) + calc_exp(x,2) * (1 / fat(5) + calc_exp(x,2) * (-1 / fat(7) + calc_exp(x,2) * (1 / fat(9) - calc_exp(x,2) * (11 / (fat(11) * 4) - calc_exp(x,2) * (11 / (fat(11) * 4) - calc_exp(x,2) * (77 / (fat(11) * 64) - calc_exp(x,2) * (55 / (fat(11) * 256) - calc_exp(x,2) * (11 / (fat(11) * 1024)))))))))))

    return S_X

#Funçao seno do python
def seno_py(x):
    x=abs(x)
    return math.sin(x)

#Função para calcular o cosseno pelo Chebyshev
def aprox_cosseno(x):
    x=abs(x)
      
    C_X3 = 1 + ((-x**2/2) *(1- (x**2/12)*((-x**2/30)*((1-x**2/56)*((1-x**2/90)))))) + (x**2/fat(12) * (9/256 + x**2 * (-105/256 + x**2 * (7/4 + x**2 * (-27/8 + x**2 * (3)))))) - 1/479001600*2048
    return C_X3

#Função cosseno do python
def cosseno_py(x):
    x=abs(x)
    return math.cos(x)

#Função para plotar o gráfico
def grafico(list_erro_seno, list_erro_cosseno, List_X):
    # Define o tamanho da figura
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5.5))

    # Plotando os valores de erro para seno
    ax1.plot(List_X, list_erro_seno, color='blue', marker='o', linestyle='-', label='Erro Seno')
    ax1.set_ylabel('Erro', color='red', fontweight='bold')
    ax1.set_title('Erro do Seno', color='blue', fontweight='bold')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Plotando os valores de erro para cosseno
    ax2.plot(List_X, list_erro_cosseno, color='green', marker='s', linestyle='-', label='Erro Cosseno')
    ax2.set_xlabel('Valores de X', color='red', fontweight='bold')
    ax2.set_ylabel('Erro', color='red', fontweight='bold')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()

def main():

    for x in List_X:
        
        Ap_S3 = aprox_seno(x)
        C_X3 = aprox_cosseno(x)
        S_py = seno_py(x)
        C_py = cosseno_py(x)

        list_erro_seno.append(abs(S_py - Ap_S3))
        list_erro_cosseno.append(abs(C_py - C_X3))

        print("x: ", x)

        print("--SENO--") 
        print("Aprox Seno3: ", Ap_S3)
        print("seno_py    : ", S_py)
        print("Erro       : ", abs(S_py - Ap_S3))
        print()

        print("--COSSENO--")
        print("Aprox Cosseno3: ", C_X3)        
        print("Cosseno_py    : ", C_py)
        print("Erro          : ", abs(C_py - C_X3))
        print("-----------------------")
    
    grafico(list_erro_seno, list_erro_cosseno, List_X)

main()





def calcular_termo(x, n):

    # Calcula o expoente do termo
    exp = 2 * n + 1
    sinal = calc_exp(-1,n)

    numerador = sinal  *  calc_exp(x,exp)
    denominador = math.factorial(exp)

    return numerador / denominador



#def aprox_seno_coseno(func,x):

    #if func.lower() == 'sen':
        



'''
def serie_termos(func,n,x):


    #Monta a série de Taylor para o seno
    if func.lower() == 'sen':
        num = 1
        n=1
        T0 = 1* x_elv_n(x,n) / fat(n)  # Começamos com o primeiro termo da série
        coeff.append(T0)  # Adicionamos o primeiro termo à lista de coeficientes
        
        for i in range(1, n):

            d = 2*i+1
            fat_d = fat(d)


            Tn= 1 * x_elv_n(x,d) / fat(d)


            coeff.append(d)



            #termo = 1 / math.factorial(2 * i + 1)  # Calcula o termo da série

            #soma += termo  # Adiciona o termo à soma
    #return soma

'''        


#serie_termos(11)
#print(coeff)
