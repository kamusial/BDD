import numpy as np
import matplotlib.pyplot as plt

X = [i+1 for i in range(0,10)] # generowanie 10 punktów na osi Y
Y = [5*i - 2 for i in X] # generowanie wartości na osi Y
plt.plot(X,Y,'ro-')
plt.show()