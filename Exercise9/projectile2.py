from math import pi, sin, tan, cos
theta = 80*(pi/180)
g = 9.81
Vo = 44
x = 0.5
Yo = 1
height = Yo + x*tan(theta) - ((g*0.5**2)/(2*(Vo*cos(theta))**2))
print(height)

# theta is (0 with a strike through)