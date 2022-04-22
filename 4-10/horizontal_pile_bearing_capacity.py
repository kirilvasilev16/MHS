import numpy as np
import matplotlib.pyplot as plt


def calculate(gamma, W, I, h, K_p):
    t_0 = I / 1.2
    return gamma * K_p * t_0 ** 3 / 24 * (t_0 + 4 * W) / (t_0 + h)


def capacity_plot(gamma=10, W=0.3, I=5, h=6, K_p=4):

    P_horizontal = calculate(gamma, W, I, h, K_p)
    print(f"P_horizontal: {round(P_horizontal, 1)}kN\n")

    fig, ax = plt.subplots(1, 4, figsize=(25, 5))
    x = np.linspace(0, 1, 100)
    y = calculate(gamma, x, I, h, K_p)
    ax[0].plot(x, y, "b", linewidth=2)
    ax[0].plot(W, P_horizontal, "r.", markersize=20)
    ax[0].set_xlabel("W - tickness [m]")

    x = np.linspace(0, 10, 100)
    y = calculate(gamma, W, x, h, K_p)
    ax[1].plot(x, y, "g", linewidth=2)
    ax[1].plot(I, P_horizontal, "r.", markersize=20)
    ax[1].set_xlabel("I - moment of inertia of the pile [m]")

    x = np.linspace(1, 10, 100)
    y = calculate(gamma, W, I, x, K_p)
    ax[2].plot(x, y, "purple", linewidth=2)
    ax[2].plot(h, P_horizontal, "r.", markersize=20)
    ax[2].set_xlabel("h - length of the unsupported part [-]")

    x = np.linspace(0, 10, 100)
    y = calculate(gamma, W, I, h, x)
    ax[3].plot(x, y, "black", linewidth=2)
    ax[3].plot(K_p, P_horizontal, "r.", markersize=20)
    ax[3].set_xlabel("K_p - passive soil pressure coefficient [m]")

    for axes in ax:
        axes.set_ylabel("P_horizontal [kN]")
        axes.grid()

    plt.tight_layout()
    plt.show()
