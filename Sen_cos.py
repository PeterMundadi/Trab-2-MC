import math

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
    
    k = x * (1 + calc_exp(x,2) * (-1 / fat(3) + calc_exp(x,2) * (1 / fat(5) + calc_exp(x,2) * (-1 / fat(7) + calc_exp(x,2) * (1 / fat(9) + calc_exp(x,2) * (11 / (fat(11) * 4) + calc_exp(x,2) * (-11 / (fat(11) * 4) + calc_exp(x,2) * (77 / (fat(11) * 64) + calc_exp(x,2) * (55 / (fat(11) * 256) + calc_exp(x,2) * (-11 / (fat(11) * 1024)))))))))))
    
    #y = y - 259/256

    y = x * (1 + calc_exp(x,2) * (- 1/fat(3) + calc_exp(x,2) * (1/fat(5) + calc_exp(x,2) * (- 1/fat(7) + calc_exp(x,2) * (1/fat(9) + calc_exp(x,2) * (- 11/fat(11)*4 + calc_exp(x,2) * (35/fat(11)*32 + calc_exp(x,2) * (25/fat(11)*64 + calc_exp(x,2) * (25/fat(11)*512 - 1/fat(11)*1024)))))))))
    #print("y aprox : ", y)
    

    S_X = x * (1 + calc_exp(x,2) * (-1 / fat(3) + calc_exp(x,2) * (1 / fat(5) + calc_exp(x,2) * (-1 / fat(7) + calc_exp(x,2) * (1 / fat(9) - calc_exp(x,2) * (11 / (fat(11) * 4) - calc_exp(x,2) * (11 / (fat(11) * 4) - calc_exp(x,2) * (77 / (fat(11) * 64) - calc_exp(x,2) * (55 / (fat(11) * 256) - calc_exp(x,2) * (11 / (fat(11) * 1024)))))))))))

    
    
    return y,k,S_X

#Funçao seno do python
def seno_py(x):
    x=abs(x)
    return math.sin(x)

#Função para calcular o cosseno pelo Chebyshev
def aprox_cosseno(x):
    x=abs(x)
    
    P_x = (1/fat(12)) * calc_exp(x,2) * (1 + (calc_exp(x,2) / 3) * (1 + (calc_exp(x,2) / 5) * (1 + (calc_exp(x,2) / 7) * (1 + (calc_exp(x,2) / 9) * (1 + (calc_exp(x,2) / 11) * (3 + (calc_exp(x,2) / 12) * (-27 + (7/8) * (calc_exp(x,2) + (105/4) * (calc_exp(x,2) + (9/256) * calc_exp(x,2))))))))))


    #C_X=980995276799/980995276800 - P_x
    C_X =1 - P_x - 1/fat(12)*2048
    
    
    #y = 1 - x**2 / fat(2) + x**4 / fat(4) - x**6 / fat(6) + x**8 / fat(8) - x**10 / fat(10) + x**12 / fat(12)
    return C_X,P_x

#Função cosseno do python
def cosseno_py(x):
    x=abs(x)
    return math.cos(x)
 
def main():

    for x in List_X:
        
        Ap_S,Ap_S2,Ap_S3 = aprox_seno(x)
        Ap_C,P_X = aprox_cosseno(x)
        S_py = seno_py(x)
        C_py = cosseno_py(x)

        print("x: ", x)
        print("SENO")
        print("Aprox seno1: ", Ap_S)
        print("Aprox Seno2: ", Ap_S2)
        print("Aprox Seno3: ", Ap_S3)
        print("seno_py    : ", S_py)
        print()
        print("COSSENO")
        print("P_x: ", P_X)
        print("Aprox Cosseno: ", Ap_C)
        print("Cosseno_py: ", C_py)

        print("-----------------------")

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