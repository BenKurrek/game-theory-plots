import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def compute_points(delta, left_coord, right_coord, num_points, num_generations):
    x_values = []
    y_values = []

    x1, y1 = left_coord
    x2, y2 = right_coord

    # Split the interval [0, 1] into num_points intervals
    partition = np.linspace(x1, x2, num_points + 1)
    for i in range(num_points + 1):
        num_c = num_points - i
        num_d = i

        payoff = 0
        iterations = 0
        n_loops = 1
        converged = False
        
        for j in range(num_generations):
            idx = n_loops % num_points

            # One cycle is done
            if idx == 0:
                iterations += 1

            top_val = y1 if y1 > y2 else y2
            bot_val = y1 if y1 < y2 else y2
            # We hit a C (cooperate) therefore payoff is closer to 2
            if idx < num_c:
                net = top_val * (delta ** n_loops)
                payoff += net
            # We hit a D (defect) therefore payoff is closer to 3
            else:
                net = bot_val * (delta ** n_loops)
                payoff += net

            n_loops += 1

        avg_payoff = payoff / n_loops

        # Append the coordinates for plotting
        x_values.append(partition[i])
        y_values.append(avg_payoff)

    return x_values, y_values

# Animation update function
def update(frame, ax):
    delta = 1 - frame * 0.0001
    num_points = 30
    num_generations = 10000

    x1, y1 = compute_points(delta, (0, 3), (2, 2), num_points, num_generations)
    x2, y2 = compute_points(delta, (0, 3), (1, 1), num_points, num_generations)
    x3, y3 = compute_points(delta, (2, 2), (3, 0), num_points, num_generations)
    x4, y4 = compute_points(delta, (1, 1), (3, 0), num_points, num_generations)


    # Update the scatter plot
    ax.clear()
    ax.scatter(x1, y1, s=100)
    ax.scatter(x2, y2, s=100)
    ax.scatter(x3, y3, s=100)
    ax.scatter(x4, y4, s=100)

    # Set fixed axis limits
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_title(f'Best Response Values Scatter Plot (Delta={delta})')

# Create a figure and axis
fig = plt.figure(figsize=(12, 10))
ax_scatter = fig.add_subplot(111)
ax_scatter.scatter([1], [2], s=100, label='Best Response Player 1')
ax_scatter.set_xlabel('Number of Cooperate (C)')
ax_scatter.set_ylabel('Average Payoff')
ax_scatter.set_title('Payoff vs. Number of Cooperate (C)')

# Number of frames for the animation
num_frames = 100

# Create the animation
animation = FuncAnimation(fig, update, frames=range(num_frames), repeat=False, fargs=(ax_scatter,), interval=100)

# Show the animation
plt.show()
