# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tsNOmYE1eVJXls2Q_lYzzESjZ3MEp8e3
"""

x=2                #variable initialize
lr=0.046            #learning rate
precision=0.000001    #difference btw next and previous iteration
previous_step_size=1
max_iter=10000      #new var initialize
iter=0
gf=lambda x:(x+3)**2

gd=[]

while(precision < previous_step_size and iter < max_iter):
  prv=x
  x=x-lr*gf(prv)
  previous_step_size=abs(x-prv)
  iter+=1
  print("Iteration: ",iter,"Value: ",x)
  gd.append(x)

import matplotlib.pyplot as plt
plt.plot(gd)

