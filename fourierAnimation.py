import matplotlib.pyplot as plt

import matplotlib.patches as patches

import numpy as np

import matplotlib.animation as animation



fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5), sharey=True)

plt.subplots_adjust(wspace=0)

im = []

ims = []

rightX = []

rightY = []

rds = [0, 1, 0.33, 0.2, 1./7, 1./9, 1./11, 1./13, 1./15, 1./17]

# rds = [0, 1]



for wt in np.arange(0, 3.1415 * 10, 0.1):

    art1 = []

    art2 = []



    ax1.set_xlim(-2, 2)

    ax1.set_ylim(-2, 2)

    ax1.set_position([0.1, 0.1, 0.4, 0.8])

    ax1.spines["right"].set_color("none")

    ax1.spines["left"].set_color("none")

    ax1.spines["top"].set_color("none")

    ax1.spines["bottom"].set_color("none")

    ax1.tick_params(labelbottom=False, labelleft=False, labelright=False,

                    labeltop=False, bottom=False, left=False, right=False, top=False)

    # ax1.set_aspect('equal')



    ax2.set_xlim(-0.5, 6)

    ax2.set_ylim(-2, 2)

    ax2.set_position([0.5, 0.1, 0.4, 0.8])

    ax2.spines["right"].set_color("none")

    ax2.spines["left"].set_color("none")

    ax2.spines["top"].set_color("none")

    ax2.spines["bottom"].set_color("none")

    ax2.tick_params(labelbottom=False, labelleft=False, labelright=False,

                    labeltop=False, bottom=False, left=False, right=False, top=False)

    # ax3.set_aspect('equal')



    xn = np.zeros(len(rds))

    yn = np.zeros(len(rds))

    cntx = np.zeros(len(rds))

    cnty = np.zeros(len(rds))

    pntx = np.zeros(len(rds))

    pnty = np.zeros(len(rds))



    for n in range(1, len(rds)):

        xn[n] = rds[n] * np.cos((2 * n - 1) * wt)

        yn[n] = rds[n] * np.sin((2 * n - 1) * wt)

        for m in range(1, n + 1):

            cntx[n] += xn[m - 1]

            cnty[n] += yn[m - 1]

            pntx[n] += xn[m]

            pnty[n] += yn[m]

        cn = patches.Circle(xy=(cntx[n], cnty[n]), radius=rds[n], fill=False, ec='grey')

        art1.append(ax1.add_patch(cn))

        art2 += ax1.plot([cntx[n], pntx[n]], [cnty[n], pnty[n]], ':', c='grey', linewidth=1)

    art3 = ax1.plot([pntx[n], 2], [pnty[n], pnty[n]], linewidth=1, c='red')

    art4 = ax1.scatter(pntx[1:], pnty[1:], s=8, c='red')



    art5 = ax2.plot([-2, 0], [pnty[n], pnty[n]], linewidth=1, c='red')

    art6 = ax2.scatter(0, pnty[n], s=8, c='red')



    rightX.append(wt * 0.5)

    rightY.insert(0, pnty[n])



    art7 = ax2.plot(rightX, rightY, linewidth=1, c='red')



    im = art1 + art2 + art3 + [art4] + art5 + [art6] + art7

    ims.append(im)





ani = animation.ArtistAnimation(fig, ims, interval=60, repeat_delay=0)

ani.save('anim.mp4', writer='ffmpeg', fps=8)



plt.show()

