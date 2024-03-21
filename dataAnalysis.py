"""
Title: 3D and Time Geovisualization Assignment

Summary 

This script pertains to the "3D and Time Geovisualization" assignment 
from the "Extraction & Dissemination of Geo Information (2023-2A)" course 
in the MSc Geoinformatics program at ITC, University of Twente.

The script reads a dataset containing the location and timestamp of birds
and creates space-time cubes for each class of birds (anosmic, magnetic, control)
to visualize their movement in 3D space and time.

The script performs the following steps:
1. Load the dataset containing bird data.
2. Convert the 'timestamp' column to datetime objects.
3. Convert the 'timestamp' column to Unix time.
4. Create space-time cubes for each class of birds (anosmic, magnetic, control).
5. Plot the space-time cubes for each class of birds in 3D space and all classes.
6. Save the plots as HTML files for visualization.

The script uses the following libraries:
- pandas: to work with dataframes.
- plotly.graph_objects: to create 3D plots.
- plotly.express: to create interactive plots.

The script is divided into the following sections:
1. Load the dataset.
2. Create space-time cubes for each class of each birds and all classes at the end.
3. Save the plots as HTML files.

Author: Abdillahi Osman Omar - March 2024
ITC, University of Twente

"""

# Step 1: Import necessary libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Stp 2: Load the dataset
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\data.csv"
data = pd.read_csv(file_path)
data.head()

# Step 3: Convert 'timestamp' to datetime objects
data['timestamp'] = pd.to_datetime(data['timestamp'], format='%d/%m/%Y %H:%M')

