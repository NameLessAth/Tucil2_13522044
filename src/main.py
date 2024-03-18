from DivideNConquer import *
from BruteForce import *
import matplotlib.pyplot as plt
import time

print("===BEZIER CALCULATOR===")
print("program untuk membandingkan algoritma Divide and Conquer dengan Brute Force")

itrTimes = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Divide and Conquer): "))
while (itrTimes < 1):
    print("Mohon masukkan jumlah iterasi lebih dari atau sama dengan 1 !")
    itrTimes = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Divide and Conquer): "))

itrTimesBF = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Brute Force): "))
while (itrTimesBF < 1):
    print("Mohon masukkan jumlah iterasi lebih dari atau sama dengan 1 !")
    itrTimesBF = int(input("Masukkan jumlah iterasi yang diinginkan (untuk Brute Force): "))

jumlPoint = int(input("Masukkan berapa banyak titik yang diinginkan (n > 2) : "))
while (jumlPoint <= 2):
    print("Mohon masukkan jumlah titik di atas 2 !")
    jumlPoint = int(input("Masukkan berapa banyak titik yang diinginkan (n > 2) : "))

arrBezIt: List[Point] = []
xOrigin: List[float] = []
yOrigin: List[float] = []
for i in range(jumlPoint):
    x = float(input(f"masukkan x{i+1}: "))
    y = float(input(f"masukkan y{i+1}: "))
    xOrigin.append(x)
    yOrigin.append(y)
    arrBezIt.append(Point(x, y))

startBF = time.perf_counter()
resBF : List[Point] = bezierBF(arrBezIt, itrTimesBF)
endBF = time.perf_counter()

startDNC = time.perf_counter()
resDNC : List[Point] = [arrBezIt[0]]
resDNC = resDNC + bezierDNC(arrBezIt, 0, itrTimes)
resDNC.append(arrBezIt[len(arrBezIt)-1])
endDNC = time.perf_counter()

xBF: List[float] = []; yBF: List[float] = []
for i in resBF:
    xBF.append(i.x)
    yBF.append(i.y)

xDNC: List[float] = []; yDNC: List[float] = []
for i in resDNC:
    xDNC.append(i.x)
    yDNC.append(i.y)

fig, axes = plt.subplots(1, 3)

axes[0].plot(xOrigin, yOrigin, marker='o', markersize=5)
axes[0].plot(xBF, yBF, marker='o', markersize=1)
axes[0].plot(xDNC, yDNC, marker='o', markersize=1)

axes[1].plot(xOrigin, yOrigin, marker='o', markersize=5)
axes[1].plot(xDNC, yDNC, marker='o', markersize=1)

axes[2].plot(xOrigin, yOrigin, marker='o', markersize=5)
axes[2].plot(xBF, yBF, marker='o', markersize=1)

axes[0].legend(["Titik Aseli", "Algoritma Brute Force", "Algoritma Divide n Conquer"])
axes[1].legend(["Titik Aseli", "Algoritma Divide n Conquer"])
axes[2].legend(["Titik Aseli", "Algoritma Brute Force"])

print(f"Waktu yang dibutuhkan untuk menghitung kurva bezier dengan algoritma Divide and Conquer: {endDNC-startDNC} sekon")
print(f"Waktu yang dibutuhkan untuk menghitung kurva bezier dengan algoritma Brute Force: {endBF-startBF} sekon")

plt.show()