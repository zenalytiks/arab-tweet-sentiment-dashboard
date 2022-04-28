import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

app.title = "Twitter Sentiment Dashboard"

