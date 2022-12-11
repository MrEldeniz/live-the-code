from turtle import*
import colorsys
tracer(560)
bgcolor("black")
pensize(3)
h =0.4
def a ():
 h=0
 n=10
 for i in range (220):
  c=colorsys.hsv_to_rgb(h,1,1)
  color("black")
  h+=1/n
  fillcolor (c)
  right (89)
  circle (i,159,steps=1)
  begin_fill ()
  rt(208)
  bk(20)
  circle (i,296,steps=1)
  end_fill ()
  for j in range (26):
    up()
    goto (0,0)
    down ()
    color (c)
    rt(29)
    circle (i,346,steps=1)
    right (80)


a()
done ()    
