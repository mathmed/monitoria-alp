import math
for i in range (0,361,15):
    y=math.sin(math.radians(i))
    x=math.cos(math.radians(i))
    print('seno de %d é %5.2f e cosseno de %d é %5.2f (arredondados)' % (i,y,i,x))
