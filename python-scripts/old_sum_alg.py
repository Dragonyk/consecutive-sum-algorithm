import math
import time

def sumGaussBetween(i, n):
    s = ((n*(n + 1)) - (i*(i - 1)));
    return s//2

def generatePares(values):
    n = 6
    z = 1
    start_time = time.time()
    while(n<values):
        soma_anterior = ((n - 1)*n) // 2
        ultimo_par = n + 1
        soma_proxima = n + 1

        while(soma_proxima<soma_anterior):
            ultimo_par = ultimo_par + 1
            soma_proxima = soma_proxima + ultimo_par
            if soma_proxima == soma_anterior:
                a = (time.time() - start_time)
                print("{0:.3f}".format(round(a,3)))
				
                break
        n+=1
    print('END CODE')

generatePares(100000000)
