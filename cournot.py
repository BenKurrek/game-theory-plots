import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_payoff(q1, q2, c, a):
    p = 0
    if (q1 + q2) <= a:
        p = q1 * (a - c - q1 - q2)
    return p

def plot_best_response(q1, q2, c, a):
    best_response = 1/2 * (a - c - q2)

    tolerance = 1e-1
    if abs(q1 - best_response) < tolerance:
        return plot_payoff(q1, q2, c, a)
    else:
        return np.nan

a = 100  # Market Saturation Param
c = 10  # Cost of Production

# Generate points for the payoff surface
q1_values = np.linspace(0, a-c, 100)
q2_values = np.linspace(0, a-c, 100)
Q1, Q2 = np.meshgrid(q1_values, q2_values)

# Player 1
payoff_values_1 = np.vectorize(plot_payoff)(Q1, Q2, c, a)
best_response_values_1 = np.vectorize(plot_best_response)(Q1, Q2, c, a)
# Player 2
payoff_values_2 = np.vectorize(plot_payoff)(Q2, Q1, c, a)
best_response_values_2 = np.vectorize(plot_best_response)(Q2, Q1, c, a)

# Create a 3D plot
fig = plt.figure(figsize=(12, 10))

# Plot payoff values and best response values for Player 1
ax3d_1 = fig.add_subplot(221, projection='3d')
surf1 = ax3d_1.plot_surface(Q1, Q2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.5, label='Payoff Player 1')
sc1 = ax3d_1.scatter(Q1, Q2, best_response_values_1, color='red', s=50, label='Best Response Player 1', depthshade=False)
ax3d_1.set_xlabel('Q1')
ax3d_1.set_ylabel('Q2')
ax3d_1.set_zlabel('Payoff')
ax3d_1.set_title('Payoff and Best Response Player 1')

# Plot payoff values and best response values for Player 2
ax3d_2 = fig.add_subplot(222, projection='3d')
surf2 = ax3d_2.plot_surface(Q1, Q2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.5, label='Payoff Player 2')
sc2 = ax3d_2.scatter(Q1, Q2, best_response_values_2, color='blue', s=50, label='Best Response Player 2', depthshade=False)
ax3d_2.set_xlabel('Q1')
ax3d_2.set_ylabel('Q2')
ax3d_2.set_zlabel('Payoff')
ax3d_2.set_title('Payoff and Best Response Player 2')

# Plot best response values for Player 1 and Player 2
ax_scatter = fig.add_subplot(212)
sc3 = ax_scatter.scatter(Q1.flatten(), Q2.flatten(), c=best_response_values_1.flatten(), s=50, cmap='Reds', label='Best Response Player 1')
sc4 = ax_scatter.scatter(Q1.flatten(), Q2.flatten(), c=best_response_values_2.flatten(), s=50, cmap='Blues', label='Best Response Player 2')
ax_scatter.set_xlabel('Q1')
ax_scatter.set_ylabel('Q2')
ax_scatter.set_title('Best Response Values Scatter Plot')
# Add a colorbar for the scatter plot
cbar = fig.colorbar(sc3, ax=ax_scatter, label='Payoff')
cbar = fig.colorbar(sc4, ax=ax_scatter, label='Payoff')


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()