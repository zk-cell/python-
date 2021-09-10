# subplot 多合一显示
import matplotlib.pyplot as plt
def a1():
    plt.figure(1)
    plt.subplot(2,2,1)
    plt.plot([0,1],[0,1])

    plt.subplot(2,2,2)
    plt.plot([0,1],[0,1])

    plt.subplot(2,2,3)
    plt.plot([0,1],[0,1])

    plt.subplot(2,2,4)
    plt.plot([0,1],[0,1])

    plt.show()

def a2():
    plt.figure(2)
    plt.subplot(2,3,1)
    plt.plot([0,1],[0,1])

    plt.subplot(2,3,4)
    plt.plot([0,1],[0,2])

    plt.subplot(2,3,5)
    plt.plot([0,1],[0,3])

    plt.subplot(2,3,6)
    plt.plot([0,1],[0,4])

    plt.show()

a1()
a2()