# Convert 'timestamp' to Unix time (seconds since 1970-01-01)
data['timestamp_unix'] = (data['timestamp'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

# Display the modified dataframe to verify changes
data[['timestamp', 'timestamp_unix', 'utm-easting', 'utm-northing']].head()


# Step 4: We will now create space-time cubes for each anosmic bird, plotting each one individually
# Extract unique identifiers from 'individual-local-identifier'
unique_identifiers = data['individual-local-identifier'].unique()

# First, let's extract the unique identifiers for the anosmic birds again to ensure we have the right ones
anosmic_identifiers = [identifier for identifier in unique_identifiers if 'anosmic' in identifier]

# Now we will plot each bird with a different color
colors = px.colors.qualitative.Plotly

# Create the space-time cubes for the 'anosmic' class, each with a different color
anosmic_cubes = []
for i, identifier in enumerate(anosmic_identifiers):
    # Filter data for the current identifier
    bird_data = data[data['individual-local-identifier'] == identifier]
    # Create the scatter plot for the current bird
    cube = go.Scatter3d(
        x=bird_data['utm-easting'],
        y=bird_data['utm-northing'],
        z=bird_data['timestamp_unix'],
        mode='markers',
        marker=dict(size=3, color=colors[i % len(colors)]),
        name=identifier
    )
    anosmic_cubes.append(cube)

# Create a layout for the 3D plot
layout = go.Layout(
    title="Space-Time Cube for Anosmic Birds",
    scene=dict(
        xaxis=dict(title='UTM Easting'),
        yaxis=dict(title='UTM Northing'),
        zaxis=dict(title='Timestamp (Unix)'),
        camera=dict(eye=dict(x=2.5, y=2.5, z=2.5))
    ),
    legend=dict(
        title="Legend",
        itemsizing='constant'
    )
)

# Create a figure with the space-time cubes and layout
fig = go.Figure(data=anosmic_cubes, layout=layout)

# Show the 3D plot
fig.show()

# Save the plot as an HTML file
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\space_time_cube_anosmic.html"
fig.write_html(file_path)

# Now we will create space-time cubes for 'magnetic' birds.
# Extract unique identifiers from 'individual-local-identifier'
unique_identifiers = data['individual-local-identifier'].unique()

# First, let's extract the unique identifiers for 'magnetic' birds
# Extract unique identifiers for 'magnetic' birds
magnetic_identifiers = [identifier for identifier in unique_identifiers if 'magnetic' in identifier]

# Now we will plot each bird with a different color
colors = px.colors.qualitative.Plotly

# Create the space-time cubes for the 'magnetic' class, each with a different color
magnetic_cubes = []
for i, identifier in enumerate(magnetic_identifiers):
    # Filter data for the current identifier
    bird_data = data[data['individual-local-identifier'] == identifier]
    # Create the scatter plot for the current bird
    cube = go.Scatter3d(
        x=bird_data['utm-easting'],
        y=bird_data['utm-northing'],
        z=bird_data['timestamp_unix'],
        mode='markers',
        marker=dict(size=3, color=colors[i % len(colors)]),
        name=identifier
    )
    magnetic_cubes.append(cube)

# Create a layout for the 3D plot
layout = go.Layout(
    title="Space-Time Cube for Magnetic Birds",
    scene=dict(
        xaxis=dict(title='UTM Easting'),
        yaxis=dict(title='UTM Northing'),
        zaxis=dict(title='Timestamp (Unix)'),
        camera=dict(eye=dict(x=2.5, y=2.5, z=2.5))
    ),
    legend=dict(
        title="Legend",
        itemsizing='constant'
    )
)

# Create a figure with the space-time cubes and layout
fig = go.Figure(data=magnetic_cubes, layout=layout)

# Show the 3D plot
fig.show()

# Save the plot as an HTML file
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\space_time_cube_magnetic.html"
fig.write_html(file_path)


# Now we will create space-time cubes for 'control' birds, plotting each one individually
# Extract unique identifiers for 'control' birds 
control_identifiers = [identifier for identifier in unique_identifiers if 'control' in identifier]

# Now we will plot each bird with a different color
colors = px.colors.qualitative.Plotly

# Create the space-time cubes for the 'control' class, each with a different color
control_cubes = []
for i, identifier in enumerate(control_identifiers):
    # Filter data for the current identifier
    bird_data = data[data['individual-local-identifier'] == identifier]
    # Create the scatter plot for the current bird
    cube = go.Scatter3d(
        x=bird_data['utm-easting'],
        y=bird_data['utm-northing'],
        z=bird_data['timestamp_unix'],
        mode='markers',
        marker=dict(size=3, color=colors[i % len(colors)]),
        name=identifier
    )
    control_cubes.append(cube)

# Create a layout for the 3D plot
layout = go.Layout(
    title="Space-Time Cube for Control Birds",
    scene=dict(
        xaxis=dict(title='UTM Easting'),
        yaxis=dict(title='UTM Northing'),
        zaxis=dict(title='Timestamp (Unix)'),
        camera=dict(eye=dict(x=2.5, y=2.5, z=2.5))
    ),
    legend=dict(
        title="Legend",
        itemsizing='constant'
    )
)

# Create a figure with the space-time cubes and layout
fig = go.Figure(data=control_cubes, layout=layout)

# Show the 3D plot
fig.show()

# Save the plot as an HTML file
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\space_time_cube_control.html"
fig.write_html(file_path)


# Step 5: Now we will create a space-time cube for each class of birds in the same plot
# Create the space-time cubes for each class of birds
cubes = []
for i, identifier in enumerate(unique_identifiers):
    # Filter data for the current identifier
    bird_data = data[data['individual-local-identifier'] == identifier]
    # Create the scatter plot for the current bird
    cube = go.Scatter3d(
        x=bird_data['utm-easting'],
        y=bird_data['utm-northing'],
        z=bird_data['timestamp_unix'],
        mode='markers',
        marker=dict(size=3, color=colors[i % len(colors)]),
        name=identifier
    )
    cubes.append(cube)

# Create a layout for the 3D plot
layout = go.Layout(
    title="Space-Time Cube for All Classes of Birds",
    scene=dict(
        xaxis=dict(title='UTM Easting'),
        yaxis=dict(title='UTM Northing'),
        zaxis=dict(title='Timestamp (Unix)'),
        camera=dict(eye=dict(x=2.5, y=2.5, z=2.5))
    ),
    legend=dict(
        title="Legend",
        itemsizing='constant'
    )
)

# Create a figure with the space-time cubes and layout
fig = go.Figure(data=cubes, layout=layout)

# Show the 3D plot
fig.show()

# Save the plot as an HTML file
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\space_time_cube_all_classes.html"
fig.write_html(file_path)


# Step 6: Now we will create a space-time cube for each class of birds in the same plot with a slider
# Create the space-time cubes for each class of birds
cubes = []

# Create a slider for the plot
steps = []
for i, identifier in enumerate(unique_identifiers):
    # Filter data for the current identifier
    bird_data = data[data['individual-local-identifier'] == identifier]
    # Create the scatter plot for the current bird
    cube = go.Scatter3d(
        x=bird_data['utm-easting'],
        y=bird_data['utm-northing'],
        z=bird_data['timestamp_unix'],
        mode='markers',
        marker=dict(size=3, color=colors[i % len(colors)]),
        name=identifier
    )
    cubes.append(cube)

    # Create a step for the slider
    step = dict(
        method='restyle',
        args=['visible', [False] * len(cubes)],
        label=identifier
    )
    step['args'][1][i] = True
    steps.append(step)

# Create a layout for the 3D plot
layout = go.Layout(
    title="Space-Time Cube for All Classes of Birds",
    scene=dict(
        xaxis=dict(title='UTM Easting'),
        yaxis=dict(title='UTM Northing'),
        zaxis=dict(title='Timestamp (Unix)'),
        camera=dict(eye=dict(x=2.5, y=2.5, z=2.5))
    ),
    legend=dict(
        title="Legend",
        itemsizing='constant'
    ),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)]
        )]
    )]
)

