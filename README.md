# Pendulum-with-free-frictionless-support
This program simulates the movement of a pendulum with a free fritionless support on the x-coordinate. See the following image:


To calculate te path of the masses i defined an EDO with the ecuations that define the Lagrangian. We have two masses the support $M_1$, 
and the pendulum $M_2$. Then we define the position and velocitis of each particle with $x$ and $\theta$:

$$
\begin{array}{cc}
  x_1 =  x & y_1 =  0 \\
  x_2 =  x + lsin(\theta) & y_2 = -lcos(\theta)
\end{array}
$$

Therefore we have the velociti for the particle one is $(\dot{x},0)$ and for the particle two is $(\dot{x} + l\dot{\theta}cos(\theta), l\dot{\theta}sin(\theta))$.
Calculating the cinetic energy and the potencial energy we obtain the next lagrangian:

$$
\begin{aligned}
  L &= T - U = (T_1 + T_2) - (U_1 + U_2) \\
  & = \frac{1}{2}(M_1+M_2)\dot{x}^2 + M_2l\dot{\theta}\dot{x}cos(\theta) + \frac{1}{2}M_2l^2\dot{\theta}^2 + mglcos(\theta)
\end{aligned}
$$

Then computing the Euler-Lagrange equations: $\frac{d}{dt}\frac{\partial L}{\partial\dot{x}} - \frac{\partial L}{\partial x} = 0$ and $\frac{d}{dt}\frac{\partial L}{\partial\dot{\theta}} - \frac{\partial L}{\partial \theta} = 0$
we obtain the next two equations:

$$
\begin{aligned}
  (E_1):& \frac{1}{2}(M_1 + M_2)\ddot{x} + M_2l\ddot{\theta}cos(\theta) - M_2l\dot{\theta}^2sin(\theta) = 0 \\
  (E_2): & l\ddot{\theta} + \ddot{x}cos(\theta) + gsin(\theta) = 0
\end{aligned}
$$

After that we only have to rename the variables $v:= \dot{x}$ and $w:=\dot{\theta}$ define our EDO and apply for example a Runge Kutta so we can aproximate the trayectori. Here we have an example with
initial conditions $x = -7.5; \theta = 120º; v = 1; w = 0$:
![pendulo](https://github.com/user-attachments/assets/bdc6ef6d-56b5-424c-920a-07e69942e981)
