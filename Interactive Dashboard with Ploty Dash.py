# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Div([html.Label("Launch Site:"),
                                        dcc.Dropdown(id='site-dropdown',
                                                    options=[{'label':'All sites', 'value':'All'},
                                                             {'label':'CCAFS LC-40', 'value':'CCAFS LC-40'},
                                                             {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'},
                                                             {'label':'KSC LC-39A', 'value':'KSC LC-39A'},
                                                             {'label':'CCAFS SLC-40', 'value':'CCAFS SLC-40'}],
                                                    value="All",
                                                    placeholder='Select a Launch Site here',
                                                    searchable=True)]),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                html.Div(dcc.RangeSlider(id='payload-slider',
                                        min=0, max=10000, step=1000,
                                        value=[min_payload,max_payload])),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart',component_property='figure'),
              Input(component_id='site-dropdown',component_property='value'))

def get_pie_chart(enterd_site):
    filtered_df1 = spacex_df
    if enterd_site == 'All':
        df1=filtered_df1.groupby("Launch Site")["class"].mean().reset_index()
        fig = px.pie(df1, values='class',
        names='Launch Site',
        title='Total Success Launches By Site')
        return fig
    else:
        df2=filtered_df1[filtered_df1["Launch Site"]==enterd_site]
        df2=df2.groupby("class").size().reset_index()
        fig = px.pie(df2, values=0,
        names='class',
        title='Total Success Launches for site ' + enterd_site)
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart',component_property='figure'),
    [Input(component_id='site-dropdown',component_property='value'),
     Input(component_id='payload-slider',component_property='value')])

def get_scatter_chart(enterd_site,slider_range):
    low, high = slider_range
    filtered_df2 = spacex_df[(spacex_df["Payload Mass (kg)"]>low) & (spacex_df["Payload Mass (kg)"]<high)]
    if enterd_site == 'All':
        fig = px.scatter(filtered_df2, x='Payload Mass (kg)', y='class',
        color='Booster Version Category',
        title='Coorelation between Payload and Success for all Sites')
        return fig
    else:
        df3 = filtered_df2[filtered_df2["Launch Site"]==enterd_site]
        fig = px.scatter(df3, x='Payload Mass (kg)', y='class',
        color='Booster Version Category',
        title='Coorelation between Payload and Success for ' + enterd_site)
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
