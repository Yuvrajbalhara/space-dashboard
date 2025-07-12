
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load data
df_year = pd.read_excel("space_missions_dashboard_data.xlsx", sheet_name="Launches by Year")
df_country = pd.read_excel("space_missions_dashboard_data.xlsx", sheet_name="Launches by Country")
df_org = pd.read_excel("space_missions_dashboard_data.xlsx", sheet_name="Launches by Organization")

# Create figures
fig_launches = px.line(
    df_year, x="Year", y=["Total Launches", "Successes", "Failures"],
    labels={"value": "Number of Launches", "variable": "Launch Type"},
    title="Launches Over Time (1957-2020)"
)
fig_launches.update_layout(legend_title_text='Launch Type', template='plotly_dark')

fig_country = px.bar(
    df_country.sort_values("Launches", ascending=True),
    x="Launches", y="Country", orientation="h",
    title="Top 15 Countries by Number of Launches"
)
fig_country.update_layout(template='plotly_dark')

fig_org = px.bar(
    df_org.sort_values("Launches", ascending=True),
    x="Launches", y="Organization", orientation="h",
    title="Top 15 Launch Organizations (1957-2020)"
)
fig_org.update_layout(template='plotly_dark')

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Decades in Orbit Dashboard"

# Layout
app.layout = html.Div(style={"backgroundColor": "#111111", "color": "#FFFFFF", "padding": "20px"}, children=[
    html.H1("🚀 Decades in Orbit: The Evolution of Space Missions (1957-2020)", style={"textAlign": "center"}),

    dcc.Tabs([
        dcc.Tab(label='📈 Launches Over Time', children=[
            dcc.Graph(figure=fig_launches)
        ]),
        dcc.Tab(label='🌍 Launches by Country', children=[
            dcc.Graph(figure=fig_country)
        ]),
        dcc.Tab(label='🏢 Launch Organizations', children=[
            dcc.Graph(figure=fig_org)
        ]),
    ], style={'color': '#000'}, content_style={'backgroundColor': '#222', 'padding': '20px'})
])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)

