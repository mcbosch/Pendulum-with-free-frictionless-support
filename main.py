"""
Aquest codi es una simulació del moviment del pèndul amb un suport 
sense fricció. Per calcular la seva trajectoria ens hem ajudat de 
les ecuacions d'Euler Lagrange del seu Lagrangia

L = T - V
  = 1/2*(m1+m2)*v^2 + m2*l*v*w*cos(theta) + 1/2/m*l^2*w^2 + m*g*l*cos(theta)

"""

# Càrrega de paquets necessaris
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definim paràmetres

m1, m2 = 1, 2 # kg, kg
l, g = 5, 9.8 # m, m/s^2

"""
Les ecuacions d'Euler Lagrange ens defineixen una EDO que describim
amb la següent funció que donat un punt defineix la variació com una 
matriu fila.
"""

def F(Y, t):
    x, theta, v, w = Y
    dx_dt = v
    dtheta_dt = w

    # Calculam dv_dt
    K = (m1 + m2 - m2*np.cos(theta)*np.cos(theta))
   
    dv_dt = (m2*g*np.sin(2*theta)*0.5+m2*l*w*w*np.sin(theta))/K

    # Calculam dw_dt amb dv_dt

    dw_dt = - (dv_dt*np.cos(theta))/l-(g*np.sin(theta))/l

    return np.array([dx_dt, dtheta_dt, dv_dt, dw_dt])


def rk4(Y,f,h,t):
    k1 = h * f(Y, t)    
    k2 = h * f(Y + 0.5*k1, t + 0.5*h)
    k3 = h * f(Y + 0.5*k2, t + 0.5*h)
    k4 = h * f(Y + k3, t + h)
    Y2 = Y + (k1 + 2*(k2 + k3 ) + k4) / 6
    return Y2


"""
La funcio rk4 ens dona el valor de la trajectoria en la següent iteració.
Feiem llavors una partició del temps i calculem la trajectoria.
"""
t0, tf, n = 0, 10, 10000
h = (tf -t0)/n
t = np.linspace(t0,tf,n+1)
Y0 = np.array([-7.5,np.radians(120),1,0]) 
trajectoria= np.array((n+1)*[Y0])

# Calculam la trajectoria

for i in range(n): trajectoria[i+1] = rk4(trajectoria[i],F,h,t[i])

X, TH, V, W = trajectoria.T[0], trajectoria.T[1], trajectoria.T[2], trajectoria.T[3]

# Cram una animació

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlim(-2 * l, 2 * l)
ax.set_ylim(-2 * l, 2 * l)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)  # Línea del péndulo
trail, = ax.plot([], [], 'r-', lw=1, alpha=0.5)  # Trazo del péndulo

x_trail, y_trail = [], []

def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail

def update(frame):
    x = X[frame] + l * np.sin(TH[frame])
    y = -l * np.cos(TH[frame])
    line.set_data([X[frame], x], [0, y])
    x_trail.append(x)
    y_trail.append(y)
    trail.set_data(x_trail, y_trail)
    return line, trail


ani = FuncAnimation(fig, update, frames=range(0,n,10), init_func=init, blit=True,interval = 5)
plt.show()
# Mostrar animación
# ani.save('pendulo.gif', fps=120, writer='pillow')


