import math
import matplotlib.pyplot as plt
from sympy import Symbol, Eq, solve
from numpy import arange,linspace

def equa(y1,x1,c):
    x = Symbol('x')
    y = Symbol('y')
    e = Eq((y-y1)/(x-x1),c)
    return solve(e,y)

def m(y2,y1,x2,x1):
    mm = (y2-y1)/(x2-x1)
    return mm
    
lista=[]

for i in ("ABC"):
    for h in ("XY"):
        ax = float(input(f"Digite a coordenada {h} da vertice {i} do triangulo: "))
        lista.append(ax)

mab= m(lista[3],lista[1],lista[2],lista[0])
mac= m(lista[5],lista[1],lista[4],lista[0])
mbc= m(lista[5],lista[3],lista[4],lista[2])
eqa= equa(lista[1],lista[0],mab)
eqb= equa(lista[1],lista[0],mac)
eqc= equa(lista[3],lista[2],mbc)

x = linspace(lista[0],lista[2], endpoint=True)
plt.plot(x,eval(str(eqa[0])), color='blue')
    
x = linspace(lista[0],lista[4], endpoint=True)
plt.plot(x,eval(str(eqb[0])), color='blue')
    
x = linspace(lista[2],lista[4], endpoint=True)
plt.plot(x,eval(str(eqc[0])), color='blue')

ang = float(input("Digite um ângulo para rotação em sentido horário : "))
angrad = math.radians(ang)

lista2=[]

for a in range(0, len(lista), 2):
    ncx = round(((lista[a]) * math.cos(angrad)) + ((lista[a+1]) * (math.sin(angrad))),1)
    lista2.append(ncx)
    ncy = round(((lista[a]) * (math.sin(angrad) * (-1))) + ((lista[a+1]) * math.cos(angrad)),1)
    lista2.append(ncy)

mab2= m(lista2[3],lista2[1],lista2[2],lista2[0])
mac2= m(lista2[5],lista2[1],lista2[4],lista2[0])
mbc2= m(lista2[5],lista2[3],lista2[4],lista2[2])
eqa2= equa(lista2[1],lista2[0],mab2)
eqb2= equa(lista2[1],lista2[0],mac2)
eqc2= equa(lista2[3],lista2[2],mbc2)

x = linspace(lista2[0],lista2[2], endpoint=True)
plt.plot(x,eval(str(eqa2[0])), color='red')
    
x = linspace(lista2[0],lista2[4], endpoint=True)
plt.plot(x,eval(str(eqb2[0])), color='red')
    
x = linspace(lista2[2],lista2[4], endpoint=True)
plt.plot(x,eval(str(eqc2[0])), color='red')

ang2 = float(input("Digite outro ângulo para rotação em sentido horário : "))
angrad2 = math.radians(ang2)

lista3=[]

for a in range(0, len(lista), 2):
    ncx2 = round(((lista[a]) * math.cos(angrad2)) + ((lista[a+1]) * (math.sin(angrad2))),1)
    lista3.append(ncx2)
    ncy2 = round(((lista[a]) * (math.sin(angrad2) * (-1))) + ((lista[a+1]) * math.cos(angrad2)),1)
    lista3.append(ncy2)

mab3= m(lista3[3],lista3[1],lista3[2],lista3[0])
mac3= m(lista3[5],lista3[1],lista3[4],lista3[0])
mbc3= m(lista3[5],lista3[3],lista3[4],lista3[2])
eqa3= equa(lista3[1],lista3[0],mab3)
eqb3= equa(lista3[1],lista3[0],mac3)
eqc3= equa(lista3[3],lista3[2],mbc3)

x = linspace(lista3[0],lista3[2], endpoint=True)
plt.plot(x,eval(str(eqa3[0])), color='green')
    
x = linspace(lista3[0],lista3[4], endpoint=True)
plt.plot(x,eval(str(eqb3[0])), color='green')
    
x = linspace(lista3[2],lista3[4], endpoint=True)
plt.plot(x,eval(str(eqc3[0])), color='green')
     
print(f"""As coordenadas para {ang}° são:
A({lista2[0]} , {lista2[1]})
B({lista2[2]} , {lista2[3]})
C({lista2[4]} , {lista2[5]})

E para {ang2}° são:
A({lista3[0]} , {lista3[1]})
B({lista3[2]} , {lista3[3]})
C({lista3[4]} , {lista3[5]})""")

plt.title(f"""Original(Azul)
Rotacionado em {ang}°(Vermelho)
Rotacionado em {ang2}°(Verde)""")
plt.grid(True)
plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.show()       