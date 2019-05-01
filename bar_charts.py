import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    num_bars = len(data) # Number of bars to draw
    positions = range(1, num_bars+1) # Positions of bars on y-axis
    plt.bar(positions, data, align='center') # Generate the bar chart
    plt.xticks(positions, labels) # Add little markers to each label on x-axis
    plt.xlabel('Day') # At x-axis label
    plt.ylabel('Steps') # Add y-axis label
    plt.title('Number of steps walked') # Add title
    plt.grid() # Add a grid for easier visual estimation of values
    plt.show()
    
stepsWalked = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

create_bar_chart(stepsWalked, labels)
