
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load data
df_year = pd.read_excel("space_missions_dashboard_data.xlsx", sheet_name="Launches by Year")
df_country = pd.read_excel("space_missions_dashboard_data.xlsx", sheet_name="Launches by Country")
df_org = pd.read_excel("space_missions_dashboard_data.xlsx", sheet_name="Launches by Organization")

# Create figures
fig_launches = px.line(df_year, x="Year", y=["Total Launches", "Successes", "Failures"],
                       labels={"value": "Number of Launches", "variable": "Launch Type"},
                       title="Launches Over Time (1957–2020)")

fig_country = px.bar(df_country.sort_values("Launches", ascending=False),
                     x="Launches", y="Country", orientation="h",
                     title="Top 15 Countries by Number of Launches")

fig_org = px.bar(df_org.sort_values("Launches", ascending=True),
                 x="Launches", y="Organization", orientation="h",
                 title="Top 15 Launch Organizations")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Decades in Orbit Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Decades in Orbit: The Evolution of Space Missions (1957–2020)", style={"textAlign": "center"}),

    dcc.Graph(figure=fig_launches),
    dcc.Graph(figure=fig_country),
    dcc.Graph(figure=fig_org)
])

if __name__ == "__main__":
    app.run(debug=True)
