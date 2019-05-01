import matplotlib.pyplot as plt

# Draw the graph - takes the x and y sets of data as parameters
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance (metres)')
    plt.ylabel('Gravitational force (newtons)')
    plt.title('Gravitational force and distance')
    plt.show()

def generate_F_r():
    r = range(100, 1001, 50) # Set from 100 to 1000 in steps of 50
    F = [] # Empty set ready to fill with values
    G = 6.674 * (10**-11) # Gravitational constant
    m1 = 0.5 # First mass in kg
    m2 = 1.5 # Second mass in kg
    
    # Calculate force and add it to the list, F
    for dist in r:
        force = G * (m1 * m2) / (dist ** 2)
        F.append(force)
    draw_graph(r, F)
    
generate_F_r()
