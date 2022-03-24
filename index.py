from turtle import onclick
from dash import dcc, html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import homePage, totalValues
from data import rankings, bestTeams


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div(className="nav", children=[
            html.Button(type="button", id="nav-close", children=[
                "Rankings",
                html.Div(id='nav-links-container', children=[
                    html.Ol(id='rankings', children=rankings),
                    html.Ol(id='bestTeams', children=bestTeams)
                ])
            ])
        ]),
        dcc.Link('Home', href='/apps/homePage'),
        dcc.Link('Team Information', href='/apps/totalValues'),
        html.Main(children=[
            html.Button("Open Navigation", type='button', onclick="toggleNav()")
        ], className="main")
    ], className="row"),
    html.Div(id='page-content', children=[])
], id='fullPage')


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    # if pathname == '/apps/vgames':
    #     return vgames.layout
    # if pathname == '/apps/global_sales':
    #     return global_sales.layout
    # else:
    #     return "404 Page Error! Please choose a link"
    if pathname == "/apps/totalValues":
        return totalValues.layout
    if pathname == "/apps/homePage":
        return homePage.layout
    else:
        return f"You are cringe. \nYou are on '{pathname}. Go to an actual valid url."


if __name__ == '__main__':
    app.run_server(debug=False)