import math
import matplotlib.pyplot as plt

DEG_2_RAD = 3.14159 / 180.0

def draw_graph(sinVals, cosVals, angles):
    plt.plot(angles, sinVals, marker = 'o', label='sine')
    plt.plot(angles, cosVals, marker = 'x', label='Cosine')
    plt.legend()
    plt.show()

def generate_data():
    angles = range(0, 360, 10)
    angles = [x * DEG_2_RAD for x in angles]
    sinVals = []
    cosVals = []

    for a in angles:
        sinVals.append(math.sin(a))
        cosVals.append(math.cos(a))

    draw_graph(sinVals, cosVals, angles)

generate_data()
    
