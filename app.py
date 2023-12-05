from flask import Flask, render_template, jsonify
import numpy as np
from src.bertrand import bertrand_game
from src.cournot import cournot_game
from src.relationship_brf import brf_game
import plotly.express as px
from plotly.io import to_json
from plotly.io import to_html
from plotly.subplots import make_subplots
import json

app = Flask(__name__)

class PlotlyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.generic):
            return np.asscalar(obj)
        return super(PlotlyJSONEncoder, self).default(obj)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bertrand/<float:a>/<float:c>')
def bertrand(a, c):
    try:
        # Code to generate Plotly figure
        fig = plot_bertrand(a, c)
        
        # Convert the Plotly figure to HTML
        fig_html = plot_to_html(fig)

        # Return the HTML
        return jsonify(figure=fig_html)

    except Exception as e:
        # Log the error and return an error response
        print(f"Error: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/cournot/<float:a>/<float:c>')
def cournot(a, c):
    fig1, fig2, fig3 = plot_cournot(a, c)
    response = jsonify(figure=plot_to_html(fig1, fig2, fig3))
    print(response.get_data(as_text=True))  # Add this line for logging
    return response

@app.route('/relationship_brf/<float:c>')
def relationship_brf(c):
    fig1, fig2, fig3 = plot_relationship_brf(c)
    response = jsonify(figure=plot_to_html(fig1, fig2, fig3))
    print(response.get_data(as_text=True))  # Add this line for logging
    return response

def plot_to_html(fig):
    print(f"Plot to HTML Fig: {fig}")
    # Directly convert the Plotly figure to HTML
    fig_html = to_html(fig)
    return render_template('plotly_template.html', img_str=fig_html)


def plot_bertrand(a, c):
    # Your existing bertrand_game code here
    fig = bertrand_game(a, c)
    print(f"Plot Bertrand BEFORE: {fig}")

    filtered_fig = filter_nan_values(fig)
    print(f"Plot Bertrand AFTER: {filtered_fig}")
    return filtered_fig

def plot_cournot(a, c):
    # Your existing cournot_game code here
    fig = cournot_game(a, c)
    return fig

def plot_relationship_brf(c):
    # Your existing brf_game code here
    fig = brf_game(c)
    return fig

def filter_nan_values(fig):
    # Iterate through data and remove NaN values
    for trace in fig['data']:
        trace['x'] = trace['x'][~np.isnan(trace['z'])]
        trace['y'] = trace['y'][~np.isnan(trace['z'])]
        trace['z'] = trace['z'][~np.isnan(trace['z'])]

    return fig

if __name__ == '__main__':
    app.run(debug=True)
