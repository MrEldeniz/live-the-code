import math
from turtle import*
import colorsys
def heartx(n):
    return 14* math.sin(n)**3
def hearty (n):
    return 12*math.cos(n)-5*\
        math.cos(2*n)-2*\
        math.cos(3*n)-\
        math.cos(4*n)
tracer (10)
h =0.4
bgcolor ("black")
v=["red", "pink"]
for i in range (5000):
    goto (heartx(i)*20, hearty(i)*20)
    for j in range (5):
        color (v[i%2])
        goto (0,0)
done ()