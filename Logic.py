import math

def DistanceToPoint(position1, position2):
    return math.sqrt(pow(abs(position1[0] - position2[0]), 2) + pow(abs(position1[1] - position2[1]), 2))

def DistanceToLine(position, line):
    lP1, lP2, p = line[0], line[1], position
    if not (lP1[0] == lP2[0] or lP1[1] == lP2[1]):
        a = (lP1[1] - lP2[1]) / (lP1[0] - lP2[0])
        aP = - 1 / a
        xPer = (a * lP1[0] - lP1[1] - aP * p[0] + p[1]) / (a - aP)
        yPer = aP * (xPer - p[0]) + p[1]
    elif lP1[0] == lP2[0]:
        xPer = lP1[0]
        yPer = p[1]
    else:
        xPer = p[0]
        yPer = lP1[1]
    dp1 = DistanceToPoint(p, lP1)
    dp2 = DistanceToPoint(p, lP2)
    dpP = DistanceToPoint(p, (xPer, yPer))
    bl1 = lP1[0] <= xPer <= lP2[0]
    bl2 = lP1[1] <= yPer <= lP2[1]
    bm1 = lP1[0] >= xPer >= lP2[0]
    bm2 = lP1[1] >= yPer >= lP2[1]

    if (bl1 and bl2) or (bm1 and bm2) or (bm1 and bl2) or (bl1 and bm2):
        return dpP
    else:
        return min(dp1, dp2)

def DistanceToCircle(position, circle):
    return DistanceToPoint(position, (circle[0], circle[1])) - circle[2]

def DistanceToBox(position, box):
    x0, y0, x1, y1 = box
    x, y = position
    dx = min(abs(x - x0), abs(x - x1))
    dy = min(abs(y - y0), abs(y - y1))
    if x0 < x < x1:
        return dy
    elif y0 < y < y1:
        return dx
    else:
        return math.sqrt(dx ** 2 + dy ** 2)

def DistanceToPolygon(position, polygon):
    distances = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        if i < len(polygon) - 1:
            p2 = polygon[i + 1]
        else:
            p2 = polygon[0]
        distances.append(DistanceToLine(position, (p1, p2)))
    return min(distances)
