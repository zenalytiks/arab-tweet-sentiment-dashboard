from dash import dcc,html
import dash_bootstrap_components as dbc

layout = dbc.Container(
            [
                dbc.Row(
                    [
                        dcc.Location(id='err404', refresh=True),
                        html.H1("404",className='text-center'),
                        html.H3("Not Found",className='text-center'),
                        html.H5("The resource requested could not be found on this server!",className='text-center')
        
                    ]
                )
            ]
    )