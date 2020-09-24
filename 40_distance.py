#Python program to compute the distance between the points (x1, y1) and (x2, y2)

from math import sqrt
p1=[4,2]
p2=[6,5]
distance=sqrt(((p1[0]-p2[0])**2 )+ ((p1[1]-p2[1])**2))
print(distance)
