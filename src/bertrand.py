import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def plot_payoff(p1, p2, c, a):
    if p1 > p2:
        return 0
    
    if p1 == p2:
        return 1/2 * (p1 - c)*(a - p1)
    
    return (p1 - c)*(a - p1)

def plot_best_response(p1, p2, c, a):
    tolerance = (5.48) * 1e-1
    p_m = 1/2 * (a + c)

    if p2 < c and p1 > p2:
        return plot_payoff(p1, p2, c, a)
    elif abs(p2 - c) < tolerance and  p1 >= p2:
        return plot_payoff(p1, p2, c, a)
    elif p_m < p2:
        if abs(p1 - p_m) < tolerance:
            return plot_payoff(p_m, p2, c, a)

def update(frame, initial_a, initial_c, dot_size, p_1_points, p_2_points, P1, P2, ax3d_1, ax3d_2, ax_scatter, surf1, surf2, sc1, sc2, sc3, sc4):
    a = initial_a  # Constant a term
    c = initial_c + frame * 1  # Varying 'c' term
    if c >= a:
        c = a

    # Loop through all points in the payoff surface
    best_response_values_1 = [[],[],[]]
    best_response_values_2 = [[],[],[]]
    for p_1 in p_1_points:
        for p_2 in p_2_points:
            res_1 = plot_best_response(p_1, p_2, c, a)
            if res_1 is not None:
                best_response_values_1[0].append(p_1)
                best_response_values_1[1].append(p_2)
                best_response_values_1[2].append(res_1)
            
            res_2 = plot_best_response(p_2, p_1, c, a)
            if res_2 is not None:
                best_response_values_2[0].append(p_1)
                best_response_values_2[1].append(p_2)
                best_response_values_2[2].append(res_2)

    # Update Player 1 plots
    payoff_values_1 = np.vectorize(plot_payoff)(P1, P2, c, a)
    # Update Player 2 plots
    payoff_values_2 = np.vectorize(plot_payoff)(P2, P1, c, a)

    ax3d_1.clear()
    ax3d_1.plot_surface(P1, P2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.7, label='Payoff Player 1')
    ax3d_1.scatter(best_response_values_1[0], best_response_values_1[1], best_response_values_1[2], color='red', s=dot_size, label='Best Response Player 1', depthshade=False)
    ax3d_1.set_xlabel('P1')
    ax3d_1.set_ylabel('P2')
    ax3d_1.set_zlabel('Payoff')
    ax3d_1.set_title(f'Payoff and Best Response Player 1 (a={a}, c={c})')

    ax3d_2.clear()
    ax3d_2.plot_surface(P1, P2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.7, label='Payoff Player 2')
    ax3d_2.scatter(best_response_values_2[0], best_response_values_2[1], best_response_values_2[2], color='blue', s=dot_size, label='Best Response Player 2', depthshade=False)
    ax3d_2.set_xlabel('P1')
    ax3d_2.set_ylabel('P2')
    ax3d_2.set_zlabel('Payoff')
    ax3d_2.set_title(f'Payoff and Best Response Player 2 (a={a}, c={c})')
    
    # Update scatter plot
    ax_scatter.clear()
    ax_scatter.scatter(best_response_values_1[0], best_response_values_1[1], c=best_response_values_1[2], s=dot_size, cmap='Reds', label='Best Response Player 1')
    ax_scatter.scatter(best_response_values_2[0], best_response_values_2[1], c=best_response_values_2[2], s=dot_size, cmap='Blues', label='Best Response Player 2')
    ax_scatter.set_xlabel('P1')
    ax_scatter.set_ylabel('P2')
    ax_scatter.set_xlim(0, P1.max())
    ax_scatter.set_ylim(0, P2.max())
    ax_scatter.set_title(f'Best Response Values Scatter Plot (a={a}, c={c})')

