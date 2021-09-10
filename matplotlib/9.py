# contour
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return(1-x/2+x**5+y**3)*np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
#创建网格(等高线基于网格生成)
X, Y = np.meshgrid(x,y)
#use plt.contourf to filling contours
#X,Y and value for (X,Y) point       8:画出8+1条等高线，分为10瓣
plt.contourf(X,Y,f(X,Y),8,alpha = 0.75,cmap = 'hot')

#use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,colors = 'black', linewidth = 0.5)
#adding label
plt.clabel(C, inline = True,fontsize = 10)

plt.xticks(())
plt.yticks(())
plt.show()