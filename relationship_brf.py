import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_payoff(a1, a2, c):
    return a1 * (c + a2 - a1)

def plot_best_response(a1, a2, c):
    best_response = 1/2 * (c + a2)
    tolerance = 1

    if abs(a1 - best_response) < tolerance:
        return plot_payoff(a1, a2, c)
    else:
        return np.nan

c = 100  # Cost of Relationship

# Generate points for the payoff surface
a1_values = np.linspace(0, 4*c, 100)
a2_values = np.linspace(0, 4*c, 100)
A1, A2 = np.meshgrid(a1_values, a2_values)

# Player 1
payoff_values_1 = np.vectorize(plot_payoff)(A1, A2, c)
best_response_values_1 = np.vectorize(plot_best_response)(A1, A2, c)
# Player 2
payoff_values_2 = np.vectorize(plot_payoff)(A2, A1, c)
best_response_values_2 = np.vectorize(plot_best_response)(A2, A1, c)

# Create a 3D plot
fig = plt.figure(figsize=(12, 10))

# Plot payoff values and best response values for Player 1
ax3d_1 = fig.add_subplot(221, projection='3d')
surf1 = ax3d_1.plot_surface(A1, A2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.5, label='Payoff Player 1')
sc1 = ax3d_1.scatter(A1, A2, best_response_values_1, color='red', s=50, label='Best Response Player 1', depthshade=False)
ax3d_1.set_xlabel('A1')
ax3d_1.set_ylabel('A2')
ax3d_1.set_zlabel('Payoff')
ax3d_1.set_title('Payoff and Best Response Player 1')

# Plot payoff values and best response values for Player 2
ax3d_2 = fig.add_subplot(222, projection='3d')
surf2 = ax3d_2.plot_surface(A1, A2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.5, label='Payoff Player 2')
sc2 = ax3d_2.scatter(A1, A2, best_response_values_2, color='blue', s=50, label='Best Response Player 2', depthshade=False)
ax3d_2.set_xlabel('A1')
ax3d_2.set_ylabel('A2')
ax3d_2.set_zlabel('Payoff')
ax3d_2.set_title('Payoff and Best Response Player 2')

# Plot best response values for Player 1 and Player 2
ax_scatter = fig.add_subplot(212)
sc3 = ax_scatter.scatter(A1.flatten(), A2.flatten(), c=best_response_values_1.flatten(), s=50, cmap='Reds', label='Best Response Player 1')
sc4 = ax_scatter.scatter(A1.flatten(), A2.flatten(), c=best_response_values_2.flatten(), s=50, cmap='Blues', label='Best Response Player 2')
ax_scatter.set_xlabel('A1')
ax_scatter.set_ylabel('A2')
ax_scatter.set_title('Best Response Values Scatter Plot')
# Add a colorbar for the scatter plot
cbar = fig.colorbar(sc3, ax=ax_scatter, label='Payoff')
cbar = fig.colorbar(sc4, ax=ax_scatter, label='Payoff')


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()