from typing import List
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x:float, y:float):
        self.x = x; self.y = y

def midPoint(p1:Point, p2:Point) -> Point:
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)

def bagiBezierBF(arrBez: List[Point], t:int) -> Point:
    if (len(arrBez) > 2):
        arrLerp:List[Point] = []
        for i in range(len(arrBez)-1):
            arrLerp.append(Point((t*arrBez[i].x + (1-t)*arrBez[i+1].x), (t*arrBez[i].y + (1-t)*arrBez[i+1].y)))
        return bagiBezierBF(arrLerp, t)
    else:
        return Point((t*arrBez[0].x + (1-t)*arrBez[1].x), (t*arrBez[0].y + (1-t)*arrBez[1].y))
        

def bezierBF(arrBez: List[Point], itrTimes: int) -> List[Point]:
    arrBezRes:List[Point] = []
    for t in range(itrTimes+1):
        arrBezRes.append(bagiBezierBF(arrBez, (1/itrTimes)*t))
    return arrBezRes

