import pandas as pd
from dash import html,dcc,Input,Output,State,callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import datetime
import os

df_tweets = pd.read_csv(os.path.abspath("./data/processed_data.csv"))

def create_cards(card_content,df,i,color):
     card_content.append(dbc.Card(children=[
                                               dbc.CardHeader(children=[datetime.datetime.strptime(str(df['tweetCreated'][i])[:19], '%Y-%m-%d %H:%M:%S').strftime('%d %B %Y %H:%M:%S')]),
                                               html.A(
                                                   [
                                                       dbc.CardBody(
                                                                [
                                                                    html.P(children=[df['tweetText'][i]],
                                                                    className="card-text",
                                                                    ),

                                                                ]
                                                        )

                                                   ],href="https://twitter.com/"+str(df['userScreen'][i])+"/status/"+str(df['tweetID'][i]),
                                                     target="_blank",style={'text-decoration':'none','color':'inherit'}
                                                )
                                               
                                               ],color=color,style={'margin':'10px 0px 10px 10px'}
                                    )
                            )

layout = dbc.Container(
                           [
                               dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H1(['Twitter Sentiment Analysis'],style={'text-align':'center'})

                                            ],width={"size": 6, "offset": 3}
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Button(id='logout-btn',children='Logout',className='float-end'),

                                            ],width=3
                                        ),
                                        
                                        html.Hr(style={'background-color':'rgba(61,61,61,0.5)'}),
                                        
                                    ],style={'margin-top':'10px'}
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Label('Select Topic:'),
                                                dcc.Dropdown(id='dropdown-topics',
                                                options=df_tweets['reqKeywords'].unique(),
                                                value=df_tweets['reqKeywords'].unique(),
                                                multi=True
                                                )

                                            ],width=4
                                        )
                                        
                                    ],class_name='mb-5',justify='center'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader("Total Tweets",className='fs-3 text-center'),
                                                        dbc.CardBody(
                                                            [
                                                                html.H5(id='total-tweets',className='card-text text-center fs-1 mb-2')

                                                            ]
                                                        )
                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                )
                                                

                                            ],md=2
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader("Average Likes",className='fs-3 text-center'),
                                                        dbc.CardBody(
                                                            [
                                                                html.H5(id='average-likes',className='card-text text-center fs-1 mb-2')

                                                            ]
                                                        )
                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                )
                                                

                                            ],md=2
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader('Average Retweets',className='fs-3 text-center'),
                                                        dbc.CardBody(
                                                            [
                                                                html.H5(id='average-retweets',className='card-text text-center fs-1 mb-2')

                                                            ]
                                                        )
                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                )
                                                

                                            ],md=2
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader(
                                                            [
                                                                dbc.Row(
                                                                    [
                                                                        dbc.Col(
                                                                            [
                                                                                html.P("Most Positive Tweet",className='mb-0 fs-3 text-center'),

                                                                            ],md=9
                                                                        ),dbc.Col(
                                                                            [
                                                                                html.P(id='pos-count',className='mb-0 fs-3 text-center')

                                                                            ],md=3
                                                                        )
                                                                    ],align='center'
                                                                )
                                                                
                                                                
                                                            ],style={'background-color':'rgb(0, 204, 150)'}
                                                        ),
                                                        dbc.CardBody(
                                                            [
                                                                html.H5(id='most-positive-tweet',className='card-text fs-6')

                                                            ]
                                                        )
                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                )
                                                

                                            ],md=3
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader(
                                                            [
                                                                dbc.Row(
                                                                    [
                                                                        dbc.Col(
                                                                            [
                                                                                html.P("Most Negative Tweet",className='mb-0 fs-3 text-center'),

                                                                            ],md=9
                                                                        ),dbc.Col(
                                                                            [
                                                                                html.P(id='neg-count',className='mb-0 fs-3 text-center')

                                                                            ],md=3
                                                                        )
                                                                    ],align='center'
                                                                )
                                                            ],style={'background-color':'rgb(239, 85, 59)'}
                                                        ),
                                                        dbc.CardBody(
                                                            [
                                                                html.H5(id='most-negative-tweet',className='card-text fs-6')

                                                            ]
                                                        )
                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                )
                                                

                                            ],md=3
                                        ),
                                        

                                    ]
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader('Tweets Timeline',className='text-center fs-3'),
                                                        dbc.CardBody(id='sentiment-timeline')

                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                dbc.Card(
                                                                    [
                                                                        dbc.CardHeader('Keywords Distribution',className='text-center fs-3'),
                                                                        dbc.CardBody(id='keyword-bar')

                                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                                )
                                                            ],md=6
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                dbc.Card(
                                                                    [
                                                                        dbc.CardHeader('Tweets',className='text-center fs-3'),
                                                                        dbc.CardBody(id='tweets-card',style={'overflow':'scroll','overflow-x':'hidden','height':'480px'})

                                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                                )
                                                            ],md=6
                                                        )
                                                        
                                                    ]
                                                )
                                                

                                            ],md=9
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader('Average Sentiment Score',className='text-center fs-3'),
                                                        dbc.CardBody(id='sentiment-indicator')
                                                        

                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                ),
                                                dbc.Card(
                                                    [
                                                        dbc.CardHeader('Sentiment Distribution',className='text-center fs-3'),
                                                        dbc.CardBody(id='sentiment-pie')
                                                        
                                                    ],className="shadow p-0 mb-3 bg-white rounded border-light"
                                                )

                                            ],md=3
                                        )

                                    ]
                                )
                           ],fluid=True
)


