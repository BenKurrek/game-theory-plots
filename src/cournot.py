import numpy as np
import plotly.graph_objects as go

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

def cournot_game(a, c):
    # Generate points for the payoff surface
    num_points = 300
    Q1, Q2 = np.meshgrid(np.linspace(0, a-c, num_points), np.linspace(0, a-c, num_points))

    # Player 1
    payoff_values_1 = np.vectorize(plot_payoff)(Q1, Q2, c, a)
    best_response_values_1 = np.vectorize(plot_best_response)(Q1, Q2, c, a)
    # Player 2
    payoff_values_2 = np.vectorize(plot_payoff)(Q2, Q1, c, a)
    best_response_values_2 = np.vectorize(plot_best_response)(Q2, Q1, c, a)

    # Create a 3D plot using Plotly
    fig = go.Figure()

    # Plot payoff values and best response values for Player 1
    fig.add_trace(go.Surface(x=Q1, y=Q2, z=payoff_values_1, colorscale='viridis', opacity=0.5, name='Payoff Player 1'))
    fig.add_trace(go.Scatter3d(x=Q1.flatten(), y=Q2.flatten(), z=best_response_values_1.flatten(),
                               mode='markers', marker=dict(size=5, color='red'), name='Best Response Player 1'))

    # Plot payoff values and best response values for Player 2
    fig.add_trace(go.Surface(x=Q1, y=Q2, z=payoff_values_2, colorscale='plasma', opacity=0.5, name='Payoff Player 2'))
    fig.add_trace(go.Scatter3d(x=Q1.flatten(), y=Q2.flatten(), z=best_response_values_2.flatten(),
                               mode='markers', marker=dict(size=5, color='blue'), name='Best Response Player 2'))

    # Set layout
    fig.update_layout(scene=dict(xaxis_title='Q1', yaxis_title='Q2', zaxis_title='Payoff'),
                      title='Payoff and Best Response Cournot Model')

    return fig
