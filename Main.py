from DivideNConquer import *
from BruteForce import *


print("===BEZIER CALCULATOR===")
print("program untuk membandingkan algoritma Divide and Conquer dengan Brute Force")
arrBezIt = []
xOrigin: List[float] = []
yOrigin: List[float] = []
itrTimes = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Divide and Conquer): "))
while (itrTimes < 1):
    print("Mohon masukkan jumlah iterasi diatas 1 !")
    itrTimes = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Divide and Conquer): "))
for i in range(3):
    x = float(input(f"masukkan x{i+1}: "))
    y = float(input(f"masukkan y{i+1}: "))
    xOrigin.append(x)
    yOrigin.append(y)
    arrBezIt.append(Point(x, y))


resBF : List[Point] = bezierBF(arrBezIt)
resDNC : List[Point] = [arrBezIt[0]]
resDNC = resDNC + bezierDNC(arrBezIt, 0, itrTimes)
resDNC.append(arrBezIt[2])

xBF: List[float] = []; yBF: List[float] = []
for i in resBF:
    xBF.append(i.x)
    yBF.append(i.y)

xDNC: List[float] = []; yDNC: List[float] = []
for i in resDNC:
    xDNC.append(i.x)
    yDNC.append(i.y)

plt.plot(xOrigin, yOrigin)
plt.plot(xBF, yBF)
plt.plot(xDNC, yDNC)

plt.legend(["Titik Aseli", "Algoritma Brute Force", "Algoritma Divide n Conquer"])
plt.show()