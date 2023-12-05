import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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

def update(frame, initial_a, initial_c, Q1, Q2, ax3d_1, ax3d_2, ax_scatter, surf1, surf2, sc1, sc2, sc3, sc4):
    a = initial_a # Constant a term
    c = initial_c + frame * 1 # Varying 'c' term
    if c >= a:
        c = a
    
    # Update Player 1 plots
    payoff_values_1 = np.vectorize(plot_payoff)(Q1, Q2, c, a)
    best_response_values_1 = np.vectorize(plot_best_response)(Q1, Q2, c, a)
    
    surf1.set_array(payoff_values_1.flatten())
    sc1.set_array(best_response_values_1.flatten())
    
    contour_levels_1 = np.linspace(np.nanmin(payoff_values_1), np.nanmax(payoff_values_1), 25)
    ax3d_1.clear()
    ax3d_1.plot_surface(Q1, Q2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.7, label='Payoff Player 1')
    ax3d_1.scatter(Q1, Q2, best_response_values_1, color='red', s=50, label='Best Response Player 1', depthshade=False)
    ax3d_1.contour(Q1, Q2, payoff_values_1, zdir='z', offset=ax3d_1.get_zlim()[0], levels=contour_levels_1, cmap='viridis', alpha=0.5)
    ax3d_1.set_xlabel('Q1')
    ax3d_1.set_ylabel('Q2')
    ax3d_1.set_zlabel('Payoff')
    ax3d_1.set_title(f'Payoff and Best Response Player 1 (a={a}, c={c})')

    # Update Player 2 plots
    payoff_values_2 = np.vectorize(plot_payoff)(Q2, Q1, c, a)
    best_response_values_2 = np.vectorize(plot_best_response)(Q2, Q1, c, a)
    
    surf2.set_array(payoff_values_2.flatten())
    sc2.set_array(best_response_values_2.flatten())
    
    contour_levels_2 = np.linspace(np.nanmin(payoff_values_2), np.nanmax(payoff_values_2), 10)
    ax3d_2.clear()
    ax3d_2.plot_surface(Q1, Q2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.7, label='Payoff Player 2')
    ax3d_2.scatter(Q1, Q2, best_response_values_2, color='blue', s=50, label='Best Response Player 2', depthshade=False)
    ax3d_2.contour(Q1, Q2, payoff_values_2, zdir='z', offset=ax3d_2.get_zlim()[0], levels=contour_levels_2, cmap='plasma', alpha=0.5)
    ax3d_2.set_xlabel('Q1')
    ax3d_2.set_ylabel('Q2')
    ax3d_2.set_zlabel('Payoff')
    ax3d_2.set_title(f'Payoff and Best Response Player 2 (a={a}, c={c})')

    # Update Scatter plot
    best_response_values_1 = np.vectorize(plot_best_response)(Q1, Q2, c, a)
    best_response_values_2 = np.vectorize(plot_best_response)(Q2, Q1, c, a)
    
    sc3.set_array(best_response_values_1.flatten())
    sc4.set_array(best_response_values_2.flatten())
    
    contour_levels_scatter = np.linspace(np.nanmin(payoff_values_1), np.nanmax(payoff_values_1), 10)
    ax_scatter.clear()
    ax_scatter.scatter(Q1.flatten(), Q2.flatten(), c=best_response_values_1.flatten(), s=50, cmap='Reds', label='Best Response Player 1', alpha=0.7)
    ax_scatter.scatter(Q1.flatten(), Q2.flatten(), c=best_response_values_2.flatten(), s=50, cmap='Blues', label='Best Response Player 2', alpha=0.7)
    ax_scatter.set_xlabel('Q1')
    ax_scatter.set_ylabel('Q2')
    
    # Set fixed axis limits
    ax_scatter.set_xlim(0, Q1.max())
    ax_scatter.set_ylim(0, Q2.max())

    contour_levels_scatter = np.linspace(np.nanmin(payoff_values_1), np.nanmax(payoff_values_1), 10)
    ax_scatter.contour(Q1, Q2, payoff_values_1, levels=contour_levels_scatter, colors='black', alpha=0.5)
    ax_scatter.set_title(f'Best Response Values Scatter Plot (a={a}, c={c})')

