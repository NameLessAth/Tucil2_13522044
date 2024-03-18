from typing import List
from typing import Optional
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x:float, y:float):
        self.x = x; self.y = y

def midPoint(p1:Point, p2:Point) -> Point:
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)

def bagiBezierDNC(arrBez:List[Point]) -> List[Point]:
    if (len(arrBez) > 2):
        arrRes = [arrBez[0]]
        arrBezNew = []
        for i in range(len(arrBez)-1):
            arrBezNew.append(midPoint(arrBez[i], arrBez[i+1]))
        arrRes = arrRes + bagiBezierDNC(arrBezNew)
        arrRes.append(arrBez[len(arrBez)-1])
        return arrRes
    else:
        return [arrBez[0], midPoint(arrBez[0], arrBez[1]), arrBez[1]]

def bezierDNC(arrBez:List[Point], currentIterations:int, wantedIterations:int) -> Optional[Point]:
    if (currentIterations < wantedIterations):
        # declare var dan masukkan bahan iterasi selanjutnya dengan midpoint2 tertentu
        arrBezRes:List[Point] = []
        arrBezNew = bagiBezierDNC(arrBez)

        iterate1 = arrBezNew[:((len(arrBezNew)//2)+1)]
        arrTemp1:Optional[Point] = bezierDNC(iterate1, currentIterations+1, wantedIterations)
        if arrTemp1 != None:
            arrBezRes = arrBezRes + arrTemp1

        arrBezRes.append(arrBezNew[len(arrBezNew)//2])
        
        iterate2 = arrBezNew[len(arrBezNew)//2:]
        arrTemp2:Optional[Point] = bezierDNC(iterate2, currentIterations+1, wantedIterations)
        if arrTemp2 != None:
            arrBezRes = arrBezRes + arrTemp2

        return arrBezRes
    else:
        return None
    

# arrBezIt = []
# arrbezRes = []
# xOrigin: List[float] = []
# yOrigin: List[float] = []
# for i in range(2):
#     x = float(input(f"masukkan x{i+1}: "))
#     y = float(input(f"masukkan y{i+1}: "))
#     xOrigin.append(x)
#     yOrigin.append(y)
#     arrBezIt.append(Point(x, y))
# arrbezRes.append(arrBezIt[0])
# arrbezRes = arrbezRes + bezierDNC(arrBezIt, 0, 10)
# arrbezRes.append(arrBezIt[len(arrBezIt)-1])
# xlist: List[float] = []
# ylist: List[float] = []
# for i in arrbezRes:
#     xlist.append(i.x)
#     ylist.append(i.y)

# plt.plot(xlist, ylist)
# plt.plot(xOrigin, yOrigin)
# plt.legend(["Hasil Via Divide and Conquer", "Titik Aseli"])
# plt.show()
# # print(xlist)
# # print(ylist)