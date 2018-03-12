# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:59:49 2018

@author: thiago
"""
'''
Este programa resolve a equação de Schrodinger 
para um potencial V(x) = V0 em 1D.
'''
#-----------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import math as mt
#-----------------------------------------------------------------------------
# Valores iniciais do problema

m = 1.0
V0 = 1
h_ = 1.0
passos = int(200)
dx = .01
x = np.empty(passos)
psi = np.copy(x)
E = np.copy(x)
E[0] = 0.0
x[0] = 0.0
psi[0] = .5

#-----------------------------------------------------------------------------

# Variáveis auxiliares

p = []
f = []
v = []

#-----------------------------------------------------------------------------

# Definição da barreira de potencial

def V(x):
    
    if(x < 0.25):
        
        return 0.0
    
    else:
        
        return V0

#-----------------------------------------------------------------------------

def schrodinger(x,psi,pot,m,h_):
    
    pot = V(x) 

#psi'' + (2m/h**2)*(V(x)-E)psi = 0

#f  = psi'
#f' = psi'' 

#f' + (2m/h**2)*(V(x)-E)psi = 0
       
    return -(2*m/h_**2)*pot*psi
#-----------------------------------------------------------------------------

# Arquivos que gravaremos os resultados da barreira de potencial e
# da densidade de probabilidade

V_x = open('Barreira_de_potencial.dat','w')
PSI = open('Densidade_de_probabilidade.dat','w')
#-----------------------------------------------------------------------------
for i in range(0,passos-1):
    # Método de Runge-Kutta de 4ª ordem
    x[i+1] = x[i] + dx
    pot = V(x[i])
    k1 = dx*schrodinger(x[i],psi[i],pot,m,h_)
    k2 = dx*schrodinger(x[i]+dx/2,psi[i]+dx*k1/2,pot + dx*k1/2,m,h_)
    k3 = dx*schrodinger(x[i]+dx/2,psi[i]+dx*k2/2,pot + dx*k2/2,m,h_)
    k4 = dx*schrodinger(x[i]+dx,psi[i]+dx*k3,pot + dx*k3/2,m,h_)
    psi[i+1] = psi[i] + (k1 + 2*(k2+k3)+k4)/6
#-----------------------------------------------------------------------------    
    PSI.write(str(x[i])+' '+str(psi[i]**2)+'\n')    
    V_x.write(str(x[i])+' '+str(V(x[i]))+'\n')
#-----------------------------------------------------------------------------
    p.append(x[i])
    f.append(psi[i])
    v.append(V(x[i]))
    
#    print(x[i],V(x[i]),psi[i]**2)
    
plt.plot(p,v,'-',color='red')
plt.plot(p,f,'-',color='blue')
plt.legend([r'Barreira de potencial $V(x)$',u'Densidade de probabilidade $|\psi(x)|^{2}$'])
plt.xlabel(r'$x(\mu m)$',fontsize=20)
plt.title('Barreira de potencial em 1D')
plt.show()
plt.savefig(u'função_de_onda.pdf')
PSI.close()    
V_x.close()













