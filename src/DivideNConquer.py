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
    
