import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x=np.linspace(-20,20,5001)

def omega(kk):
	wp=3
	v0=1
	return (wp**2+v0**2*kk**2)**0.5

fig=plt.figure(figsize=(6,2))

def graphFunc(time):
	fig.clf()

	tt=time*0.05

	y1=0
	for k1 in np.arange(0, 15, 0.2):
		y1=y1+np.exp(-(k1-4)**2/4**2)*np.cos(k1*x-omega(k1)*tt)
	ax=fig.add_subplot(111)
	ax.set_ylim([-40,40])
	ax.plot(x,y1, lw=0.5, c="red")



ani = animation.FuncAnimation(fig, graphFunc, interval=100, frames=500)

ani.save('wavePacket.mp4', writer='ffmpeg', fps=20)
#plt.show()
