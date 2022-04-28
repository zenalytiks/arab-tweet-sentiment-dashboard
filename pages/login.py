import os
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html,dcc,callback,Input, Output, State

df_users = pd.read_csv(os.path.abspath("./data/users.csv"))

layout = dbc.Container([
    dcc.Location(id='urlLogin',refresh=True),
    html.Br(),
    dbc.Row([
    dbc.Col([
                

                dbc.Row(
                        [
                        html.Img(
                            src='/assets/icons8-twitter.svg',
                            className='center',
                            width=144,
                            height=144
                        )

                        ],justify="center"
                ),

                dbc.Row(
                        [
                        dbc.Col(
                                [
                                dbc.InputGroup(
                                    [
                                        dbc.Input(id="input-username",placeholder="Username", type="text")

                                    ]
                                )
                                ]
                        )


                        ],style={'padding':'10px'},justify="center"
                ),
                dbc.Row(
                        [
                        dbc.Col(
                                [
                                dbc.InputGroup(
                                    [
                                        dbc.Input(id="input-password",placeholder="Password", type="password")

                                    ]
                                )

                                ]
                        )
                        ],style={'padding':'10px'},justify="center"
                ),
                dbc.Row(
                        [
                        
                            html.Button(
                            children='Login',
                            n_clicks=0,
                            id='loginButton',
                            className='btn btn-primary btn-lg'
                            )

                          
                        

                        ],style={'padding':'10px'},justify="center"
                )
                ],width=6)
    ],justify="center", className='jumbotron')
],fluid=True)


@callback([Output('urlLogin', 'pathname'),Output('login-status','data')],
              [Input('loginButton', 'n_clicks')],
              [State('input-username', 'value'),
               State('input-password', 'value'),
               State('login-status','data')])
def sucess(n_clicks, username, password, status):
    if n_clicks >0:
        n_clicks = 0
        user_df = df_users[(df_users['username'] == username) & (df_users['password'] == password)]
        user_df = user_df.reset_index()
        if ((user_df['username'][0] == username) & (user_df['password'][0] == password)):
            status = True
            return ['/main',status]
        else:
            status = False
            return ['/login',status]
    else:
        status = False
        return ['/login',status]