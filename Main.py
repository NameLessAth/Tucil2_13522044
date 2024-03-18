from DivideNConquer import *
from BruteForce import *


print("===BEZIER CALCULATOR===")
print("program untuk membandingkan algoritma Divide and Conquer dengan Brute Force")

itrTimes = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Divide and Conquer): "))
while (itrTimes <= 1):
    print("Mohon masukkan jumlah iterasi diatas 1 !")
    itrTimes = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Divide and Conquer): "))

itrTimesBF = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Brute Force): "))
while (itrTimesBF <= 1):
    print("Mohon masukkan jumlah iterasi diatas 1 !")
    itrTimesBF = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Brute Force): "))

jumlPoint = int(input("Masukkan berapa banyak titik yang diinginkan (n > 2) : "))
while (jumlPoint <= 2):
    print("Mohon masukkan jumlah titik di atas 2 !")
    jumlPoint = int(input("Masukkan berapa banyak titik yang diinginkan (n > 2) : "))

arrBezIt = []
xOrigin: List[float] = []
yOrigin: List[float] = []
for i in range(jumlPoint):
    x = float(input(f"masukkan x{i+1}: "))
    y = float(input(f"masukkan y{i+1}: "))
    xOrigin.append(x)
    yOrigin.append(y)
    arrBezIt.append(Point(x, y))


resBF : List[Point] = bezierBF(arrBezIt, itrTimesBF)
resDNC : List[Point] = [arrBezIt[0]]
resDNC = resDNC + bezierDNC(arrBezIt, 0, itrTimes)
resDNC.append(arrBezIt[len(arrBezIt)-1])

xBF: List[float] = []; yBF: List[float] = []
for i in resBF:
    xBF.append(i.x)
    yBF.append(i.y)

xDNC: List[float] = []; yDNC: List[float] = []
for i in resDNC:
    xDNC.append(i.x)
    yDNC.append(i.y)

plt.plot(xOrigin, yOrigin, marker='o', markersize=5)
plt.plot(xBF, yBF, marker = 'o', markersize=1)
plt.plot(xDNC, yDNC, marker='o', markersize=1)

plt.legend(["Titik Aseli", "Algoritma Brute Force", "Algoritma Divide n Conquer"])
plt.show()