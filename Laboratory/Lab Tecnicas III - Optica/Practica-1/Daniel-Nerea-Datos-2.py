# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:49:04 2024

@author: danie
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as cte
from tabulate import tabulate

# Medida de la primera focal

def concatenarbueno(lista):
    a=np.zeros([len(lista[0]),len(lista)])
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            a[j,i]=lista[i][j]
    return a

# Primera lente

objeto=[10]*4 # En centimetros
lente1=[25,25,25,25]
imagen1=[54.4,57.1,55.6,57.2]

objeto=[10]*4 # En centimetros
lente2=[27.5,27.5,27.5,27.5]
imagen2=[52.5,52.5,51.8,51.4]

objeto=[10]*4 # En centimetros
lente3=[30]*4
imagen3=[50.3,50.8,50.4,50.6]


# Segunda lente

objeto=[10]*4 # En centimetros
lente1=[20]*4
imagen1=[31,30.1,30.9,30.7]

objeto=[10]*4 # En centimetros
lente2=[19]*4
imagen2=[31.1,33,31.4,33.1]

objeto=[10]*4 # En centimetros
lente3=[23]*4
imagen3=[31.5,31.6,31.1,31.5]



"""
# Uso de la lupa

d0=40 # cm

cuadradosog=4 # Los cuadrados grandes, 8 de los pequeños
tamañoog=[258.3,253.1,259.2] # Tamaño original

def bt(d0,d,f):
    return (1-(d0-d)/f)
    
def bexp(t1,t2):
    tamañolupa=np.average(t1)
    tamañoog=np.average(t2)
    return tamañolupa/tamañoog

# Incertidumbre de la medida de los cuadrados es 0.1 por la medida

# Primera medida

d=46.1-39.5 # cm, distancia lupa-camara (entre las bases)
tamañolupa=[1033.0,1030.0,1024.0] # Tamaño original

cuadrados=4
bt1=bt(d0,d,fl1)
bexp1=bexp(tamañolupa,tamañoog)

print("bt%d= %.2f, \t bexp%d=%.2f"%(1,bt1,1,bexp1))

# Segunda medida

d=46.1-36.5 # cm, distancia lupa-camara (entre las bases)
tamañolupa=[1030.4,1022.4,1021.4] # Tamaño original

cuadrados=4
bt2=bt(d0,d,fl1)
bexp2=bexp(tamañolupa,tamañoog)

print("bt%d= %.2f, \t bexp%d=%.2f"%(2,bt2,2,bexp2))

# Tercera medida

cuadrados=2 # 2 grandes, 4 pques
d=46.1-33.1 # cm, distancia lupa-camara (entre las bases)
tamañolupa=np.array([471.1,465.1,468.1]) # Tamaño original

bt3=bt(d0,d,fl1)
bexp3=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

print("bt%d= %.2f, \t bexp%d=%.2f"%(3,bt3,3,bexp3))

# Cuarta medida

cuadrados=2 # 2 grandes, 4 p2ques
d=46.1-25 # cm, distancia lupa-camara (entre las bases)
tamañolupa=np.array([379.0,382.0,378.0]) # Tamaño original

bt4=bt(d0,d,fl1)
bexp4=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

print("bt%d= %.2f, \t bexp%d=%.2f"%(4,bt4,4,bexp4))




#Quinta medida
cuadrados=0.5 # 0.5 grandes, 1 p2ques
d=46.1-20.9 # cm, distancia lupa-camara (entre las bases)
tamañolupa=np.array([94,92,93]) # Tamaño original

bt5=bt(d0,d,fl1)
bexp5=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

print("bt%d= %.2f, \t bexp%d=%.2f"%(5,bt5,5,bexp5))





#Doble lupa es decir microsocopio

def di(f,do):
    di=(1/f-1/do)**(-1)
    return di

def bteo(l,lp,d0,d,f):
    bteo=(lp/l)*(1-(d0-d)/(fl1))
    return bteo

# Distancia 1
    #medida1 micro

cuadrados=(1/5)*0.5
tamañolupa=np.array([46,44])
d=46.1-40.1 #cm lupa1-camara
l=18.0-8.8 #lente2-objeto
lp=di(fl2,l) #cm lente2-imagen (calculado con la focal)

bexp11=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)
bt1=bteo(l,lp,d0,d,fl1)

    #medida2 micro
cuadrados=(1/5)*0.5
tamañolupa=np.array([46,47,42])

bexp12=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

 #medida3 micro
cuadrados=(1/5)*0.5
tamañolupa=np.array([46,44,45])

bexp13=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

# Distancia 2
    #medida1 micro

cuadrados=(1/5)*0.5
tamañolupa=np.array([61,60])
d=46.1-40.1 #cm lupa1-camara
l=15.3-7.3 #lente2-objeto
lp=di(fl2,l) #cm lente2-imagen (calculado con la focal)

bexp21=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)
bt2=bteo(l,lp,d0,d,fl1)

    #medida2 micro
cuadrados=(1/5)*0.5
tamañolupa=np.array([62,61])

bexp22=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

 #medida3 micro
cuadrados=(1/5)*0.5
tamañolupa=np.array([60,60])

bexp23=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)


# Distancia 3
    #medida1 micro

cuadrados=(4/5)*0.5
tamañolupa=np.array([99.0,99.0,100.0])
d=46.1-40.1 #cm lupa1-camara
l= 21.1-9.8#lente2-objeto
lp=di(fl2,l) #cm lente2-imagen (calculado con la focal)

bexp31=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)
bt3=bteo(l,lp,d0,d,fl1)

    #medida2 micro
cuadrados=(4/5)*0.5
tamañolupa=np.array([100.0,100.0,99.0])

bexp32=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

 #medida3 micro
cuadrados=(4/5)*0.5
tamañolupa=np.array([98.0,100.0,99.0])

bexp33=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

# Distancia 4
    #medida1 micro

cuadrados=0.5#un medio cuadrado grande uno pequerrechiño
tamañolupa=np.array([63,61,61])
d=46.1-40.1 #cm lupa1-camara
l=24-7.1 #lente2-objeto
lp=di(fl2,l) #cm lente2-imagen (calculado con la focal)

bexp41=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)
bt4=bteo(l,lp,d0,d,fl1)

    #medida2 micro
cuadrados=0.5
tamañolupa=np.array([61,61,61])

bexp42=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

 #medida3 micro
cuadrados=0.5
tamañolupa=np.array([62,62,61])

bexp43=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

# Distancia 5
    #medida1 micro

cuadrados=1#un  cuadrado grande
tamañolupa=np.array([85,85,84])
d=46.1-40.1 #cm lupa1-camara
l=25-3.2 #lente2-objeto cuanto mayor sea menor es el error entre exp y teo
lp=di(fl2,l) #cm lente2-imagen (calculado con la focal)

bexp51=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)
bt5=bteo(l,lp,d0,d,fl1)

    #medida2 micro
cuadrados=1
tamañolupa=np.array([86,86,84])

bexp52=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)

 #medida3 micro
cuadrados=1
tamañolupa=np.array([87,86,85])

bexp53=bexp(tamañolupa*(cuadradosog/cuadrados),tamañoog)
"""