import math



list_A = [0.5,1,2,10,40,100,1000,100000]
#list_chute_x0 =[0.7,1,2,4,7,11,31,301]

list_chute_x0 = [0.3,0.6,1.6,3.6,6.3,10.3,31.3,301.3]

list_chute_py = []
list_mySqrt = []

Parada = 1e-2

def raiz(list_X):
    for x in list_X:
        #print(x)

        # Raiz pela formula
        K = int(math.log2(x))
        m = x / (2**K) # m =1+f // mantiça
        f = m - 1
        raiz_calc = 1 + (f/2) * (1 - f/(4 + 2*f))
        list_chute_x0.append(raiz_calc)    

        # Raiz pela função do python
        raiz_py = math.sqrt(m)
        list_chute_py.append(raiz_py)

def mySqrt(A,X0,Parada):
   
    Xk = X0
    '''
    print("---------------")
    print("     MySqrt")
    print("     A: ", A) 
    print("     X0: ", X0)
    print("     Parada: ", Parada)
    print("---------------")'''
   
    #while True:
    for _ in range(100):
        
        X_prox_k =0.5 * (Xk + A/Xk)
        #print("X_prox_k: ", X_prox_k)

        if abs(X_prox_k - Xk) < Parada:
            return X_prox_k
        
        Xk = X_prox_k

#raiz(list_A)
print("tamnho de list_A: ", len(list_A))
print("tamnho de list_chute_x0: ", len(list_chute_x0))
print("tamnho de list_chute_py: ", len(list_chute_py))
      
for i in range(len(list_A)):
    print(i)
    print("A: ", list_A[i])
    print("chute x0: ", list_chute_x0[i])
       
    mS=mySqrt(list_A[i],list_chute_x0[i],Parada)
    list_mySqrt.append(mS)

    print("Raiz Calculada mySqrt: ", mS)
    print("Raiz Calculada Python: ", math.sqrt(list_A[i]))
    print("---------------")