@callback(
    [Output('total-tweets','children'),
    Output('average-likes','children'),
    Output('average-retweets','children'),
    Output('most-positive-tweet','children'),
    Output('most-negative-tweet','children'),
    Output('pos-count','children'),
    Output('neg-count','children'),
    Output('sentiment-timeline','children'),
    Output('sentiment-indicator','children'),
    Output('sentiment-pie','children'),
    Output('keyword-bar','children'),
    Output('tweets-card','children')],
    Input('dropdown-topics','value')
)

def update_fig(topics):

    frames = []

    for topic in topics:
        df_topics = df_tweets[df_tweets['reqKeywords'] == topic]
        frames.append(df_topics)
    df_tweets_filtered = pd.concat(frames, ignore_index=True)
    df_tweets_filtered.sort_values(by='tweetCreated',inplace=True,ignore_index=True)

    total_tweets = str(len(df_tweets_filtered))
    average_likes = str(round(df_tweets_filtered['tweetFavoriteCt'].mean(),2))
    average_retweets = str(round(df_tweets_filtered['tweetRetweetCt'].mean(),2))

    most_pos_ind = df_tweets_filtered['pos_count'].idxmax()
    most_pos_tweet = df_tweets_filtered['tweetText'][most_pos_ind]
    most_neg_ind = df_tweets_filtered['neg_count'].idxmax()
    most_neg_tweet = df_tweets_filtered['tweetText'][most_neg_ind]

    #### SCATTER CHART and HISTOGRAM ####

    fig = go.Figure()
    fig4 = go.Figure()
    for sentiment in df_tweets_filtered['sentiment'].unique():
        df_filtered = df_tweets_filtered[df_tweets_filtered['sentiment'] == sentiment]
        df_filtered['tweetCreated'] =  pd.to_datetime(df_filtered['tweetCreated']).dt.date
        group_df = df_filtered.groupby(by=['tweetCreated'])['sentiment'].count().to_frame()

        if sentiment == 'Positive':
            
            
            fig.add_trace(go.Scatter(x=group_df.index, y=group_df['sentiment'],
                    mode='lines+markers',
                    name=sentiment,
                    marker=dict(color="rgb(0, 204, 150)")))
            
            fig4.add_trace(go.Histogram(
                         y=df_filtered['reqKeywords'],
                         name=sentiment,
                         orientation='h',
                         marker=dict(color="rgb(0, 204, 150)")
                         )
                )
        elif sentiment == 'Negative':
            fig.add_trace(go.Scatter(x=group_df.index, y=group_df['sentiment'],
                    mode='lines+markers',
                    name=sentiment,
                    marker=dict(color="rgb(239, 85, 59)")))
            fig4.add_trace(go.Histogram(
                         y=df_filtered['reqKeywords'],
                         name=sentiment,
                         orientation='h',
                         marker=dict(color="rgb(239, 85, 59)")
                         )
                )
        elif sentiment == 'Neutral':
            fig.add_trace(go.Scatter(x=group_df.index, y=group_df['sentiment'],
                    mode='lines+markers',
                    name=sentiment,
                    marker=dict(color="rgb(99, 110, 250)")))
            fig4.add_trace(go.Histogram(
                         y=df_filtered['reqKeywords'],
                         name=sentiment,
                         orientation='h',
                         marker=dict(color="rgb(99, 110, 250)")
                         )
                )
        fig.update_layout(yaxis=dict(title='Number of Tweets'),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")
        fig.update_xaxes(showline=True, linewidth=1, linecolor='rgba(61,61,61,0.5)',showgrid=False,zeroline=False)
        fig.update_yaxes(showline=True, linewidth=1, linecolor='rgba(61,61,61,0.5)',showgrid=False,zeroline=False)

        fig4.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title="Total no. of tweets"),
            yaxis=dict(title="Keywords"),
            barmode='stack'
        )
        fig4.update_xaxes(categoryorder='category descending')

    
    #### INDICATOR CHART ####

    

    fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = df_tweets_filtered['sentiment_codes'].mean(),
    mode = "gauge+number",
    gauge = {'axis': {'range': [-1, 1]},
             'steps' : [
                 {'range': [-1,-0.25], 'color': "rgb(239, 85, 59)"},
                 {'range': [-0.25,0.25], 'color': "rgb(99, 110, 250)"},
                 {'range': [0.25,1], 'color':'rgb(0, 204, 150)'}],
             'bar':{'color':'#343a40'}}))
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",margin=dict(l=13,r=13))


    #### PIE CHART ####

    tweets_sentiment_counts = df_tweets_filtered['sentiment'].value_counts().T
    labels = ['Negative',"Neutral","Positive"]
    values = []
    for label in labels:
        values.append(tweets_sentiment_counts[label])

    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=["rgb(239, 85, 59)","rgb(99, 110, 250)","rgb(0, 204, 150)"]))])
    fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",margin=dict(l=0,r=0))
    fig3.update_xaxes(showline=True, linewidth=1, linecolor='rgba(61,61,61,0.5)',showgrid=False,zeroline=False)
    fig3.update_yaxes(showline=True, linewidth=1, linecolor='rgba(61,61,61,0.5)',showgrid=False,zeroline=False)


    #### TWEETS LIST ####

    card_content = []

    for i in range(len(df_tweets_filtered)):
        if df_tweets_filtered['sentiment'][i] == 'Positive':
            create_cards(card_content,df_tweets_filtered,i,"rgb(0, 204, 150)")
        elif df_tweets_filtered['sentiment'][i] == 'Neutral':
            create_cards(card_content,df_tweets_filtered,i,"rgb(99, 110, 250)")
        elif df_tweets_filtered['sentiment'][i] == 'Negative':
            create_cards(card_content,df_tweets_filtered,i,"rgb(239, 85, 59)")
       

    
    return [total_tweets,
            average_likes,
            average_retweets,
            most_pos_tweet,
            most_neg_tweet,
            "+"+str(df_tweets_filtered['pos_count'][most_pos_ind]),
            "-"+str(df_tweets_filtered['neg_count'][most_neg_ind]),
            dcc.Graph(figure=fig),
            dcc.Graph(figure=fig2),
            dcc.Graph(figure=fig3),
            dcc.Graph(figure=fig4),
            card_content]

