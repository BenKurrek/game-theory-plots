import numpy as np
import plotly.graph_objects as go

def plot_payoff(a1, a2, c):
    return a1 * (c + a2 - a1)

def plot_best_response(a1, a2, c):
    best_response = 1/2 * (c + a2)
    tolerance = 1

    if abs(a1 - best_response) < tolerance:
        return plot_payoff(a1, a2, c)
    else:
        return np.nan

def brf_game(c):
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

    # Create a 3D plot using Plotly
    fig = go.Figure()

    # Plot payoff values and best response values for Player 1
    fig.add_trace(go.Surface(x=A1, y=A2, z=payoff_values_1, colorscale='viridis', opacity=0.5, name='Payoff Player 1'))
    fig.add_trace(go.Scatter3d(x=A1.flatten(), y=A2.flatten(), z=best_response_values_1.flatten(),
                               mode='markers', marker=dict(size=5, color='red'), name='Best Response Player 1'))

    # Plot payoff values and best response values for Player 2
    fig.add_trace(go.Surface(x=A1, y=A2, z=payoff_values_2, colorscale='plasma', opacity=0.5, name='Payoff Player 2'))
    fig.add_trace(go.Scatter3d(x=A1.flatten(), y=A2.flatten(), z=best_response_values_2.flatten(),
                               mode='markers', marker=dict(size=5, color='blue'), name='Best Response Player 2'))

    # Set layout
    fig.update_layout(scene=dict(xaxis_title='A1', yaxis_title='A2', zaxis_title='Payoff'),
                      title='Payoff and Best Response BRF Model')

    return fig