def cournot_game(a, c):
    animate = True

    # Generate points for the payoff surface
    num_points = 300
    Q1, Q2 = np.meshgrid(np.linspace(0, a-c, num_points), np.linspace(0, a-c, num_points))

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
    surf1 = ax3d_1.plot_surface(Q1, Q2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.7, label='Payoff Player 1')
    sc1 = ax3d_1.scatter(Q1, Q2, best_response_values_1, color='red', s=50, label='Best Response Player 1', depthshade=False)
    ax3d_1.set_xlabel('Q1')
    ax3d_1.set_ylabel('Q2')
    ax3d_1.set_zlabel('Payoff')
    ax3d_1.set_title('Payoff and Best Response Player 1')

    # Add isoprofit curves for Player 1
    contour_levels_1 = np.linspace(np.nanmin(payoff_values_1), np.nanmax(payoff_values_1), 25)
    ax3d_1.contour(Q1, Q2, payoff_values_1, zdir='z', offset=ax3d_1.get_zlim()[0], levels=contour_levels_1, cmap='viridis', alpha=0.5)

    # Plot payoff values and best response values for Player 2
    ax3d_2 = fig.add_subplot(222, projection='3d')
    surf2 = ax3d_2.plot_surface(Q1, Q2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.7, label='Payoff Player 2')
    sc2 = ax3d_2.scatter(Q1, Q2, best_response_values_2, color='blue', s=50, label='Best Response Player 2', depthshade=False)
    ax3d_2.set_xlabel('Q1')
    ax3d_2.set_ylabel('Q2')
    ax3d_2.set_zlabel('Payoff')
    ax3d_2.set_title('Payoff and Best Response Player 2')

    # Add isoprofit curves for Player 2
    contour_levels_2 = np.linspace(np.nanmin(payoff_values_2), np.nanmax(payoff_values_2), 10)
    ax3d_2.contour(Q1, Q2, payoff_values_2, zdir='z', offset=ax3d_2.get_zlim()[0], levels=contour_levels_2, cmap='plasma', alpha=0.5)

    # Plot best response values for Player 1 and Player 2
    ax_scatter = fig.add_subplot(212)
    sc3 = ax_scatter.scatter(Q1.flatten(), Q2.flatten(), c=best_response_values_1.flatten(), s=50, cmap='Reds', label='Best Response Player 1', alpha=0.7)
    sc4 = ax_scatter.scatter(Q1.flatten(), Q2.flatten(), c=best_response_values_2.flatten(), s=50, cmap='Blues', label='Best Response Player 2', alpha=0.7)
    ax_scatter.set_xlabel('Q1')
    ax_scatter.set_ylabel('Q2')
    ax_scatter.set_title('Best Response Values Scatter Plot')
    # Add a colorbar for the scatter plot
    cbar = fig.colorbar(sc3, ax=ax_scatter, label='Payoff')
    cbar = fig.colorbar(sc4, ax=ax_scatter, label='Payoff')

    # Add isoprofit curves for the scatter plot
    contour_levels_scatter = np.linspace(np.nanmin(payoff_values_1), np.nanmax(payoff_values_1), 10)
    ax_scatter.contour(Q1, Q2, payoff_values_1, levels=contour_levels_scatter, colors='black', alpha=0.5)

    # Adjust layout
    plt.tight_layout()

    # Animate the plots
    num_frames = a - c
    print(f"Number of frames: {num_frames}")
    if animate:
        animation = FuncAnimation(fig, update, frames=int(num_frames), interval=50, repeat=True, fargs=(a, c, Q1, Q2, ax3d_1, ax3d_2, ax_scatter, surf1, surf2, sc1, sc2, sc3, sc4))

    # Show the plot
    plt.show()
