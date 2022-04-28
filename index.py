from dash import dcc
from dash import html,Input, Output,State, callback
from app1 import app,server
from pages import (
    dashboard,
    login,
    error
)



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='login-status',storage_type='session',data=False),
    dcc.Store(id='logout-status',storage_type='session',data=True),
    html.Div([
        html.Div(id='pageContent')
    ])
])


################################################################################
# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
################################################################################
@callback(Output('pageContent', 'children'),
              [Input('url', 'pathname'),Input('login-status','data'),Input('logout-status','data')])
def displayPage(pathname,login_status,logout_status):
    if pathname == '/':
        if logout_status:
            return login.layout
        elif login_status:
            return dashboard.layout
    elif pathname == '/login':
        if logout_status:
            return login.layout
        elif login_status:
            return dashboard.layout

    elif pathname == '/logout':
        if logout_status:
            return login.layout

    elif pathname == '/main':
        if login_status:
            return dashboard.layout
        elif logout_status:
            return login.layout

    else:
        return error.layout




@callback(
    [Output('url', 'pathname'),Output('logout-status','data')],
    [Input('logout-btn','n_clicks')],
    [State('logout-status','data')]
)

def logout(n_clicks,status):
    if n_clicks > 0:
        n_clicks = 0
        status = True
        return ['/logout',status]
    else:
        status = False
        return ['/main',status]


if __name__ == '__main__':
    app.run_server(debug=False)
