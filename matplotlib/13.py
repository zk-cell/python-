#subplot 分格显示
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method1 : subplot2grid   这里为ax设置label xlim等等，需要采用 set_label这种形式
# plt.figure()
# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)
# ax1.plot([1,2],[1,2])
# ax1.set_title('ax1_title')

# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)

# ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)

# ax4 = plt.subplot2grid((3,3),(2,0))

# ax5 = plt.subplot2grid((3,3),(2,1))


# method2 : gridspec
# plt.figure()
# gs = gridspec.GridSpec(3,3)
# ax1 = plt.subplot(gs[0,:])
# ax2 = plt.subplot(gs[1,:2])
# ax3 = plt.subplot(gs[1:,2])
# ax4 = plt.subplot(gs[2,0])
# ax5 = plt.subplot(gs[2,1])


# method3: easy to define structure   适合x、y轴对齐的情况
figure1, ((ax11,ax12),(ax21,ax22)) =plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])

#简易调整标题、标签位置
plt.tight_layout()
plt.show()