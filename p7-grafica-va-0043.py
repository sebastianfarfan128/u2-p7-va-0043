import numpy as np
import matplotlib.pyplot as plt
# Sebastian Farfan NC 0043
no_lista=[1,2,3,17,48]
califa_ml=[20,30,80,100,90]
califa_va=[70,90,60,90,100]
plt.plot(no_lista,califa_ml,label="Calificaciones ML")
plt.plot(no_lista,califa_va,label="Calificaciones VA")
plt.title(" calificaciones materias 0043")
plt.xlabel("Numero de lista ")
plt.ylabel("Calificacion")
plt.legend()
plt.show()