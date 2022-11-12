import math
from random import randint

R = [
    (math.inf, -1, -1),
    (13, 1, 2),
    (18, 1, 3),
    (17, 1, 4),
    (14, 1, 5),
    (22, 1, 6),
    (26, 2, 3),
    (19, 2, 5),
    (30, 3, 4),
    (22, 4, 6),
]


def get_max(R):
    x = max(R, key=lambda x: x[1])
    y = max(R, key=lambda x: x[2])
    max1 = x[2]
    max2 = y[2]
    if max1 >= max2:
        maximum = max1
    else:
        maximum = max2
    return maximum


def get_min(R, U):
    rm = (math.inf, -1, -1)
    for v in U:
        rr = min(
            R,
            key=lambda x: x[0]
            if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U)
            else math.inf,
        )
        if rm[0] > rr[0]:
            rm = rr

    return rm


def prima(R):
    N = 6
    U = {R[1][2]}
    T = []

    while len(U) < N:
        r = get_min(R, U)
        if r[0] == math.inf:
            break

        T.append(r)
        U.add(r[1])
        U.add(r[2])

    print(T)


prima(R)
