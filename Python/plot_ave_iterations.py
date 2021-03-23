import numpy as np
import matplotlib.pyplot as plt

import matplotlib.font_manager

flist = matplotlib.font_manager.get_fontconfig_fonts()
names = [
    matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist
]


# data = np.array(
#     [
#         [0, 4.525, 5.075, 5.625, 6.025, 5.313],
#         [0.1, 4.425, 5.1, 5.575, 6.4, 5.375],
#         [0.2, 4.7, 5.2, 5.7, 6.55, 5.538],
#         [0.3, 4.775, 5.3, 5.45, 5.575, 5.275],
#         [0.4, 4.85, 5.175, 5.55, 5.625, 5.3],
#         [0.5, 4.9, 4.75, 4.85, 5.175, 4.919],
#         [0.6, 5, 4.8, 4.7, 5.025, 4.881],
#         [0.7, 4.45, 4.425, 4.525, 4.575, 4.494],
#         [0.8, 4.25, 4.25, 4.475, 4.4, 4.344],
#         [0.9, 4.4, 4.35, 4.45, 4.4, 4.4],
#         [1, 4.2, 4.175, 4.375, 4.275, 4.256],
#         [1.1, 4.475, 4.4, 4.45, 4.525, 4.46],
#         [1.2, 4.225, 4.3, 4.4, 4.4, 4.331],
#         [1.3, 4.625, 4.4, 4.7, 4.55, 4.569],
#         [1.4, 5.075, 4.725, 4.9, 5, 4.925],
#         [1.5, 5, 4.725, 4.975, 4.95, 4.913],
#         [1.6, 4.875, 5.25, 5.35, 5.575, 5.263],
#         [1.7, 4.75, 5.275, 5.5, 5.6, 5.28],
#         [1.8, 4.55, 5.025, 5.425, 6.475, 5.369],
#         [1.9, 4.425, 5.25, 5.55, 6.175, 5.35],
#     ]
# )

data = np.array(
    [
        [0, 4.225, 4.7, 5.25, 5.6, 4.944],
        [0.1, 4.215, 4.75, 5.275, 5.65, 4.95],
        [0.2, 4.225, 4.875, 5.1, 5.8, 5.0],
        [0.3, 4.425, 4.725, 5.125, 5.8, 5.019],
        [0.4, 4.6, 5.05, 5.275, 5.325, 5.063],
        [0.5, 4.475, 4.925, 5.225, 5.3, 4.981],
        [0.6, 4.5, 4.725, 4.875, 4.825, 4.731],
        [0.7, 4.45, 4.75, 4.975, 4.85, 4.756],
        [0.8, 4.5, 4.55, 4.65, 4.65, 4.588],
        [0.9, 4.55, 4.65, 4.7, 4.825, 4.681],
        [1, 4.6, 4.425, 4.475, 4.65, 4.538],
        [1.1, 4.6, 4.575, 4.825, 4.75, 4.688],
        [1.2, 4.7, 4.5, 4.65, 4.7, 4.638],
        [1.3, 4.425, 4.825, 4.95, 5.05, 4.813],
        [1.4, 4.4, 4.8, 4.875, 4.825, 4.725],
        [1.5, 4.475, 4.975, 5.2, 5.35, 5.0],
        [1.6, 4.475, 4.875, 5.275, 5.15, 4.944],
        [1.7, 4.15, 4.675, 5.075, 5.975, 4.969],
        [1.8, 4.175, 4.725, 5.1, 5.725, 4.931],
        [1.9, 4.175, 4.7, 5.025, 5.6, 4.875],
    ]
)


x_label_list = [
    r"0",
    r"0.1$\pi$",
    r"0.2$\pi$",
    r"0.3$\pi$",
    r"0.4$\pi$",
    r"0.5$\pi$",
    r"0.6$\pi$",
    r"0.7$\pi$",
    r"0.8$\pi$",
    r"0.9$\pi$",
    r"$\pi$",
    r"1.1$\pi$",
    r"1.2$\pi$",
    r"1.3$\pi$",
    r"1.4$\pi$",
    r"1.5$\pi$",
    r"1.6$\pi$",
    r"1.7$\pi$",
    r"1.8$\pi$",
    r"1.9$\pi$",
]
graph_list = [
    r"$A_{5 \times 5}$",
    r"$A_{10 \times 10}$",
    r"$A_{20 \times 20}$",
    r"$A_{50 \times 50}$",
]

plt.figure(figsize=(12, 8))
x_vals = data[:, 0]
for i in range(1, data.shape[1] - 1):
    y_vals = data[:, i]
    plt.plot(x_vals, y_vals, "-", label=graph_list[i - 1], alpha=0.4)

y_vals = data[:, data.shape[1] - 1]
plt.plot(x_vals, y_vals, "-", label="Average", color="r", linewidth=2, alpha=1)
plt.xticks(list(np.arange(0, 2, step=0.1)), x_label_list, fontsize=12, rotation=0)
plt.yticks(fontsize=12)
plt.legend(loc="upper right")
# plt.xlabel(r"$\beta$", fontsize=14)

plt.xlim(0, 1.9)
plt.ylim(4, 7)
plt.savefig("./ave_iterations.png")
