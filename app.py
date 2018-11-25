import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


pv = pd.read_csv("history.csv",names=['date','time','amount','currency','name','surname','mobile'],sep=' ')
#pv = pd.pivot_table(df, index=['time'], columns=["amount"], values=['name'], aggfunc=sum, fill_value=0)
#print(pv)
trace1 = go.Scatter(x=pv.index, y=pv['amount'], name='Spendings',mode='lines')
#trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
#trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
#trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

app = dash.Dash()


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='MobilePay - transactions'),
    html.Div(children='''See your mobile spendings'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1],# trace2, trace3, trace4],
            'layout':
            go.Layout(title='Order Status by Customer', barmode='stack')
        })
])



if __name__ == '__main__':
    #app.run_server(debug=True)
     app.run_server(host='0.0.0.0',debug=True)
