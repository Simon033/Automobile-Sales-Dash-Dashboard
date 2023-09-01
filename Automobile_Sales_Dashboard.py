#!/usr/bin/env python
# coding: utf-8

# install the following to run on terminal
# pip3.8 install setuptools
# python3.8 -m pip install packaging
# python3.8 -m pip install pandas dash
# pip3.8 install httpx==0.20 dash plotly
# (To run use this)
# python3.8 Automobile_Sales_Dashboard.py

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Statistics Dashboard"

# Create the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard", 
    style={"textAlign": "center", 'color': '#3A00B0', 'font-size': 30}
    ),
    #adding two drop down
    #select stat type dropdown
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': "Yearly Statistics", "value": "Yearly Statistics"},
                {'label': 'Recession Period Statistics', "value": 'Recession Period Statistics'}
            ],
            value='Select Statistics',
            placeholder='Select a report type',
            style={'font-weight': 'bold'}
        )
    ], style={ "alignItems": "center", "padding": "3px", "font-size": "20px", "textAlign": "center"}),
    #select year dropdown
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': str(i), 'value': i} for i in data['Year'].unique()],
            value='Select Year',
            style={'font-weight': 'bold'}
        )
    ], style={"alignItems": "center", "padding": "3px", "font-size": "20px", "textAlign": "center"}),
    #adding a division to output all plots
    html.Div(
        id='output-container', 
        className='chart-grid', 
        style={'display': "flex",'backgroundColor':'#dcf5fc'}),
])

# Callback for updating year dropdown based on selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_statistics):
    return False if selected_statistics == 'Yearly Statistics' else True

# Callback for updating output container based on selected statistics and year
@app.callback(
    Output(component_id='output-container', component_property='children'),
    Input(component_id='dropdown-statistics', component_property='value'),
    Input(component_id='select-year', component_property='value')
)
def update_output_container(selected_statistics, input_year):
# Recession Data Plots
    if selected_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]
        
        #Plot 1- Average Automobile sales using line chart for the Recession Period using line chart.
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec,
                           x='Year',
                           y='Automobile_Sales',
                           title="Average Automobile Sales fluctuation over Recession Period")
        )

        #Plot 2- Average number of vehicles sold by vehicle type using bar chart
        average_sales = recession_data.groupby("Vehicle_Type")['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                          x='Vehicle_Type',
                          y='Automobile_Sales',
                          title="Average Automobile Sales by Vehicle Type during Recession Period")
        )

        #Plot 3- Total expenditure share by vehicle type during recession usssing pie chart
        exp_rec = recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"].mean().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                          values='Advertising_Expenditure',
                          names='Vehicle_Type',
                          title="Total Expenditure Share by Vehicle Type During Recessions")
        )
        
        #Plot 4- Effect of unemployment rate on vehicle type and sales using bar chart
        unempl = recession_data.groupby(['Vehicle_Type','unemployment_rate'])['Automobile_Sales'].sum().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unempl,
                        x='unemployment_rate',
                        y= 'Automobile_Sales',
                        color='Vehicle_Type',
                        title= 'Effect of Unemployment Rate on Vehivle Type and Sales')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart3)],
                     style={'flex': '50%'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart2), html.Div(children=R_chart4)],
                     style={'flex': '50%'}),
        ]
        
#Yearly Automobile Sales Plots
    elif selected_statistics == 'Yearly Statistics':
        yearly_data = data[data['Year'] == input_year]
        
        # Plot1- Yearly Average Automobile sales using line chart for the whole period.
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas,
                                            x='Year',
                                            y='Automobile_Sales',
                                            title="Yearly Average Automobile Sales"
                                            ))
        
        #Plot 2- Total Monthly Automobile sales using line chart.
        ym = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(ym,
                                            x='Month',
                                            y='Automobile_Sales',
                                            title=f"Total Monthly Automobile sales for year {input_year}"
                                            ))
        
        #Plot 3- Average Monthly Automobile sales of each vehicle type using bar chart.
        avr_vdata = yearly_data.groupby("Vehicle_Type")['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata,
                                           x='Vehicle_Type',
                                           y='Automobile_Sales',
                                           title=f'Average Vehicles Sold by Vehicle Type in the year {input_year}',
                                           color='Vehicle_Type'))
        
        #Plot 4- Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(exp_data,
                                           values='Advertising_Expenditure',
                                           names='Vehicle_Type',
                                           title=f"Total Advertisement Expenditure by Vehicle Type in the year {input_year}"))

        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart3)],
                     style={'flex': '50%'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart2), html.Div(children=Y_chart4)],
                     style={'flex': '50%'}),
        ]

    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)