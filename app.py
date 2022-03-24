from flask import Flask, render_template, request, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

from data import totalPoints_fig, subplots_fig, eventCode, bestTeams, rankings, getBar, teamInfo, teamsDone

app = Flask(__name__)

# @app.route('/')
# def layout():
#     return render_template('layout.html')




df = px.data.medals_wide()
fig = px.bar(df, x = "nation", y = ['gold', 'silver', 'bronze'], title = "Wide=Form Input")

graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

@app.route('/')
def index():
    return render_template('homePage.html', rankings=rankings, bestTeams=bestTeams, eventCode=eventCode)


@app.route('/homePage')
def homePage():
    return render_template('homePage.html', rankings=rankings, bestTeams=bestTeams, eventCode=eventCode)


@app.route('/totalValues')
def totalValues():
#    totalScoreJSON = json.dumps(totalPoints_fig, cls=plotly.utils.PlotlyJSONEncoder)
    subplotsJSON = json.dumps(subplots_fig, cls=plotly.utils.PlotlyJSONEncoder)

    percentData_x = []
    percentData_y = []
    for team in teamInfo:
        if team['teamNumber'] == getDropdown():
            for x in range(5):
                if x == 0:
                    percentData_y.append(team['PercentNone'])
                    percentData_x.append("None")
                if x == 1:
                    percentData_y.append(team['PercentLow'])
                    percentData_x.append("Low")
                if x == 2:
                    percentData_y.append(team['PercentMid'])
                    percentData_x.append("Mid")
                if x == 3:
                    percentData_y.append(team['PercentHigh'])
                    percentData_x.append("High")
                if x == 4:
                    percentData_y.append(team['PercentTraversal'])
                    percentData_x.append("Traversal")
    percent_bargraph = px.bar(x=percentData_x, y=percentData_y, range_y=[0, 100])
   
    return render_template('totalValues.html', rankings=rankings, bestTeams=bestTeams, totalPoints_fig=totalPoints_fig, subplots_fig=subplotsJSON, percent_bargraph=percent_bargraph, sample_barfig=fig, teamsDone=teamsDone)


@app.route('/getDropdown')
def getDropdown():
    output = request.get_json()
    result = json.dumps(output)
    # print(output)
    # print(type(output))
    # print(result)
    # print(type(result))

    return result