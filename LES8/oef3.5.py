import numpy as np
import matplotlib.pyplot as plt

def opgave1():
    x = np.linspace(0, 100, 1000)
    y = np.log10(x)
    plt.plot(x,y, 'b:')
    plt.title("logs van basis 10")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()
def opgave3():
    klassen = ["Asphalt", "Concrete", "Grass", "Tree", "Building"]
    truth = [2397, 337, 908, 1099, 2067]
    predicted = [2394, 333, 917, 1093, 2071]
    plt.subplot(2, 1, 1)
    plt.bar(klassen, predicted)
    plt.title("predicted")
    plt.subplot(2, 1, 2)
    plt.bar(klassen, truth)
    plt.title("truth")
    plt.show()

if __name__ == '__main__':
    #opgave1()
    opgave3()