# import matplotlib.pyplot as plt


# plt.axhline(y=3, color="red", linestyle="-")
# plt.axhline(y=1)
# # plt.axhline(y=0.5, xmin=0.25, xmax=0.75)
# plt.show()


import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import random

plt.figure(figsize=(50, 80), dpi=300)

start = 0.0
stop = 1.0

# represents the days, should be 29200
number_of_lines = 1000
cm_subsection = linspace(start, stop, number_of_lines)

random.shuffle(cm_subsection)

# prism color map
# colors = [cm.prism(x) for x in cm_subsection]

# jet color map
colors = [cm.jet(x) for x in cm_subsection]

for i, color in enumerate(colors):
    plt.axhline(i, color=color)

plt.axis("off")
plt.savefig("life_lines.png", bbox_inches="tight")
