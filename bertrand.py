import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_payoff(p1, p2, c, a):
    if p1 > p2:
        return 0
    
    if p1 == p2:
        return 1/2 * (p1 - c)*(a - p1)
    
    return (p1 - c)*(a - p1)

def plot_best_response(p1, p2, c, a):
    tolerance = 1e-2
    p_m = 1/2 * (a + c)

    if p2 < c:
        return plot_payoff(p1, p2, c, a) if p1 > p2 else np.nan
    if abs(p2 - c) < tolerance:
        return plot_payoff(p1, p2, c, a) if p1 >= p2 else np.nan
    if c < p2 and p2 <= p_m:
        return np.nan
    if p_m < p2:
        plot_payoff(p_m, p2, c, a)
    
    return np.nan
    
        
a = 5 # Demand
c = 4  # Cost of Production

if a <= c:
    print('a must be greater than c')
    exit()

p_m = 1/2 * (a + c)
# Generate points for the payoff surface
p1_values = np.linspace(0, 4*p_m, 100)
p2_values = np.linspace(0, 4*p_m, 100)
P1, P2 = np.meshgrid(p1_values, p2_values)

# Player 1
payoff_values_1 = np.vectorize(plot_payoff)(P1, P2, c, a)
best_response_values_1 = np.vectorize(plot_best_response)(P1, P2, c, a)
# Player 2
payoff_values_2 = np.vectorize(plot_payoff)(P2, P1, c, a)
best_response_values_2 = np.vectorize(plot_best_response)(P2, P1, c, a)

# Create a 3D plot
fig = plt.figure(figsize=(12, 10))

# Plot payoff values and best response values for Player 1
ax3d_1 = fig.add_subplot(221, projection='3d')
surf1 = ax3d_1.plot_surface(P1, P2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.5, label='Payoff Player 1')
sc1 = ax3d_1.scatter(P1, P2, best_response_values_1, color='red', s=50, label='Best Response Player 1', depthshade=False)
ax3d_1.set_xlabel('P1')
ax3d_1.set_ylabel('P2')
ax3d_1.set_zlabel('Payoff')
ax3d_1.set_title('Payoff and Best Response Player 1')

# Plot payoff values and best response values for Player 2
ax3d_2 = fig.add_subplot(222, projection='3d')
surf2 = ax3d_2.plot_surface(P1, P2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.5, label='Payoff Player 2')
sc2 = ax3d_2.scatter(P1, P2, best_response_values_2, color='blue', s=50, label='Best Response Player 2', depthshade=False)
ax3d_2.set_xlabel('P1')
ax3d_2.set_ylabel('P2')
ax3d_2.set_zlabel('Payoff')
ax3d_2.set_title('Payoff and Best Response Player 2')

# Plot best response values for Player 1 and Player 2
ax_scatter = fig.add_subplot(212)
sc3 = ax_scatter.scatter(P1.flatten(), P2.flatten(), c=best_response_values_1.flatten(), s=50, cmap='Reds', label='Best Response Player 1')
sc4 = ax_scatter.scatter(P1.flatten(), P2.flatten(), c=best_response_values_2.flatten(), s=50, cmap='Blues', label='Best Response Player 2')
ax_scatter.set_xlabel('P1')
ax_scatter.set_ylabel('P2')
ax_scatter.set_title('Best Response Values Scatter Plot')
# Add a colorbar for the scatter plot
cbar = fig.colorbar(sc3, ax=ax_scatter, label='Payoff')
cbar = fig.colorbar(sc4, ax=ax_scatter, label='Payoff')


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()