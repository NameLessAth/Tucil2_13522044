from typing import List
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x:float, y:float):
        self.x = x; self.y = y

def midPoint(p1:Point, p2:Point) -> Point:
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)

def bagiBezierBF(arrBez: List[Point], t:int):
    if (len(arrBez) > 2):
        arrLerp:List[Point] = []
        for i in range(len(arrBez)-1):
            arrLerp.append(Point((t*arrBez[i].x + (1-t)*arrBez[i+1].x), (t*arrBez[i].y + (1-t)*arrBez[i+1].y)))
        return bagiBezierBF(arrLerp, t)
    else:
        return Point((t*arrBez[0].x + (1-t)*arrBez[1].x), (t*arrBez[0].y + (1-t)*arrBez[1].y))
        

def bezierBF(arrBez: List[Point], itrTimes: int):
    arrBezRes:List[Point] = []
    for t in range(itrTimes+1):
        arrBezRes.append(bagiBezierBF(arrBez, (1/itrTimes)*t))
    return arrBezRes


# arrBezIt = []
# arrbezRes = []
# xOrigin: List[float] = []
# yOrigin: List[float] = []
# for i in range(5):
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