def bertrand_game(a, c, animate):
    animate = animate == 'True' or animate == 'true' or animate == '1' or animate == 't' or animate == 'T'

    if a <= c:
        print('a must be greater than c')
        exit()

    dot_size = 10
    num_points = 100

    p_m = 1/2 * (a + c)
    p_1_points = np.linspace(0, 4*p_m, num_points)
    p_2_points = np.linspace(0, 4*p_m, num_points)

    # Loop through all points in the payoff surface
    best_response_values_1 = [[],[],[]]
    best_response_values_2 = [[],[],[]]
    for p_1 in p_1_points:
        for p_2 in p_2_points:
            res_1 = plot_best_response(p_1, p_2, c, a)
            if res_1 is not None:
                best_response_values_1[0].append(p_1)
                best_response_values_1[1].append(p_2)
                best_response_values_1[2].append(res_1)
            
            res_2 = plot_best_response(p_2, p_1, c, a)
            if res_2 is not None:
                best_response_values_2[0].append(p_1)
                best_response_values_2[1].append(p_2)
                best_response_values_2[2].append(res_2)
    
    # Generate points for the payoff surface
    P1, P2 = np.meshgrid(p_1_points, p_2_points)
    # Player 1
    payoff_values_1 = np.vectorize(plot_payoff)(P1, P2, c, a)                
    # Player 2
    payoff_values_2 = np.vectorize(plot_payoff)(P2, P1, c, a)

    # Create a 3D plot
    fig = plt.figure(figsize=(12, 10))

    # Plot payoff values and best response values for Player 1
    ax3d_1 = fig.add_subplot(221, projection='3d')
    surf1 = ax3d_1.plot_surface(P1, P2, payoff_values_1, cmap='viridis', edgecolor='k', alpha=0.5, label='Payoff Player 1')
    sc1 = ax3d_1.scatter(best_response_values_1[0], best_response_values_1[1], best_response_values_1[2], color='red', s=dot_size, label='Best Response Player 1', depthshade=False)
    ax3d_1.set_xlabel('P1')
    ax3d_1.set_ylabel('P2')
    ax3d_1.set_zlabel('Payoff')
    ax3d_1.set_title('Payoff and Best Response Player 1')

    # Plot payoff values and best response values for Player 2
    ax3d_2 = fig.add_subplot(222, projection='3d')
    surf2 = ax3d_2.plot_surface(P1, P2, payoff_values_2, cmap='plasma', edgecolor='k', alpha=0.5, label='Payoff Player 2')
    sc2 = ax3d_2.scatter(best_response_values_2[0], best_response_values_2[1], best_response_values_2[2], color='blue', s=dot_size, label='Best Response Player 2', depthshade=False)
    ax3d_2.set_xlabel('P1')
    ax3d_2.set_ylabel('P2')
    ax3d_2.set_zlabel('Payoff')
    ax3d_2.set_title('Payoff and Best Response Player 2')

    # Plot best response values for Player 1 and Player 2
    ax_scatter = fig.add_subplot(212)
    sc3 = ax_scatter.scatter(best_response_values_1[0], best_response_values_1[1], c=best_response_values_1[2], s=dot_size, cmap='Reds', label='Best Response Player 1')
    sc4 = ax_scatter.scatter(best_response_values_2[0], best_response_values_2[1], c=best_response_values_2[2], s=dot_size, cmap='Blues', label='Best Response Player 2')
    ax_scatter.set_xlabel('P1')
    ax_scatter.set_ylabel('P2')
    ax_scatter.set_title('Best Response Values Scatter Plot')
    # Add a colorbar for the scatter plot
    cbar = fig.colorbar(sc3, ax=ax_scatter, label='Payoff')
    cbar = fig.colorbar(sc4, ax=ax_scatter, label='Payoff')
    
    # Adjust layout
    plt.tight_layout()

    # Animate the plots
    num_frames = a - c
    print(f"Number of frames: {num_frames}")
    if animate:
        animation = FuncAnimation(fig, update, frames=int(num_frames), interval=50, repeat=True, fargs=(a, c, dot_size, p_1_points, p_2_points, P1, P2, ax3d_1, ax3d_2, ax_scatter, surf1, surf2, sc1, sc2, sc3, sc4))

    # Show the plot
    plt.show()