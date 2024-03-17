from typing import List
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x:float, y:float):
        self.x = x; self.y = y

def midPoint(p1:Point, p2:Point) -> Point:
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)

def bezierBF(arrBez: List[Point]):
    arrBezRes:List[Point] = []
    for t in range(101):
        lerp1 = Point(((0.01*t)*arrBez[0].x + (1-(0.01*t))*arrBez[1].x), ((0.01*t)*arrBez[0].y + (1-(0.01*t))*arrBez[1].y))
        lerp2 = Point(((0.01*t)*arrBez[1].x + (1-(0.01*t))*arrBez[2].x), ((0.01*t)*arrBez[1].y + (1-(0.01*t))*arrBez[2].y))
        lerp3 = Point(((0.01*t)*lerp1.x + (1-(0.01*t))*lerp2.x), ((0.01*t)*lerp1.y + (1-(0.01*t))*lerp2.y))
        arrBezRes.append(lerp3)
    return arrBezRes


# arrBezIt = []
# arrbezRes = []
# xOrigin: List[float] = []
# yOrigin: List[float] = []
# for i in range(3):
#     x = float(input(f"masukkan x{i+1}: "))
#     y = float(input(f"masukkan y{i+1}: "))
#     xOrigin.append(x)
#     yOrigin.append(y)
#     arrBezIt.append(Point(x, y))
# # arrbezRes.append(arrBezIt[0])
# arrbezRes = arrbezRes + bezierBF(arrBezIt)
# # arrbezRes.append(arrBezIt[len(arrBezIt)-1])
# xlist: List[float] = []
# ylist: List[float] = []
# for i in arrbezRes:
#     xlist.append(i.x)
#     ylist.append(i.y)
# plt.plot(xlist, ylist)
# plt.plot(xOrigin, yOrigin)
# plt.legend(["Hasil Via Divide and Conquer", "Titik Aseli"])
# plt.show()