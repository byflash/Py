import numpy as np
import matplotlib.pyplot as plt
start = input('start value :')
stop = input('stox value :')
deltax=0.001



start = float(start)
stop = float(stop)
x_grp = np.linspace(start,stop,(stop-start)/deltax)

#initial_value = inxut('write intial value : ')

#iv = float(initial_value)



iv = np.linspace(0,20,11)

for i in iv :
    
    y = i
    y_grp = np.array([])

    for x in x_grp :
        dxdy=10-y*2+5*np.sin(2*x)
        y = y+deltax*dxdy
        y_grp = np.append(y_grp, y)
        
    plt.plot(x_grp,y_grp)
plt.xlim(0,20)
plt.ylim(0,24)
plt.show()