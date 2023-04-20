import plotly
import plotly.graph_objs as go
import requests

# Send a GET request to the endpoint
response = requests.get('http://localhost:5000/predict?product=MR314503 ')
data = response.json()

# Extract the data
topn = data['topn']
x_coords = data['x_coords']
y_coords = data['y_coords']
z_coords = data['z_coords']

# Create a trace for the data points
trace = go.Scatter3d(
    x=x_coords,
    y=y_coords,
    z=z_coords,
    mode='markers',
    marker=dict(
        size=5,
        color='rgb(255, 0, 0)',
        opacity=0.8
    )
)

# Create a trace for the text labels
text_labels = [f'{desc} ({id})' for id, desc, sim in topn]
text_trace = go.Scatter3d(
    x=x_coords,
    y=y_coords,
    z=z_coords,
    mode='text',
    text=text_labels,
    textposition='top center'
)

# Create the layout for the plot
layout = go.Layout(
    title='Product Similarity',
    scene=dict(
        xaxis_title='PCA Component 1',
        yaxis_title='PCA Component 2',
        zaxis_title='PCA Component 3'
    )
)

# Create the figure and plot it
fig = go.Figure(data=[trace, text_trace], layout=layout)
fig.show()