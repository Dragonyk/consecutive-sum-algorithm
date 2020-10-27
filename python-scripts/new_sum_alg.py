import math
import time

def sumGaussBetween(i, n):
    s = ((n*(n + 1)) - (i*(i - 1)));
    return s//2

def generatePares(values):
    n = 6
    z = 1
    p = 20
    ant = 0
    dan = 0
    
    while(n<values):
        s = ((n - 1)*n) // 2
        i = n + 1
        d = 1 - (4 * (-((s * 2) + (i*(i - 1)))))
        x = int(((-1) + (math.sqrt(d))) / 2)
        g = (((x*(x + 1)) - (i*(i - 1)))//2)
        if g == s:
		
            print('{:<5d}{:>20d}{:>20d}'.format(z, n, x))
            if z > 1:
                div = n / ant
                dif = dan - div
				
                dan = div
            if z == p:
                break
            ant = x
            n = int(x * 4.121320343559646)
            z+=1
        else:
            n += 1
    print('END CODE')

generatePares(10000000000000000000000)
