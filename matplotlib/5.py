# annotation
import matplotlib.pyplot as  plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure(1,figsize = (8,5))
plt.plot(x,y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('white')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))   
ax.spines['left'].set_position(('data',0))   

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,s = 50, color = 'red')
plt.plot([x0,x0],[y0,0],'k--',linewidth = 2.5)

'''
Annotation : method 1
'''
plt.annotate(text = r'$2x+1=%s$'%y0, xy = (x0,y0), xycoords = 'data', xytext = (+30, -30), 
textcoords = 'offset points', fontsize = 16, arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0.2'))

# method 2
plt.text(-3.7,3,r'$These\ are\ some\ texts.\ \mu\ \sigma_i\ \alpha_t$', fontdict = {'size':16, 'color':'r'})

plt.show()