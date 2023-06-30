import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# The following import configures Matplotlib for 3D plotting.
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm, genlaguerre, factorial
plt.rc('text', usetex=True)

a0 = 0.05292
points = 101

def R(r, n, l):
    rho = 2*r/(n*a0)
    return -np.sqrt((2/(n*a0))**3 * factorial(n - l - 1)/(2*n*factorial(n+l)**3)) * np.exp(-rho/2) * rho**l * genlaguerre(n-l-1,2*l+1)(rho)
# R = lambda r, n, l: (2*r/n/a0)**l * np.exp(-r/n/a0) * genlaguerre(n-l-1,2*l+1)(2*r/n/a0)

def plot_Y(fig, ax, el, m, n, jaja):
    """Plot the spherical harmonic of degree el and order m on Axes ax."""
    r0 = jaja*a0

    x = np.linspace(-r0, r0, points)
    y = np.linspace(-r0, r0, points)

    WF = np.zeros((points, points))
    s = 0

    for dx in range(points):
        for dy in range(points):
            kx = x[dx]
            ky = y[dy]
            phi = math.atan2(ky, kx)
            theta = np.pi/2
            r = np.hypot(kx, ky)
            # theta e phi ao contrário
            Y = sph_harm(abs(m), el, theta, phi)

            #if m < 0:
            #    Y = np.sqrt(2) * (-1)**m * Y.imag
            #elif m > 0:
            #    Y = np.sqrt(2) * (-1)**m * Y.real

            # k = np.abs(R(r, n, l) * Y)**2
            k = R(r, n, l) * Y
            s += np.abs(k)**2

            WF.itemset((dx, dy), np.abs(k))
            # WF[dx, dy] = np.abs(R(r, n, l) * Y)**2

    # WF = np.log10(WF + 1)
    # cmap.set_clim(0, .5)

    # plot R
    """
    kx = np.linspace(0, r0, 100)
    ky = list(map(lambda r: R(r, n, l), kx))

    ax.plot(kx, ky)
    ax.set_xticks(np.linspace(0, r0, 6))
    ax.set_xticklabels(range(0, 6))
    """

    # plot bla
    min = np.min(WF)
    max = np.max(WF)
    print('min: {}, max: {}, sum: {}'.format(min, max, s))

    im = ax.imshow(WF, cmap='inferno', clim=(0, 1))
    ax.set_xticks(np.linspace(0, 101, 11))
    ax.set_yticks(np.linspace(0, 101, 11))
    ax.set_xticklabels(np.linspace(-r0, r0, 11))
    ax.set_yticklabels(np.linspace(-r0, r0, 11))

    # Colour the plotted surface according to the sign of Y.

def plotblablabla(l, m, n, jaja):
    fig = plt.figure(figsize=(8, 8), dpi=100)
    fig.tight_layout(pad=0.0)
    ax = plt.axes()
    plot_Y(fig, ax, l, m, n, jaja)
    plt.savefig('Y{}_{}_{}.png'.format(n, l, m), transparent=False, bbox_inches='tight')
    plt.close()

bla = False

if bla:
    for n in range(1, 5):
        for l in range(0, n):
            for m in range(-l, l + 1):
                while True:
                    print('n: {}, l: {}, m: {}'.format(n, l, m))
                    laklsdjf = int(input('multiplo: '))
                    if laklsdjf != 0:
                        plotblablabla(l, m, n, laklsdjf)
                    else:
                        break
else:
    for n in range(1, 5):
        for l in range(0, n):
            for m in range(-l, l + 1):
                print('n: {}, l: {}, m: {}'.format(n, l, m))
                plotblablabla(l, m, n, 15/(n//3+1))
