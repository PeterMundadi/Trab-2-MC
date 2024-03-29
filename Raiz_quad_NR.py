import math
import matplotlib.pyplot as plt



list_A = [0.5,1,2,10,40,100,1000,100000]
#list_chute_x0 =[0.7,1,2,4,7,11,31,301]

#list_chute_x0 = [0.3,0.6,1.6,3.6,6.3,10.3,31.3,301.3]
list_chute_T1 = []
list_chute_py = []

list_mySqrt = []
list_T1 = []
list_sqrt_log = []

list_mySqrt_iter = []
list_T1_iter = []
list_sqrt_log_iter = []

Parada = 1e-2

def raiz(list_X):
    for x in list_X:
        #print(x)

        # Raiz pela formula
        K = int(math.log2(x))
        m = x / (2**K) # m =1+f // mantiça
        f = m - 1
        raiz_calc = 1 + (f/2) * (1 - f/(4 + 2*f))
        list_chute_T1.append(raiz_calc)    

        # Raiz pela função do python
        #raiz_py = math.sqrt(m)
        #list_chute_T1.append(raiz_py)

def mySqrt(A,X0,Parada): # usando o trab 1 
   
    Xk = X0
    '''
    print("---------------")
    print("     MySqrt")
    print("     A: ", A) 
    print("     X0: ", X0)
    print("     Parada: ", Parada)
    print("---------------")'''
    iter = 1
    #while True:
    for _ in range(100):
        
        X_prox_k =0.5 * (Xk + A/Xk)
        #print("X_prox_k: ", X_prox_k)

        if abs(X_prox_k - Xk) < Parada:
            
            return X_prox_k, iter
        
        Xk = X_prox_k
        iter += 1
    
    #print("Iterações necessrias: ", iter)


def sqrt_log(A,Parada):
    
    Xk = math.exp(0.5 * math.log(A))
    #print("Chute log: ", Xk)
    iter = 1
    for _ in range(100):
        
        X_prox_k =0.5 * (Xk + A/Xk)
        #print("X_prox_k: ", X_prox_k)

        if abs(X_prox_k - Xk) < Parada:
            return X_prox_k, iter
        
        Xk = X_prox_k
        iter += 1


def grafico(L1, L2, A):
    plt.figure(figsize=(8, 5.5))  # Define o tamanho da figura

    # Plotando os valores de A, B e C
    plt.plot(A, L1, color='blue', marker='o', linestyle='-', label='X0 do Trabalho 1')  # A versus B
    plt.plot(A, L2, color='green', marker='s', linestyle='-', label='X0 log ieee')  # A versus C

    # Adicionando rótulos e título
    plt.xlabel('A', color='red', fontweight='bold')
    plt.ylabel('Quantidade de Iterações', color='red', fontweight='bold')

    # Adicionando legenda
    plt.legend()

    # Adicionando grade
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

raiz(list_A) # calcula o chute inicial para cada A usando o trab 1

for i in range(len(list_A)):
    print(i)
    print("A: ", list_A[i])
   
    ms_T1,it = mySqrt(list_A[i],list_chute_T1[i],Parada)
    list_T1.append(ms_T1)
    list_T1_iter.append(it)

    mS_log,iterlog=sqrt_log(list_A[i],Parada)
    list_sqrt_log.append(mS_log)
    list_sqrt_log_iter.append(iterlog)

   
    print("Raiz Calc   mySqrt T1: ", ms_T1, "|| Iterações : ", it)
    print("Raiz Calc sqrt_log   : ", mS_log, "|| Iterações: ", iterlog)
    print("Raiz Calc   Python   : ", math.sqrt(list_A[i]))
    print("---------------")

grafico(list_T1_iter, list_sqrt_log_iter,list_A)


    
