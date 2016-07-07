'''
Created on 07/07/2016
https://www.hackerrank.com/challenges/equal
@author: ernesto
'''
import array
import fileinput

def ranas_generar_pasos_minimos():
    pasos_minimos = array.array("I")
    
    for numerin in range(1000):
        numerin_reducido = 0
        num_pasitos = 0
        
        numerin_reducido = numerin
        
        num_pasitos = int(numerin_reducido / 5)
        numerin_reducido = int(numerin_reducido % 5)
        
        num_pasitos += int(numerin_reducido / 2)
        numerin_reducido = int(numerin_reducido % 2)
        
        num_pasitos += int(numerin_reducido / 1)
        numerin_reducido = int(numerin_reducido % 1)
        
        pasos_minimos.append(num_pasitos)
    
    return pasos_minimos

def ranas_core(chocolates, pasos_minimos):
    choco_min = 0
    num_movs = 0
    
    chocolates.sort()
    
    choco_min = chocolates[0]
    
    print("min de choco %d" % choco_min)
    
    for chocolatin in chocolates:
        diferencia = 0
        
        diferencia = chocolatin - choco_min
        
        print("la diferencia entre %u y el min %u es %u" % (chocolatin, choco_min, diferencia))
        
        num_movs += pasos_minimos[diferencia]
#        print(type(num_movs))
#        print(type(pasos_minimos[diferencia]))
        
        print("los movs act %u acum %u" % (pasos_minimos[diferencia], num_movs))
        
    return num_movs
    
def ranas_main():
    casos = 0
    lineas = []
    pasos_minimos = array.array("I")
    
    lineas = list(fileinput.input())
    casos = int(lineas[0])
    
    pasos_minimos = ranas_generar_pasos_minimos()
    
    for num_linea in range(1, casos * 2 , 2):
        movs = 0
        num_nums = 0
        numeros = []
        
        num_nums = int(lineas[num_linea])
        
        numeros = [int(x) for x in lineas[num_linea + 1].strip().split(" ")]
        
        assert(num_nums == len(numeros))
        
#        print("los numeros %s" % numeros)
        
        movs = ranas_core(numeros, pasos_minimos)
        
        print("%u" % movs)
        
if __name__ == '__main__':
    ranas_main()
