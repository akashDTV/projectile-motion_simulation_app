import numpy as np
import streamlit as st
import math
import plotly.graph_objects as go

# Function to calculate projectile trajectory
def projectile_trajectory(v0, theta, g=9.81, dt=0.001):
    theta = math.radians(theta)
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)
    t_max = 2 * vy / g
    t = np.arange(0, t_max, dt)
    x = vx * t
    y = vy * t - 0.5 * g * t**2
    max_height = max(y)
    max_distance = max(x)
    return x, y, max_height, max_distance

# Streamlit app code
st.title("Projectile Trajectory Simulation")

# Input for initial velocity and launch angle
v0 = st.slider("Initial Velocity (m/s)", 1, 50, 20)
theta = st.slider("Launch Angle (degrees)", 1, 90, 45)

# Calculate the trajectory
x, y, max_height, max_distance = projectile_trajectory(v0, theta)

# Create Plotly figure
fig = go.Figure()

# Add the trajectory path to the plot
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Projectile Path'))

# Annotate max height and max distance
fig.add_annotation(
    x=0,
    y=max_height,
    text=f'Max Height: {max_height:.2f} m',
    showarrow=True,
    arrowhead=2
)
fig.add_annotation(
    x=max_distance,
    y=0,
    text=f'Max Distance: {max_distance:.2f} m',
    showarrow=True,
    arrowhead=2
)

# Update the layout of the plot
fig.update_layout(
    title=f"Projectile Trajectory (v0={v0} m/s, θ={theta}°)",
    xaxis_title='Distance (m)',
    yaxis_title='Height (m)',
    template='plotly_dark'  # Optional: a dark theme
)

# Display the plot in the Streamlit app
st.plotly_chart(fig)

# Display the max height and max distance below the plot
st.write(f"Maximum Height: {max_height:.2f} meters")
st.write(f"Maximum Distance: {max_distance:.2f} meters")
