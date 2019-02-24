# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:01:12 2019

@author: Asus
"""

import math
import matplotlib.pyplot as plt

Vo    = int(input('Masukan nilai Vo  : '))
sudut = int(input('Masukan nilai sudut  : '))
theta = math.radians(sudut)
Xo    = int(input('Masukan nilai Xo : '))
Yo    = int(input('Masukan nilai Yo : '))
T     = 10
N     = 100
deltaT= T/N
g     = 9.8
i     = 0
X_Num = []
Y_Num = []
X_Eks  = []
Y_Eks  = []
Vy_Num= []

X_Num.append(Xo)
Y_Num.append(Yo)
X_Eks.append(Xo)
Y_Eks.append(Yo)

Vx            = Vo*math.cos(theta)
Vy_Num.append(Vo*math.sin(theta))

while i <= 100:
  X_Num.append(X_Num[i] + Vx * deltaT)
  Vy_Num.append(-g*deltaT + Vy_Num[i])
  Y_Num.append(Y_Num[i] + (g*deltaT**2)+(Vy_Num[i+1]*deltaT))
  i=i+1
  
i = 0
while i <= 100:
  X_Eks.append(Vo*math.cos(theta)*(i*deltaT))
  Y_Eks.append( (-(0.5)*g*(i*deltaT)**2) +(i*deltaT*Vo*math.sin(theta)))
  i=i+1

plt.plot(X_Eks, Y_Eks, '-b', label='Solusi Eksak')
plt.plot(X_Num, Y_Num, '-r', label='Solusi Numerik')
plt.legend(loc='upper right')
plt.show()