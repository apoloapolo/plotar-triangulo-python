import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math
from celluloid import Camera

lista=[]

fig = plt.figure()
camera = Camera(fig)
ax = fig.add_subplot(111)
ax.grid(True)

for i in ("ABC"):
    for h in ("XY"):
        ax = float(input(f"Digite a coordenada {h} da vertice {i} do triangulo: "))
        lista.append(ax)
        
ang1 = float(input(f"Digite um ângulo para rotação: "))
ang2 = float(input(f"Digite outro um ângulo para rotação: "))

for i in np.arange(1,360.5,0.5):
    lista2=[]
    angrad = math.radians(i)
    
    pts = np.array([[lista[0],lista[1]], [lista[2],lista[3]], [lista[4],lista[5]]])
    p = Polygon(pts,facecolor='lightsteelblue', edgecolor='blue', linewidth=2)
    ax = plt.gca()
    ax.add_patch(p)
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    
    for a in range(0, len(lista), 2):
        ncx = round(((lista[a]) * math.cos(angrad)) + ((lista[a+1]) * (math.sin(angrad))),1)
        lista2.append(ncx)
        ncy = round(((lista[a]) * (math.sin(angrad) * (-1))) + ((lista[a+1]) * math.cos(angrad)),1)
        lista2.append(ncy)
    while i < 360:    
        ax = plt.gca()    
        pts2 = np.array([[lista2[0],lista2[1]], [lista2[2],lista2[3]], [lista2[4],lista2[5]]])
        p2 = Polygon(pts2,facecolor='lightsalmon', edgecolor='orangered', linewidth=2)
        ax.add_patch(p2)
        break
    
    if i == ang1:
        lista3=lista2
    while i >= ang1:
        ax = plt.gca()    
        pts2 = np.array([[lista3[0],lista3[1]], [lista3[2],lista3[3]], [lista3[4],lista3[5]]])
        p2 = Polygon(pts2,facecolor='mediumspringgreen', edgecolor='green', linewidth=2)
        ax.add_patch(p2)
        break
    if i ==ang2:
        lista4=lista2
    while i >= ang2:
        ax = plt.gca()    
        pts2 = np.array([[lista4[0],lista4[1]], [lista4[2],lista4[3]], [lista4[4],lista4[5]]])
        p2 = Polygon(pts2,facecolor='lightcoral', edgecolor='red', linewidth=2)
        ax.add_patch(p2)
        break
    
    camera.snap()

print()
print(f"""As coordenadas para {ang1}° são:
A({lista3[0]} , {lista3[1]})
B({lista3[2]} , {lista3[3]})
C({lista3[4]} , {lista3[5]})

E para {ang2}° são:
A({lista4[0]} , {lista4[1]})
B({lista4[2]} , {lista4[3]})
C({lista4[4]} , {lista4[5]})""")

plt.title(f"""Original (Azul)
Rotacionado em {ang1}° (Verde)
Rotacionado em {ang2}° (Vermelho)""")

plt.xlim(((max(lista)*-1)-1), max(lista)+1)
plt.ylim(((max(lista)*-1)-1), max(lista)+1)
animation = camera.animate(interval=1.5, blit=True, repeat=False)
plt.show()
