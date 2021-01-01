import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the free tutoring website", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This website is created for students to submit their questions and get\
                            answers with free of charge.'
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='Please post your question in the textbox below, and provide your email address.\
                            Alternatively, you can take a picture of your question and drop it in the drop zone.\
                            An answer will be sent to you shortly.')
                    , className="mb-5")
        ]),

        dbc.Row([
            dbc.Card(children=[html.H3(children='Question Box',
                                               className="text-center"),
                                       dbc.Row([
                                           
                                           # dbc.Col(dbc.Button("Global", href="https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data/resource/55e8f966-d5c8-438e-85bc-c7a5a26f4863",
                                           #                         color="primary"),
                                           #              className="mt-3"),
                                           #      dbc.Col(dbc.Button("Singapore", href="https://data.world/hxchua/covid-19-singapore",
                                           #                         color="primary"),
                                           #              className="mt-3")
                                                
                                                
                                                ],
                                           justify="center")
                                       ],
                             body=True, color="dark", outline=True),
            ]),
        dbc.Row([
             dcc.Upload(id='upload-image',
                            children=html.Div(['Drag and Drop or ',
                                html.A('Select Files')]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            # Allow multiple files to be uploaded
                            multiple=True,
                        ),
             html.Div(id='output-image-upload'),
            ],justify="center"
            ),
             html.A("This website is created by Duy Nguyen with the intention to help students free-of-charge. ")     
                 ])
                        
                    
                    
                    
                    
                    
                    ])

        #     dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this dashboard',
        #                                        className="text-center"),
        #                                dbc.Button("GitHub",
        #                                           href="https://github.com/meredithwan/covid-dash-app",
        #                                           color="primary",
        #                                           className="mt-3"),
        #                                ],
        #                      body=True, color="dark", outline=True)
        #             , width=4, className="mb-4"),

        #     dbc.Col(dbc.Card(children=[html.H3(children='Read the Medium article detailing the process',
        #                                        className="text-center"),
        #                                dbc.Button("Medium",
        #                                           href="https://medium.com/@meredithwan",
        #                                           color="primary",
        #                                           className="mt-3"),

        #                                ],
        #                      body=True, color="dark", outline=True)
        #             , width=4, className="mb-4")
        # 
        # ], className="mb-5"),
            
       



# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)