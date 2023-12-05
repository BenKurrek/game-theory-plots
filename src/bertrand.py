import numpy as np
import plotly.graph_objects as go

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
        return plot_payoff(p_m, p2, c, a)
    
    return np.nan
    
def bertrand_game(a, c):   
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

    # Create a 3D plot using Plotly
    fig = go.Figure()

    # Plot payoff values and best response values for Player 1
    fig.add_trace(go.Surface(x=P1, y=P2, z=payoff_values_1, colorscale='viridis', opacity=0.5, name='Payoff Player 1'))
    fig.add_trace(go.Scatter3d(x=P1.flatten(), y=P2.flatten(), z=best_response_values_1.flatten(), 
                               mode='markers', marker=dict(size=5, color='red'), name='Best Response Player 1'))

    # Plot payoff values and best response values for Player 2
    fig.add_trace(go.Surface(x=P1, y=P2, z=payoff_values_2, colorscale='plasma', opacity=0.5, name='Payoff Player 2'))
    fig.add_trace(go.Scatter3d(x=P1.flatten(), y=P2.flatten(), z=best_response_values_2.flatten(), 
                               mode='markers', marker=dict(size=5, color='blue'), name='Best Response Player 2'))

    # Set layout
    fig.update_layout(scene=dict(xaxis_title='P1', yaxis_title='P2', zaxis_title='Payoff'),
                      title='Payoff and Best Response Bertrand Model')

    print(f"Figure inside bertrand: {fig}")
    return fig