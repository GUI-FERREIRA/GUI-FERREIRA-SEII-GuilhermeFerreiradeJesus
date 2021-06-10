#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
import math

def x_dot(t,x,u):
    A = np.array( [[-2., -9.],\
                  [ 1.,  0.]])
    B = np.array([[1.],\
                 [0.]])
    xkp1 = A @ x + B @ u
    return xkp1

def rk4(tk,h,xk,uk):
    xk = xk.reshape([2,1])
    uk = uk.reshape([1,1])
    k1 = x_dot(tk,xk,uk)
    k2 = x_dot(tk+h/2.0,xk+h*k1/2.0,uk)
    k3 = x_dot(tk+h/2.0,xk+h*k2/2.0,uk)
    k4 = x_dot(tk+h,xk+h*k3,uk)
    xkp1 = xk + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
    return xkp1.reshape([2,])

if __name__ == '__main__':
    # Função de transferencia
    G = tf([9],[1,2,9])
    
    #Projeto compensador
    MS = 0.10
    ts = 3
    zeta = np.sqrt(np.log(MS)**2/(np.pi**2+np.log(MS)**2))
    wn = 4/(zeta*ts)

    polo = [zeta*wn,wn*np.sqrt(1-zeta**2)]
    s = -polo[0]+polo[1]*1j    #polos dominantes
    theta = math.atan(polo[1]/polo[0])
    phi = math.pi/2 - theta
    beta = (math.pi - theta)/2
    gamma = theta+beta-phi/2-math.pi/2
    a = polo[0] + polo[1]*math.tan(gamma)
    b = polo[0] + polo[1]*math.tan(gamma+phi)
    C = tf([1,a],[1,b])
    K = abs(1/(evalfr(C,s)*evalfr(G,s)))
    C = K*C
    print(C)

    #letra a
    t = np.arange(1,20, 0.1)
    u = t*0+1
    Tf = feedback(C*G)
    Y, T, *_ = lsim(Tf, u, t)
 
    plt.figure('1')
    plt.plot(T,Y,label='G*C')
    plt.grid()
    plt.legend()
    plt.title('Utilizando lsim')

    #Item b
    Ts = 0.01
    Cd = c2d(C,Ts,method = 'zoh')
    print(Cd)
    Gs = tf2ss(G)
    print(Gs)

    h = 1e-4
    maxT = 10
    mult = Ts/h
    t = np.arange(0,maxT,h)
    tu = np.arange(0,maxT,Ts)

    
    x = np.zeros([2,len(t)])
    u = np.zeros([len(tu)])
    r = np.ones([len(t)-1])
    y = np.zeros([len(t)-1])

    kmax = len(t)-1

    ekm1 = 0
    ukm1 = 0
    p = 0
    for k in range(kmax):
        y[k] = Gs.C @ x[:,k]
        if (k%mult)==0:
            ek = r[k]-y[k]
            u[p] = 0.969*ukm1 + 0.7691*ek - 0.7569*ekm1
            ekm1 = ek
            ukm1 = u[p]
            p += 1
        x[:,k+1] = rk4(t[k],h,x[:,k],u[p-1])
    
    plt.figure('2')
    plt.subplot(2,1,1)
    plt.plot(t,x[0,:])
    plt.subplot(2,1,2)
    plt.plot(t,x[1,:])

    plt.figure('3')
    plt.plot(t[0:-1],y)
    plt.plot(t[0:-1],r)
    plt.title('Utilizando runge kuta')

    plt.figure('4')
    plt.plot(tu[0:len(u)],u)
    plt.ylabel('u_1')
    plt.show()