# Create a figure with the space-time cubes and layout
fig = go.Figure(data=cubes, layout=layout)

# Show the 3D plot
fig.show()

# Save the plot as an HTML file
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\space_time_cube_all_classes_slider.html"
fig.write_html(file_path)


# Step 7: Now we will create a space-time cube for each class of birds in the same plot with a slider and buttons
# Create the space-time cubes for each class of birds
cubes = []

# Create a slider for the plot
steps = []

# Create a button for each class of birds
buttons = []

for i, identifier in enumerate(unique_identifiers):
    # Filter data for the current identifier
    bird_data = data[data['individual-local-identifier'] == identifier]
    # Create the scatter plot for the current bird
    cube = go.Scatter3d(
        x=bird_data['utm-easting'],
        y=bird_data['utm-northing'],
        z=bird_data['timestamp_unix'],
        mode='markers',
        marker=dict(size=3, color=colors[i % len(colors)]),
        name=identifier
    )
    cubes.append(cube)

    # Create a step for the slider
    step = dict(
        method='restyle',
        args=['visible', [False] * len(cubes)],
        label=identifier
    )
    step['args'][1][i] = True
    steps.append(step)

    # Create a button for the class of birds
    button = dict(
        label=identifier,
        method='restyle',
        args=['visible', [False] * len(cubes)]
    )
    button['args'][1][i] = True
    buttons.append(button)

# Create a layout for the 3D plot
layout = go.Layout(
    title="Space-Time Cube for All Classes of Birds",
    scene=dict(
        xaxis=dict(title='UTM Easting'),
        yaxis=dict(title='UTM Northing'),
        zaxis=dict(title='Timestamp (Unix)'),
        camera=dict(eye=dict(x=2.5, y=2.5, z=2.5))
    ),
    legend=dict(
        title="Legend",
        itemsizing='constant'
    ),
    updatemenus=[
        dict(
            type='buttons',
            buttons=buttons
        )
    ]
)

# Create a figure with the space-time cubes and layout
fig = go.Figure(data=cubes, layout=layout)

# Show the 3D plot
fig.show()

# Save the plot as an HTML file
file_path = r"C:\Users\Zako3\Downloads\Assignment 3D and time geoviz\space_time_cube_all_classes_slider_buttons.html"
fig.write_html(file_path)

# END OF CODE
# More information on the code can be found in the workflow documentation in the submission folder and repository.
# Thank you for your time.
# Abdillahi Osman Omar - March 2024

