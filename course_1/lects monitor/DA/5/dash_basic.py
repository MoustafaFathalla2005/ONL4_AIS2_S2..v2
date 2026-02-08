import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_excel('Dash.xlsx')
app = Dash()
app.title = 'Interactive Dashboard'
num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("Interactive Dashboard with Pie Plot"),
    html.Label("Select a column to show in pie chart"),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0]
    ),
    dcc.Graph(id='pie-chart')
])

@app.callback(
    Output('pie-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_pie(selected_col):
    counts = df[selected_col].value_counts().reset_index()
    counts.columns = [selected_col, 'Count']
    fig = px.pie(
        counts,
        names=selected_col,
        values='Count',
        title=f'<b>Distribution of {selected_col}</b>',
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)