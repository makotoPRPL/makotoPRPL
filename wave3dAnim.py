import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



cm = plt.get_cmap("Spectral_r")
fig=plt.figure(dpi=150)

def graphFunc(time):
  plt.clf()
  ax=fig.add_subplot(111, projection="3d")

  x0=0.2
  y0=0.3
  z0=0.1

  ax.scatter(x0,y0,z0, s=30, c="red")
  xyzlim=1
  ax.set_xlim(-xyzlim, xyzlim)
  ax.set_ylim(-xyzlim, xyzlim)
  ax.set_zlim(-xyzlim, xyzlim)
  ax.set_xticks([-1, 0, 1])
  ax.set_yticks([-1, 0, 1])
  ax.set_zticks([-1, 0, 1])
  ax.set_xlabel("x [m]")
  ax.set_ylabel("y [m]")
  ax.set_zlabel("z [m]")
  #ax.view_init(30, -30)

  kx=7
  ky=0
  kz=0
  omg=np.sqrt(kx+ky+kz)/2
  t=0.2*time

  dxyz=0.25
  for x in np.arange(-1, 1.1, dxyz):
    for y in np.arange(-1, 1.1, dxyz):
      for z in np.arange(-1, 1.1, dxyz):
        density=np.cos(kx*x+ky*y+kz*z-omg*t)
        txt="{:.1f}".format(density)
        cindex=(density+1)/2
        #ax.text(x,y,z, txt, alpha=density, size=8, c=cm(density))
        ax.text(x,y,z, txt, alpha=0.6, size=8, c=cm(cindex))

ani = animation.FuncAnimation(fig, graphFunc, interval=100, frames=100)

#ani.save('anim.mp4', writer='ffmpeg', fps=20)
plt.show()
