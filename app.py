import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Total': [100, 200, 300, 400, 500],
    'Start Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'],
    'Interest': [10, 20, 30, 40, 50],
    'End Date': ['2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01']
})

# Convert dates to datetime objects
data['Start Date'] = pd.to_datetime(data['Start Date'])
data['End Date'] = pd.to_datetime(data['End Date'])

# Create the line chart
fig = px.line(data, x='Start Date', y='Total', title='Total vs Interest', markers=True)
fig.add_scatter(x=data['End Date'], y=data['Interest'], name='Interest')
fig.show()