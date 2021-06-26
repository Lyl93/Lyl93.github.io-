import numpy as np
import matplotlib.pyplot as plt


mu_0 = 4* np.pi * 1e-7
i = 20e-3


def rayon_section_sphere(hauteur, rayon_sphere):
    return np.sqrt(rayon_sphere**2 - hauteur**2)


def champ_bobine_i(x, o_i, rayon_sphere):
    return mu_0 * i * rayon_section_sphere(o_i, rayon_sphere) / (2 * (rayon_section_sphere(o_i, rayon_sphere)**2 + (x - o_i)**2)**(3./2))


rayon = 0.5
h = 0.02

x = np.linspace(-1, 1, 500)
bobine_centres = np.linspace(-0.40, 0.42, num=41, endpoint=False)
print(bobine_centres)

champs = []
for o in bobine_centres:
    # s = str(o) + '\t' + str(rayon_section_sphere(o, rayon))
    # print(s)
    champs.append(champ_bobine_i(x, o, rayon))

champ_total = [0]*len(champs[0])
for i in range(len(champs[0])):
    for o in range(len(champs)):
        champ_total[i] += champs[o][i]

fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(8, 8))

for champ in champs:
    ax2.plot(x, champ, 'b-')

ax2.set_xlabel("$x$ (m)", fontsize=15)
ax2.set_xlim(left=-1, right=1)
ax2.set_ylim(bottom=0)
ax2.set_ylabel("$B_x^i$ (T)", fontsize=15)

ax1.plot(x, champ_total, 'b-')
ax1.set_ylabel("$B_x^{\\rm tot}$ (T)", fontsize=15)
# plt.yscale("log")

plt.show()
