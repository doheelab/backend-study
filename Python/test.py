import numpy as np

aa

l1 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([293.609, 1277.047, 1670.766, 2778.359, 4225.313, 6366.609]) / 50,
    )
)
l2 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([340.734, 1469.312, 2029.094, 3109.469, 4623.078, 7476.813]) / 50,
    )
)
l3 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([289.265, 1071.468, 1384.906, 2309.313, 3188.531, 4572.031]) / 50,
    )
)
l4 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([172.844, 987.640, 774.985, 1462.703, 2326.485, 3605.875]) / 50,
    )
)
l5 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([263.016, 1032.312, 1524.719, 2710.359, 3768.219, 4129.125]) / 50,
    )
)
l6 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([159.812, 614.000, 1390.640, 1824.594, 3472.031, 3636.094]) / 50,
    )
)
l7 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([161.703, 785.297, 600.625, 1053.562, 1609.547, 2339.969]) / 50,
    )
)
l8 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([170.891, 832.984, 657.375, 1187.844, 1813.985, 2646.922]) / 50,
    )
)
l9 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([251.203, 1151.516, 825.703, 1537.453, 2337.5, 3442]) / 50,
    )
)
l10 = list(
    map(
        lambda x: np.round(x, 2),
        np.array([244.015, 1058.641, 744.047, 1282.094, 1970.891, 2744.016]) / 50,
    )
)

for i in [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]:
    print(np.round(np.mean(i), 2))

#######

l1 = [19.18, 20.8, 22.34, 22.08, 22.78, 23.20, 21.73]
l2 = [12.28, 13.34, 14.28, 14.14, 14.62, 14.84, 13.92]
l3 = [6.66, 7.38, 7.88, 7.74, 7.88, 7.92, 7.60]
l4 = [6.46, 6.98, 7.44, 7.5, 7.56, 7.68, 0]
l5 = [6.28, 6.68, 7.12, 7.40, 7.66, 7.64, 7.27]
l6 = [6.24, 7.12, 7, 7, 7.1, 7.34, 7.27]
l7 = [4.22, 4.30, 4.26, 4.30, 4.36, 4.22, 4.28]
l8 = [4.56, 4.60, 4.62, 5.08, 5.40, 5.34, 4.93]
l9 = [4.78, 4.96, 5.38, 6.04, 6.42, 6.84, 4.28]
l10 = [4.36, 4.40, 4.54, 4.48, 4.68, 4.52, 4.93]

for i in [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]:
    print(np.round(np.mean(i), 2))
