from typing import List
from typing import Optional
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x:float, y:float):
        self.x = x; self.y = y

def midPoint(p1:Point, p2:Point) -> Point:
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)



def bezier(arrBez:List[Point], currentIterations:int, wantedIterations:int) -> Optional[Point]:
    if (currentIterations < wantedIterations):
        # declare var dan masukkan bahan iterasi selanjutnya dengan midpoint2 tertentu
        arrBezRes:List[Point] = []
        arrBezNew:List[Point] = []
        arrBezNew.append(midPoint(arrBez[0], arrBez[1]))
        arrBezNew.append(midPoint(arrBez[1], arrBez[2]))
        arrBezNew.append(midPoint(arrBezNew[0], arrBezNew[1]))

        iterate1 = [arrBez[0], arrBezNew[0], arrBezNew[2]]
        arrTemp1:Optional[Point] = bezier(iterate1, currentIterations+1, wantedIterations)
        if arrTemp1 != None:
            arrBezRes = arrBezRes + arrTemp1

        arrBezRes.append(arrBezNew[2])
        
        iterate2 = [arrBezNew[2], arrBezNew[1], arrBez[2]]
        arrTemp2:Optional[Point] = bezier(iterate2, currentIterations+1, wantedIterations)
        if arrTemp2 != None:
            arrBezRes = arrBezRes + arrTemp2

        return arrBezRes
    else:
        return None
    

arrBezIt = []
arrbezRes = []
for i in range(3):
    x = float(input(f"masukkan x{i+1}: "))
    y = float(input(f"masukkan y{i+1}: "))
    arrBezIt.append(Point(x, y))
arrbezRes.append(arrBezIt[0])
arrbezRes = arrbezRes + bezier(arrBezIt, 0, 2)
arrbezRes.append(arrBezIt[len(arrBezIt)-1])
xlist: List[float] = []
ylist: List[float] = []
for i in arrbezRes:
    xlist.append(i.x)
    ylist.append(i.y)
plt.plot(xlist, ylist)
plt.show()
# print(xlist)
# print(ylist)